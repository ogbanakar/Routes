from django.contrib import admin
from django.urls import path
from bus_routes1.views import calculate_routes  # Adjusted import based on directory structure

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/calculate_routes/', calculate_routes, name='calculate_routes'),
    # ... any other URL patterns you might have ...
]
