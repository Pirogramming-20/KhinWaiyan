# devtool/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import DevTool
from .forms import DevToolForm

def list(request):
    search_query = request.GET.get('search_txt', '')  # Get the search query from request
    if search_query:
        devtools = DevTool.objects.filter(name__icontains=search_query)  # Filter by name containing the search_query
    else:
        devtools = DevTool.objects.all()
    
    return render(request, 'devtool/devtool_list.html', {'devtools': devtools})

def create(request):
    if request.method == 'GET':
        form = DevToolForm()
        context = {
            'form':form,
        }
        return render(request,'devtool/devtool_create.html',context)
    
    form = DevToolForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
    return redirect('devtool:list')

def detail(request, pk):
    devtool = get_object_or_404(DevTool, pk=pk)
    related_ideas = devtool.idea_set.all() # 역참조
    ctx = {'devtool':devtool, 'related_ideas':related_ideas}
    return render(request, 'devtool/devtool_detail.html', ctx)

def update(request, pk):
    devtool = get_object_or_404(DevTool, pk=pk)
    if request.method == 'GET':
        form = DevToolForm(instance = devtool)
        ctx = {'form':form, 'pk':pk}
        return render(request, 'devtool/devtool_update.html',ctx)
    form = DevToolForm(request.POST, request.FILES, instance=devtool) # update form
    if form.is_valid():
        form.save()
    return redirect('devtool:detail',pk)

def delete(request, pk):
    if request.method == 'POST':
        DevTool.objects.get(id=pk).delete()
    return redirect('devtool:list')