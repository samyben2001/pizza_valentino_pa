from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header  =  "Administration Pizza Valentino"  
admin.site.site_title  =  "Administration Pizza Valentino"
admin.site.index_title  =  "Pizza Valentino Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('menu.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
