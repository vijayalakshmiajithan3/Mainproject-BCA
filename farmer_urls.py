from django.urls import path
from threadapp.farmer_views import farmer_index, add_thread, view_thread, delete_thread, View_Booking


urlpatterns = [
    path('',farmer_index.as_view()),
    path('add_thread',add_thread.as_view()),
    path('view_thread',view_thread.as_view()),
    path('delete_thread',delete_thread.as_view()),
    path('View_Booking',View_Booking.as_view()),

]

def urls():
    return urlpatterns,'farmer', 'farmer'