from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('libros', views.listar_libros, name="listar_libros"),
    path('crear_libros/', views.crear_libros, name='crear_libros'),
    path('libros/<int:pk>/', views.detalles_libros, name='detalles_libros'),
    path('libros/<int:pk>/editar/', views.editar_libros, name='editar_libros'),
    path('libros/<int:pk>/eliminar/', views.eliminar_libros, name='eliminar_libros'),
    path('autores', views.listar_autores, name="listar_autores"),
    path('crear_autores/', views.crear_autores, name='crear_autores'),
    path('autores/<int:pk>/', views.detalles_autores, name='detalles_autores'),
    path('autores/<int:pk>/editar/', views.editar_autores, name='editar_autores'),
    path('autores/<int:pk>/eliminar/', views.eliminar_autores, name='eliminar_autores'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
