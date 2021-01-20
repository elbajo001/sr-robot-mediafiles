from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import *
from srrobot import urls

def error_404_view(request, exception):
    """ print("urls:")
    for url in urls.urlpatterns.index(1):
        print(url) """
    return render(request, 'registro/404.html', {}, status=404)

def index(request):
    return render(request, 'registro/index.html')

# Clientes

def agregarCliente(request):
    return render(request, 'registro/agregar-cliente.html')

def listarClientes(request):
    customers = Customer.objects.all()
    return render(request, 'registro/lista-clientes.html', {'customers': customers})

def enviarCliente(request):
    customer = Customer()
    customers = Customer.objects.all()
    customer.document = request.POST.get('document')
    customer.first_name = request.POST.get('first_name')
    customer.last_name = request.POST.get('last_name')
    customer.genre = request.POST.get('genre')
    customer.age = request.POST.get('age')
    customer.phone_num = request.POST.get('phone_num')
    customer.phone_num_wa = request.POST.get('phone_num_wa')
    customer.email_address = request.POST.get('email_address')
    customer.home_address = request.POST.get('home_address')
    customer.office_address = request.POST.get('office_address')
    customer.save()
    return redirect('lista-clientes')

def detalleCliente(request, id):
    try:
        customer = Customer.objects.get(id=id)
    except Customer.DoesNotExist:
        raise Http404('Lo sentimos. No se pudo encontrar el cliente.')
    return render(request, 'registro/detalle-cliente.html', {'customer': customer})

def eliminarCliente(request, id):
    customer = Customer.objects.get(id=id)
    #customers = Customer.objects.all()
    try:
        customer.delete()
    except Customer.DoesNotExist:
        raise Http404('No se pudo encontrar el cliente :c sorry')
    #return render(request, 'registro/lista-clientes.html', {'customers': customers})
    return redirect('lista-clientes')

def editarCliente(request,id):
    customer = Customer.objects.get(id=id)
    datos = {
        "id": customer.id,
        "document" : customer.document,
        "first_name" : customer.first_name,
        "last_name" : customer.last_name,
        "genre" : customer.genre,
        "age" : customer.age,
        "phone_num": customer.phone_num,
        "phone_num_wa": customer.phone_num_wa,
        "email_address": customer.email_address,
        "home_address": customer.home_address,
        "office_address": customer.office_address,
    }
    return render(request, 'registro/editar-cliente.html', context=datos)


def actualizarCliente(request, id):
    customer = Customer.objects.get(id=id)
    #customers = Customer.objects.all()
    customer.document = request.POST.get('document')
    customer.first_name = request.POST.get('first_name')
    customer.last_name = request.POST.get('last_name')
    customer.genre = request.POST.get('genre')
    customer.age = request.POST.get('age')
    customer.phone_num = request.POST.get('phone_num')
    customer.phone_num_wa = request.POST.get('phone_num_wa')
    customer.email_address = request.POST.get('email_address')
    customer.home_address = request.POST.get('home_address')
    customer.office_address = request.POST.get('office_address')
    import datetime
    updated_at = datetime.datetime.now()
    customer.updated_at = updated_at
    customer.save()
    #return render(request,'registro/lista-clientes.html', {'customers' : customers})
    return redirect('lista-clientes')

# Visitas

def agregarVisita(request, id):
    customer = Customer.objects.get(id=id)
    return render(request, 'registro/agregar-visita.html', {'customer' : customer})

def listarVisitas(request):
    visits = Visit.objects.all()
    return render(request, 'registro/lista-visitas.html', {'visits': visits})

def enviarVisita(request, id):
    if request.method == 'POST':
        msg_error = ''
        customer = Customer.objects.get(id=id)
        visit = Visit()
        visits = Visit.objects.all()
        visit.customer = customer
        visit.description = request.POST.get('description')
        visit.visit_location = request.POST.get('visit_location')
        visit.value = request.POST.get('value')
        visit.hour_start = request.POST.get('hour_start')
        visit.hour_end = request.POST.get('hour_end')
        # Validación de valor cero
        if visit.value == '':
            visit.value = 0.0
        # Validación si existe un archivo cargado
        if request.FILES.get('myfile'):
            myfile = request.FILES.get('myfile')
            #myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            newname = myfile.name
            newname = newname.replace(" ", "_")
            filename = fs.save(newname, myfile)
            url = fs.url(filename)
            visit.media = url
        # validación si la hora inicio es mayor o igual que la hora de finalización
        if visit.hour_start >= visit.hour_end:
            msg_error = '¡Ups! La hora de inicio no puede ser mayor a la hora de finalización.'
            return render(request, 'registro/agregar-visita.html', {'customer':customer, 'visit':visit, 'msg_error':msg_error})
        visit.save()
        return redirect('lista-visitas')
    else:
        return redirect('lista-visitas')
    #return render(request, 'registro/lista-clientes.html', {'customers': customers})

