from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import SignupForm,PostForm
from .form import SignUpForm
from django.contrib import messages
from .models import Post
def index_function(request):
     return render(request,'index.html')




def signup_function(request):   
     if request.method=="POST":
          signupform=SignupForm(request.POST)
          if signupform.is_valid():
               signupform.save()
               messages.success(request,('signup complete!!welcome blogger'))
               return redirect('post')
          else:
               signupform=SignupForm()
               messages.success(request,('user signup validation rules not followed.try again!!'))
               return render(request,'signupform.html',{'form':signupform})
               
               #return HttpResponse('error') 
     else:     
          signupform=SignupForm()
     return render(request,'signupform.html',{'form':signupform})



def sign_up(request):
     if request.method=='POST':
          form=SignUpForm(request.POST )
          if form.is_valid():
             form.save(commit=True)

     # postform=PostForm()
     # return render(request,'postform.html',{'form':postform})     
          else:
              return HttpResponse("NO BUG BUT NOT SAVED!")

     else:
          form=SignUpForm() 
          return render(request,'signupform.html',{'form':form})


def postform_function(request):
          if request.method=='POST':
               postform=PostForm(request.POST)
               if postform.is_valid():
                    postform.save()
                    print('hiiiiiiiiiiiiiiiiiiiiiiii')
                    messages.success(request,('your post created!!!'))
                    return redirect('post_show')
               else:
                    return HttpResponse('BUGGGGGGGGGG')     

          else:     
               postform=PostForm()
               return render(request,'postform.html',{'form':postform})


def post_show_function(request):
     return render(request,'post_show.html')




def show_all_post_function(request):
     queryset=Post.objects.all()
     return render(request,'showallpost.html' ,{'queryset':queryset})





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


