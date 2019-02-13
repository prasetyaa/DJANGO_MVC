from django.shortcuts import render

# Create your views here.

def empat(request):
    return render(request, 'peserta/empat.html', {})