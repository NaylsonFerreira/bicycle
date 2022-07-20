from random import randrange
from faker import Faker
from api_app.models import Empresas, Estabelecimentos, Notas, Parametros, Prestadores, Usuarios


def generateData():
    fake = Faker(['pt_BR'])
    maxRows = 100

    count = Prestadores.objects.all().count()
    count = maxRows - count
    for i in range(0, count):
        prestador = Prestadores()
        prestador.nome = fake.unique.name()
        prestador.cnpjcpf_prest = fake.unique.company_id()
        prestador.save()

    count = Empresas.objects.all().count()
    count = maxRows - count
    for i in range(0, count):
        empresa = Empresas()
        empresa.nome = fake.unique.company()
        empresa.cnpjcpf_emp = fake.unique.company_id()
        empresa.save()

    count = Estabelecimentos.objects.all().count()
    count = maxRows - count
    for i in range(0, count):
        estabelecimento = Estabelecimentos()
        estabelecimento.nome = fake.city()
        estabelecimento.cnpjcpf_est = fake.unique.company_id()
        estabelecimento.save()

    count = Usuarios.objects.all().count()
    count = maxRows - count
    for i in range(0, count):
        usuario = Usuarios()
        usuario.email = fake.email()
        usuario.nome = fake.name()
        usuario.save()

    for emp in Empresas.objects.all():
        emp.cnpjcpf_emp = emp.cnpjcpf_emp[:8]
        emp.save()

    aux = 1
    serie = 1
    empresa_id = 1
    for estab in Estabelecimentos.objects.all():

        if aux % 9 == 0:
            empresa_id += 1
            serie = 1
        try:
            empresa = Empresas.objects.get(pk=empresa_id)
            estab.cnpjcpf_est = f'{empresa.cnpjcpf_emp}000{serie}'
            estab.nome = f'{empresa.nome} - {estab.nome.split("-")[-1]}'
            estab.save()
        except:
            pass

        aux += 1
        serie += 1

    for estab in Estabelecimentos.objects.all():
        try:
            parametro, created = Parametros.objects.get_or_create(
                cnpjcpf_est=estab.cnpjcpf_est)
            parametro.nome = estab.nome
            parametro.day = randrange(1, 30)
            parametro.hour = f'{randrange(8,12)}:00:00.000'
            parametro.save()
        except:
            pass

    firstsTen = Empresas.objects.all()[:20]
    prestadors = Prestadores.objects.all()[:20]
    empresa = 0
    serie = 1
    aux = 1
    count = Notas.objects.all().count()
    count = maxRows - count
    for i in range(0, count):

        empresa += 1
        if aux % 9 == 0:
            empresa = 1

        serie += 1
        if aux % 6 == 0:
            serie = 1

        aux += 1

        nota = Notas()
        nota.cnpjcpf_emp = firstsTen[empresa].cnpjcpf_emp
        nota.cnpjcpf_est = f'{firstsTen[empresa].cnpjcpf_emp}000{serie}'
        nota.cnpjcpf_prest = prestadors[serie].cnpjcpf_prest
        nota.numero_nota = aux
        nota.serie = fake.ean(length=8)
        nota.deducao = randrange(100)
        nota.valor_servico = randrange(100)
        nota.dh_emissao = f'2022-{randrange(1,12)}-{randrange(1,30)}T00:00:00'
        nota.descricao = fake.job()
        nota.codigo_servico = randrange(100)
        nota.cancelada = randrange(100)
        nota.iss_retido = randrange(100)
        nota.aliq_iss = randrange(100)
        nota.valor_iss = randrange(100)
        nota.valor_pis = randrange(100)
        nota.valor_cofins = randrange(100)
        nota.valor_csll = randrange(100)
        nota.valor_irrf = randrange(100)
        nota.valor_inss = randrange(100)
        nota.serie_rps = randrange(100)
        nota.rps = randrange(100)
        nota.codigo_verificacao = randrange(100)
        nota.save()

    return
