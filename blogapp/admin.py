from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
   list_display=['title','author','description','last_update']

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=['email','description','last_update']
    
    


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=['name','email','date_of_birth','proffession']
    





