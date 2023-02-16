from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.homePage, name='homepage'),
    path('map', views.viewMap, name='map'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('what-we-do', views.about_wwd, name='what-we-do'),
    path('our-team', views.about_op, name='our-team'),
    path('partners', views.about_p, name='partners'),
    path('category', views.category, name='category'),
    path('category_1', views.category_1, name='category_1'),
    path('category_2', views.category_2, name='category_2'),
    path('category_3', views.category_3, name='category_3'),
    path('about_us', views.about_us, name='about_us'),
    path('mr', views.homepage_mr, name='mr'),
    path('mr/contact_us', views.contact_us_mr, name='mr/contact_us'),
    path('mr/our-team', views.about_op_mr, name='mr/our-team'),
    path('mr/what-we-do', views.about_wwd_mr, name='mr/what-we-do'),
    path('mr/partners', views.about_p_mr, name='mr/partners'),
    path('wcdmap', views.viewWcdMap,name='viewWcdMap'),
    # path("women_state_home", views.women_state_home, name="women_state_home"),
    # path("one_stop_center", views.one_stop_center, name="one_stop_center"),
    # path("counselling_center", views.counselling_center, name="counselling_center"),
    # path("swadhaar_greh", views.swadhaar_greh, name="swadhaar_greh"),
    # path("ujjwal_greh", views.ujjwal_greh, name="ujjwal_greh"),
    path('dist_proj', views.dist_proj,name='dist_proj'),
    path('tal_proj', views.tal_proj,name='tal_proj'),
    
    
   
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

