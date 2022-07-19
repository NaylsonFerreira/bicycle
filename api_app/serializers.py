from django.contrib.auth.models import Group, Permission, User
from rest_framework import serializers

from api_app.models import (Empresas, EmpresasEstabelecimentos,
                            EmpresasPrestadores, Estabelecimentos, Notas,
                            Parametros, Permissoes, Prestadores, Servicos,
                            Usuarios)


class ParametrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parametros
        fields = "__all__"


class PermissoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permissoes
        fields = "__all__"


class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = "__all__"

#


class EstabelecimentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estabelecimentos
        fields = "__all__"


class EmpresasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresas
        fields = "__all__"


class PrestadoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestadores
        fields = "__all__"


class ServicosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicos
        fields = "__all__"


class EmpresasEstabelecimentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpresasEstabelecimentos
        fields = "__all__"


class EmpresasPrestadoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpresasPrestadores
        fields = "__all__"


class NotasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notas
        fields = "__all__"
        depth = 1
        # fields = ('cnpjcpf_emp', 'cnpjcpf_est', 'cnpjcpf_pres', 'numero_nota', 'serie', 'deducao', 'valor_servico', 'dh_emissao', 'descricao')
        # fields = ('cnpjcpf_emp', 'cnpjcpf_est', 'cnpjcpf_pres', 'numero_nota', 'serie', 'deducao', 'valor_servico', 'dh_emissao', 'descricao')
        # fields = ('cnpjcpf_emp', 'cnpjcpf_est', 'cnpjcpf_pres', 'numero_nota', 'serie', 'deducao', 'valor_servico', 'dh_emissao', 'descricao')
        # fields = ('cnpjcpf_emp', 'cnpjcpf_est', 'cnpjcpf_pres', 'numero_nota', 'serie', 'deducao', 'valor_servico', 'dh_emissao', 'descricao')
        # fields = ('cnpjcpf_emp', 'cnpjcpf_est', 'cnpjcpf_pres', 'numero_nota', 'serie', 'deducao', 'valor_servico', 'dh_emissao', 'descricao')
        # fields = ('cnpjcpf_emp', 'cnpjcpf_est', 'cnpjcpf_pres', 'numero_nota', 'serie', 'deducao', 'valor_servico', 'dh_emissao', 'descricao')
        # fields = ('cnpjcpf_emp', 'cnpjcpf_est', 'cnpjcpf_pres', 'numero_nota', 'serie', 'deducao', 'valor_servico', 'dh_emissao',


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'is_superuser', 'is_staff']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"
