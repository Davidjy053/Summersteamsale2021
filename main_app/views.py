from django.shortcuts import render, redirect
from main_app.models import Sales , Genres
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import ModForm

# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request,'about.html')

def index(request):
    sales = Sales.objects.all()
    return render(request, 'sales/index.html', { 'sales': sales })

def sale_detail(request, sales_id):
  sale = Sales.objects.get(id=sales_id)
  genres_sale_doesnt_have = Genres.objects.exclude(id__in = sale.genres.all().values_list('id'))
  mod_form = ModForm()
  return render(request, 'sales/detail.html', { 'sale': sale , 'mod_form': mod_form ,'genres': genres_sale_doesnt_have })

class SalesCreate(CreateView):
  model = Sales
  fields = '__all__'
  success_url = '/sales/'

class SalesUpdate(UpdateView):
  model = Sales
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['ogprice', 'percentage', 'afprice']

class SalesDelete(DeleteView):
  model = Sales
  success_url = '/sales/'

def add_mod(request, sale_id):
  form = ModForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.sale_id = sale_id
    new_feeding.save()
  return redirect('detail', sale_id=sale_id)
class GenresList(ListView):
  model = Genres

class GenresDetail(DetailView):
  model = Genres

class GenresCreate(CreateView):
  model = Genres
  fields = '__all__'

class GenresUpdate(UpdateView):
  model = Genres
  fields = ['name', 'color']

class GenresDelete(DeleteView):
  model = Genres
  success_url = '/genres/'


def assoc_genres(request, sale_id, genres_id):
  Sales.objects.get(id=sale_id).genres.add(genres_id)
  return redirect('detail', sale_id=sale_id)