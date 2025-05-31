from django.http import HttpResponse
import datetime

from django.views import View
from rest_framework import routers



class UserController(View):
    def current_datetime(request) -> HttpResponse:
        now = datetime.datetime.now()
        html = "<html><body>It is now %s.</body></html>" % now
        return HttpResponse(html)