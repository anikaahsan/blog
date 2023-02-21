from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns=[
             path('',views.index_function),
             path('signup/',views.signup_function ,name='signup'),
             path('signupx/',views.sign_up),
             path('postform/',views.postform_function, name='post'),
             path('post_show/',views.post_show_function, name='post_show'),
             path('login/', auth_view.LoginView.as_view(template_name='loginform.html') ,name='login'),
             path('showallpost',views.show_all_post_function ,name='show_all_post')



]