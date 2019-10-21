from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from tinymce.models import HTMLField

class Profile(models.Model):

    bio = models.TextField(max_length=250, null=True, blank=True, default='bio')
    profile_pic = models.ImageField(upload_to = 'pic/', blank=True, null=True)
    user=models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    


    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    # @classmethod

    def __str__(self):
        return self.username

    @classmethod
    def search_by_profile(cls,username):
        wanted_user = cls.objects.filter(user_id__username__icontains=username)

        return wanted_user

class Image(models.Model):
    image=models.ImageField(upload_to='pic/',)
    image_name = models.CharField(max_length =60)
    user = models.ForeignKey(User,related_name = 'username', on_delete=models.CASCADE, blank=True,)
    profile = models.ForeignKey(User,related_name = 'username', on_delete=models.CASCADE, blank=True)
    caption=models.TextField()
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

    # def total_likes(self)
    #     self.likes.count()

    def __str__(self):
        return self.caption


class Follow(models.Model):
    following=models.ForeignKey(User, on_delete=models.CASCADE, related_name='rel_from_set')
    follower=models.ForeignKey(User, on_delete=models.CASCADE, related_name='rel_to_set')

    # @classmethod
    # def save_following(self):
    #     self.save()

    # @classmethod
    # def delete_follower(self):
    #     self.delete()

    def __str__(self):
        return '{} follows {}'.format(self.user_to)

# User.add_to_class('following', models.ManyToManyField('self', throuh=Follow, related_name='followers',symmetrical=False))

