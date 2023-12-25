from django.shortcuts import render, redirect

from pages.forms import RegistrationForm
from pages.models import ScrollModel, GallaryModel, MenuModel


def home_page_view(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('pages:home')
        else:
            return render(request, 'index.html')

    scrolls = ScrollModel.objects.all().order_by('-id')[:5]
    gallaries = GallaryModel.objects.all().order_by('-id')
    menus = MenuModel.objects.all().order_by('id')
    burgers = MenuModel.objects.filter(category__title__icontains='Burgers').order_by('-id')
    pizzas = MenuModel.objects.filter(category__title__icontains='Pizzas').order_by('-id')
    salads = MenuModel.objects.filter(category__title__icontains='Salads').order_by('-id')
    fries = MenuModel.objects.filter(category__title__icontains='Fries').order_by('-id')
    drinks = MenuModel.objects.filter(category__title__icontains='Drinks').order_by('-id')
    context = {
        'scrolls': scrolls,
        'gallaries': gallaries,
        'menus': menus,
        'burgers': burgers,
        'pizzas': pizzas,
        'salads': salads,
        'fries': fries,
        'drinks': drinks

    }
    return render(request, "index.html", context)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('pages:home')
        else:
            return render(request, 'index.html')
    else:
        return render(request, 'index.html')
