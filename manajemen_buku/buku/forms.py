from django import forms
from .models import Buku, Kategori

class KategoriForm(forms.ModelForm):
    class Meta:
        model = Kategori
        fields = ['nama']
        error_messages = {
            'nama': {'required': "Nama kategori tidak boleh kosong"},
        }

    def clean_nama(self):
        nama = self.cleaned_data.get('nama')
        instance_id = self.instance.pk
        
        if Kategori.objects.filter(nama__iexact=nama).exclude(pk=instance_id).exists():
            raise forms.ValidationError("Kategori ini sudah ada!")

        return nama

class BukuForm(forms.ModelForm):
    class Meta:
        model = Buku
        fields = ['judul', 'kategori', 'penulis']

    judul = forms.CharField(
        max_length=255,
        error_messages={'required': "Judul tidak boleh kosong"},
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan judul buku'})
    )
    kategori = forms.ModelChoiceField(
        queryset=Kategori.objects.all(),
        empty_label="Pilih Kategori",
        error_messages={'required': "Kategori tidak boleh kosong"},
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    penulis = forms.CharField(
        max_length=255,
        error_messages={'required': "Nama penulis tidak boleh kosong"}, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan nama penulis'})
    )

    def clean_judul(self):
        judul = self.cleaned_data.get('judul')
        instance_id = self.instance.pk

        if Buku.objects.filter(judul=judul).exclude(pk=instance_id).exists():
            raise forms.ValidationError("Judul sudah ada. Gunakan judul lain.")

        return judul