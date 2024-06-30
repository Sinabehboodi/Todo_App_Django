from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from . import models
from . import forms

def home_(request):
    return render(request, 'todoapp/home.html')


@login_required(login_url='/accounts/login')
def todo_list_view(request):
    user = request.user 
    todo_queryset = models.TodoItem.objects.filter(owner = user)
    
    if request.method == 'POST':
        checked_list = request.POST.getlist('checked')
        checked_list = [int(i) for i in checked_list]
        for todoitem in todo_queryset:
            if todoitem.id in checked_list:
                models.TodoItem.objects.filter(id = todoitem.id).update(checked=True)
            else:
                models.TodoItem.objects.filter(id = todoitem.id).update(checked=False)

        return redirect('/list')
    
    todo_item_len = len(todo_queryset)

    return render(request, 'todoapp/todo_list.html', {'todo_list':todo_queryset, 'todo_list_len':todo_item_len})



@login_required(login_url='/accounts/login')
def todo_item_create(request):
    user = request.user
    if request.method == 'POST':
        form = forms.TodoItemForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = user
            instance.save()
            return redirect('todoapp:todo_list') 
        
    form = forms.TodoItemForm()
    
    return render(request, 'todoapp/create_todo_item.html', {'form':form})


def todo_item_delete(request,pk):
    try:
        todo_item = models.TodoItem.objects.get(pk=pk)
    except:
        return redirect('todoapp:toso_list')
    
    if todo_item.owner == request.user:
        todo_item.delete()
        return redirect('/list')
    else:
        return redirect('todoapp:toso_list')
