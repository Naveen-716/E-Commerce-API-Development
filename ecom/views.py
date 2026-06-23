from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import admin,staff,vendor,product_add,student

# Create your views here.

def home(request):
    return render(request,'home.html')
def main(request):
    return render(request,'main.html')
def staffagain(request):
    return render(request,'staffmain.html')
def vendoragain(request):
    return render(request,'vendormain.html')
def productagain(request):
    return render(request,'staffproduct.html')
def uslog(request):
    return render(request,'userlogin.html')
def adminlog(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        if admin.objects.filter(email=email).exists():
            return render(request,'admin.html',{'message':'ACCOUNT IS ALREADY EXIST'})
        else:
            admin.objects.create(name=name,email=email,password=password)
    return render(request,'admin.html')
def stafflog(request):
    if request.method=='POST':
        staff_id=request.POST.get('staff_id')
        name=request.POST.get('name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        if staff.objects.filter(username=username).exists():
            return render(request,'staff.html',{'msg':'username is already exist'})
        if staff.objects.filter(email=email).exists():
            return render(request,'staff.html',{'msg':'email is already exist'})
        staff.objects.create(staff_id=staff_id,name=name,username=username,email=email,password=password)
        send_mail(
        subject="Hello from Django",
        message=f"Staff Account created successfully.{username}",
        from_email="naveenkumarmurugesan936@gmail.com",
        recipient_list=[email],
        fail_silently=False,
        )
    return render(request,'staff.html')
def vendorlog(request):
    if request.method=='POST':
        vendorname=request.POST.get('vendorname')
        vendor_id=request.POST.get('vendor_id')
        email=request.POST.get('email')
        vendorpassword=request.POST.get('vendorpassword')
        productbrought=request.POST.get('productbrought')
        if vendor.objects.filter(vendor_id=vendor_id).exists():
            return render(request,'vendor.html',{'msg':'vendor id is already exist'})
        if vendor.objects.filter(email=email).exists():
            return render(request,'vendor.html',{'msg':'email is already exist'})
        vendor.objects.create(vendorname=vendorname,vendor_id=vendor_id,email=email,vendorpassword=vendorpassword,productbrought=productbrought)
        send_mail(
        subject="Hello from Django",
        message=f"Vendor Account created successfully vendorname={vendorname},password={vendorpassword}.{vendorname}",
        from_email="naveenkumarmurugesan936@gmail.com",
        recipient_list=[email],
        fail_silently=False,
        )
    return render(request,'vendor.html')
def adminlogin(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        User=admin.objects.filter(email=email,password=password).exists()
        if User:
            return redirect(main)
        else:
            return redirect(home)
    return render(request,'adminlog.html')
def staffview(request):
    a=staff.objects.all()
    return render(request,'stafflist.html',{'a':a})
def vendorview(request):
    a=vendor.objects.all()
    return render(request,'vendorlist.html',{'a':a})
def staff_log(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        if staff.objects.filter(email=email,password=password).exists():
            return redirect(editproduct)
        else:
            return redirect(home)
    return render(request,'staff_login.html',{'warning':'enter your valid credentials'})
def vendor_log(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        if vendor.objects.filter(email=email,vendorpassword=password).exists():
            return redirect(venproduct_add)
        else:
            return redirect(home)
    return render(request,'vendor_login.html',{'warning':'enter your valid credentials'})
def add_product(request):
    if request.method=='POST':
        product_id=request.POST.get('product_id')
        product_name=request.POST.get('product_name')
        describtion=request.POST.get('describtion')
        category=request.POST.get('category')
        price=request.POST.get('price')
        manufacture_date=request.POST.get('manufacture_date')
        image=request.FILES['image']
        uploaded_at=request.POST.get('uploaded_at')
        product_add.objects.create(product_id=product_id,product_name=product_name,describtion=describtion,category=category,price=price,manufacture_date=manufacture_date,image=image,uploaded_at=uploaded_at)
    return render(request,'product.html')
def venproduct_add(request):
    if request.method=='POST':
        product_id=request.POST.get('product_id')
        product_name=request.POST.get('product_name')
        vendor_name=request.POST.get('vendor_name')
        vendor_product_brand=request.POST.get('vendor_product_brand')
        describtion=request.POST.get('describtion')
        category=request.POST.get('category')
        price=request.POST.get('price')
        manufacture_date=request.POST.get('manufacture_date')
        image=request.FILES['image']
        uploaded_at=request.POST.get('uploaded_at')
        created_by=request.POST.get('created_by')
        product_add.objects.create(product_id=product_id,product_name=product_name,vendor_name=vendor_name,vendor_product_brand=vendor_product_brand,describtion=describtion,category=category,price=price,manufacture_date=manufacture_date,image=image,uploaded_at=uploaded_at,created_by=created_by)
    return render(request,'vendor_add_product.html')
def product_log(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        if admin.objects.filter(email=email,password=password).exists():
            return redirect(add_product)
        else:
            return render(request,'forproductlog.html',{'msg':'enter the valid credentials'})
    return render(request,'forproductlog.html')
def display_product(request):
    a=product_add.objects.all()
    
    r={"a":a}
    return render(request,'productdetails.html',r)
def staff_update(request):
    if request.method=='POST':
        staff_id=request.POST.get('staff_id')
        name=request.POST.get('name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        staff.objects.filter(staff_id=staff_id).update(name=name,username=username,email=email,password=password)
        return redirect(staffview)
    return render(request,'staffupdate.html')
def updatestaff(request,staff_id):
    a=staff.objects.filter(staff_id=staff_id).first()
    return render(request,'staffupdate.html',{'a':a})
def staff_delete(request):
    if request.method=='POST':
        staff_id=request.POST.get('staff_id')
        name=request.POST.get('name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        staff.objects.filter(staff_id=staff_id).delete()
        return redirect(staffview)
    return render(request,'staffdelete.html')
def deletestaff(request,staff_id):
    a=staff.objects.filter(staff_id=staff_id).first()
    return render(request,'staffdelete.html',{'a':a})
def vendor_update(request):
    if request.method=='POST':
        vendorname=request.POST.get('vendorname')
        vendor_id=request.POST.get('vendor_id')
        email=request.POST.get('email')
        vendorpassword=request.POST.get('vendorpassword')
        productbrought=request.POST.get('productbrought')
        vendor.objects.filter(vendor_id=vendor_id).update(vendorname=vendorname,email=email,vendorpassword=vendorpassword,productbrought=productbrought)
        return redirect(vendorview)
    return render(request,'vendorupdate.html')
def updatevendor(request,vendor_id):
    a=vendor.objects.filter(vendor_id=vendor_id).first()
    return render(request,'vendorupdate.html',{'a':a})
def vendor_delete(request):
    if request.method=='POST':
        vendorname=request.POST.get('vendorname')
        vendor_id=request.POST.get('vendor_id')
        email=request.POST.get('email')
        vendorpassword=request.POST.get('vendorpassword')
        productbrought=request.POST.get('productbrought')
        vendor.objects.filter(vendor_id=vendor_id).delete()
        return redirect(vendorview)
    return render(request,'vendordelete.html')
def deletevendor(request,vendor_id):
    a=vendor.objects.filter(vendor_id=vendor_id).first()
    return render(request,'vendordelete.html',{'a':a})
def editproduct(request):
    s=product_add.objects.all()
    return render(request,'staffproduct.html',{'s':s})
def product_update(request):
    if request.method=='POST':
        product_id=request.POST.get('product_id')
        product_name=request.POST.get('product_name')
        describtion=request.POST.get('describtion')
        category=request.POST.get('category')
        price=request.POST.get('price')
        manufacture_date=request.POST.get('manufacture_date')
        image=request.FILES['image']
        a=product_add.objects.get(product_id=product_id)
        a.image=image
        a.save()
        product_add.objects.filter(product_id=product_id).update(product_name=product_name,describtion=describtion,category=category,price=price,manufacture_date=manufacture_date)
        return redirect(display_product)
    return render(request,'productupdate.html')
def venpro_update(request):
    if request.method=='POST':
        product_id=request.POST.get('product_id')
        product_name=request.POST.get('product_name')
        vendor_name=request.POST.get('vendor_name')
        vendor_product_brand=request.POST.get('vendor_product_brand')
        describtion=request.POST.get('describtion')
        category=request.POST.get('category')
        price=request.POST.get('price')
        manufacture_date=request.POST.get('manufacture_date')
        image=request.FILES['image']
        a=product_add.objects.get(product_id=product_id)
        a.image=image
        a.save()
        product_add.objects.filter(product_id=product_id).update(product_name=product_name,describtion=describtion,category=category,price=price,manufacture_date=manufacture_date,vendor_name=vendor_name,vendor_product_brand=vendor_product_brand)
        return redirect(display_product)
    return render(request,'productupdate.html')
def updateproduct(request,product_id):
    a=product_add.objects.filter(product_id=product_id).first()
    return render(request,'productupdate.html',{'a':a})
def deleteproduct(request,product_id):
    a=product_add.objects.get(product_id=product_id).delete()
    d={'a':a}
    return redirect(editproduct)
# def ac_create(request):
#     if request.method=='POST':
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#         mail=request.POST.get('mail')
#         if ecomuser.objects.filter(username=username).exists():
#             return render(request,'user.html',{'msg':'username is already exist'})
#         else:
#             ecomuser.objects.create(username=username,password=password,mail=mail)
#             User.objects.create_user(username=username,password=password)
#             send_mail(
#             subject="ACCOUNT CREATE",
#             message=f" your ecommerce a/c created.{username}",
#             from_email="naveenkumarmurugesan936@gmail.com",
#             recipient_list=[mail],
#             fail_silently=False,
#         )
#         return redirect(login_user)
#     return render(request,'user.html')
# def login_user(request):
#     if request.method=='POST':
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#         user=authenticate(username=username,password=password)
#         if user is not None:
#             return render(request,'userlogin.html',{'msg':'invalid username or password'})
#         else:
#              login(request,user)
#              return redirect(display_product)       
#     return render(request,'userlogin.html')
# def userout(request):
#     logout(request)
#     return redirect(login_user)

def stud(request):
    if request.method=='POST':
        image=request.FILES['image']
        student_name=request.POST.get('student_name')
        standard=request.POST.get('standard')
        doj=request.POST.get('doj')
        student.objects.create(image=image,student_name=student_name,standard=standard,doj=doj)
    return render(request,'student.html')
        
def show(request):
    s=student.objects.all()
    return render(request,'data.html',{'s':s})

def studup(request):
    if request.method=='POST':
        student_name=request.POST.get('student_name')
        standard=request.POST.get('standard')
        doj=request.POST.get('doj')
        image=request.FILES['image']
        a=student.objects.get(id=id)
        a.image=image
        a.save()
        student.objects.filter(id=id).update(student_name=student_name,standard=standard,doj=doj)
        return redirect(show)
    return render(request,'dataupdate.html')
def upstud(request,id):
    a=student.objects.filter(id=id).first()
    return render(request,'dataupdate.html',{'a':a})


def studdelete(request):
    if request.method=='POST':
        student_name=request.POST.get('student_name')
        standard=request.POST.get('standard')
        doj=request.POST.get('doj')
        image=request.FILES['image']
        a=student.objects.get(id=id)
        a.image=image
        a.save()
        student.objects.filter(id=id).delete(student_name=student_name,standard=standard,doj=doj)
        return redirect(show)
    return render(request,'dataupdate.html')
def delstud(request):
    a=student.objects.filter(id=id).first()
    return render(request,'datadelete.html',{'a':a})









    





















