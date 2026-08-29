from django.urls import path
from . import views

urlpatterns = [
    path("", views.course_list, name="course_list"),
    path("my-courses/", views.my_courses, name="my_courses"),
    path("course/<slug:slug>/", views.course_detail, name="course_detail"),
    path("course/<slug:slug>/enroll/", views.enroll, name="enroll"),
    path("<int:course_id>/submit/", views.submit, name="submit"),
    path("course/<int:course_id>/submission/<int:submission_id>/result/", views.show_exam_result, name="show_exam_result"),
]