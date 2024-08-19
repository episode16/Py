from django.shortcuts import render, redirect
from .forms import ProductForm

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Предположим, что у вас есть представление для списка продуктов
    else:
        form = ProductForm()
    return render(request, 'myapp/add_product.html', {'form': form})
