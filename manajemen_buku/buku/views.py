from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import Http404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Buku, Kategori
from buku.forms import BukuForm, KategoriForm

def buku(request):    
    search_query = request.GET.get('q', '')  # Get search input
    sort_by = request.GET.get('sort', 'id')  # Get sort column
    order = request.GET.get('order', 'asc')  # Get sorting order

    # Determine sorting direction
    if order == 'desc':
        sort_by = f'-{sort_by}'

    # Filter data based on search query
    buku_list = Buku.objects.filter(
        Q(judul__icontains=search_query)
    ).order_by(sort_by)

    # Pagination (10 items per page)
    paginator = Paginator(buku_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'buku/index.html', {
        'title': 'Buku | Manajemen Buku & Kategori',
        'page_obj': page_obj,
        'search_query': search_query,
        'sort_by': sort_by.lstrip('-'),
        'order': order,
    })

def tambah_buku(request):
    if request.method == "POST":
        form = BukuForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Buku berhasil ditambahkan!")
            return redirect("buku")
        else:
            messages.error(request, "Terjadi kesalahan, periksa input Anda.")
    else:
        form = BukuForm()

    return render(request, 'buku/form.html', {
        'title': 'Tambah Buku | Manajemen Buku & Kategori',
        'mode': 'tambah',
        'form': form,
    })

def edit_buku(request, id):
    try:
        buku = Buku.objects.get(id=id)
    except Buku.DoesNotExist:
        messages.error(request, "Buku tidak ditemukan.")
        return redirect("buku")

    if request.method == "POST":
        form = BukuForm(request.POST, instance=buku)
        if form.is_valid():
            form.save()
            messages.success(request, "Buku berhasil diperbarui!")
            return redirect("buku")
        else:
            messages.error(request, "Terjadi kesalahan, periksa input Anda.")
    else:
        form = BukuForm(instance=buku)

    return render(request, 'buku/form.html', {
        'title': 'Edit Buku | Manajemen Buku & Buku',
        'mode': 'edit',
        'form': form,
    })

def hapus_buku(request, buku_id):
    buku = get_object_or_404(Buku, id=buku_id)
    buku.delete()
    messages.success(request, "Buku berhasil dihapus!")
    return redirect('buku')

def kategori(request):    
    search_query = request.GET.get('q', '')  # Get search input
    sort_by = request.GET.get('sort', 'id')  # Get sort column
    order = request.GET.get('order', 'asc')  # Get sorting order

    # Determine sorting direction
    if order == 'desc':
        sort_by = f'-{sort_by}'

    # Filter data based on search query
    kategori_list = Kategori.objects.filter(
        Q(nama__icontains=search_query)
    ).order_by(sort_by)

    # Pagination (10 items per page)
    paginator = Paginator(kategori_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'kategori/index.html', {
        'title': 'Kategori | Manajemen Buku & Kategori',
        'page_obj': page_obj,
        'search_query': search_query,
        'sort_by': sort_by.lstrip('-'),
        'order': order,
    })

def tambah_kategori(request):
    if request.method == "POST":
        form = KategoriForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Kategori berhasil ditambahkan!")
            return redirect("kategori")
        else:
            messages.error(request, "Terjadi kesalahan, periksa input Anda.")
    else:
        form = KategoriForm()

    return render(request, 'kategori/form.html', {
        'title': 'Tambah Kategori | Manajemen Buku & Kategori',
        'mode': 'tambah',
        'form': form,
    })

def edit_kategori(request, id):
    try:
        kategori = Kategori.objects.get(id=id)
    except Kategori.DoesNotExist:
        messages.error(request, "Kategori tidak ditemukan.")
        return redirect("kategori")

    if request.method == "POST":
        form = KategoriForm(request.POST, instance=kategori)
        if form.is_valid():
            form.save()
            messages.success(request, "Kategori berhasil diperbarui!")
            return redirect("kategori")
        else:
            messages.error(request, "Terjadi kesalahan, periksa input Anda.")
    else:
        form = KategoriForm(instance=kategori)

    return render(request, 'kategori/form.html', {
        'title': 'Edit Kategori | Manajemen Buku & Kategori',
        'mode': 'edit',
        'form': form,
    })

def hapus_kategori(request, kategori_id):
    kategori = get_object_or_404(Kategori, id=kategori_id)
    kategori.delete()
    messages.success(request, "Kategori berhasil dihapus!")
    return redirect('kategori')