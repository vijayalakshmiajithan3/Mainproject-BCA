from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import TemplateView, View
from django.core.files.storage import FileSystemStorage

from threadapp.models import farmer_cart, farmer_thread, merchant_reg, farmer_reg


# Create your views here.
class farmer_index(TemplateView):
    template_name='farmer/farmer_index.html'

class add_thread(TemplateView):
    template_name='farmer/add_thread.html'
    
    def post(self , request,*args,**kwargs):
        farmer=farmer_reg.objects.get(user_id=self.request.user.id)
        name = request.POST['name']
        price=request.POST['price']
        description=request.POST['desc']
        image=request.FILES['image']
        fii=FileSystemStorage()
        filesss=fii.save(image.name,image)

        se = farmer_thread()
        se.farmer_id = farmer.id
        se.name = name
        se.price = price
        se.description=description
        se.image=filesss
        se.status="Added"
        se.save()


        return render(request, 'farmer/farmer_index.html', {'message': "successfully added"})   
    

class view_thread(TemplateView):
    template_name = 'farmer/view_thread.html'
    def get_context_data(self, **kwargs):
        context = super(view_thread,self).get_context_data(**kwargs)
        farmer=farmer_reg.objects.get(user_id=self.request.user.id)
        thread = farmer_thread.objects.filter(farmer_id=farmer.id)
        context['thread'] = thread
        return context
    
class delete_thread(View):
    def dispatch(self,request,*args,**kwargs):
        id = request.GET['id']
        farmer_thread.objects.get(id=id).delete()

        return render(request,'farmer/farmer_index.html',{'message':"Thread Removed"})
    
    
class View_Booking(TemplateView):
    template_name = 'farmer/view_booking.html'
    def get_context_data(self, **kwargs):
        context = super(View_Booking,self).get_context_data(**kwargs)
        farmer=farmer_reg.objects.get(user_id=self.request.user.id)
        farr = farmer_cart.objects.filter(status='paid', thread__farmer_id = farmer.id)

        context['farr'] = farr
        return context