from django.test import TestCase
from .models import Profile,Image,Comment
from django.contrib.auth.models import User
# Create your tests here.

class ImageTestClass(TestCase):
    #set up method
    def setUp(self):
        
        self.user=User.objects.create(id=1,username='jo')
        self.profile=Profile.objects.create(id=1,bio='lionne',profile_pic='default.jpg',user=self.user)
        self.dadju=Image(id=1,image_name='reine',caption='dadju',comments='cool',likes='1',user=self.user)
       

    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.dadju,Image))
        self.assertTrue(isinstance(self.profile,Profile))
        self.assertTrue(isinstance(self.user,User))


    def test_save_method(self):
        self.dadju.save_image()
        image=Image.objects.all()
        self.assertTrue(len(image)>0)

    def test_delete(self):
        self.reine.save_image()
        image=Image.objects.filter(caption="dadgu").first()
        delete=Image.objects.filter(id=image.id).delete()
        image=Image.objects.all()
        self.assertTrue(len(image)==0) 

    def test_display(self):
        self.dadju.save_image()
        image=Image.objects.all()
        self.assertTrue(len(image)==1)

class ProfileTestClass(TestCase):
    def setUp(self):

        self.user=User.objects.create(id=1,username='jo')
        self.profile=Profile.objects.create(id=2,bio='lionne',profile_photo='default.jpg',user=self.user)

    #testing instance
    def test_instance(self):
        
        self.assertTrue(isinstance(self.profile,Profile))
        self.assertTrue(isinstance(self.user,User))

    def test_save_profile(self):
        self.profile.save_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)>0)

    def test_display(self):
        self.profile.save_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)==1)

    def test_delete(self):
        self.profile.save_profile()
        profile=Profile.objects.filter(bio="lionne").first()
        delete=Profile.objects.filter(id=profile.id).delete()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)==0) 
             

class CommentTestClass(TestCase):
    def setUp(self):
        self.user=User.objects.create(id=1,username='jo')
        self.dadju=Image.objects.create(id=1,image_name='reine',caption='dadju',comments='cool',likes='1',user=self.user)
        self.comment=Comment.objects.create(comment='hello',user=self.user,image=self.dadju)
       
    def test_instance(self):
        
        self.assertTrue(isinstance(self.comment,Comment))
        self.assertTrue(isinstance(self.user,User))
        self.assertTrue(isinstance(self.dadju,Image))

    def test_display(self):
        self.comment.save_comment()
        comments=Comment.objects.all()
        self.assertTrue(len(comments)==1)

    def test_delete(self):
        self.comment.save_comment()
        comment=Comment.objects.filter(comment="cool").first()
        delete=Comment.objects.filter(id=comment.id).delete()
        comments=Comment.objects.all()
        self.assertTrue(len(comments)==0) 
         
         
