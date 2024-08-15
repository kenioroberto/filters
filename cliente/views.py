from django.shortcuts import render
from cliente.models import Cliente

# Create your views here.
def listar_cliente(request):
    clientes_list = Cliente.objects.all().order_by('-id')
    
    context ={
        'clientes_list': clientes_list,
    }
    return render(request, 'clientes/listar_cliente.html', context)