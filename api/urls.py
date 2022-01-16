from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_routes),
    path('quotes/', views.get_quotes),
    path('quotes/create/', views.create_quote),
    path('quotes/<int:pk>/delete/', views.delete_quote),
]
