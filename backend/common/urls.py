
from django.urls import path
from . import views

# UD3.7b - URLs del módulo Common
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('panel/', views.PanelView.as_view(), name='panel'),
]
