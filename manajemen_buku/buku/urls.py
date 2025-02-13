from django.urls import path
from buku.views import buku, tambah_buku, edit_buku, hapus_buku, kategori, tambah_kategori, edit_kategori, hapus_kategori

urlpatterns = [
    path('', buku),
    path('buku', buku, name='buku'),
    path('buku/tambah', tambah_buku, name='tambah_buku'),
    path('buku/edit/<int:id>/', edit_buku, name='edit_buku'),
    path('buku/hapus/<int:buku_id>/', hapus_buku, name='hapus_buku'),
    path('kategori', kategori, name='kategori'),
    path('kategori/tambah', tambah_kategori, name='tambah_kategori'),
    path('kategori/edit/<int:id>/', edit_kategori, name='edit_kategori'),
    path('kategori/hapus/<int:kategori_id>/', hapus_kategori, name='hapus_kategori'),
]