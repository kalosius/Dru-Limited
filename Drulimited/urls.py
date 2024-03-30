from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('druu.urls')),
    path('cart/', include('cart.urls')),
    path('payment/', include('payment.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

admin.site.site_header = "Dru Enterprises Admin"
admin.site.site_title = "Welcome to The Admin Dashboard"
admin.site.index_title = "Welcome To Dru  Enterprises Admin Dashboard "
