#from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def satu(request):
    return render(request, 'rumah/satu.html', {})