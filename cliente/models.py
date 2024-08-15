from django.db import models

class Cliente (models.Model):
    nome = models.CharField(max_length=255)
    nome_fantasia = models.CharField(max_length=255)
    email = models.EmailField(max_length=75, blank=True, null=True)
    telefone =  models.CharField(max_length=75, blank=True)
    cnpj = models.CharField(max_length=75, blank=True)
    endereco = models.CharField(max_length=255, blank=True)
    cidade = models.CharField(max_length=255, blank=True)
    estado = models.CharField(
        max_length=2,
        default='DF',
        choices=(
            ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantins'),
        )
    )
    descricao = models.TextField(blank=True)
    tipo = models.CharField(
        default='Varejo',
        max_length=20,
        choices=(
            ('Varejo', 'Varejo'),
            ('Atacado', 'Atacado'),
            ('Food', 'Food'),
            ('Distribuidor', 'Distribuidor'),
        )
    )
    
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Data de Cadastro')
    data_atializacao = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nome
