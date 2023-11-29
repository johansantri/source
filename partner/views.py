from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.conf import settings
from .models import Partner
from django.contrib import messages
from django.contrib.auth.models import User
import os

def partnerView(request):
     if request.user.is_staff == True:
           partner_list = Partner.objects.all()
           context = {'partnerlist':partner_list}   

           return render (request,'partner_view.html', context)
     else:
          
        return redirect ('/')

def partnerAdd(request):

    if request.user.is_staff == True:
        if request.method == "POST":
                par = Partner()
                par.partner_name = request.POST.get('partner_name')
                par.partner_abbreviation = request.POST.get('partner_abbreviation')
                par.partner_email_id = request.POST.get('partner_email')
                par.partner_phone = request.POST.get('partner_phone')
                par.partner_address = request.POST.get('partner_address')
                par.partner_tax = request.POST.get('partner_tax')
                par.partner_status = request.POST.get('partner_status')
                #par.partner_logo = request.POST.get('partner_logo')
                par.partner_check = request.POST.get('partner_check')

                if len(request.FILES) != 0:
                    par.partner_logo = request.FILES['partner_logo']
                    par.save()
                    messages.success(request, "PARTNER ADD SUCCESSFULLY")
                    return redirect('/partner/list')
        
        user_list = User.objects.all()
        context = {'us':user_list}
        return render (request,'partner_add.html', context)
    else:
        
        return redirect ('/')

# Create your views here.
def partnerEdit(request, pk):
    par = Partner.objects.get(id=pk)
    user_list = User.objects.all()
    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(par.partner_logo) > 0:
                os.remove(par.partner_logo.path)
                 #prod.image = request.FILES['image']
            par.partner_logo = request.FILES['partner_logo']
        par.partner_name = request.POST.get('partner_name')
        par.partner_abbreviation = request.POST.get('partner_abbreviation')
        par.partner_email_id = request.POST.get('partner_email')
        par.partner_phone = request.POST.get('partner_phone')
        par.partner_address = request.POST.get('partner_address')
        par.partner_tax = request.POST.get('partner_tax')
        par.partner_status = request.POST.get('partner_status')
        
        par.partner_check = request.POST.get('partner_check')
        par.save()
        messages.success(request, "Product Updated Successfully")
        return redirect('/partner/list')

    context = {'partner':par,'user':user_list}
    return render(request, 'partner_edit.html', context)

