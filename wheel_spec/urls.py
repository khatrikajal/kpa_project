from django.urls import path
from . import views

urlpatterns = [
    path('forms/wheel-specifications', views.get_filtered_wheel_specs, name='get_filtered_wheel_specs'),
    path('forms/wheel-specifications/', views.submit_wheel_spec, name='submit_wheel_spec'),
]
