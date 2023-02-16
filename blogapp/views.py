from django.shortcuts import render,redirect
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from django.http import HttpResponse
from blogapp.form import SignUpForm,PostForm,LoginForm


def sign_up(request):
     if request.method=='POST':
          form=SignUpForm(request.POST )
          if form.is_valid():
               form.save(commit=True)
               postform=PostForm()
               return render(request,'postform.html',{'form':postform})     
          else:
               return HttpResponse("NO BUG BUT NOT SAVED!")

     else:
         form=SignUpForm() 
         return render(request,'signupform.html',{'form':form})








# def log_in(request):
#      if request.method=="POST":
#           loginform=LoginForm(request.POST)
#           if loginform.is_valid():
#                username=loginform.cleaned_data['username']
#                password=loginform.cleaned_data['password']
#                print(username)
#                return HttpResponse('ok')

#      else:     
#           loginform=LoginForm()
#           return render(request,'loginform.html',{'form':loginform})         


