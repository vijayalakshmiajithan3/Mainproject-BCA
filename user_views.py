from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import TemplateView, View

from threadapp.models import merch_thread, farmer_thread, mfeedback, user_reg, merch_cart, farmer_cart

# Create your views here.

class user_index(TemplateView):
    template_name='user/index.html'

class thread_btn(TemplateView):
    template_name='user/thread_btn.html'

class view_merchant_thread(TemplateView):
    template_name='user/merchant_thread.html'
    def get_context_data(self, **kwargs):
        context = super(view_merchant_thread,self).get_context_data(**kwargs)
        
        thread = merch_thread.objects.filter(status="added")
        context['thread'] = thread
        return context
    
class m_thread_detail_view(TemplateView):
    template_name = 'user/merchant_thread_details.html'

    def get_context_data(self, **kwargs):
        context = super(m_thread_detail_view,self).get_context_data(**kwargs)
        id= self.request.GET['id']
        
        pet = merch_thread.objects.filter(status="added",id=id)

        context['pet'] = pet
        return context
    
    def post(self , request,*args,**kwargs):
        user=user_reg.objects.get(user_id=self.request.user.id)
        id= self.request.GET['id']
        pe = merch_thread.objects.get(id=id)
        
       
        se = merch_cart()
        se.user_id=user.id
        se.thread_id=pe.id
        se.status='added'
        
        se.save()
        
        return render(request, 'user/index.html', {'message': "successfully added"})
    
class view_farmer_thread(TemplateView):
    template_name='user/farmer_thread.html'
    def get_context_data(self, **kwargs):
        context = super(view_farmer_thread,self).get_context_data(**kwargs)
        
        thread = farmer_thread.objects.filter(status="approved")
        context['thread'] = thread
        return context
    
class f_thread_detail_view(TemplateView):
    template_name = 'user/farmer_thread_details.html'

    def get_context_data(self, **kwargs):
        context = super(f_thread_detail_view,self).get_context_data(**kwargs)
        id= self.request.GET['id']
        
        pet = farmer_thread.objects.filter(status="approved",id=id)

        context['pet'] = pet
        return context
    
    def post(self , request,*args,**kwargs):
        user=user_reg.objects.get(user_id=self.request.user.id)
        id= self.request.GET['id']
        pe = farmer_thread.objects.get(id=id)
        
       
        se = farmer_cart()
        se.user_id=user.id
        se.thread_id=pe.id
        se.status='added'
        
        se.save()
        
        return render(request, 'user/index.html', {'message': "successfully added"})
    

class cart_view(TemplateView):
    template_name = 'user/cart.html'
    def get_context_data(self, **kwargs):
        context = super(cart_view, self).get_context_data(**kwargs)
        # user = User.objects.get(id=self.request.user.id)
        # id =self.request.GET['id']

        user=user_reg.objects.get(user_id=self.request.user.id)

        ct = merch_cart.objects.filter(status='added', user_id=user.id)
        pet = farmer_cart.objects.filter(status='added', user_id=user.id)

        context['ct'] = ct
        context['pet'] = pet
        return context
    
    
    
class delete_mcart(View):
    def dispatch(self,request,*args,**kwargs):
        id = request.GET['id']
        merch_cart.objects.get(id=id).delete()

        return render(request,'user/index.html',{'message':"item Removed"})  

class delete_fcart(View):
    def dispatch(self,request,*args,**kwargs):
        id = request.GET['id']
        farmer_cart.objects.get(id=id).delete()

        return render(request,'user/index.html',{'message':"item Removed"}) 
    
class check_out_m(TemplateView):
    template_name = 'user/mpayment.html'
    def get_context_data(self, **kwargs):
        context = super(check_out_m, self).get_context_data(**kwargs)
        # user = User.objects.get(id=self.request.user.id)
        # id =self.request.GET['id']

        cr = self.request.user.id

        ct = merch_cart.objects.filter(status='cart', user_id=cr)

        total = 0
        for i in ct:
            total = total + int(i.total)

        context['ct'] = ct
        context['asz'] = total

        return context
    

class check_out_f(TemplateView):
    template_name = 'user/fpayment.html'
    def get_context_data(self, **kwargs):
        context = super(check_out_f, self).get_context_data(**kwargs)
        # user = User.objects.get(id=self.request.user.id)
        # id =self.request.GET['id']

        cr = self.request.user.id

        sh = farmer_cart.objects.filter(status='cart', user_id=cr)

        total = 0
        for i in sh:
            total = total + int(i.total)

        context['sh'] = sh
        context['pr'] = total

        return context
    
    

class me_payment(TemplateView):
    template_name= 'user/mpayment.html'
    def dispatch(self,request,*args,**kwargs):
        user=user_reg.objects.get(user_id=self.request.user.id)


        ch = merch_cart.objects.filter(user_id=user.id,status='added')


        print(ch)
        for i in ch:
            i.status='paid'
            i.save()

        return render(request,'user/index.html',{'message':" payment Successfull, Check Booking Details"})
    
class fa_payment(TemplateView):
    template_name= 'user/fpayment.html'
    def dispatch(self,request,*args,**kwargs):
        user=user_reg.objects.get(user_id=self.request.user.id)

        ch = farmer_cart.objects.filter(user_id=user.id,status='added')


        print(ch)
        for i in ch:
            i.status='paid'
            i.save()

        return render(request,'user/index.html',{'message':" payment Successfull, Check Booking Details"})
    

class booking(TemplateView):
    template_name = 'user/view_booking.html'
    def get_context_data(self, **kwargs):
        context = super(booking,self).get_context_data(**kwargs)
        user=user_reg.objects.get(user_id=self.request.user.id)
        caa = merch_cart.objects.filter(status='paid', user_id=user.id)
        far = farmer_cart.objects.filter(status='paid', user_id=user.id)
        context['caa'] = caa
        context['far'] = far
        return context
    
    
class mfeed_back(TemplateView):
    template_name='user/mfeedback.html'
    def get_context_data(self, **kwargs):
        context = super(mfeed_back,self).get_context_data(**kwargs)
        user=user_reg.objects.get(user_id=self.request.user.id)
        fe = merch_cart.objects.filter(status='paid', user_id=user.id)

        context['fe'] = fe
        return context
    
    def post(self , request,*args,**kwargs):
        user = User.objects.get(pk=self.request.user.id)
        work= request.POST['id']
        feed= request.POST['feedback']
        
        fee =mfeedback()
        fee.user = user
        fee.mcart_id = work
        fee.feedback = feed
        fee.save()

        return render(request, 'user/index.html', {'message':"successfully Submit Your Feedback"})
    
    
class view_track(TemplateView):
    template_name = 'user/view_track.html'
    def get_context_data(self, **kwargs):
        context = super(view_track,self).get_context_data(**kwargs)
        user=user_reg.objects.get(user_id=self.request.user.id)
        merr = merch_cart.objects.filter(status='paid', user_id=user.id)
        context['merr'] = merr
        return context