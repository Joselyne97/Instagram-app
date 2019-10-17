from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from .models import Profile
from .forms import InstagramLetterForm,NewPhotoForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required

# Create your views here.

# def feeds_photos(request):
#     date = dt.date.today
#     feeds = Profile.todays_photo()
#     if request.method == 'POST':
#         form = NewsLetterForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['your_username']
#             email = form.cleaned_data['email']
#             recipient = NewsLetterRecipients(name = username,email =email)
#             recipient.save()
#             send_welcome_email(name,email)
            
#             HttpResponseRedirect('news_today')
#     else:
#         form = NewsLetterForm()
#     return render(request, 'all-news/today-news.html', {"date": date,"news":news,"letterForm":form})