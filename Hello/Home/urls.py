from django.contrib import admin
from django.urls import path
from Home import views
urlpatterns = [
   path('',views.index,name='Home'),
   path('about/',views.about,name='About'),
   path('orders/',views.orders,name='Orders'),
   path('contacts/',views.contacts,name='contacts'),
   path('India/',views.india,name='India'),
   path('U.S.A/',views.usa,name='USA'),
   path('germany/',views.germany,name='germany'),
   path('srilanka/',views.srilanka,name='srilanka'),
   path('custom/',views.custom,name='custom'),

]