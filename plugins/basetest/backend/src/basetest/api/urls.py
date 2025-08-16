from django.urls import re_path

from .views import StartingView, CoursesView, SampleView, EnrolmentsView, ObtainJSONWebTokens, DebugAuthView

app_name = "basetest.api"

urlpatterns = [
    re_path(r"starting/$", StartingView.as_view(), name="starting"),
    # Course endpoints
    re_path(r"courses/$", CoursesView.as_view(), name="courses"),  # GET list, POST create
    re_path(r"courses/(?P<course_id>\d+)/$", CoursesView.as_view(), name="course_detail"),  # GET, PUT, DELETE
    # Sample endpoints
    re_path(r"sample/$", SampleView.as_view(), name="sample"),  # GET list, POST create
    re_path(r"sample/(?P<sample_id>\d+)/$", SampleView.as_view(), name="sample_detail"),  # GET, PUT, DELETE
    # Enrollment endpoints
    re_path(r"enrolments/$", EnrolmentsView.as_view(), name="enrolments"),  # GET list, POST create, GET with ?student_id=X
    re_path(r"enrolments/(?P<enrollment_id>\d+)/$", EnrolmentsView.as_view(), name="enrollment_detail"),  # GET, PUT, DELETE
    re_path(r"token-auth/$", ObtainJSONWebTokens.as_view(), name="token_auth"),
    # Debug endpoint
    re_path(r"debug-auth/$", DebugAuthView.as_view(), name="debug_auth"),

]
