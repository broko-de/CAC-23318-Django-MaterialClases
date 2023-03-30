from django.urls import path

from . import views

urlpatterns = [    
    path('', views.index, name='inicio'),
    path('quienes_somos', views.quienes_somos, name='quienes_somos'),
    path('saludar/<str:nombre>',views.saludar)
]