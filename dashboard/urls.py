
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('province/', views.province_page, name='province'),
    path('distribution/', views.distribution_page, name='distribution'),
    path('trend/', views.trend_page, name='trend'),

    path('filter-data/', views.filter_data, name='filter_data'),
]


