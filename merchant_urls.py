from django.urls import path
from threadapp.merchant_views import merchant_index, add_thread, view_thread, view_farmer_thread, \
                                     thread_approve, thread_reject, delete_thread, View_Booking, View_feed, Add_track, update_track


urlpatterns = [
    path('',merchant_index.as_view()),
    path('add_thread',add_thread.as_view()),
    path('view_thread',view_thread.as_view()),
    path('view_farmer_thread',view_farmer_thread.as_view()),
    path('thread_approve',thread_approve.as_view()),
    path('thread_reject',thread_reject.as_view()),
    path('delete_thread',delete_thread.as_view()),
    path('View_Booking',View_Booking.as_view()),
    path('View_feed',View_feed.as_view()),
    path('Add_track',Add_track.as_view()),
    path('update_track',update_track.as_view()),

]

def urls():
    return urlpatterns,'merchant', 'merchant'