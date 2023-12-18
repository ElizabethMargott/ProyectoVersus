from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.listar_libros, name='listar_libros'),
    path('libros/crear/', views.crear_libros, name='crear_libro'),
    path('libros/<int:pk>/', views.detalles_libros, name='detalles_libro'),
    path('libros/<int:pk>/editar/', views.editar_libros, name='editar_libro'),
    path('libros/<int:pk>/eliminar/', views.eliminar_libros, name='eliminar_libro'),
    
    path('autores', views.listar_autores, name="listar_autores"),
    path('autores/crear/', views.crear_autores, name='crear_autor'),
    path('autores/<int:pk>/', views.detalles_autores, name='detalles_autor'),
    path('autores/<int:pk>/editar/', views.editar_autores, name='editar_autores'),
    path('autores/<int:pk>/eliminar/', views.eliminar_autores, name='eliminar_autor'),

    path('editoriales', views.listar_editoriales, name="listar_editoriales"),
    path('editoriales/crear/', views.crear_editoriales, name='crear_editorial'),
    path('editoriales/<int:pk>/', views.detalles_editoriales, name='detalles_editorial'),
    path('editoriales/<int:pk>/editar/', views.editar_editoriales, name='editar_editorial'),
    path('editoriales/<int:pk>/eliminar/', views.eliminar_editoriales, name='eliminar_editorial'),

    path('estudiantes/', views.listar_estudiantes, name="listar_estudiantes"),
    path('estudiantes/crear/', views.crear_estudiantes, name='crear_estudiante'),
    path('estudiantes/<int:pk>/', views.detalles_estudiantes, name='detalles_estudiante'),
    path('estudiantes/<int:pk>/editar/', views.editar_estudiantes, name='editar_estudiante'),
    path('estudiantes/<int:pk>/eliminar/', views.eliminar_estudiantes, name='eliminar_estudiante'),
    
    path('prestamos/', views.listar_prestamos, name="listar_prestamos"),
    path('prestamos/crear/', views.crear_prestamos, name='crear_prestamo'),
    path('prestamos/<int:pk>/', views.detalles_prestamos, name='detalles_prestamo'),
    path('prestamos/<int:pk>/editar/', views.editar_prestamos, name='editar_prestamo'),
    path('prestamos/<int:pk>/eliminar/', views.eliminar_prestamos, name='eliminar_prestamo'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
