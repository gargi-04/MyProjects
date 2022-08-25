"""scantist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from frontend import views,api
from django.conf import settings
from django.conf.urls.static import static

 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('login/',views.login,name='login'),
    path('loginuser/',views.loginuser,name='loginuser'),
    path('register/',views.register,name='register'),
    path('mytickets/',views.mytickets,name='mytickets'),
    path('Book/<int:venueid>/',views.bookvenue,name='bookvenue'),
    path('download/<int:venuecode>/<int:idcode>/',views.download,name='download'),
    path("verifyTicket/",api.TicketCheck ,name ="verifyTicket"),
    path('scanner/',views.scanner,name='scanner'),
    path('logout/',views.logoutuser,name='logout'),
    path('findvenue/<int:pin_code>',api.findVenue,name='venues')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

