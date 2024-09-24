from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('heroes/', views.hero_index, name='hero-index'),
  path('heroes/<int:hero_id>/', views.hero_detail, name='hero-detail'),
  path('heroes/create', views.HeroCreate.as_view(), name='hero-create'),
  path('heroes/<int:pk>/update/', views.HeroUpdate.as_view(), name='hero-update'),
  path('heroes/<int:pk>/delete/', views.HeroDelete.as_view(), name='hero-delete'),
  path('heroes/<int:hero_id>/add-training/', views.add_training, name='add-training'),
  path('heroes/<int:hero_id>/assoc-workout/<int:workout_id>/', views.assoc_workout, name='assoc-workout'),
  path('workouts/create/', views.WorkoutCreate.as_view(), name='workout-create'),
  path('workouts/<int:pk>/', views.WorkoutDetail.as_view(), name='workout-detail'),
  path('workouts/', views.WorkoutList.as_view(), name='workout-index'),
  path('workouts/<int:pk>/update/', views.WorkoutUpdate.as_view(), name='workout-update'),
  path('workouts/<int:pk>/delete/', views.WorkoutDelete.as_view(), name='workout-delete'),
  path('accounts/signup/', views.signup, name='signup'),
]