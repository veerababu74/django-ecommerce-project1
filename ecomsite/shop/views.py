from django.shortcuts import render
from shop.models import Products,Order
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    product_obj=Products.objects.all()
    #serch code
    item_name =request.GET.get('item_name')
    if item_name != "" and item_name is not None:
        product_obj=product_obj.filter(title__icontains=item_name)
    
    #paginator code
    paginator=Paginator(product_obj,4)
    page=request.GET.get('page')
    product_obj=paginator.get_page(page)


    return render(request,'shop/index.html',{"product_obj":product_obj})


def detail(request,id):
    product_object=Products.objects.get(id=id)
    return render(request,'shop/detail.html',{'product_object':product_object})



def checkout(request):

    if request.method =="POST":
        items=request.POST.get('items',"")
        name=request.POST.get('name',"")
        email=request.POST.get('email',"")
        address=request.POST.get('address',"")
        city=request.POST.get('city',"")
        State=request.POST.get('State',"")
        Zip=request.POST.get('Zip',"")
        total=request.POST.get('total',"")
        order=Order(items=items,name=name,email=email,address=address,city=city,State=State,Zip=Zip,total=total)
        order.save()
    return render(request,'shop/checkout.html')