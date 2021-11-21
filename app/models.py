from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.fields import URLField
from django.http import request
from django.shortcuts import render
from embed_video.fields import EmbedVideoField
from django.urls import reverse
from PIL import Image
from ckeditor.fields import RichTextField

# Create your models here.

SERVICE_TYPE={
    ('WebD','Web Development'),
    ('AppD','App Development'),
    ('SoftD','Software Development'),
    ('DgtlM','Digtial Marketing')

}

class Quote(models.Model):
    full_name       = models.CharField(max_length=50, unique=True)
    email           = models.EmailField()
    contact_number  = models.IntegerField()
    country         = models.CharField(max_length=100)
    whatsapp_number = models.IntegerField()
    budget          = models.IntegerField(blank=True)
    field           = models.CharField(max_length=50, choices=SERVICE_TYPE, blank=True)
    description     = models.TextField(max_length=1000)
    document        = models.FileField(upload_to='quote_file/', max_length=100, blank=True)

    def __str__(self) -> str:
        return self.full_name

class Project(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    category = models.ForeignKey('Category', on_delete= models.CASCADE,  blank=True)
    description = models.CharField(max_length=50)
    url_link = models.URLField()
    image = models.ImageField(null=True, blank=True,upload_to='project/' ,default="default.jpg")

    def __str__(self):
        return f'{self.title} - {self.category}'
        


class Team(models.Model):
    name=models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    fb_link = URLField(blank=True)
    insta_link = URLField(blank=True)
    linked_in_link = URLField(blank=True)
    twitter_link = URLField(blank=True)
    image = models.ImageField(null=True, blank=True,upload_to='team_member/' ,default="default.jpg")

    def __str__(self) -> str:
        return self.name
    




class Careers(models.Model):
    categories = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    deadline = models.DateField(auto_now=False, auto_created=False)
    description = models.TextField()
    work_experience = models.CharField(max_length=50)
    education = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title

class Package(models.Model):
    title = models.CharField(max_length=250)
    price = models.IntegerField()
    Discount = models.IntegerField()

    def __str__(self) -> str:
        return self.title

# class Service(models.Model):
#     title = models.CharField(max_length=250)
#     description = models.CharField(max_length=500)

class Testimonials(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True,upload_to='testimonials/' ,default="default.jpg")
    description = models.CharField(max_length=500)

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    comments = models.CharField(max_length=200)

    def __str__(self):
        return self.name
class Home(models.Model):
    name='home-data'
    positive_reviews = models.IntegerField()
    team_members = models.IntegerField()
    happy_client = models.IntegerField()
    completed_projects = models.IntegerField()
    video = EmbedVideoField(blank=True)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=250)
    blog_slug = models.SlugField(max_length=250, blank=True)
    image = models.ImageField(null=True, blank=True,upload_to='media/blogs/' ,default="default.jpg")
    created_by= models.ForeignKey(User, on_delete= models.CASCADE)
    published_date = models.DateField(auto_now_add=True)
    description = RichTextField(blank=True, null=True)
    vote = models.IntegerField()

    # def get_url(self):
    #     return reverse('single-blog', args=[self.slug])

    def __str__(self):
        return self.title

class Gallery(models.Model):
    image = models.ImageField(null=True, blank=True,upload_to='blogs/' ,default="default.jpg")
    description = models.TextField()

    def __str__(self):
        return self.description

class Package_order(models.Model):
    package_field = models.CharField(max_length=10, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=False)
    number = models.IntegerField()
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    document = models.FileField(upload_to='package_file/', max_length=100, blank=True)

    def __str__(self):
        return self.name

class Subscribe(models.Model):
    email_address = models.EmailField()

    def __str__(self) -> str:
        return self.email_address
    
class Faq(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question

class Category(models.Model):
    name= models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    category_slug = models.SlugField(max_length=50, blank=True)
    description = models.CharField(max_length=250, blank=True)
    image = models.ImageField(null=True, blank=True,upload_to='category/' ,default="default.jpg")



    def get_url(self):
        return reverse('project_by_category', args=[self.category_slug])

    def __str__(self):
        return self.name