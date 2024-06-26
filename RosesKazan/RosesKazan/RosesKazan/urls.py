
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('auth/', include('auth_sites.urls')),
    path('profile/', include('profiles.urls')),
    path('bouquet_designer/', include('bouquet_designer.urls'))
]
