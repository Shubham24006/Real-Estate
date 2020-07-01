from django.shortcuts import render
from properties.models import Property

# Create your views here.


def index(request):
    properties = Property.objects.order_by('-list_date').filter(is_published=True)[:3]
    search_properties = Property.objects.all()
    cities = []
    states = []
    for property in search_properties:
        city = property.city
        state = property.state
        if city not in cities:
            cities.append(city)
        if state not in states:
            states.append(state)
    return render(request, 'pages/index.html', {'properties': properties, 'cities': cities, 'states': states})


def about(request):
    # sellers = Seller.objects.order_by('-register_date')
    return render(request, 'pages/about.html')


def search(request):
    query_list = {}
    cities = []
    states = []

    for property in query_list:
        city = property.city
        state = property.state
        if city not in cities:
            cities.append(city)
        if state not in states:
            states.append(state)

    if len(request.GET['keywords']) > 0:
        keywords = request.GET['keywords']
        query_list = Property.objects.filter(name__icontains=keywords)

    if len(request.GET['state']) > 0:
        state = request.GET['state']
        query_list = Property.objects.filter(state__iexact=state)

    if len(request.GET['city']) > 0:
        city = request.GET['city']
        query_list = Property.objects.filter(city__iexact=city)

    return render(request, 'pages/search.html', {'query_list': query_list, 'cities': cities, 'states': states})
