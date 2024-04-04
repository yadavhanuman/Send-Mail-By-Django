
from django.contrib import admin
from django.urls import path
from nsti import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),

     path('mail/', views.mailer),
     path('today/', views.contact),
    path('sell/', views.contact),

]
