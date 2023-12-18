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
    path('editoriales', views.listar_editoriales, name="listar_editoriales"),
    path('crear_editoriales/', views.crear_editoriales, name='crear_editoriales'),
    path('editoriales/<int:pk>/', views.detalles_editoriales, name='detalles_editoriales'),
    path('editoriales/<int:pk>/editar/', views.editar_editoriales, name='editar_editoriales'),
    path('editoriales/<int:pk>/eliminar/', views.eliminar_editoriales, name='eliminar_editoriales'),
    path('estudiantes', views.listar_estudiantes, name="listar_estudiantes"),
    path('crear_estudiantes/', views.crear_estudiantes, name='crear_estudiantes'),
    path('estudiantes/<int:pk>/', views.detalles_estudiantes, name='detalles_estudiantes'),
    path('estudiantes/<int:pk>/editar/', views.editar_estudiantes, name='editar_estudiantes'),
    path('estudiantes/<int:pk>/eliminar/', views.eliminar_estudiantes, name='eliminar_estudiantes'),
    path('prestamos', views.listar_prestamos, name="listar_prestamos"),
    path('crear_prestamos/', views.crear_prestamos, name='crear_prestamos'),
    path('prestamos/<int:pk>/', views.detalles_prestamos, name='detalles_prestamos'),
    path('prestamos/<int:pk>/editar/', views.editar_prestamos, name='editar_prestamos'),
    path('prestamos/<int:pk>/eliminar/', views.eliminar_prestamos, name='eliminar_prestamos'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