def listarVisitasPorCliente(request, id):
    customer = Customer.objects.get(id=id)
    visits = Visit.objects.filter(customer=customer)
    return render(request, 'registro/lista-visitas-cliente.html', {'visits': visits, 'customer':customer})

def detalleVisita(request, id_cliente, id_visita):
    customer = Customer.objects.get(id=id_cliente)
    try:
        visit = Visit.objects.get(id=id_visita)
        import os
        name, extension = os.path.splitext(str(visit.media))
        #from math import floor
        #value = floor(visit.value)
    except Visit.DoesNotExist:
        raise Http404('Lo sentimos. No se pudo encontrar la visita.')
    #return render(request, 'registro/detalle-visita.html', {'visit':visit, 'customer':customer, 'value':value})
    return render(request, 'registro/detalle-visita.html', {'visit':visit, 'customer':customer, 'extension':findTypeOfMedia(extension)})

def editarVisita(request, id_cliente, id_visita):
    msg_error = ''
    customer = Customer.objects.get(id=id_cliente)
    visit = Visit.objects.get(id=id_visita)
    from math import floor
    value = floor(visit.value)
    datos = {
        "id": visit.id,
        "customer" : customer,
        "description" : visit.description,
        "media" : visit.media,
        "hour_start" : visit.hour_start,
        "hour_end" : visit.hour_end,
        "visit_location": visit.visit_location,
        "value": floor(visit.value),
        "msg_error":None
    }
    # validación si la hora inicio es mayor o igual que la hora de finalización
    if visit.hour_start >= visit.hour_end:
        msg_error = '¡Ups! La hora de inicio no puede ser mayor a la hora de finalización.'
        return render(request, 'registro/editar-visita.html', {'customer':customer, 'visit':visit, 'msg_error':msg_error, 'value':value})
    return render(request, 'registro/editar-visita.html', {'customer':customer, 'visit':visit, 'msg_error':msg_error, 'value':value})


def actualizarVisita(request, id_cliente, id_visita):
    if request.method == 'POST':
        msg_error = ''
        customer = Customer.objects.get(id=id_cliente)
        visit = Visit.objects.get(id=id_visita)
        #customers = Customer.objects.all()
        visit.customer = customer
        visit.description = request.POST.get('description')
        visit.hour_start = request.POST.get('hour_start')
        visit.hour_end= request.POST.get('hour_end')
        visit.visit_location = request.POST.get('visit_location')
        visit.value = request.POST.get('value')
        if visit.value == '':
            visit.value = 0.0
        # Validación si existe un archivo cargado
        if request.FILES.get('myfile'):
            myfile = request.FILES.get('myfile')
            #myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            newname = myfile.name
            newname = newname.replace(" ", "_")
            filename = fs.save(newname, myfile)
            url = fs.url(filename)
            visit.media = url
        # validación si la hora inicio es mayor o igual que la hora de finalización
        import datetime
        updated_at = datetime.datetime.now()
        visit.updated_at = updated_at
        if visit.hour_start >= visit.hour_end:
            msg_error = '¡Ups! La hora de inicio no puede ser mayor a la hora de finalización.'
            return render(request, 'registro/editar-visita.html', {'customer':customer, 'visit':visit, 'msg_error':msg_error})
        visit.save()
        #return render(request,'registro/lista-clientes.html', {'customers' : customers})
        return redirect('lista-visitas')
    else:
        return redirect('lista-visitas')


def eliminarVisita(request, id_cliente, id_visita):
    customer = Customer.objects.get(id=id_cliente)
    visit = Visit.objects.get(id=id_visita)
    #customers = Customer.objects.all()
    try:
        visit.delete()
    except Customer.DoesNotExist:
        raise Http404('No se pudo encontrar la visita :c sorry')
    #return render(request, 'registro/lista-clientes.html', {'customers': customers})
    return redirect('lista-visitas')

def findTypeOfMedia(extension):
    img = ('.jpg', '.jpeg', '.pjpeg', '.png', '.svg')
    audio = ('.mp3', '.m4a', '.ogg', '.wav')
    video = ('.mp4', '.m4p', '.flv', '.ogg', '.avi', '.wav', '.gif', '.amv')
    tipo = ''
    if extension in img:
        tipo = 'imagen'
    elif extension in audio:
        tipo = 'audio'
    else:
        tipo = 'video'
    return tipo