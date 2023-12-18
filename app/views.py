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
    autores = Autores.objects.all()
    return render(request, 'listar_autores.html', {'autores': autores})

def crear_autores(request):
    if request.method == 'POST':
        form = AutoresForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_autores')
    else:
        form = AutoresForm()
    return render(request, 'crear_autores.html', {'form': form})

def detalles_autores(request):
    autor = get_object_or_404(Autores, pk=pk)
    return render(request, 'detalles_autores.html', {'autor': autor})

def editar_autores(request, pk):
    autor = get_object_or_404(Autores, pk=pk)
    if request.method == 'POST':
        form = AutoresForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('listar_autores')
    else:
        form = AutoresForm(instance=autor)
    return render(request, 'editar_autores.html', {'form': form})

def eliminar_autores(request, pk):
    autor = get_object_or_404(Autores, pk=pk)
    if request.method == 'POST':
        autor.delete()
        return redirect('listar_autores')
    return render(request, 'eliminar_autores.html', {'autor': autor})