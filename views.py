from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate

from threadapp.models import UserType, user_reg,  merchant_reg, farmer_reg

# Create your views here.
class indexView(TemplateView):
    template_name='index.html'


class Login(TemplateView):
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password= request.POST['password']

        user = authenticate(username=email,password=password)
        if user is not None:

            login(request,user)
            if user.last_name == '1':

                if user.is_superuser:
                    return redirect('/admin')
                elif UserType.objects.get(user_id=user.id).type == "user":
                    return redirect('/user')
                elif UserType.objects.get(user_id=user.id).type == "merchant":
                    return redirect('/merchant')
                elif UserType.objects.get(user_id=user.id).type == "farmer":
                    return redirect('/farmer')
                # elif UserType.objects.get(user_id=user.id).type == "shop":
                #     return redirect('/shop')
                # else:
                #     return redirect('/shop')

            else:


                return render(request,'login.html',{'message':" User Account Not Authenticated"})
        else:

            return render(request,'login.html',{'message':"Invalid Username or Password"})    
        

class mer_registration(TemplateView):
    template_name='mer_reg.html'

    def post(self , request,*args,**kwargs):
        name = request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email= request.POST['email']
        password = request.POST['password']
        if User.objects.filter(email=email,username=email):
            print ('pass')
            return render(request,'index.html',{'message':"already added the username or email"})

        else:
            user = User.objects._create_user(username=email,password=password,email=email,first_name=name,is_staff='0',last_name='0')
            user.save()
            se = merchant_reg()
            se.user = user
            se.phone = phone
            se.address=address
            se.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "merchant"
            usertype.save()


            return render(request, 'index.html', {'message': "successfully added"})   



class farmer_registration(TemplateView):
    template_name='farmer_reg.html'

    def post(self , request,*args,**kwargs):
        name = request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email= request.POST['email']
        password = request.POST['password']
        if User.objects.filter(email=email,username=email):
            print ('pass')
            return render(request,'index.html',{'message':"already added the username or email"})

        else:
            user = User.objects._create_user(username=email,password=password,email=email,first_name=name,is_staff='0',last_name='0')
            user.save()
            se = farmer_reg()
            se.user = user
            se.phone = phone
            se.address=address
            se.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "farmer"
            usertype.save()


            return render(request, 'index.html', {'message': "successfully added"})       
        


class user_registration(TemplateView):
    template_name='user_reg.html'

    def post(self , request,*args,**kwargs):
        name = request.POST['name']
        phone=request.POST['phone']
        address=request.POST['address']
        email= request.POST['email']
        password = request.POST['password']
        if User.objects.filter(email=email,username=email):
            print ('pass')
            return render(request,'index.html',{'message':"already added the username or email"})

        else:
            user = User.objects._create_user(username=email,password=password,email=email,first_name=name,is_staff='0',last_name='1')
            user.save()
            se = user_reg()
            se.user = user
            se.phone = phone
            se.address=address
            se.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "user"
            usertype.save()


            return render(request, 'index.html', {'message': "successfully added"})       