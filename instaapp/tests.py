from django.test import TestCase
from .models import Profile,Image,Comment
from django.contrib.auth.models import User
import datetime as dt

# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.new_user=User(id=1,username='Jo')
        self.new_profile=Profile(id=2,bio='lionne',profile_pic='default.jpg',full_name='jojo', user=self.new_user)


    def test_instance(self): 
        self.assertTrue(isinstance(self.new_profile,Profile))  
        self.assertTrue(isinstance(self.new_user,User))
    

    def test_save_profile(self):
        self.new_profile.save_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)>0)


    def tearDown(self):
        Profile.objects.all().delete()
    
    
    def test_delete_profile(self):
        self.new_profile.delete_profile()
        self.assertEqual(len(Profile.objects.all()),0)


         
class ImageTestClass(TestCase):
    def setUp(self):

        self.new_user=User(id=1,username='Jo')
        self.new_profile=Profile(id=2,bio='lionne',profile_pic='default.jpg',full_name='jojo', user=self.new_user)
        self.new_image=Image(id=3,image='default.jpg',image_name='lionne', user=self.new_user, profile=self.new_profile, caption='cool',likes=5,comments='comment it')

    def test_instance(self): 
        self.assertTrue(isinstance(self.new_profile,Profile))  
        self.assertTrue(isinstance(self.new_user,User))
        self.assertTrue(isinstance(self.new_image,Image))

    def test_save_image(self):
        self.new_image.save_image()
        images=Image.objects.all()
        self.assertTrue(len(images)>0)

    def tearDown(self):
        Image.objects.all().delete()

    def test_delete_image(self):
        self.new_image.delete_image()
        self.assertEqual(len(Image.objects.all()),0)
 

class CommentTestClass(TestCase):
    def setUp(self):

        self.new_user=User(id=1,username='Jo')
        self.new_image=Image(id=3,image='default.jpg',image_name='lionne', user=self.new_user, caption='cool',likes=5,comments='comment it')
        self.new_comment=Comment(id=4,comment='comments',user=self.new_user, image=self.new_image)

    def test_instance(self): 
        
        self.assertTrue(isinstance(self.new_user,User))
        self.assertTrue(isinstance(self.new_image,Image))
        self.assertTrue(isinstance(self.new_comment,Comment))


    def test_save_comment(self):
        self.new_comment.save_comment()
        comments=Comment.objects.all()
        self.assertTrue(len(comments)>0)

    def tearDown(self):
        Comment.objects.all().delete()

    def test_delete_comment(self):
        self.new_comment.delete_comment()
        self.assertEqual(len(Comment.objects.all()),0)
 

