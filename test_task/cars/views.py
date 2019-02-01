from django.db.models.functions import Lower
from django.shortcuts import render

# Create your views here.
from cars.models import Car, Category


def car_list(request):
    cars = Car.objects
    categories = Category.objects.all()
    order = request.GET.get("order", '')
    choosen_category = request.GET.get('category','')

    if choosen_category:
        cars = cars.filter(category=choosen_category)
    if order:

        if order == "brand":
            cars = cars.order_by(Lower("brand__name"))
        elif order == "model":
            cars = cars.order_by(Lower("model__name"))
        elif order == "price":
            cars = cars.order_by("price")
        elif order == "category":
            cars = cars.order_by("category")

    else:
        cars = cars.all()



    context = {
        'cars':cars,
        'categories':categories,
        'choosen_category':choosen_category,
    }
    return render(request,"car_list.html",context)
