from django.contrib import admin
from django.urls import path
from core import views as principal
from servicios import views as service
from django.conf import settings

urlpatterns = [
    path('', principal.index, name='index'),
    path('historia/', principal.historia, name='historia'),
     path('contacto/', principal.contacto, name='contacto'),
    path('blog/', principal.blog, name='blog'),
    path('servicio/', service.servicio, name='servicio'),
    path('admin/', admin.site.urls),
]
# DEBUG esta en true, importamos static, trabajamos en modo desarrollo
# para mostrar las imagenes de las recetas en el navegador

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    # static('/media/','http://localhost/media/')





