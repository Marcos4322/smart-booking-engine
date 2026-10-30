
from django.urls import path
from . import views

# UD3.7b - URLs del módulo Billing
urlpatterns = [
    # Cliente
    path('cliente_list/', views.ClienteListView.as_view(), name='cliente_list'),
    path('cliente_detail/<int:pk>/', views.ClienteDetailView.as_view(), name='cliente_detail'),

    # Factura
    path('factura_list/', views.FacturaListView.as_view(), name='factura_list'),
    path('factura_detail/<int:pk>/', views.FacturaDetailView.as_view(), name='factura_detail'),

    # Cobro
    path('cobro_list/', views.CobroListView.as_view(), name='cobro_list'),
    path('cobro_detail/<int:pk>/', views.CobroDetailView.as_view(), name='cobro_detail'),
]
