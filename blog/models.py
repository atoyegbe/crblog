from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField



class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    profile_pic = models.ImageField(default="download.png", null=True, blank=True)
    phone = models.IntegerField(null=True)
    date_created= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Blog(models.Model):
    title = models.CharField(max_length=100, null=False, unique=True)
    slug = models.SlugField(max_length=100, unique=True, null=True)
    body = RichTextField(blank=True, null=True)

    # body = models.TextField()
    creator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    date_posted= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return ('blog', (), {
            'slug': self.slug,
        })
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)
        
    

        
    

    