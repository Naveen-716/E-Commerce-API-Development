from django.urls import path,include
from .views import home,adminlog,stafflog,main,adminlogin,vendorlog,staffagain,staffview,vendoragain,vendorview,product_log,add_product,display_product,staff_update,updatestaff,staff_delete,deletestaff,updatevendor,vendor_update,vendor_delete,deletevendor,staff_log,productagain,editproduct,product_update,updateproduct,deleteproduct,vendor_log,venproduct_add,venpro_update,stud,show,studup,upstud


urlpatterns=[
    path('home',home),
    path('main',main),
    path('adminlog',adminlog),
    path('adminlogin',adminlogin),
    path('stafflog',stafflog),
    path('vendorlog',vendorlog),
    path('staffagain',staffagain),
    path('staffview',staffview),
    path('vendoragain',vendoragain),
    path('vendorview',vendorview),
    path('product_log',product_log),
    path('add_product',add_product),
    path('display_product',display_product),
    path('staff_update',staff_update),
    path('updatestaff/<staff_id>',updatestaff),
    path('staff_delete',staff_delete),
    path('deletestaff/<staff_id>',deletestaff),
    path('vendor_update',vendor_update),
    path('updatevendor/<vendor_id>',updatevendor),
    path('vendor_delete',vendor_delete),
    path('deletevendor/<vendor_id>',deletevendor),
    path('staff_log',staff_log),
    path('productagain',productagain),
    path('editproduct',editproduct),
    path('product_update',product_update),
    path('updateproduct/<product_id>',updateproduct),
    path('deleteproduct/<product_id>',deleteproduct),
    path('vendor_log',vendor_log),
    path('venproduct_add',venproduct_add),
    path('venpro_update',venpro_update),
    # path('ac_create',ac_create),
    # path('login_user',login_user),
    # path('userout',userout)
    path('stud',stud),
    path('show',show),
    path('studup',studup),
    path('upstud/<id>',upstud)

]
