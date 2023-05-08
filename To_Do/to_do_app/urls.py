from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="todo"),
	path('del/<str:item_id>', views.remove, name="del"),
	path('update/<str:pk>', views.update, name="update"),
    path('generate-pdf/', views.generate_pdf, name='pdf'),

    ]
