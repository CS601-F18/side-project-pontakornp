from django.urls import path

from . import views

urlpatterns = [
	path('', views.show_dashboard, name='index'),
	path('extract_stock/', views.extract_stock_data, name='stock_data'),
    path('dashboard/', views.show_dashboard, name='dashboard')
]