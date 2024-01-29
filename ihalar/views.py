from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from rest_framework import generics
from .models import IHA, Lessees, Orders
from .serializer import IHASerializer, LesseeSerializer, OrdersSerializer
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


global lessee_id

# Create your views here.
# Create an IHA and to display
class IHAListCreate(generics.ListCreateAPIView):
    queryset = IHA.objects.all()
    serializer_class = IHASerializer

# to retrieve, update or delete an iha by ID
class IHARetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = IHA.objects.all()
    serializer_class = IHASerializer

#this main function that invoked in urls.py to appear in home page as admin login interface
def render_login(request):
    return render(request,'login.html')    

#it will be processed after click onto 'submit' button in admin login page  
def perform_login(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
       input_user_mode = request.POST.get("login_user_mode")
       if input_user_mode == "admin":
          username = request.POST.get("username")
          password = request.POST.get("password")
          user_obj = authenticate(request, username=username, password=password)
          if user_obj is not None:
            login(request,user_obj)
            # i used dynamic url router with parameter to seperate between admin and lessee mode
            return HttpResponseRedirect(reverse('iha_products',kwargs={"mode":"admin","my_id":0}))
          else:
            HttpResponseRedirect("/")
       else:
          #biraz ilkel bir yöntem ile kullanıcı girişi sağlandı :)
          username = request.POST.get("username")
          password = request.POST.get("password")
          users = Lessees.objects.all() #retrieve all iha database table data
          for user in users:
               if user.username == username and user.password == password :
                lessee_id = user.id
                # i used dynamic url router with parameter to seperate between admin and lessee mode
                return HttpResponseRedirect(reverse('iha_products',kwargs={"mode":"lessee","my_id":lessee_id}))

          if len(users) == 0:
                return HttpResponse("There is no user in that information you entered")  
               

          


def iha_products(request,mode,my_id):
    obj = IHA.objects.all() #retrieve all iha database table data
    context = { #bağlam  (to make a bound between the datas and the view layer)
       "obj":obj,
       "mode":mode,
       "user_id":my_id
    } 
    return render(request,"iha_products.html",context)


#this funtion will delete the iha model with technical features that inserted by admin
def deleteIha(request):
    if request.method != "POST":
       return  HttpResponse("Method Not Allowed to Delete")
    else:
       id = request.POST.get("iha_id")
       iha_product = IHA.objects.get(id=id) 
       iha_product.delete()
       return HttpResponse("Product's Box Has Been Deleted Successfully, You May Go Back and See the consequence after refreshing the page")    

#this funtion will update the iha model with technical features that inserted by admin
def editIha(request):
    if request.method == 'POST':
        id = request.POST.get("iha_id")
        iha_product = IHA.objects.get(id=id) 

        iha_product.brand =  request.POST.get("brand")
        iha_product.model =  request.POST.get("model")
        iha_product.weight =  request.POST.get("weight")
        iha_product.category =  request.POST.get("category")
        iha_product.save()

        return HttpResponse("Product's Detail Has Been Updated Successfully, You May Go Back and See the consequence after refreshing the page")

def render_members(request):
    members = Lessees.objects.all() #retrieve all lessees database table data
    context = { #bağlam  (to make a bound between the datas and the view layer)
       "members":members,
    } 
    return render(request,'member.html',context)    

def render_orders(request):
    orders = Orders.objects.all() 
    context = { #bağlam  (to make a bound between the datas and the view layer)
       "orders":orders,
    } 
    return render(request,'orders.html',context)    

def rentIha(request,iha_id,u_id):
    order = Orders(user_id=u_id,order_id=iha_id)
    order.save()

    return HttpResponse("Ne yazık ki kiralanan iahları silebilmek ve değerlendirebilmek adına listelemek amaçlı konusunda yetişemedim :()")


# Create an Lessee and to display
class LesseeListCreate(generics.ListCreateAPIView):
    queryset = Lessees.objects.all()
    serializer_class = LesseeSerializer

# to retrieve, update or delete an lessee by ID
class LesseeRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lessees.objects.all()
    serializer_class = LesseeSerializer



  
class OrdersListCreate(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer


class OrdersRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

        

      


    
       

    


   