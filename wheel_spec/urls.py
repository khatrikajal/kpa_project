from django.urls import path
from . import views

urlpatterns = [
    path('forms/wheel-specifications', views.get_filtered_wheel_specs),  # GET
    path('forms/wheel-specifications/', views.submit_wheel_spec),        # POST
]