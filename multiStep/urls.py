
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('plan/', include('plan.urls')),
    path('add/', include('addOn.urls')),
    path('summary/', include('summary.urls')),
    path('admin/', admin.site.urls),
]
