from django.shortcuts import render, get_object_or_404
from .models import Post # . means current directory or current application
from django.utils import timezone

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') # filter posts that are published
    return render(request, 'blog/post_list.html', {'posts': posts}) # show post_list.html template #'posts': posts is parameter to be passed to template

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk) # get post with pk=pk or return 404 error
    return render(request, 'blog/post_detail.html', {'post': post}) # show post_list.html template #'posts': posts is parameter to be passed to template