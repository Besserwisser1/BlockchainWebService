from django.urls import path
from . import views
# from views import *

urlpatterns = [
	path('', views.home, name='home'),
	path('about/', views.about, name='about'),
	path('lists/', views.lists, name='lists_str'),
]

