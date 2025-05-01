from django.urls import path # type: ignore
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('counter',views.counter, name="counter"),
    path('about', views.aboutMe, name='about'),
]

  
  