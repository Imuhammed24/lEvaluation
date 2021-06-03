from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from .views import index


admin.site.site_header = "ADMINISTRATION BACK-END"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome to your portal"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('accounts/', include(('account.urls', 'account'), namespace='account')),
    path('assessment/', include(('assessment.urls', 'assessment'), namespace='assessment')),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
