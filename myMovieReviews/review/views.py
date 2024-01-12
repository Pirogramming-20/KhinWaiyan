from django.shortcuts import render, get_object_or_404, redirect
from .models import Review
from django.views.decorators.http import require_POST


def review_list(request):
    sort_by = request.GET.get('sort', 'title')  # Default sorting is by title
    reviews = Review.objects.all().order_by(sort_by)
    for review in reviews:
        review.formatted_running_time = mins_to_hours(int(review.running_time))
    return render(request, 'review_list.html', {'reviews': reviews})

def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    review.formatted_running_time = mins_to_hours(int(review.running_time))
    return render(request, 'review_detail.html', {'review': review, 'review_detail': True})



def review_delete(request, pk):
    review = get_object_or_404(Review, pk=pk)
    review.delete()
    return redirect('review_list')


def review_create(request):
    if request.method == 'POST':
        review = Review(
            title=request.POST.get('title'),
            year = request.POST.get('year'),
            genre = request.POST.get('genre'),
            rating = request.POST.get('rating'),
            running_time = request.POST.get('running_time'),
            content=request.POST.get('content'),
            director=request.POST.get('director'),
            actors=request.POST.get('actors'),
        )
        review.save()
        return redirect('review_list')  
    return render(request, 'review_edit.html')


def review_edit(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == 'POST':
        review.title = request.POST.get('title')
        review.year = request.POST.get('year')
        review.genre = request.POST.get('genre')
        review.rating = request.POST.get('rating')
        review.running_time = request.POST.get('running_time')
        review.content = request.POST.get('content')
        review.director = request.POST.get('director')
        review.actors = request.POST.get('actors')
        review.save()
        return redirect('review_detail', pk=review.pk)  
    return render(request, 'review_edit.html', {'review': review})


def mins_to_hours(minutes):
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours}h {mins}min"
