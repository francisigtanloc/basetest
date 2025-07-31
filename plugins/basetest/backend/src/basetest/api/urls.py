from django.urls import re_path

from .views import StartingView, CoursesView

app_name = "basetest.api"

urlpatterns = [
    re_path(r"starting/$", StartingView.as_view(), name="starting"),
    # Course endpoints
    re_path(r"courses/$", CoursesView.as_view(), name="courses"),  # GET list, POST create
    re_path(r"courses/(?P<course_id>\d+)/$", CoursesView.as_view(), name="course_detail"),  # GET, PUT
]
