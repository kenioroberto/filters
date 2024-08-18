import django_filters
from cliente.models import Cliente

class ClienteFilter(django_filters.FilterSet):
    
    nome = django_filters.CharFilter(
        field_name='nome',
        lookup_expr='icontains',
        label='Nome do Cliente'
    )
    
    ativo = django_filters.ChoiceFilter(
        field_name = 'ativo',
        choices = (
            (True, 'Ativo'),
            (False, 'Inativo'),
        ),
        empty_label = 'Todos'
    )
    class Meta:
        model = Cliente
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(ClienteFilter, self).__init__(*args, **kwargs)
        
        self.form.fields['nome'].widget.attrs['class']= 'form-control form-control-sm'
        self.form.fields['cnpj'].widget.attrs['class']= 'form-control form-control-sm'
        self.form.fields['ativo'].widget.attrs['class']= 'form-control form-control-sm'
        self.form.fields['estado'].widget.attrs['class']= 'form-control form-control-sm'
        self.form.fields['tipo'].widget.attrs['class']= 'form-control form-control-sm'