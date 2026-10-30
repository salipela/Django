from django.contrib import admin
from myapp.models import product
from myapp.models import customer

# Register your models here.
class productAdmin(admin.ModelAdmin):
    list_display=["ProId","ProName","ProPrice"]
    class Meta:
        model=product
admin.site.register(product,productAdmin)

# class customerAdmin(admin.ModelAdmin):
    # list_display=["CusId","CusName","CusPrice"]
    # class Meta:
        # model=customer
# admin.site.register(customer,customerAdmin)
