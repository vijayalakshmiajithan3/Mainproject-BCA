from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import TemplateView, View
from django.core.files.storage import FileSystemStorage

from threadapp.models import merch_cart, merch_thread, merchant_reg, farmer_thread, mfeedback

# Create your views here.
class merchant_index(TemplateView):
    template_name='merchant/mer_index.html'

class add_thread(TemplateView):
    template_name='merchant/add_thread.html'
    
    def post(self , request,*args,**kwargs):
        merch=merchant_reg.objects.get(user_id=self.request.user.id)
        name = request.POST['name']
        price=request.POST['price']
        description=request.POST['desc']
        image=request.FILES['image']
        fii=FileSystemStorage()
        filesss=fii.save(image.name,image)

        se = merch_thread()
        se.merchant_id = merch.id
        se.name = name
        se.price = price
        se.description=description
        se.image=filesss
        se.status="Added"
        se.save()


        return render(request, 'merchant/mer_index.html', {'message': "successfully added"})   
    

class view_thread(TemplateView):
    template_name = 'merchant/view_thread.html'
    def get_context_data(self, **kwargs):
        context = super(view_thread,self).get_context_data(**kwargs)
        merch=merchant_reg.objects.get(user_id=self.request.user.id)
        thread = merch_thread.objects.filter(merchant_id=merch.id)
        context['thread'] = thread
        return context
    
class delete_thread(View):
    def dispatch(self,request,*args,**kwargs):
        id = request.GET['id']
        merch_thread.objects.get(id=id).delete()

        return render(request,'merchant/mer_index.html',{'message':"Thread Removed"})

class view_farmer_thread(TemplateView):
    template_name = 'merchant/view_farmer_thread.html'
    def get_context_data(self, **kwargs):
        context = super(view_farmer_thread,self).get_context_data(**kwargs)
        
        thread = farmer_thread.objects.all()
        context['thread'] = thread
        return context
    
class thread_approve(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        th = farmer_thread.objects.get(pk=id)
        th.status='approved'
        th.save()
        return render(request,'merchant/mer_index.html',{'message':"Approved"})
    
class thread_reject(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        th = farmer_thread.objects.get(pk=id)
        th.status='rejected'
        th.save()
        return render(request,'merchant/mer_index.html',{'message':"Approved"})
    
class View_Booking(TemplateView):
    template_name = 'merchant/view_booking.html'
    def get_context_data(self, **kwargs):
        context = super(View_Booking,self).get_context_data(**kwargs)
        merch=merchant_reg.objects.get(user_id=self.request.user.id)
        merr = merch_cart.objects.filter(status='paid', thread__merchant_id = merch.id)

        context['merr'] = merr
        return context
    
    
class View_feed(TemplateView):
    template_name = 'merchant/view_feedback.html'
    def get_context_data(self, **kwargs):
        context = super(View_feed,self).get_context_data(**kwargs)
        merch=merchant_reg.objects.get(user_id=self.request.user.id)
        merr = mfeedback.objects.filter(mcart__thread__merchant_id = merch.id)

        context['merr'] = merr
        return context
    

class Add_track(TemplateView):
    template_name = 'merchant/add_track.html'
    def get_context_data(self, **kwargs):
        context = super(Add_track,self).get_context_data(**kwargs)
        merch=merchant_reg.objects.get(user_id=self.request.user.id)
        merr = merch_cart.objects.filter(status='paid', thread__merchant_id = merch.id)

        context['merr'] = merr
        return context
    
class update_track(TemplateView):
    template_name = 'merchant/update_track.html'
    def get_context_data(self, **kwargs):
        context = super(update_track,self).get_context_data(**kwargs)
        merch=merchant_reg.objects.get(user_id=self.request.user.id)
        id = self.request.GET['id']
        up = merch_cart.objects.filter(thread__merchant_id = merch.id, id=id)

        context['up'] = up
        return context
    
    def post(self,request,*args,**kwargs):
        id = request.GET['id'] 
        
        a =merch_cart.objects.get(id=id)
        a.track = request.POST['track']
        a.save()
        
        return render(request,'merchant/mer_index.html',{'message':"Track Updated"})