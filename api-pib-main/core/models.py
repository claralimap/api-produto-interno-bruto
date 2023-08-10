from django.db import models

class Indice(models.Model): 
    ano = models.CharField(max_length=1000, blank = True, null = True)
    mes = models.CharField(max_length=1000, blank = True, null = True)
    indice = models.CharField(max_length=50, blank = True, null = True)
    variacao_mensal = models.CharField(max_length=1000, blank = True, null = True)
    variacao_12_meses = models.CharField(max_length=1000, blank = True, null = True)
    variacao_acumulada_ano = models.CharField(max_length=1000, blank = True, null = True)
    indice_fechamento_mensal = models.CharField(max_length=1000)

class PIB(models.Model):
    ano = models.CharField(max_length=100, default = 0)
    id_uf = models.CharField(max_length=100, default = 0)
    sigla_uf = models.CharField(max_length=100, default = 0)
    pib = models.CharField(max_length=100, default = 0)
    impostos_liquidos = models.CharField(max_length=100, default = 0)
    va = models.CharField(max_length=100, default = 0)
    va_agropecuaria = models.CharField(max_length=100, default = 0)
    va_industria = models.CharField(max_length=100, default = 0)
    va_servicos = models.CharField(max_length=100, default = 0)
    va_adespss = models.CharField(max_length=100, default = 0)

    def __str__(self):
        return self.ano 