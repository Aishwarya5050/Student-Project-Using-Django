from django.urls import path
from student_App import views

urlpatterns = [
    path('add/',views.add_student),
    path('list/',views.student_list),
    path('delete/<int:id>/',views.delete),
    path('update/<int:id>/',views.update),
]