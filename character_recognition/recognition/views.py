# recognition/views.py

from django.shortcuts import render
from .forms import UploadImageForm
from .models import UploadedImage
import pytesseract
from PIL import Image

def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = form.save()
            image_path = uploaded_image.image.path
            try:
                # Open the image file
                img = Image.open(image_path)
                # Perform OCR on the image
                text = pytesseract.image_to_string(img)
                return render(request, 'result.html', {'text': text})
            except Exception as e:
                return render(request, 'result.html', {'error': str(e)})
    else:
        form = UploadImageForm()
    return render(request, 'upload.html', {'form': form})
