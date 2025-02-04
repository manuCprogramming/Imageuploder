from django.shortcuts import render
from .forms import ImageForm
from .models import Image
# Create your views here.

import os
from django.conf import settings

def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    form = ImageForm()
    img = Image.objects.all()

    # Remove images that don’t exist in the filesystem
    img = [i for i in img if i.photo and os.path.exists(os.path.join(settings.MEDIA_ROOT, str(i.photo)))]

    return render(request, 'home.html', {'img': img, 'form': form})
