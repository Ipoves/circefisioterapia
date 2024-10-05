from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.administrar, name="administrar"),
    path('equipo/', views.equipo, name='equipo'),
    path('galeria/', views.galeria, name='galeria'),
    path('edit/<int:id>', views.edit, name='administrar_edit'),
    path('create/', views.create, name='administrar_create'),
    path('delete/<int:id>', views.delete, name='administrar_delete'),
    
    path('edit_galeria/<int:id>', views.edit_galeria, name='administrar_edit-galeria'),
    path('create_galeria/', views.create_galeria, name='administrar_create-galeria'),
    path('delete_galeria/<int:id>', views.delete_galeria, name='administrar_delete-galeria'),
    
    path('logear/', views.logear, name='logear'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),

]