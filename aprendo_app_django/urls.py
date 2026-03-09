from django.contrib import admin
from django.urls import path, include

from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/signup/', core_views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('core.urls')),
]
