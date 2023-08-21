from django.shortcuts import render
from django.conf import settings
from App.models import Banner, About, GalleryItem
import pyrebase

config = {
    "apiKey": "AIzaSyA2IdiynVVonDEzRHfCJ7f5VegBnB65J8c",
    "authDomain": "schoolapp-f7483.firebaseapp.com",
    "projectId": "schoolapp-f7483",
    "databaseURL": "https://schoolapp-f7483-default-rtdb.firebaseio.com",
    "storageBucket": "schoolapp-f7483.appspot.com",
    "messagingSenderId": "79589135836",
    "appId": "1:79589135836:web:96eec634aefd324f876b19"
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

# Create your views here.

def home(request):
    banner_images = list(Banner.objects.all())
    # print(banner_images)
    return render(request, 'index.html', {'banner_images': banner_images})

def about_view(request):
    about = list(About.objects.all())  
    # print(about)
    data = {
        'about': about,
    }
    return render(request, 'about.html', data)

def error_404(request):
    pass

def contact(request):
    pass

def gallery(request):
    # Get distinct categories from the Gallery model
    distinct_categories = GalleryItem.objects.values_list('category', flat=True).distinct()

    # Fetch all gallery images
    gallery_items = GalleryItem.objects.all()
    
    data = {
        'distinct_categories': distinct_categories,
        'gallery': gallery_items,
    }
    return render(request, 'gallery.html', data)
    
