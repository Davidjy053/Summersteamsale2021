from django.shortcuts import render, redirect
from main_app.models import Sales
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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
  mod_form = ModForm()
  return render(request, 'sales/detail.html', { 'sale': sale , 'mod_form': mod_form })

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
  return redirect('detail', sales_id=sale_id)