from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Volume, Text, Image, Spanish, TextSpanish, ImageSpanish

# List of Volumes in English.
def volume_list(request):
    volumes = Volume.objects.filter(published_date__lte=timezone.now()).order_by('published_date').prefetch_related('text_set', 'image_set')
    return render(request, 'blog/volume_list.html', {'volumes': volumes })

# Individual Volumes in English.
def volume_detail(request, pk):
    volume = get_object_or_404(Volume, pk=pk)
    return render(request, 'blog/volume_detail.html', {'volume': volume})

# List of Volumes in Spanish.
def spanish_volume_list(request):
    volumes_sp = Spanish.objects.filter(published_date__lte=timezone.now()).order_by('published_date').prefetch_related('textspanish_set', 'imagespanish_set')
    return  render(request, 'blog/spanish_volume_list.html', {'volumes_sp': volumes_sp })

# Individual Volumes in Spanish.
def spanish_volume_detail(request, pk):
    volume_sp = get_object_or_404(Spanish, pk=pk)
    return render(request, 'blog/spanish_volume_detail.html', {'volume_sp': volume_sp})

# About Me page in English.
def about(request):
    return  render(request, 'blog/about.html')

# About Me page in Spanish.
def spanish_about(request):
    return  render(request, 'blog/spanish_about.html')