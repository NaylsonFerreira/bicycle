from django.contrib import admin
from rest_framework.authtoken.models import Token


class AdminSite(admin.AdminSite):
    def index(self, request, extra_context=None):
        extra_context = extra_context or {}
        token, created = Token.objects.get_or_create(user=request.user)
        extra_context['token'] = token.key
        extra_context['index'] = True
        return super(AdminSite, self).index(request, extra_context)
