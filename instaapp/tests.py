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
    
    
    def test_delete_method(self):
        self.new_profile.delete_profile()
        self.assertEqual(len(Profile.objects.all()),0)


         
