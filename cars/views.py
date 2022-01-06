from django.shortcuts import render,get_object_or_404
from .models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger,Paginator
# Create your views here.
def cars(request) :
    cars = Car.objects.order_by('-created_date') #we get all data
    paginator = Paginator(cars, 2) # we get only 3 data among al at once
    page = request.GET.get('page') #stor that 3 in in paged_cars
    paged_cars = paginator.get_page(page)
    data = {
        'cars' : paged_cars,
    }
    return render(request,'cars/cars.html',data)


def car_detail(request,id) :   #from here we have to bring data from data base for back end use to show in front end
    single_car = get_object_or_404(Car ,pk = id) #primary key getting from func call as argument
    data = {
        'single_car' : single_car,
    }
    return render(request , 'cars/car_detail.html',data) # pass the data fetched in to this as datato the back end hmtl page