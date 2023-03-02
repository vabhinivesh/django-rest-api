from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview),
    path('healthcheck/', views.health_check),

    path('users', views.get_users_list),
    path('add-user/', views.create_user),
    path('user/<str:pk>/', views.get_user_data),

]
