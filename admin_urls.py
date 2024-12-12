from django.urls import path
from threadapp.admin_views import admin_index, farmer_approve, farmer_reject, farmer_verify, merchant_approve, merchant_reject, merchant_verify,\
    view_mbooking, view_fbooking, View_feed, view_track, view_fthread,view_mthread
urlpatterns = [
    path('',admin_index.as_view()),
    path('farmer_approve',farmer_verify.as_view()),
    path('approve',farmer_approve.as_view()),
    path('reject',farmer_reject.as_view()),
    path('merchant_approve',merchant_verify.as_view()),
    path('approve',merchant_approve.as_view()),
    path('reject',merchant_reject.as_view()),
    path('view_mbooking',view_mbooking.as_view()),
    path('view_fbooking',view_fbooking.as_view()),
    path('View_feed',View_feed.as_view()),
    path('view_track',view_track.as_view()),
    path('view_fthread',view_fthread.as_view()),
    path('view_mthread',view_mthread.as_view()),



]
def urls():
    return urlpatterns,'admin', 'admin'