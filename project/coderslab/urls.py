"""coderslab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from exercises_app.views import SchoolView, SchoolClassView, my_view, StudentView, StudentGradeView, StudentSearchView,\
    CreateStudentView, PizzaToppingsView, ClassPresence, SetColor


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', SchoolView.as_view(), name="index"),
    path('class/<int:school_class>/', SchoolClassView.as_view(), name="school-class"),
    path('student/<int:student_id>/', StudentView.as_view(), name="student-view"),
    path('grade/<int:student_id>/<int:subject_id>/', StudentGradeView.as_view(), name="student-grade"),
    path('student_search/', StudentSearchView.as_view(), name="student-search"),
    path('add_student/', CreateStudentView.as_view(), name="student-add"),
    path('pizza/', PizzaToppingsView.as_view(), name="pizza"),
    path('class_presence/<int:student_id>/<str:date>/', ClassPresence.as_view(), name="classpresence"),
    path('set_color/', SetColor.as_view(), name="setcolor"),
    path('my_page/', my_view, name="my-view")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

