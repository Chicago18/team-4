from django.urls import path , include
from . import views 


urlpatterns = [
path("",views.index,name='index'),
path('form',views.form,name='form'),
path('house',views.housing,name='house'),
path('<int:register_id>',views.generate_pdf,name='pdf')

]