from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns=[
             path('signup/',views.signup_function),
             path('signupx/',views.sign_up),
             path('postform/',views.postform_function, name='post'),
             
             path('login/', auth_view.LoginView.as_view(template_name='loginform.html'))



]