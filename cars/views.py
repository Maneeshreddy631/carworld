from django.shortcuts import render,get_object_or_404
from .models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger,Paginator
# Create your views here.
def cars(request) :
    cars = Car.objects.order_by('-created_date') #we get all data
    paginator = Paginator(cars, 2) # we get only 3 data among al at once
    page = request.GET.get('page') #stor that 3 in in paged_cars
    paged_cars = paginator.get_page(page)

    model_search = Car.objects.values_list('model',flat=True).distinct() #all 4 will return list not dictionary
    city_search = Car.objects.values_list('city',flat=True).distinct()
    year_search = Car.objects.values_list('year',flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style',flat=True).distinct()
    data = {
        'cars' : paged_cars,
        'model_search' : model_search,
        'city_search' : city_search,
        'year_search': year_search,
        'body_style_search' : body_style_search,
    }
    return render(request,'cars/cars.html',data)


def car_detail(request,id) :   #from here we have to bring data from data base for back end use to show in front end
    single_car = get_object_or_404(Car ,pk = id) #primary key getting from func call as argument
    data = {
        'single_car' : single_car,
    }
    return render(request , 'cars/car_detail.html',data) # pass the data fetched in to this as datato the back end hmtl page
def search(request) :
    cars = Car.objects.order_by('created_date')
    model_search = Car.objects.values_list('model',flat=True).distinct() #all 4 will return list not dictionary
    city_search = Car.objects.values_list('city',flat=True).distinct()
    year_search = Car.objects.values_list('year',flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style',flat=True).distinct()
    transmission_search = Car.objects.values_list('transmission',flat=True).distinct()
    if 'keyword' in request.GET :     # if we have keyword name in url then we stores it in keyword and checks for blank or not
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword) #we are checking if keyword in description that is browser url and we take that keyword and store and check if it is blank if it is not blank then we check fr decription for this keyword (descriotion_icontain = keyword) checks the description for keyword
    if 'model' in request.GET :    
        model = request.GET['model']
        if model:
            cars = cars.filter(model__iexact=model) 
    if 'city' in request.GET :     
        city = request.GET['city']
        if city:
            cars = cars.filter(city__iexact=city) 
    if 'year' in request.GET :    
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact=year) 
    if 'body_style' in request.GET :    
        body_style = request.GET['body_style']
        if body_style:
            cars = cars.filter(body_style__iexact=body_style) 
    if 'min_price' in request.GET : 
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price :
            cars = cars.filter(price__gte=min_price, price__lte = max_price) #gte = greater than or equal
    if 'transmission' in request.GET :    
        transmission= request.GET['transmission']
        if transmission :
            cars = cars.filter(transmission__iexact=transmission) 
    data = {
        'cars' : cars,
        'model_search' : model_search,
        'city_search' : city_search,
        'year_search': year_search,
        'body_style_search' : body_style_search,
        'transmission_search' : transmission_search,
    }
    return render(request,'cars/search.html',data)