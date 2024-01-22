from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main:home')  
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def home(request):
    posts = Post.objects.all().order_by('-created_at') #최신순
    for post in posts:
        post.is_liked = post.likes.filter(user=request.user).exists()
    return render(request, 'main/home.html' , {'posts':posts})

@csrf_exempt
def toggle_like(request):
    if request.method == 'POST':
        # receive json id & type  from ajax 
        data = json.loads(request.body)
        post_id = data['post_id']

        # get post object using id from ajax
        post = Post.objects.get(pk=post_id)
        if request.user.is_authenticated:  # Check if the user is authenticated
            # Check if an like object exists for this idea
            like, created = Like.objects.get_or_create(post=post, user=request.user)
            if not created:
                # If the like object already existed, delete it
                like.delete()
                is_liked = False
            else:
                # If the like object was just created, it's liked
                is_liked = True

            return JsonResponse({'success': True, 'post_id': post_id,'is_liked': is_liked, 'like_count': post.likes.count()}) #post.likes.count() instead of post.like_set.count()
        else:
            return JsonResponse({'success': False, 'error': 'User is not authenticated'}, status=403)  #  unauthenticated user
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)  #  non-POST requests


@csrf_exempt
def add_comment(request):
    if request.method == 'POST' and request.user.is_authenticated:
        data = json.loads(request.body)
        post_id = data.get('post_id')
        content = data.get('content')
        post = Post.objects.get(pk=post_id)
        comment = Comment.objects.create(user=request.user, post=post, content=content)
        return JsonResponse({'comment_id': comment.id,'post_id': post_id, 'username': request.user.username, 'content': content})

@csrf_exempt
def delete_comment(request):
    if request.method == 'POST' and request.user.is_authenticated:
        data = json.loads(request.body)
        comment_id = data.get('comment_id')
        comment = Comment.objects.get(pk=comment_id, user=request.user)
        comment.delete()
        return JsonResponse({'success': True, 'comment_id': comment_id, 'post_id': comment.post.id})
    

from django.contrib.auth.decorators import login_required

@login_required  #  ensure only logged-in users can create posts
def create_post(request):
    if request.method == 'POST':
        image = request.FILES.get('image')  # Get the uploaded image
        user = request.user
        
        # Create and save the new post
        post = Post.objects.create(user=user, image=image)
        return redirect('main:home')  
        
    return render(request, 'main/create_post.html')  


@csrf_exempt
def delete_post(request):
    if request.method == 'POST' and request.user.is_authenticated:
        post_id = request.POST.get('post_id')
        post = Post.objects.get(pk=post_id)
        
        # Check if the current user is the owner of the post
        if post.user == request.user:
            post.delete()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'error': 'Unauthorized'}, status=403)
    return JsonResponse({'error': 'Invalid request'}, status=400)