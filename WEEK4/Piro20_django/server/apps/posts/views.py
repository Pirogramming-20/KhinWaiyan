from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

# Create your views here.
def main(request):
    search_txt = request.GET.get('search_txt')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    posts = Post.objects.all()  # SELECT * FROM posts_post;     # in the form of QuerySet

    # filtering
    if search_txt:
        posts = posts.filter(title__icontains=search_txt)  # SELECT * FROM posts_post WHERE title LIKE '%search_txt%';
    if min_price:
        posts = posts.filter(price__gte=min_price)
    if max_price:
        posts = posts.filter(price__lte=max_price)
    context = {'posts':posts}
    return render(request, 'posts/post_list.html', context)

def create(request):
    if request.method == 'GET':
        form = PostForm()
        context = {'form':form}
        return render(request, 'posts/post_create.html', context)
    
    # POST 일떄
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
    return redirect('posts:main')

def detail(request,pk):
    post = Post.objects.get(id=pk)
    ctx = {'post':post}
    return render(request, 'posts/post_detail.html',ctx)


def delete(request,pk):
    if request.method == 'POST':
        Post.objects.get(id=pk).delete()
    return redirect('posts:main')

def update(request,pk):
    post = Post.objects.get(id=pk)
    if request.method == 'GET':
        form = PostForm(instance = post)
        ctx = {'form':form, 'pk':pk}
        return render(request, 'posts/post_update.html',ctx)
    form = PostForm(request.POST, request.FILES, instance=post) # update form
    if form.is_valid():
        form.save()
    return redirect('posts:detail',pk)