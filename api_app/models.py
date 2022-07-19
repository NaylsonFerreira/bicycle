from django.db import models


class Estabelecimentos(models.Model):
    cnpjcpf_est = models.CharField(max_length=20)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Empresas(models.Model):
    cnpjcpf_emp = models.CharField(max_length=50)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Prestadores(models.Model):
    cnpjcpf_prest = models.CharField(max_length=50)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Servicos(models.Model):
    codigo_servico = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class EmpresasEstabelecimentos(models.Model):
    cnpjcpf_emp = models.CharField(max_length=50)
    cnpjcpf_est = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class EmpresasPrestadores(models.Model):
    cnpjcpf_emp = models.CharField(max_length=50)
    cnpjcpf_pres = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Parametros(models.Model):
    cnpjcpf_est = models.CharField(max_length=50)
    nome = models.CharField(max_length=50)
    day = models.PositiveIntegerField("dia", default=0)
    hour = models.TimeField("hora", auto_now=True)

    def __str__(self):
        return self.nome


class Permissoes(models.Model):
    nome = models.CharField(max_length=50)


class Usuarios(models.Model):
    email = models.EmailField(max_length=254)
    nome = models.CharField(max_length=50)
    perfil = models.PositiveIntegerField(default=2)
    notificar = models.BooleanField(default=False)
    permissoes = models.ManyToManyField("Permissoes")
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Notas(models.Model):
    cnpjcpf_emp = models.CharField(max_length=50)
    cnpjcpf_est = models.CharField(max_length=50)
    cnpjcpf_prest = models.CharField(max_length=50)
    numero_nota = models.IntegerField()
    serie = models.CharField(max_length=50, null=True, blank=True)
    deducao = models.FloatField(default=0, null=True, blank=True)
    valor_servico = models.FloatField(default=0, null=True, blank=True)
    dh_emissao = models.DateTimeField()
    descricao = models.CharField(max_length=50, null=True, blank=True)
    codigo_servico = models.FloatField(default=0, null=True, blank=True)
    cancelada = models.CharField(max_length=2, null=True, blank=True)
    iss_retido = models.CharField(
        max_length=2, default='N', null=True, blank=True)
    aliq_iss = models.FloatField(default=0, null=True, blank=True)
    valor_iss = models.FloatField(default=0, null=True, blank=True)
    valor_pis = models.FloatField(default=0, null=True, blank=True)
    valor_cofins = models.FloatField(default=0, null=True, blank=True)
    valor_csll = models.FloatField(default=0, null=True, blank=True)
    valor_irrf = models.FloatField(default=0, null=True, blank=True)
    valor_inss = models.FloatField(default=0, null=True, blank=True)
    serie_rps = models.CharField(
        max_length=50, default=0, null=True, blank=True)
    rps = models.IntegerField(default=0, null=True, blank=True)
    codigo_verificacao = models.CharField(max_length=50, blank=True, null=True)
    nome_pdf = models.CharField(max_length=50, blank=True, null=True)
