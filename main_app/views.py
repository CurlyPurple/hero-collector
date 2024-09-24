from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from .models import Hero, Workout
from .forms import TrainingForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin


class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def hero_index(request):
  heroes = Hero.objects.filter(user=request.user)
  return render(request, 'heroes/index.html', { 'heroes': heroes })

@login_required
def hero_detail(request, hero_id):
  hero = Hero.objects.get(id=hero_id)
  workouts_doesnt_have = Workout.objects.exclude(id__in = hero.workouts.all().values_list('id'))
  training_form = TrainingForm()
  return render(request, 'heroes/detail.html', {
    # Add the toys to be displayed
    'hero': hero, 'training_form': training_form, 'workouts': workouts_doesnt_have
  })

@login_required
def add_training(request, hero_id):
  # create a ModelForm instance using the data in request.POST
  form = TrainingForm(request.POST)
  # validate the form
  if form.is_valid():
    new_training = form.save(commit=False)
    new_training.hero_id = hero_id
    new_training.save()
  return redirect('hero-detail', hero_id=hero_id)

@login_required
def assoc_workout(request, hero_id, workout_id):
  # Note that you can pass a toy's id instead of the whole object
  Hero.objects.get(id=hero_id).workouts.add(workout_id)
  return redirect('hero-detail', hero_id=hero_id)

class HeroCreate(LoginRequiredMixin, CreateView):
  model = Hero
  fields = ['name', 'power', 'description', 'age']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class HeroUpdate(LoginRequiredMixin, UpdateView):
  model = Hero
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['power', 'description', 'age']

class HeroDelete(LoginRequiredMixin, DeleteView):
  model = Hero
  success_url = '/heroes/'

class WorkoutCreate(LoginRequiredMixin, CreateView):
  model = Workout
  fields = '__all__'

class WorkoutList(LoginRequiredMixin, ListView):
  model = Workout

class WorkoutDetail(LoginRequiredMixin, DetailView):
  model = Workout

class WorkoutUpdate(LoginRequiredMixin, UpdateView):
  model = Workout
  fields = ['name', 'weight']

class WorkoutDelete(LoginRequiredMixin, DeleteView):
  model = Workout
  success_url = '/workouts/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in
      login(request, user)
      return redirect('hero-index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
  # Same as: return render(request, 'signup.html', {'form': form, 'error_message': error_message})