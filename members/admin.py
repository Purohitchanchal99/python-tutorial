# members/admin.py

from django.contrib import admin
from .models import Member, Flow, Oops, Function

admin.site.register(Member)
admin.site.register(Flow)
admin.site.register(Oops)
admin.site.register(Function)
