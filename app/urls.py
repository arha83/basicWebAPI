
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('api', views.apiRoot),
    path('api/', views.apiRoot),
    path('api/vars', views.varsList),
    path('api/vars/', views.varsList),
    path('api/vars/<int:pk>', views.varsDetail),
    path('api/vars/<int:pk>/', views.varsDetail),
]