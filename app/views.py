from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.shortcuts import render, redirect, get_object_or_404

def listar_libros(request):
    libros = Libro.objects.all()
    return render(request, 'listar_libros.html', {'libros': libros})

def crear_libros(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm()
    return render(request, 'crear_libros.html', {'form': form})

def detalles_libros(request):
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, 'detalles_libros.html', {'libro': libro})

def editar_libros(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'editar_libros.html', {'form': form})

def eliminar_libros(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        return redirect('listar_libros')
    return render(request, 'eliminar_libros.html', {'libro': libro})

def listar_autores(request):
    autores = Autor.objects.all()
    return render(request, 'listar_autores.html', {'autores': autores})

def crear_autores(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_autores')
    else:
        form = AutorForm()
    return render(request, 'crear_autores.html', {'form': form})

def detalles_autores(request):
    autor = get_object_or_404(Autor, pk=pk)
    return render(request, 'detalles_autores.html', {'autor': autor})

def editar_autores(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('listar_autores')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'editar_autores.html', {'form': form})

def eliminar_autores(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        autor.delete()
        return redirect('listar_autores')
    return render(request, 'eliminar_autores.html', {'autor': autor})

def listar_editoriales(request):
    editoriales = Editorial.objects.all()
    return render(request, 'listar_editoriales.html', {'editoriales': editoriales})

def crear_editoriales(request):
    if request.method == 'POST':
        form = EditorialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_editoriales')
    else:
        form = EditorialForm()
    return render(request, 'crear_editoriales.html', {'form': form})

def detalles_editoriales(request):
    editorial = get_object_or_404(Editorial, pk=pk)
    return render(request, 'detalles_editoriales.html', {'editorial': editorial})

def editar_editoriales(request, pk):
    editorial = get_object_or_404(Editorial, pk=pk)
    if request.method == 'POST':
        form = EditorialForm(request.POST, instance=editorial)
        if form.is_valid():
            form.save()
            return redirect('listar_editoriales')
    else:
        form = EditorialForm(instance=editorial)
    return render(request, 'editar_editoriales.html', {'form': form})

def eliminar_editoriales(request, pk):
    editorial = get_object_or_404(Editorial, pk=pk)
    if request.method == 'POST':
        editorial.delete()
        return redirect('listar_editoriales')
    return render(request, 'eliminar_editoriales.html', {'editorial': editorial})

def listar_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'listar_estudiantes.html', {'estudiantes': estudiantes})

def crear_estudiantes(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_estudiantes')
    else:
        form = EstudianteForm()
    return render(request, 'crear_estudiantes.html', {'form': form})

def detalles_estudiantes(request):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    return render(request, 'detalles_estudiantes.html', {'estudiante': estudiante})

def editar_estudiantes(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('listar_estudiantes')
    else:
        form = EstudianteForm(instance=estudiante)
    return render(request, 'editar_estudiantes.html', {'form': form})

def eliminar_estudiantes(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        estudiante.delete()
        return redirect('listar_estudiantes')
    return render(request, 'eliminar_estudiantes.html', {'estudiante': estudiante})

def listar_prestamos(request):
    prestamos = Prestamo.objects.all()
    return render(request, 'listar_prestamos.html', {'prestamos': prestamos})

def crear_prestamos(request):
    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_prestamos')
    else:
        form = PrestamoForm()
    return render(request, 'crear_prestamos.html', {'form': form})

def detalles_prestamos(request):
    prestamo = get_object_or_404(Prestamo, pk=pk)
    return render(request, 'detalles_prestamos.html', {'prestamo': prestamo})

def editar_prestamos(request, pk):
    prestamo = get_object_or_404(Prestamo, pk=pk)
    if request.method == 'POST':
        form = PrestamoForm(request.POST, instance=prestamo)
        if form.is_valid():
            form.save()
            return redirect('listar_prestamos')
    else:
        form = PrestamoForm(instance=prestamo)
    return render(request, 'editar_prestamos.html', {'form': form})

def eliminar_prestamos(request, pk):
    prestamo = get_object_or_404(Prestamo, pk=pk)
    if request.method == 'POST':
        prestamo.delete()
        return redirect('listar_prestamos')
    return render(request, 'eliminar_prestamos.html', {'prestamo': prestamo})
        