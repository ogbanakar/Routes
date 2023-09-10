from django.contrib import admin
from django.urls import path
from bus_routes.views import calculate_routes
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/calculate_routes/', views.calculate_routes, name='calculate_routes'),
    # ... any other URL patterns you might have ...
]
