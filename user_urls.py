from django.urls import path
from threadapp.user_views import user_index, thread_btn, view_merchant_thread, view_farmer_thread, m_thread_detail_view, \
                                 f_thread_detail_view, cart_view, check_out_m, check_out_f, me_payment, fa_payment, delete_mcart,\
                                     delete_fcart, booking, mfeed_back,view_track

urlpatterns = [
    path('',user_index.as_view()),
    path('thread_btn',thread_btn.as_view()),
    path('view_merchant_thread',view_merchant_thread.as_view()),
    path('view_farmer_thread',view_farmer_thread.as_view()),
    path('m_thread_detail_view',m_thread_detail_view.as_view()),
    path('f_thread_detail_view',f_thread_detail_view.as_view()),
    path('cart_view',cart_view.as_view()),
    path('check_out_m',check_out_m.as_view()),
    path('check_out_f',check_out_f.as_view()),
    path('me_payment',me_payment.as_view()),
    path('fa_payment',fa_payment.as_view()),
    path('delete_mcart',delete_mcart.as_view()),
    path('delete_fcart',delete_fcart.as_view()),
    path('booking',booking.as_view()),
    path('mfeed_back',mfeed_back.as_view()),
    path('view_track',view_track.as_view()),


]
def urls():
    return urlpatterns,'user', 'user'