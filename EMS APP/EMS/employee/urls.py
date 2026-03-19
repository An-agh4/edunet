from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('home',views.home, name='home'),
    path('list',views.emp_list, name='employee'),
    path('about/',views.about, name='about'),
]
