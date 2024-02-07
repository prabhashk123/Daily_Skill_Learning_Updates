from django.urls import path
from . import views

urlpatterns = [
    path('',views.learning_view),
    path('search',views.search_view),
    # crud step-3
    path('customer/',views.customer_view ,name='customer'),
    path('add',views.add_view,name='add'),
    # crud at first edit than update both url
    path('edit',views.edit_view,name='edit'),
    path('update/<str:id>',views.update_view,name='update'),
    # for crud at delete
    path('delete/<str:id>',views.delete_view,name='delete'),
]
