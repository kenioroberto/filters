from django.shortcuts import render
from cliente.filters import ClienteFilter
from cliente.models import Cliente


# Create your views here.
def listar_cliente(request):
    clientes_list = Cliente.objects.all().order_by('-id')
    
    # Filtro
    Myfilter = ClienteFilter(request.GET, queryset=clientes_list)
    clientes_list = Myfilter.qs 
    
          
    context ={
        'clientes_list': clientes_list,
        'Myfilter': Myfilter,
                
    }
    return render(request, 'clientes/listar_cliente.html', context)