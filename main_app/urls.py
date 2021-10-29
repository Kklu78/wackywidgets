from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.WidgetCreate, name='widget_create'),
    path('<int:widget_id>/delete/', views.WidgetDelete, name='widget_delete')
]