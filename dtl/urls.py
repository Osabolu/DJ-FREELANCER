from django.urls import path
from . import views

urlpatterns = [
    path("server/", views.service, name="service"),
    path("test/", views.testimonials, name="testimonials"),
    path("case/", views.case_studies, name="case_studies"),
    path("blog/", views.Blog, name="Blog"),
    path("price/", views.pricing, name="pricing"),

]