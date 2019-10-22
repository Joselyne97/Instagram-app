from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from tinymce.models import HTMLField

class Profile(models.Model):

    bio = HTMLField()
    profile_pic = models.ImageField(upload_to = 'pic/', blank=True, null=True)
    full_name = models.CharField(max_length=60)
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
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    caption=HTMLField()
    likes=models.IntegerField(blank=True, null=True)
    comments=models.CharField(max_length=100, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)


    
    def save_image(self):

        self.save()

    
    def delete_image(self):
        self.delete()

    

    @classmethod
    def update_caption(cls,id,caption):
        caption=cls.objects.filter(caption_id=id).update(caption=caption)
        return caption

    @classmethod
    def get_images(cls):
        images=cls.objects.all().prefetch_related('comment_set')
        return images

    def __str__(self):
        return self.caption



class Comment(models.Model):
    comment = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    pub_date = models.DateTimeField(auto_now_add=True)

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    def __str__(self):
        return self.comment



