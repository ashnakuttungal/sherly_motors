from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns= [
path('add_car',views.add_car),
path('admin_carviews',views.admin_carviews),
path('cardelete/<int:id>',views.cardelete,name="cardelete"),
path('carupdate/<int:id>',views.carupdate,name="carupdate"),
path('carupdate/car_update/<int:id>',views.car_update,name="car_update"),
path('user_carviews',views.user_carviews),


]
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)