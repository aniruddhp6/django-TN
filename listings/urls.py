from django.urls import path
from listings import views


urlpatterns=[
    path('',views.index,name='listings'),
    path('<int:listing_id>',views.listing,name='listing'),
    path('create',views.create,name='create'),
    path('<id>/update', views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
]






