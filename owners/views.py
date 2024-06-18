from django.shortcuts import render
from django.views.generic import View
from owners.forms import Loginform,Signupform,AddProductForm
from django.contrib.auth.models import User
from api.models import Products

class HomeView(View):
    def get(self,request,*args,**kw):
        return render(request,"Home.html")

class SignupView(View):
    def get(self,request,*args,**kw):
        form =Signupform()
        return render(request,"Registration.html",{"form":form})
    def post(self,request,*args,**kw):
        form =Signupform(request.POST)
        formL =Loginform()
        if form.is_valid():
            # form.save()
            User.objects.create_user(**form.cleaned_data)
            return render(request,"Login.html",{"form":formL})
        else:
            return render(request,"Registration.html",{"form":form})
    
class LoginView(View):
    def get(self,request,*args,**kw):
        form=Loginform()
        return render(request,"Login.html",{"form":form})
    def post(self,request,*args,**kw):
        print(request.POST)
        print(request.POST.get("username"))
        print(request.POST.get("password"))
        return render(request,"Home.html")
    
class AddproductView(View):
    def get(self,request,*args,**kw):
        form=AddProductForm()
        return render(request,"Addproduct.html",{"form":form})
    def post(self,request,*args,**kw):
        form=AddProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request,"home.html")
        else:
            return render(request,"Addproduct.html",{"form":form})

        