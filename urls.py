from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),  # Root URL now event list!
    path('candidate/register/', views.candidate_register, name='candidate_register'),
    path('candidate/login/', views.candidate_login, name='candidate_login'),
    path('candidate/logout/', views.candidate_logout, name='candidate_logout'),
    path('events/', views.event_list, name='event_list'),  # Duplicate for direct events path
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
