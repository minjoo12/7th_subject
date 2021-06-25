from django.shortcuts import render, redirect, get_object_or_404
from .models import Signup
from django.utils import timezone

# Create your views here.

def home(request):
    signups = Signup.objects.all()
    return render(request, "home.html", {'signups':signups})

def detail(request, id):
    signup = get_object_or_404(Signup, pk=id)
    return render(request, "detail.html", {'signup':signup})

def new(request):
    return render(request, "new.html")

def create(request):
    new_signup = Signup()
    new_signup.name = request.POST['name']
    new_signup.age = request.POST['age']
    new_signup.pub_date = timezone.now()
    new_signup.email = request.POST['email']
    new_signup.introduce = request.POST['introduce']
    new_signup.save()
    return redirect("detail", str(new_signup.id))

def edit(request, id):
    edit_signup = Signup.objects.get(pk=id)
    return render(request, "edit.html", {'signup': edit_signup})

def update(request, id):
    update_signup = Signup.objects.get(pk=id)
    update_signup.name = request.POST['name']
    update_signup.age = request.POST['age']
    update_signup.pup_date = timezone.now()
    update_signup.email = request.POST['email']
    update_signup.introduce = request.POST['introduce']
    update_signup.save()
    return redirect("detail", str(update_signup.id))

def delete(reuqest, id):
    delete_signup = Signup.objects.get(pk=id)
    delete_signup.delete()
    return redirect("home")