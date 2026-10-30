from django.shortcuts import render
from myapp.models import customer, product

# Create your views here.
def home(request):
   Product=product.objects.all()
   for pro in Product:
        print(f'{pro.ProId}\t {pro.ProName}\t {pro.ProPrice}')
   return render(request,'home.html')

# def home(request):
    # Customer=customer.objects.all()
    # for cus in Customer:
        # print(f'{cus.CusId}\t {cus.CusName}\t {cus.CusPrice}')
    # return render(request,'home.html')