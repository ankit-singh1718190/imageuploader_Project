from django.shortcuts import render
from .forms import ImageUploadForm
from .models import Image

def home(request):
    success = False
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            success = True  # Set success to True if the form is valid and saved

    form = ImageUploadForm()
    return render(request, 'home.html', {'form': form, 'success': success})
