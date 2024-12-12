from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View
from django.views.generic import TemplateView
from threadapp.models import farmer_cart, farmer_reg, farmer_thread, merch_cart, merch_thread, merchant_reg, mfeedback

# Create your views here.
class admin_index(TemplateView):
    template_name='admin/index.html'


class farmer_verify(TemplateView):
    template_name = 'admin/farmer_approvel.html'
    def get_context_data(self, **kwargs):
        context = super(farmer_verify,self).get_context_data(**kwargs)

        farmer = farmer_reg.objects.filter(user__last_name='0',user__is_staff='0',user__is_active='1')

        context['farmer'] = farmer
        return context
    
class farmer_approve(View):
    def dispatch(self, request, *args, **kwargs):

        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.save()
        return render(request,'admin/index.html',{'message':" Account Approved"})

class farmer_reject(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.is_active='0'
        user.save()
        return render(request,'admin/index.html',{'message':"Account Removed"})
    



class merchant_verify(TemplateView):
    template_name = 'admin/mer_approvel.html'
    def get_context_data(self, **kwargs):
        context = super(merchant_verify,self).get_context_data(**kwargs)

        merchant = merchant_reg.objects.filter(user__last_name='0',user__is_staff='0',user__is_active='1')

        context['merchant'] = merchant
        return context
    
class merchant_approve(View):
    def dispatch(self, request, *args, **kwargs):

        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.save()
        return render(request,'admin/index.html',{'message':" Account Approved"})

class merchant_reject(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.is_active='0'
        user.save()
        return render(request,'admin/index.html',{'message':"Account Removed"})
    
    
class View_feed(TemplateView):
    template_name = 'admin/view_feedback.html'
    def get_context_data(self, **kwargs):
        context = super(View_feed,self).get_context_data(**kwargs)
        merr = mfeedback.objects.all()

        context['merr'] = merr
        return context
    
    
class view_mbooking(TemplateView):
    template_name = 'admin/view_mbooking.html'
    def get_context_data(self, **kwargs):
        context = super(view_mbooking,self).get_context_data(**kwargs)
        merr = merch_cart.objects.filter(status='paid')

        context['merr'] = merr
        return context
    
class view_fbooking(TemplateView):
    template_name = 'admin/view_fbooking.html'
    def get_context_data(self, **kwargs):
        context = super(view_fbooking,self).get_context_data(**kwargs)
        farr = farmer_cart.objects.filter(status='paid')

        context['farr'] = farr
        return context
    
class view_track(TemplateView):
    template_name = 'admin/view_track.html'
    def get_context_data(self, **kwargs):
        context = super(view_track,self).get_context_data(**kwargs)
        merr = merch_cart.objects.filter(status='paid')
        context['merr'] = merr
        return context
    
class view_mthread(TemplateView):
    template_name = 'admin/view_mthread.html'
    def get_context_data(self, **kwargs):
        context = super(view_mthread,self).get_context_data(**kwargs)
        thread = merch_thread.objects.all()
        context['thread'] = thread
        return context
    
class view_fthread(TemplateView):
    template_name = 'admin/view_fthread.html'
    def get_context_data(self, **kwargs):
        context = super(view_fthread,self).get_context_data(**kwargs)
        thread = farmer_thread.objects.all()
        context['thread'] = thread
        return context