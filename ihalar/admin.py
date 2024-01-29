from django.contrib import admin

# Register your models here. [sure :) ]

from .models import IHA, Lessees, Orders

# You have two alternative of inserting new IHA model. one of them by going to Django administration and the second is redirect 
#by url names as /ihalar 
admin.site.register(IHA)  

admin.site.register(Lessees) 

admin.site.register(Orders) 

