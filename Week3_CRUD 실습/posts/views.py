from django.shortcuts import render,redirect
from .models import *

def posts_list(request):
    posts = Post.objects.all() # get all posts objects
    context = {
        'posts': posts # function name to be used in template : object
    }
    return render(request, 'posts_list.html', context)

def posts_read(request, pk):
    post = Post.objects.get(id=pk) # get post object with a certain id
    context = {
        'post': post
    }
    return render(request, 'posts_read.html', context)

def posts_create(request):
    # for submitting the form
    if(request.method == 'POST'):
        # create a new post object
        Post.objects.create(
            title=request.POST['title'], 
            user = request.POST['user'],
            content=request.POST['content']
        )
        return redirect('/posts') # redirect to posts list page
    return render(request, 'posts_create.html') # do this when get request

# # for submitting the form
# def posts_create_final(request):
#     if(request.method == 'POST'):
#         # create a new post object
#         Post.objects.create(
#             title=request.POST['title'], 
#             user = request.POST['user'],
#             content=request.POST['content']
#         )
#     return redirect('/posts') # redirect to posts list page
