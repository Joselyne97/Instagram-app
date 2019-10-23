from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from .models import Profile,Image,Comment
from .forms import NewImageForm,NewProfileForm,NewCommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

@login_required(login_url='/accounts/login/')
def welcome(request):
    current_user = request.user
    # profile=Profile.objects.all()
    images = Image.objects.all()
    # images = Image.get_images()
    user_profile= Profile.objects.filter(user=current_user.id).first()
  
    comment= Comment.objects.filter(user=current_user.id).first()
    



    return render(request, 'users/welcome.html', {'images':images,'user_profile':user_profile,'comment':comment})



@login_required(login_url='/accounts/login/')
def new_picture(request):
    current_user = request.user
  
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()

        return redirect ("welcome")

    else:
        form = NewImageForm()

    return render(request, 'users/new_picture.html', {"form": form})



@login_required(login_url='/accounts/login/')
def user_profile(request):
    current_user = request.user
    images = Image.objects.filter(user=current_user).all()
    user_profile = Profile.objects.filter(user=current_user.id).first()
    

    return render(request, 'users/user_profile.html', {'images':images, 'user_profile':user_profile,})




@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user = request.user
    # user_profile = Profile.objects.filter(user=current_user.id).first()

    if request.method == 'POST':
        form=NewProfileForm(request.POST, request.FILES)

        if form.is_valid():
            profile=form.save(commit=False)
            profile.user = current_user
            profile.save()

            return redirect('user-profile')

    else:
            form=NewProfileForm()

    return render(request, 'users/edit_profile.html', {'form':form,})


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



@login_required(login_url='/accounts/login/')
def new_comment(request, image_id):
    current_user = request.user
    image = Image.objects.get(id=image_id)
    profile = Profile.objects.filter(user=current_user.id).first()
    if request.method == 'POST':
        form=NewCommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.image=image
            comment.save()
            
            return redirect('welcome')

    else:
        form = NewCommentForm()

    return render(request, 'users/new_comment.html', {'form': form,'profile':profile, 'image':image, 'image_id':image_id})


@login_required(login_url='/accounts/login/')
def likes(request,id):
    likes=1
    image = Image.objects.get(id=id)
    image.likes = image.likes=+1
    image.save()
    return redirect('/')

