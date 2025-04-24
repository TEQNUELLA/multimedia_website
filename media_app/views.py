from django.shortcuts import render, redirect
from .models import Media
from .forms import MediaForm

def index(request):
    media_items = Media.objects.all().order_by('-uploaded_at')
    return render(request, 'index.html', {'media_items': media_items})

def upload_media(request):
    if request.method == 'POST':
        form = MediaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MediaForm()
    return render(request, 'upload.html', {'form': form})