from django.shortcuts import render, redirect, get_object_or_404
from .models import MangoExport
from .forms import MangoExportForm
from django.contrib import messages

def mango_list(request):
    query = request.GET.get('search', '')

    if query.isdigit():  # Ensure it's a valid number before filtering
        mangoes = MangoExport.objects.filter(order_id=int(query))
    else:
        mangoes = MangoExport.objects.all()

    return render(request, 'exports/mango_list.html', {'mangoes': mangoes})

def mango_create(request):
    if request.method == 'POST':
        form = MangoExportForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mango Export entry created successfully.")
            return redirect('mango_list')
    else:
        form = MangoExportForm()
    return render(request, 'exports/mango_form.html', {'form': form})

def mango_update(request, pk):
    mango = get_object_or_404(MangoExport, pk=pk)
    if request.method == 'POST':
        form = MangoExportForm(request.POST, instance=mango)
        if form.is_valid():
            form.save()
            messages.success(request, "Mango Export entry updated successfully.")
            return redirect('mango_list')
    else:
        form = MangoExportForm(instance=mango)
    return render(request, 'exports/mango_form.html', {'form': form})

def mango_delete(request, pk):
    mango = get_object_or_404(MangoExport, pk=pk)
    if request.method == 'POST':
        mango.delete()
        MangoExport.reorder_ids()  # Reorder the remaining records
        messages.success(request, "Mango Export entry deleted successfully.")
        return redirect('mango_list')
    return render(request, 'exports/mango_confirm_delete.html', {'mango': mango})
