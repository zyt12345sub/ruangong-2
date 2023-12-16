from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:reporter_id>/report/",views.report,name="report"),
    path("<int:reporter_id>/detail/",views.detail,name="detail"),
    path("<int:reporter_id>/interface/",views.interface,name="interface")
]