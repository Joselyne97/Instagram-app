from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    # user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(max_length=250, null=True, blank=True, default='bio')
    profile_pic = models.ImageField(upload_to = 'pic/', blank=True, null=True)
    user=models.OneToOneField(User, on_delete=models.CASCADE, blank=True)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    # @classmethod

    def __str__(self):
        return self.user.username


class Image(models.Model):
    image=models.ImageField(upload_to='pic/',)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True,)
    # profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
    caption=models.TextField()
    # likes=models.IntegerField(default=0)
    # comment=models.TextField(blank=True)

    def __str__(self):
        return self.caption

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

#     @classmethod
#     def get_image_by_id(cls, tags):
#         images = cls.objects.get(pk=id)
#         return images

#     @classmethod
#     def filter_by_tag(cls, tags):
#         images = cls.

