from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/search/', views.search_api, name='search_api'),
    path('api/get-by-code/', views.get_by_code, name='get_by_code'),
]