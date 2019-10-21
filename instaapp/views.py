from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from .models import Profile,Image,Follow
from .forms import NewImageForm, NewProfileForm
# from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm

@login_required(login_url='/accounts/login/')
def welcome(request):
    images = Image.objects.all()

    return render(request, 'users/welcome.html', {'images':images,})


@login_required(login_url='/accounts/login/')
def picture(request,picture_id):
    try:
        picture = Image.objects.get(id = picture_id)
    except DoesNotExist:
        raise Http404()

    return render(request,"users/welcome.html", {"picture":picture})


@login_required(login_url='/accounts/login/')
def new_picture(request):
    current_user = request.user
    profile = Profile.objects.get(user=request.user.id)
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            picture = form.save(commit=False)
            picture.user = current_user
            picture.save()

        return redirect ('profile',current_user.id)

    else:
        form = NewImageForm()

    return render(request, 'users/new_picture.html', {'form': form})



@login_required(login_url='/accounts/login/')
def user_profile(request, user_id):

 
    images=Image.objects.filter(profile=user_id)
    user = User.objects.get(pk=user_id)
    profile = Profile.objects.filter(user=user_id)
    owner = User.objects.get(pk=user_id).username

    if Follow.objects.filter(following=request.user,follower=user).exists():
        is_follow=True
        
    else:
        is_follow=False

    followers=Follow.objects.filter(follower=user).count()
    followers=Follow.objects.filter(following=user).count()

    return render(request, 'users/user_profile.html', {'image':image, 'profile':profile, 'owner':owner, 'is_follow':is_follow, 'followers':followers, 'followings':followings})




@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user = request.user

    if request.method == 'POST':
        if Profile.objects.filter(user_id=current_user).exists():

            form = NewProfileForm(request.POST, request.FILES,instance=Profile.objects.get(user_id=current_user))

        else:
            form=NewProfileForm(request.POST, request.FILES)

        if form.is_valid():
            profile=form.save(commit=False)
            profile.user = current_user
            profile.save()

            return redirect('user_profile',current_user.id)

    else:
        if Profile.objects.filter(user_id=current_user).exists():
            form = NewProfileForm(instance=Profile.objects.get(user_id=current_user))

        else:
            form=NewProfileForm()

    return render(request, 'users/edit_profile.html', {'form':form})


# def follow(request,user_to):

#     user=User.objects.get(id=use_to)
#     is_follow=False

#     if Follow.objects.filter(following=request.user,follower=user).exists()
#         Follow.objects.filter(following=request.user,follower=user).delete()
#         is_follow=False

#     else:
#         Follow.objects.filter(following=request.user,follower=user).save()
#         is_follow=True

#     return HttpResponseRedirect(request.Meta.get('HTTP_REFER'))


@login_required(login_url='/accounts/login/')
def search_results(request):

    if 'username' in request.GET and request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_users = Profile.search_by_profile(search_term)
        message = f"{search_term}"

        return render(request, 'users/search.html',{"message":message,"users": searched_users})

    else:
        message = "You haven't searched for any term"
        return render(request, 'users/search.html',{"message":message})


