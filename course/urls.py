from django.urls import path

from . import views

app_name = 'course'

urlpatterns = [
    path("list/", views.courseView, name= "course_view"),
    path("course-add/", views.courseAdd, name= "course_add"),
    path("course-edit/<str:pk>", views.courseEdit, name= "course_edit"),
    path("course-detail/<str:pk>", views.courseDetail, name= "course_detail"),
    path("course-section/", views.courseSection, name= "course_section"),
    path("list-section/", views.listSection, name= "list_section"),
    path("course-sub-section",views.courseSubSection, name="course_sub_section"),
    

   
]
