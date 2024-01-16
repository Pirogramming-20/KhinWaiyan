from django.shortcuts import render,redirect
from .models import LocalUser
from .forms import LocalUserForm

# Create your views here.
def user_list(request):
    users = LocalUser.objects.all()
    search_text = request.GET.get('search_text')
    if search_text:
        users = users.filter(name__icontains=search_text)
    ctx = {
        'users':users,
    }
    return render(request,'users/user_list.html',ctx)

def create(request):
    if request.method == 'GET':
        form = LocalUserForm()
        context = {
            'form':form,
        }
        return render(request,'users/user_create.html',context)
    form = LocalUserForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('users:list')

def delete(request,pk):
    if request.method == 'POST':
        LocalUser.objects.get(id=pk).delete()
    return redirect('users:list')

def update(request,pk):
    user = LocalUser.objects.get(id=pk)
    if request.method == 'GET':
        form = LocalUserForm(instance=user)
        ctx = {
            'form':form,
            'pk':pk,
        }
        return render(request,'users/user_update.html',ctx)
    form = LocalUserForm(request.POST,instance=user)
    if(form.is_valid()):
        form.save()
    return redirect('users:list')