from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from django.contrib.auth.models import User
from datetime import date, time, datetime
from cloudinary_storage.storage import VideoMediaCloudinaryStorage
from cloudinary_storage.validators import validate_video

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.name
    

    
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User,on_delete= models.CASCADE)
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to = 'images',default = 'defaults/kobydrillsdotkom.png')
    body = RichTextUploadingField()
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField(blank = True, null = True)
    
    
    def __str__(self):
        return self.title
    
    def save(self, *args,**kwargs):
        
        if self.slug == None:
            slug = slugify(self.title)
            
            slug_exist = Post.objects.filter(slug = slug).exists()
            
            count = 0
            while slug_exist:
                count += 1
                slug = slugify(self.title) + '-' + str(count)
                slug_exist = Post.objects.filter(slug = slug).exists()
                
            self.slug = slug
            
        
        super().save(*args,**kwargs)
        
    @property
    def get_body_length(self):
        length = len(self.body)
        return length
    
    
class VideoPost(models.Model):
    caption = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/%y/',storage=VideoMediaCloudinaryStorage(),validators=[validate_video])
    thumbnail = models.ImageField(null = True, blank = True, default = 'defaults/kobydrillsdotkom.png', upload_to = 'videos/%y/thumbnails')
    body = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete = models.CASCADE, blank=True, null=True)
    category = models.ManyToManyField(Category)
    date = models.DateTimeField(auto_now_add=True, blank=True, null= True)
    slug = models.SlugField(blank = True, null = True)
    
    def __str__(self):
        return self.caption
    
    def save(self,*args,**kwargs):
        
        if self.slug == None:
            slug = slugify(self.caption)
            
            count = 0
            slug_exist = VideoPost.objects.filter(slug = slug).exists()
            
            while slug_exist:
                slug = slugify(self.caption) + '-' + count
                count += 1
                
                slug_exist = VideoPost.objects.filter(slug = slug).exists()

            self.slug = slug
            
        super().save(*args,**kwargs)
        
    @property
    def get_body_length(self):
        length = len(self.body)
        return length
    
    
class PostComment(models.Model):
    post= models.ForeignKey(Post,on_delete = models.CASCADE, related_name='comments')
    name = models.CharField(max_length=200)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.post.title} - {self.name}'


class VideoPostComment(models.Model):
    video = models.ForeignKey(VideoPost,on_delete = models.CASCADE, related_name='video_comments')
    name = models.CharField(max_length=200)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.video.caption} - {self.name}'
    
class AudioPost(models.Model):
    audio = models.FileField(upload_to='audio/%y/')
    caption = models.CharField(max_length=100)
    thumbnail = models.ImageField(null = True, blank = True, default = 'defaults/kobydrillsdotkom.png', upload_to = 'audios/%y/thumbnails')
    body = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete = models.CASCADE, blank=True, null=True)
    category = models.ManyToManyField(Category)
    date = models.DateTimeField(auto_now_add=True, blank=True, null= True)
    slug = models.SlugField(blank = True, null = True)
    
    def __str__(self):
        return f'{self.caption}'
     
    def save(self,*args,**kwargs):
        
        if self.slug == None:
            slug = slugify(self.caption)
            
            count = 0
            slug_exist = VideoPost.objects.filter(slug = slug).exists()
            
            while slug_exist:
                slug = slugify(self.caption) + '-' + count
                count += 1
                
                slug_exist = VideoPost.objects.filter(slug = slug).exists()

            self.slug = slug
            
        super().save(*args,**kwargs)
        
    @property
    def get_body_length(self):
        length = len(self.body)
        return length
    

class AudioPostComment(models.Model):
    audio = models.ForeignKey(AudioPost,on_delete = models.CASCADE, related_name='audio_comments')
    name = models.CharField(max_length=200)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.audio.caption} - {self.name}'