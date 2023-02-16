from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    author=models.CharField(max_length=255)
    last_update=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title



class Comment(models.Model):
    email=models.EmailField()
    description=models.TextField()
    last_update=models.DateTimeField(auto_now_add=True)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)    
  
    def __str__(self):
        return self.email


class Profile(models.Model):
    name=models.CharField(max_length=255,null=True)
    email=models.EmailField(null=True)
    password=models.CharField(max_length=255,null=True)
    date_of_birth=models.DateField()
    proffession=models.CharField(max_length=255)
    #post=models.ForeignKey(Post,on_delete=models.CASCADE)

    