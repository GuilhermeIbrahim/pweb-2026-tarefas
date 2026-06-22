from django.shortcuts import render
from .models import Topic

# Create your views here.

def index(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, "app/index.html", context)
