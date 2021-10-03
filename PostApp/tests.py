from django.test import TestCase
from PostApp.models import *
from django.utils import timezone


class postmanTestCase(TestCase):
    def setUp(self):

        Postman.objects.create(Username="user3", Password="user3", Full_Name="user1_user1", Age=25,
                               Birthday=timezone.now(), Postman_Title="admin")
        Postman.objects.create(Username="user2", Password="user2", Full_Name="user2_user2", Age=30,
                               Birthday=timezone.now(), Postman_Title="agent")
    def Postman_fields(self):
        """Animals that can speak are correctly identified"""
        user1 = Postman.objects.get(Username="user1")
        user2 = Postman.objects.get(Username="user2")
        self.assertEqual(user1.Username, 'user1')
        self.assertEqual(user2.Username, 'user2')


class postTestCase(TestCase):
    def setUp(self):
        Postman1=Postman.objects.create(Username="user1", Password="user1", Full_Name="user1_user1", Age=25,
                               Birthday=timezone.now(), Postman_Title="admin")
        Postman2=Postman.objects.create(Username="user2", Password="user2", Full_Name="user2_user2", Age=30,
                               Birthday=timezone.now(), Postman_Title="agent")
        Post.objects.create(Post_Name="post1", Postal_code="5113", Post_longitude=8496854165,
                               Post_latitude=8496854165, Post_city="mahdia", Post_current_Number=23, Postman_working_in=Postman1)
        Post.objects.create(Post_Name="post2", Postal_code="5114", Post_longitude=984655,
                            Post_latitude=65453, Post_city="mahdia", Post_current_Number=52, Postman_working_in=Postman2)

    def Post_fields(self):

        Post1 = Post.objects.get(Post_Name="post1")
        Post2 = Post.objects.get(Post_Name="post2")
        self.assertEqual(Post1.Post_current_Number, "23")
        self.assertEqual(Post2.Post_current_Number, "52")
    # Create your tests here.
