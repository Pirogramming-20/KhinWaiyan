from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.db.models import Case, When, Count, IntegerField
from .forms import IdeaForm


def list(request):

    sort_by = request.GET.get('sort', 'newest')
    
    if sort_by == 'favorite':
        ideas = Idea.objects.annotate(
            is_favorited=Count(Case(When(ideastar__isnull=False, then=1)), output_field=IntegerField())
        ).order_by('-is_favorited', 'created_date')
        
    elif sort_by == 'name':
        ideas = Idea.objects.all().order_by('title')
    elif sort_by == 'created':
        ideas = Idea.objects.all().order_by('created_date')
    elif sort_by == 'newest':
        ideas = Idea.objects.all().order_by('-created_date')
    else:
        ideas = Idea.objects.all()
    
    favorited_ideas_ids = IdeaStar.objects.values_list('idea_id', flat=True)

    for idea in ideas:
        idea.is_favorited = idea.id in favorited_ideas_ids
    
    
    context = {'ideas': ideas, 'current_sort': sort_by}
    return render(request, 'ideas/idea_list.html', context)




def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        idea = Idea(title=title, content=content, image=image)
        idea.save()
        return redirect('ideas:list')
    else:
        return render(request, 'ideas/idea_list.html')
    
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Idea, IdeaStar

@csrf_exempt
def toggle_favorite(request):
    if request.method == 'POST':
        idea_id = request.POST.get('idea_id')
        idea = get_object_or_404(Idea, pk=idea_id)
        # Check if an IdeaStar object exists for this idea
        idea_star, created = IdeaStar.objects.get_or_create(idea=idea)
        if not created:
            # If the IdeaStar object already existed, delete it
            idea_star.delete()
            is_favorite = False
        else:
            # If the IdeaStar object was just created, it's a favorite
            is_favorite = True

        return JsonResponse({'success': True, 'is_favorite': is_favorite})
    return JsonResponse({'success': False}, status=400)


@csrf_exempt
def change_interest(request):
    if request.method == 'POST':
        idea_id = request.POST.get('idea_id')
        change = int(request.POST.get('change'))
        idea = get_object_or_404(Idea, pk=idea_id)

        idea.interest = max(0, idea.interest + change) # Don't allow negative interest
        idea.save()

        return JsonResponse({'success': True, 'new_interest': idea.interest})
    return JsonResponse({'success': False}, status=400)


def create(request):
    if request.method == 'GET':
        form = IdeaForm()
        context = {
            'form':form,
        }
        return render(request,'ideas/idea_create.html',context)
    
    form = IdeaForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
    return redirect('ideas:list')


def update(request,pk):
    idea = Idea.objects.get(id=pk)
    if request.method == 'GET':
        form = IdeaForm(instance = idea)
        ctx = {'form':form, 'pk':pk}
        return render(request, 'ideas/idea_update.html',ctx)
    form = IdeaForm(request.POST, request.FILES, instance=idea) # update form
    if form.is_valid():
        form.save()
    return redirect('ideas:detail',pk)

def detail(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    idea.is_favorited = IdeaStar.objects.filter(idea=idea).exists()
    return render(request, 'ideas/idea_detail.html', {'idea': idea})

def delete(request, pk):
    if request.method == 'POST':
        Idea.objects.get(id=pk).delete()
    return redirect('ideas:list')


