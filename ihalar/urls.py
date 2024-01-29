from django.urls import path
from .views import IHAListCreate, IHARetrieveUpdateDelete, LesseeListCreate, LesseeRetrieveUpdateDelete, OrdersListCreate, LesseeRetrieveUpdateDelete
from ihalar import views


urlpatterns = [
   path('ihalar',IHAListCreate.as_view(),name="Create-IHA-List"),
   path('iha/<int:pk>/',IHARetrieveUpdateDelete.as_view(),name='iha-Details'),
   #this for admin's login platform
   path('',views.render_login,name="render_login"),
   path('perform_login',views.perform_login,name="perform_login"), 
   path('iha_products/<str:mode>/<int:my_id>/',views.iha_products,name="iha_products"),
   path('render_members',views.render_members,name="render_members"),
   path('delete_iha',views.deleteIha,name="delete_iha"), 
   path('edit_iha',views.editIha,name='edit_iha'), 
   path('rent_iha/<int:iha_id>/<int:u_id>/',views.rentIha,name='rent_iha'),

   path('lessees',LesseeListCreate.as_view(),name="Create-Lessee-List"),
   path('lessee/<int:pk>/',LesseeRetrieveUpdateDelete.as_view(),name='lessee-Details'),
   path('orders',OrdersListCreate.as_view(),name="Create-Order-List"),
   path('lessee/<int:pk>/',LesseeRetrieveUpdateDelete.as_view(),name='lessee-Details'),
  
   
]