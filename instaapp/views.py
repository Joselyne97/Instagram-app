from django.shortcuts import render,redirect, get_object_or_404
from django.http  import HttpResponse,Http404,HttpResponseRedirect
# import datetime as dt
from .models import Profile,Image
from .forms import InstagramLetterForm
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

