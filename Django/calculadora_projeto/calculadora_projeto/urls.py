from django.contrib import admin
from django.urls import path
from calculadora_app.views import calculadora, calcular

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculadora/', calculadora, name='calculadora'),
    path('calcular/', calcular, name='calcular'),
]
