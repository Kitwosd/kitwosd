from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('contact/', views.contact, name='contact'),
    path('product/', views.product, name='product'),
    path('service/', views.service, name='service'),
    path('services/', views.service, name='services'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('package/', views.package, name='package'),
    path('team/', views.team, name='team'),
    path('faq/', views.faq, name='faq'),
    path('about-us/', views.aboutus, name='about-us'),
    path('terms-and-condition/', views.terms_and_condition, name='terms-and-condition'),
    path('privacy-policy/', views.privacy_policy, name='privacy-policy'),
    path('blog/', views.blog, name='blog'),
    path('gallery/', views.gallery, name='gallery'),
    path('career/', views.career, name='career'),
    path('quote/', views.quote, name='quote'),
    path('package-order', views.package_order, name='package-order'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('portfolio/<slug:category_slug>/', views.portfolio, name='project_by_category'),
    path('blog/<slug:blog_slug>/', views.blog_detail, name='single-blog'),

]
