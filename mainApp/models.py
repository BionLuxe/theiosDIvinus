from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.
import uuid
class Aboutus(models.Model):
    background = models.TextField(default="")
    biography = models.TextField(default="")
    what_we_believe = models.TextField(default="")
    vision = models.TextField(default="")
    service_times = models.TextField(default="")
    ministry_name = models.TextField(default="")
    def __str__(self):
        return self.background
    
class Banners(models.Model):
    img = models.ImageField(upload_to='media')
    caption_text = models.CharField(default="", max_length=200)

class VideoBanners(models.Model):
    video = models.FileField(upload_to='videos_uploaded',null=True,    validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
   
class VideoSermons(models.Model):
    datetime = models.DateTimeField(auto_now=True)
    caption = models.CharField(max_length=500)
    youtube_url = models.URLField(default="",)
    pastor_name = models.CharField(max_length=100)

class EnglishAudioSermons(models.Model):
    datetime = models.DateTimeField(auto_now=True)
    caption = models.CharField(max_length=200)
    audio = models.FileField(upload_to='audio_uploaded',null=True,    validators=[FileExtensionValidator(allowed_extensions=['wav','mp3','AIFF','aac','ogg','m4a'])])
    pastor_name= models.CharField(max_length=100)

class LugandaAudioSermons(models.Model):
    datetime = models.DateTimeField(auto_now=True)
    caption = models.CharField(max_length=200)
    audio = models.FileField(upload_to='audio_uploaded',null=True,    validators=[FileExtensionValidator(allowed_extensions=['wav','mp3','AIFF','aac','ogg','m4a'])])
    pastor_name= models.CharField(max_length=100)

class Events(models.Model):
    name = models.CharField(max_length=200)
    details = models.TextField()
    date = models.DateTimeField(auto_now=True)
    video = models.FileField(upload_to='videos_uploaded',null=True,    validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    images = models.FileField(upload_to='media')

class News(models.Model):
    name = models.CharField(max_length=200)
    details = models.TextField()
    date = models.DateTimeField(auto_now=True)
    image = models.FileField(upload_to='media')

class OngoingProjects(models.Model):
    title = models.CharField(max_length=200)
    video = models.FileField(default="",upload_to='videos_uploaded',null=True,    validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    details = models.TextField()
    coverphoto = models.ImageField(upload_to="media",null=True)
    def __str__(self):
        return self.title

class PostImage(models.Model):
    post = models.ForeignKey(OngoingProjects, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'media',null=True)
 
    def __str__(self):
        return self.post.title
class Testimonials(models.Model):
    names = models.CharField(max_length=200)
    video = models.FileField(upload_to='videos_uploaded', null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    testimony = models.TextField()
    image = models.ImageField(upload_to="media",null=True)
    
    def __str__(self):
        return self.names

class TestimonyImages(models.Model):
    post = models.ForeignKey(Testimonials, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'media',null=True)
 
    def __str__(self):
        return self.post.names

class Ministries(models.Model):
    image = models.ImageField(upload_to="media")
    details = models.TextField()
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title

class Quotes(models.Model):
    Quote = models.TextField()
    From = models.CharField(max_length=500)

class OurHistory(models.Model):
    background = models.TextField(default="")
    image = models.FileField(upload_to='media',default="")
class Whatwebelieve(models.Model):
    what_we_believe = models.TextField(default="")
    image = models.FileField(upload_to='media',default="")
class Vision(models.Model):
    vision = models.TextField(default="")
    image = models.FileField(upload_to='media', default="")

class Servicetimes(models.Model):
    servicetimes = models.TextField(default="")

class MinistryName(models.Model):
    ministryName = models.TextField(default="")
    image = models.FileField(upload_to='media',default="")

class Tdaccf(models.Model):
    TDACCF = models.TextField(default="")
    image = models.FileField(upload_to='media',default="")

class OurStaff(models.Model):
    member_image = models.ImageField(upload_to='media')
    member_title = models.CharField(max_length=200)
    member_name = models.CharField(max_length=200)
    member_biography = models.TextField()

class Gallery(models.Model):
    image = models.ImageField(upload_to='media')

class Question(models.Model):
    question = models.TextField()
    answer = models.TextField()
    date = models.DateTimeField(auto_now=True)

class Articles(models.Model):
    question = models.TextField()
    answer = models.TextField()
    date = models.DateTimeField(auto_now=True)

