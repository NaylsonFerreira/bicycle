from django.contrib.auth import authenticate
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import Group, Permission, User
from api_app.randonData import generateData
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api_app.models import (Empresas, EmpresasEstabelecimentos,
                            EmpresasPrestadores, Estabelecimentos, Notas,
                            Parametros, Permissoes, Prestadores, Servicos,
                            Usuarios)
from api_app.serializers import (EmpresasEstabelecimentosSerializer,
                                 EmpresasPrestadoresSerializer,
                                 EmpresasSerializer,
                                 EstabelecimentosSerializer, GroupSerializer,
                                 NotasSerializer, ParametrosSerializer,
                                 PermissionSerializer, PermissoesSerializer,
                                 PrestadoresSerializer, ServicosSerializer,
                                 UserSerializer, UsuariosSerializer)


@api_view(['GET'])
def randonData(request):
    generateData()
    return Response('ok')


@api_view(['GET'])
def me(request):
    user = User.objects.get(pk=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['email', 'username', 'first_name', 'last_name']


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['name']


class PermissionViewSet(ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['name']


def fields_required(request, fields=[]):
    responseData = {}
    for f in fields:
        if f not in request.data:
            responseData[f] = 'This field is required'

    return responseData


@api_view(['POST'])
def password_change(request):

    check_fields = fields_required(
        request,
        fields=[
            'current_password',
            'new_password',
            'confirm_password'
        ])

    if check_fields:
        return Response(check_fields, status=400)

    current_password = request.data.get('current_password')
    new_password = request.data.get('new_password')
    confirm_password = request.data.get('confirm_password')

    if new_password != confirm_password:
        return Response({'message': 'Passwords do not match'}, status=400)

    username = request.user.username
    user = authenticate(username=f"{username}", password=f"{current_password}")
    if user is None:
        return Response(
            {'message': 'Current password is incorrect'}, status=400)

    user.set_password(f"{new_password}")
    user.save()
    Token.objects.filter(user=user).delete()
    token, created = Token.objects.get_or_create(user=request.user)

    return Response({
        'message': 'Password changed successfully',
        'token': token.key
    }, status=200)


@api_view(['POST'])
@permission_classes([AllowAny])
def password_reset(request):
    check_fields = fields_required(request, fields=['email'])
    if check_fields:
        return Response(check_fields, status=400)

    email = request.data.get('email')
    user = User.objects.filter(email=email).first()
    if user is not None:
        data = {"email": user.email}
        form = PasswordResetForm(data)
        if form.is_valid():
            form.save(request=request)

    return Response({
        'message': 'if you are registered, you will receive an email with a link to reset your password'
    }, status=200)


class EstabelecimentosViewSet(ModelViewSet):
    queryset = Estabelecimentos.objects.all()
    serializer_class = EstabelecimentosSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['cnpjcpf_est', 'nome']
    filterset_fields = '__all__'


class EmpresasViewSet(ModelViewSet):
    queryset = Empresas.objects.all()
    serializer_class = EmpresasSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['cnpjcpf_emp', 'nome']
    filterset_fields = '__all__'


class PrestadoresViewSet(ModelViewSet):
    queryset = Prestadores.objects.all()
    serializer_class = PrestadoresSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['cnpjcpf_prest', 'nome']
    filterset_fields = '__all__'


class ServicosViewSet(ModelViewSet):
    queryset = Servicos.objects.all()
    serializer_class = ServicosSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = '__all__'
    filterset_fields = '__all__'


class EmpresasEstabelecimentosViewSet(ModelViewSet):
    queryset = EmpresasEstabelecimentos.objects.all()
    serializer_class = EmpresasEstabelecimentosSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = '__all__'
    filterset_fields = '__all__'


class EmpresasPrestadoresViewSet(ModelViewSet):
    queryset = EmpresasPrestadores.objects.all()
    serializer_class = EmpresasPrestadoresSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = '__all__'
    filterset_fields = '__all__'


class NotasViewSet(ModelViewSet):
    queryset = Notas.objects.all()
    serializer_class = NotasSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = '__all__'
    filterset_fields = '__all__'
#


class PermissoesViewSet(ModelViewSet):
    queryset = Permissoes.objects.all()
    serializer_class = PermissoesSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = '__all__'
    filterset_fields = '__all__'


class UsuariosViewSet(ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = '__all__'
    filterset_fields = '__all__'


class ParametrosViewSet(ModelViewSet):
    queryset = Parametros.objects.all()
    serializer_class = ParametrosSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = '__all__'
    filterset_fields = '__all__'
