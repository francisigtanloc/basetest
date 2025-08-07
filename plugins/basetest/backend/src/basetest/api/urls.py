from django.urls import re_path

from .views import StartingView, CoursesView, ObtainJSONWebTokens, DebugAuthView

app_name = "basetest.api"

urlpatterns = [
    re_path(r"starting/$", StartingView.as_view(), name="starting"),
    # Course endpoints
    re_path(r"courses/$", CoursesView.as_view(), name="courses"),  # GET list, POST create
    re_path(r"courses/(?P<course_id>\d+)/$", CoursesView.as_view(), name="course_detail"),  # GET, PUT
    re_path(r"token-auth/$", ObtainJSONWebTokens.as_view(), name="token_auth"),
    # Debug endpoint
    re_path(r"debug-auth/$", DebugAuthView.as_view(), name="debug_auth"),

]
