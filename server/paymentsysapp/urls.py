from django.contrib import admin
from paymentsysapp import views
from django.conf.urls import include, url
from django.urls import path,re_path
from django.views.static import serve
from django.conf import settings
from AppModel import admin as appadmin
from django.views.generic.base import RedirectView

urlpatterns = [
    url('admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.+)$', serve, {'document_root': settings.MEDIA_ROOT}),
    path('user_login/', views.user_login),
    path('get_student_pay_list_info/', views.get_student_pay_list_info),
    
    
] 
 
