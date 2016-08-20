from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from posts.views import index, liveblog


urlpatterns = [
    url(r'^$', index),
    url(r'^admin/', admin.site.urls),
    url(r'^channels-api/', include('channels_api.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
