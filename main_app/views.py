from django.shortcuts import render
from main_app.models import Sales
from django.views.generic.edit import CreateView, UpdateView, DeleteView


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
  return render(request, 'sales/detail.html', { 'sale': sale })

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