from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from tinymce.models import HTMLField

class Profile(models.Model):

    bio = HTMLField()
    profile_pic = models.ImageField(upload_to = 'pic/', blank=True, null=True)
    user=models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    
    # @classmethod
    # def get_all_id(cls)
    #     profile = Profile.objects.get(user=id)
    #     return profile

    @classmethod
    def update_profile(cls,id,value):
        cls.objects.filter(id=id).update(user_id = new_user)

    
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return self.user

    @classmethod
    def search_by_profile(cls,username):
        wanted_user = cls.objects.filter(user_id__username__icontains=username)

        return wanted_user

class Image(models.Model):
    image=models.ImageField(upload_to='pic/',)
    image_name = models.CharField(max_length =60)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True,)
    # profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
    
    caption=HTMLField()
    # likes=models.ManyToManyField(User, on_delete=models.CASCADE, related_name = 'likes', blank=True)
    # comment=models.TextField(blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)


    @classmethod
    def save_image(self):

        self.save()

    @classmethod
    def delete_image(self):
        self.delete()

    @classmethod
    def update_caption(cls,id,caption):
        caption=cls.objects.filter(caption_id=id).update(caption=caption)
        return caption

    

    def __str__(self):
        return self.caption

