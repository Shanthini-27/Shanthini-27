from django.shortcuts import render, redirect
from .models import Table
from .forms import TableForm

def table_list(request):
    tables = Table.objects.all()
    return render(request, 'Tableapp/table_list.html', {'tables': tables})

def create_table(request):
    if request.method == 'POST':
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('table_list')
    else:
        form = TableForm()
    return render(request, 'Tableapp/create_table.html', {'form': form})

def update_table(request, pk):
    table = Table.objects.get(pk=pk)
    if request.method == 'POST':
        form = TableForm(request.POST, instance=table)
        if form.is_valid():
            form.save()
            return redirect('table_list')
    else:
        form = TableForm(instance=table)
    return render(request, 'Tableapp/update_table.html', {'form': form})

def delete_table(request, pk):
    table = Table.objects.get(pk=pk)
    if request.method == 'POST':
        table.delete()
        return redirect('table_list')
    return render(request, 'Tableapp/delete_table.html', {'table': table})
