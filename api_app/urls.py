from django.urls import path, re_path
from django.urls.conf import include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from api_app.views import (EmpresasViewSet, EstabelecimentosViewSet,
                           GroupViewSet, NotasViewSet, ParametrosViewSet,
                           PermissionViewSet, PermissoesViewSet,
                           PrestadoresViewSet, ServicosViewSet, UserViewSet,
                           UsuariosViewSet, me, password_change,
                           password_reset)

router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'permissions', PermissionViewSet)
router.register(r'estabelecimentos', EstabelecimentosViewSet)
router.register(r'prestadores', PrestadoresViewSet)
router.register(r'empresas', EmpresasViewSet)
router.register(r'servicos', ServicosViewSet)
router.register(r'notas', NotasViewSet)
router.register(r'usuarios', UsuariosViewSet)
router.register(r'permissoes', PermissoesViewSet)
router.register(r'parametros', ParametrosViewSet)


urlpatterns = [
    path('', include(router.urls)),
    re_path('auth/me/?', me, name='me'),
    re_path('auth/login/?', obtain_auth_token, name='login'),
    re_path('auth/password_change/?', password_change, name='password_change'),
    re_path('auth/password_reset/?', password_reset, name='password_reset')
]
