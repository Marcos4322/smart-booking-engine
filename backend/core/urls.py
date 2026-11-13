
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

    # UD4.2b - URLs de Profesional
    path('profesional_create/', views.ProfesionalCreateView.as_view(), name='profesional_create'),
    path('profesional_update/<int:pk>/', views.ProfesionalUpdateView.as_view(), name='profesional_update'),
    path('profesional_delete/<int:pk>/', views.ProfesionalDeleteView.as_view(), name='profesional_delete'),

    # UD4.2b - URLs de Servicio
    path('servicio_create/', views.ServicioCreateView.as_view(), name='servicio_create'),
    path('servicio_update/<int:pk>/', views.ServicioUpdateView.as_view(), name='servicio_update'),
    path('servicio_delete/<int:pk>/', views.ServicioDeleteView.as_view(), name='servicio_delete'),

    # UD4.2b - URLs de HorarioLaboral
    path('horariolaboral_create/', views.HorarioLaboralCreateView.as_view(), name='horariolaboral_create'),
    path('horariolaboral_update/<int:pk>/', views.HorarioLaboralUpdateView.as_view(), name='horariolaboral_update'),
    path('horariolaboral_delete/<int:pk>/', views.HorarioLaboralDeleteView.as_view(), name='horariolaboral_delete'),

    # UD4.2b - URLs de Reserva
    path('reserva_create/', views.ReservaCreateView.as_view(), name='reserva_create'),
    path('reserva_update/<int:pk>/', views.ReservaUpdateView.as_view(), name='reserva_update'),
    path('reserva_delete/<int:pk>/', views.ReservaDeleteView.as_view(), name='reserva_delete'),

    # UD4.2b - URLs de BloqueoAgenda
    path('bloqueoagenda_create/', views.BloqueoAgendaCreateView.as_view(), name='bloqueoagenda_create'),
    path('bloqueoagenda_update/<int:pk>/', views.BloqueoAgendaUpdateView.as_view(), name='bloqueoagenda_update'),
    path('bloqueoagenda_delete/<int:pk>/', views.BloqueoAgendaDeleteView.as_view(), name='bloqueoagenda_delete'),
]
