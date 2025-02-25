"""
URL configuration for MyApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('tables/', views.table_list, name='table_list'),
    path('tables/create/', views.create_table, name='create_table'),
    path('tables/<pk>/update/', views.update_table, name='update_table'),
    path('tables/<pk>/delete/', views.delete_table, name='delete_table'),
]


