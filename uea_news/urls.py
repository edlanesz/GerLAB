from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.static import serve
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='publico/geral/')),  # Redirecionamento para 'publico/geral'
    path('autenticacao/', include('autenticacao.urls')),
    path('publico/', include('publico.urls')),
    path('', include('core.urls')),
    path('', include('relatorio.urls')),
]

# Adicione esta linha para servir arquivos estáticos durante o desenvolvimento
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)