from django.contrib import admin
from django.urls import path, include
from car_dashboard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),  # Root URL for dashboard
    path('api/car/', include('car_dashboard.urls')),
]
