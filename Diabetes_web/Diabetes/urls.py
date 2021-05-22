from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.index,name = "index"),
    path('ar', views.index_ar,name = "index_ar"),
    path('tr', views.index_tr,name = "index_tr"),
    path('result', views.diagnosis,name = "result"),
    path('result/ar', views.diagnosis_ar,name = "result_ar"),
    path('result/tr', views.diagnosis_tr,name = "result_tr"),
    path('feed', views.feed,name = "feed"),
    path('feed/ar', views.feed_ar,name = "feed_ar"),
    path('feed/tr', views.feed_tr,name = "feed_tr"),
]