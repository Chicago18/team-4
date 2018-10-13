from django.urls import path , include 
from . import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
path('login', auth_views.login, name='login'),
path("",views.index,name='index'),
path('form',views.form,name='form'),
path('house',views.housing,name='house'),
path('<int:register_id>',views.generate_pdf,name='pdf'),
path('home', views.logged_in,name='home'),

]