from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import SignupForm,PostForm
from .form import SignUpForm
from django.contrib import messages

def signup_function(request):
    
     if request.method=="POST":
          signupform=SignupForm(request.POST)
          if signupform.is_valid():
               signupform.save()
               messages.success(request,('signup complete!!welcome blogger'))
               return redirect('post')
          else:
               signupform=SignupForm()
               messages.success(request,('user sign validation rules not followed.try again!!'))
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
     postform=PostForm()
     return render(request,'postform.html',{'form':postform})



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


