from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.conf import settings
from .models import *
from django.contrib import messages
from django.db import connection
from django.db.models import Q
import json
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
import os


#course view
def courseView(request):
     if request.user.is_staff == True:
           course_list = Course.objects.all()
           partner_list = Partner.objects.all()
           user_list = User.objects.all()
           context = {'courselist':course_list,'partnerlist':partner_list,'userlist':user_list}   

           return render (request,'course_view.html', context)
     else:
          
        return redirect ('/')


#courseAdd

def courseAdd(request):

    if request.user.is_staff == True:
        if request.method == "POST":
                mk = Course()
                mk.course_name = request.POST.get('course_name')
                mk.topic = request.POST.get('topic')
                
                mk.level = request.POST.get('level')
                mk.status_course = request.POST.get('status_course')
               
                mk.org_partner_id = request.POST.get('org_partner')
                mk.type_course = request.POST.get('type_course')
                mk.image_course = request.POST.get('image_course')
                mk.author_id = request.POST.get('author')
                

                if len(request.FILES) != 0:
                    mk.image_course = request.FILES['image_course']
                    mk.save()
                    messages.success(request, "Create Courses  SUCCESSFULLY")
                    return redirect('/course/list')
        partner_list = Partner.objects.all()
        user_list = User.objects.all()
        context = {'userlist':user_list,'partnerlist':partner_list}
       
        return render (request,'course_add.html', context)
    else:
        
        return redirect ('/')

# coruse edit.
def courseEdit(request, pk):
    mk = Course.objects.get(id=pk)
    user_list = User.objects.all()
    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(mk.image_course) > 0:
                os.remove(mk.image_course.path)
                 #prod.image = request.FILES['image']
            mk.image_course = request.FILES['image_course']
        mk.topic = request.POST.get('topic')

        mk.level = request.POST.get('level')
        mk.status_course = request.POST.get('status_course')

        mk.org_partner_id = request.POST.get('org_partner')
        mk.type_course = request.POST.get('type_course')
        #mk.image_course = request.POST.get('image_course')
        mk.author_id = request.POST.get('author')
        mk.save()
        messages.success(request, "Course Updated Successfully")
        return redirect('/course/list')

    context = {'course':mk,'user':user_list}
    return render(request, 'course_edit.html', context)

#course detail
def courseDetail(request, pk):
    mk = Course.objects.get(id=pk)

    catg = Category.objects.filter(parent=None, mk_id=mk)

    




    context = {'course':mk,'catg':catg}
   # print(catg)
    return render(request, 'course_detail.html', context)


#add section
@csrf_exempt
def courseSection(request):
    if request.user.is_staff == True:
             
       
        title = request.POST.get("title")
        mk = request.POST.get("mk_id")
        #print('id',course_section)
        try:
                
            vs = Category(title=title,
                         mk_id=mk)
            vs.save()
            ls = Category.objects.all().order_by( '-id')[:1].values()
            #ls = Section.objects.values()          
            section_data = list(ls)
            return JsonResponse({'status':'data section save','section_data':section_data})

        except:

            return JsonResponse({'status':'section no save'})
        

#add section
@csrf_exempt
def courseSub(request):
    if request.user.is_staff == True:
             
       
        title = request.POST.get("title")
        mk = request.POST.get("mk_id")
        parent = request.POST.get("parent_id")
        #print('id',course_section)
        try:
                
            vs = Category(title=title,
                         mk_id=mk,parent_id=parent)
            vs.save()
            ls = Category.objects.all().order_by( '-id')[:1].values()
            #ls = Section.objects.values()          
            section_data = list(ls)
            return JsonResponse({'status':'data sub save','section_data':section_data})

        except:

            return JsonResponse({'status':'sub section no save'})

    #list section
@csrf_exempt
def listSection(request):
    if request.user.is_staff == True:
           
      
        try:
            #mk = Course.objects.get(id=pk)
           

           
            ls = Section.objects.filter(section_id_course_id__isnull=True).values()
            #ls = Section.objects.values()          
            section_data = list(ls)
            print(section_data)
            return JsonResponse({'status':'200','section_data':section_data})

        except:

            return JsonResponse({'status':'404'})
                

#add sub section
@csrf_exempt
def courseSubSection(request):
    if request.user.is_staff == True:
             
       
        sub_section_name = request.POST.get("sub_section_name")
        sub_section_id_course = request.POST.get("sub_section_id_course")
        #print('id',course_section)
        try:
                
            vs = SubSection(sub_section_name=sub_section_name,
                         sub_section_id_course_id=sub_section_id_course)
            vs.save()
            ls = SubSection.objects.all().order_by( '-id')[:1].values()
            #ls = Section.objects.values()          
            sub_section_data = list(ls)
            return JsonResponse({'status':'data sub section save','sub_section_data':sub_section_data})

        except:

            return JsonResponse({'status':'sub section no save'})