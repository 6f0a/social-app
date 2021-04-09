from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import User,Posts,Profile

def index(request):
    p = Posts.objects.all()
    if request.method == 'POST':
        post = request.POST["Posting"]
        p = Posts()
        p.posts = post
        p.user = request.user
        p.save()
        return HttpResponseRedirect(reverse('index'))
    paginator = Paginator(p, 10)
    if request.GET.get("page") != None:
        try:
            p = paginator.page(request.GET.get("page"))
        except:
            p = paginator.page(1)
    else:
        p = paginator.page(1)
    return render(request, "network/index.html",{
        "Posts":p,
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            profile = Profile.objects.create(user = user)
            profile.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

def profile(request,user):
    Username = User.objects.get(username=user)
    posts = Posts.objects.filter(user=Username)
    Following = Profile.objects.get(user=Username)
    paginator = Paginator(posts, 10)
    if request.GET.get("page") != None:
        try:
            posts = paginator.page(request.GET.get("page"))
        except:
            posts = paginator.page(1)
    else:
        posts = paginator.page(1)
    return render(request,"network/profile.html",{
        "Username":Username,
        "Posts":posts,
        "Following":Following,
    })
def follow(request,user):
    Username = User.objects.get(username=user)
    Following = Profile.objects.get(user=request.user)
    Following1 = Profile.objects.get(user=Username)
    if Username in Following.following.all():
        Following.following.remove(Username)
        Following.save()
        Following1.followers.remove(Username)
        Following1.save()
        messages.success(request, 'Removed From Watchlist!')
        return HttpResponseRedirect(reverse('profile',args=(Username,)))
    else:
        Following.following.add(Username)
        Following.save()
        Following1.followers.add(Username)
        Following1.save()
        messages.success(request, 'Added to Watchlist!')
        return HttpResponseRedirect(reverse('profile',args=(Username,)))

def following(request):
    Following = Profile.objects.get(user=request.user)
    Following1 = Following.following.all()
    p = Posts.objects.filter(user__in=Following1)
    paginator = Paginator(p, 10)
    if request.GET.get("page") != None:
        try:
            p = paginator.page(request.GET.get("page"))
        except:
            p = paginator.page(1)
    else:
        p = paginator.page(1)
    return render(request,'network/following.html',{
        'Posts':p,
        'Following':Following1
    })

@csrf_exempt
def edit(request, post_id):
    post = Posts.objects.get(id=post_id)

    if request.method == "PUT":
        data = json.loads(request.body)
        if data.get("post") is not None:
            post.posts = data["post"]
        post.save()
        return HttpResponse(status=204)

@csrf_exempt
def like(request, post_id):
    post = Posts.objects.get(id=post_id)
    profile = request.user

    if request.method == "PUT":
        data = json.loads(request.body)
        print(data.get("like"))
        if data.get("like"):
            post.like.add(profile)
        else: # unlike
            post.like.remove(profile)
        post.save()
        return HttpResponse(status=203)
    





