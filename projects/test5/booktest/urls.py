from django.conf.urls import url
import views

urlpatterns =[
    url(r'^$',views.index),
    url(r'^MyExp$',views.MyExp),
    url(r'^uploadPic$',views.uploadPic),
    url(r'^uploadHandle$',views.uploadHandle),
    url(r'^herolist/(\d+)$',views.herolist),
    url(r'^area/$',views.area),
    url(r'^area/(\d+)/$',views.area2),

]