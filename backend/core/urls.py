
from django.urls import path
from . import views

# UD3.7b - URLs del módulo Core

urlpatterns = [
    # Profesional
    path('profesional_list/', views.ProfesionalListView.as_view(), name='profesional_list'),
    path('profesional_detail/<int:pk>/', views.ProfesionalDetailView.as_view(), name='profesional_detail'),

    # Servicio
    path('servicio_list/', views.ServicioListView.as_view(), name='servicio_list'),
    path('servicio_detail/<int:pk>/', views.ServicioDetailView.as_view(), name='servicio_detail'),

    # Horario laboral
    path('horariolaboral_list/', views.HorarioLaboralListView.as_view(), name='horariolaboral_list'),
    path('horariolaboral_detail/<int:pk>/', views.HorarioLaboralDetailView.as_view(), name='horariolaboral_detail'),

    # Reserva
    path('reserva_list/', views.ReservaListView.as_view(), name='reserva_list'),
    path('reserva_detail/<int:pk>/', views.ReservaDetailView.as_view(), name='reserva_detail'),

    # Bloqueo de agenda
    path('bloqueoagenda_list/', views.BloqueoAgendaListView.as_view(), name='bloqueoagenda_list'),
    path('bloqueoagenda_detail/<int:pk>/', views.BloqueoAgendaDetailView.as_view(), name='bloqueoagenda_detail'),
]
