"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('product/',views.product,name='product'),
    path('contact/',views.contact,name='contact'),
    path('search/',views.search,name='search'),
    path('search1/',views.search1,name='search1'),
    path('search2/',views.search2,name='search2'),
    path('signup/',views.signup,name='signup'),
    path('check-username/', views.check_username, name='check_username'),
    path('login/',views.login_view,name='login'),
    path('order/<str:category>/<int:id>/', views.place_order, name='place_order'),
    path('ordersuccess/', views.order_success, name='ordersuccess'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
