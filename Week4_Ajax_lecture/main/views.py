from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    ctx = {
        'posts': posts,
    }
    return render(request, 'main/post_list.html', ctx)


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:post_list')
        else:
            ctx = {
                'form': form,
            }
            return render(request, 'main/post_new.html', ctx)
    elif request.method == 'GET':
        form = PostForm()
        ctx = {
            'form': form,
        }
        return render(request, 'main/post_new.html', ctx)

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt  

@csrf_exempt
def like_ajax(request):
    # receive json id & type  from ajax 
    req = json.loads(request.body) # json to python dict
    post_id = req['id']
    button_type = req['type']

    # get post object using id from ajax
    post = Post.objects.get(id=post_id)

    # update like or dislike
    if button_type == 'like':
        post.like += 1
    else :
        post.dislike += 1
    post.save() # save to db

    # return JsonResponse({'id': post_id, 'type':button_type, 'like_cnt':post.like, 'dislike_cnt':post.dislike})
    return JsonResponse({'id': post_id, 'type':button_type}) # return json to ajax
# another method is passing num of like and dislike to ajax

