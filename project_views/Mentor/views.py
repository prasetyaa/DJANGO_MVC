from django.shortcuts import render

# Create your views here.

def tiga(request):
    return render(request, 'pengajar/tiga.html', {})