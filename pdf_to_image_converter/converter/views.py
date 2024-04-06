from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .utils import pdf_to_images
import os

def home(request):
    if request.method == 'POST' and request.FILES['pdf_file']:
        pdf_file = request.FILES['pdf_file']
        fs = FileSystemStorage()
        filename = fs.save(pdf_file.name, pdf_file)
        pdf_path = os.path.join(settings.MEDIA_ROOT, filename)
        output_folder = os.path.join(settings.MEDIA_ROOT, 'output_images')
        pdf_to_images(pdf_path, output_folder)
        return render(request, 'home.html', {
            'converted': True,
            'images_folder': 'output_images'
        })
    return render(request, 'home.html', {'converted': False})
