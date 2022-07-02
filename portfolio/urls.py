from django.urls import path 
from sojemann.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('portfolio-details', views.portfoliodetail, name='portfolio-details'),
    path('postdetails/<str:pk>/', views.postDetails, name='postdetails'),

]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)