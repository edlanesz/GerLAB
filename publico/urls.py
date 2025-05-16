from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static 
from . import views


from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('geral/', views.geral , name='geral'),
    path('view/<int:laboratorio_id>/', views.view, name='view')
]
# if settings.DEBUG:
# Adicione esta linha para servir arquivos estáticos durante o desenvolvimento
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)