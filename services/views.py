from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    return render(request, 'services/index.html')


def artii(request):
    return render(request, 'services/artii.html')

    
def artii_result(request):
    name = request.GET.get('name')
    font = request.GET.get('font')
    url = f'http://artii.herokuapp.com/make?text={name}&font={font}'
    response = requests.get(url).text
    context = {
        'response' : response
    }
    return render(request, 'services/artii_result.html', context)