from django.shortcuts import render

# Create your views here.

def lima(request):
    return render(request, 'data_diri/lima.html', {})