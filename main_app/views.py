from django.shortcuts import render, redirect
from main_app.models import Sales , Genres , Photo
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import ModForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3
S3_BASE_URL = 'https://s3.ca-central-1.amazonaws.com/'
BUCKET = 'summersteamsale'
# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request,'about.html')
@login_required
def index(request):
    sales = Sales.objects.filter(user=request.user)
    return render(request, 'sales/index.html', { 'sales': sales })
@login_required
def sale_detail(request, sales_id):
  sale = Sales.objects.get(id=sales_id)
  genres_sale_doesnt_have = Genres.objects.exclude(id__in = sale.genres.all().values_list('id'))
  mod_form = ModForm()
  return render(request, 'sales/detail.html', { 'sale': sale , 'mod_form': mod_form ,'genres': genres_sale_doesnt_have })

class SalesCreate(LoginRequiredMixin,CreateView):
  model = Sales
  fields = ['name', 'ogprice', 'percentage', 'afprice']
  def form_valid(self, form):
    form.instance.user = self.request.user 
    return super().form_valid(form)

class SalesUpdate(LoginRequiredMixin,UpdateView):
  model = Sales
  fields = ['ogprice', 'percentage', 'afprice']

class SalesDelete(LoginRequiredMixin,DeleteView):
  model = Sales
  success_url = '/sales/'
@login_required
def add_mod(request, sale_id):
  form = ModForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.sale_id = sale_id
    new_feeding.save()
  return redirect(f'/sales/{sale_id}', sale_id=sale_id)

class GenresList(LoginRequiredMixin,ListView):
  model = Genres

class GenresDetail(LoginRequiredMixin,DetailView):
  model = Genres

class GenresCreate(LoginRequiredMixin,CreateView):
  model = Genres
  fields = '__all__'

class GenresUpdate(LoginRequiredMixin,UpdateView):
  model = Genres
  fields = ['name', 'color']

class GenresDelete(LoginRequiredMixin,DeleteView):
  model = Genres
  success_url = '/genres/'

@login_required
def assoc_genres(request, sale_id, genres_id):
  Sales.objects.get(id=sale_id).genres.add(genres_id)
  return redirect(f'/sales/{sale_id}', sale_id = sale_id)


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def add_photo(request, sale_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        print(s3.list_buckets())
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        s3.upload_fileobj(photo_file, BUCKET, key)
        # build the full url string
        url = f"{S3_BASE_URL}{BUCKET}/{key}"
        # we can assign to cat_id or cat (if you have a cat object)
        photo = Photo(url=url, sales_id=sale_id)
        print(sale_id)
        photo.save()
        print(photo)
    return redirect(f'/sales/{sale_id}', sale_id=sale_id)