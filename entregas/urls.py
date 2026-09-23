from django.urls import path
from .views import *

urlpatterns = [
    path("", entrega_list, name="entrega_list"),
    path("entrega/<int:id>", entrega_detail, name="entrega_detail"),
    path("entrega/create", entrega_create, name="entrega_create"),
    path("entrega/update/<int:id>", entrega_update, name="entrega_update"),
    path("entrega/delete/<int:id>", entrega_delete, name="entrega_delete"),
]
