from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
import datetime

from inventario_cei.models import Reserve

def index(request):
    
    rooms = [MockSala(), MockSala(), MockSala(), MockSala()]

    # all week reserves 
    today = datetime.datetime.today()
    start_week = today - datetime.timedelta(today.weekday())
    end_week = start_week + datetime.timedelta(7)
    weekReserves = Reserve.objects.filter(start__range=[start_week, end_week]).values(
        'id', 'user__username','space__name','start','finish').order_by('-created')

    # Pending reserves
    pendingHeaders = ['Id', 'Usuario', 'Articulo', 'Fecha de prestamo', 'Fecha de solicitud']
    pending = Reserve.objects.filter(state='p').values(
        'id', 'user__username','space__name','start','finish').order_by('-created')
    
    # Lending
    lendingHeaders = ['Id', 'Usuario', 'Articulo', 'Fecha de prestamo', 'Fecha de solicitud']
    lendings = Reserve.objects.filter(state='a').values(
        'id', 'user__username','space__name','start','finish','state').order_by('-updated')

    context = {'message' : "Hello world!",
                'weekReserves':weekReserves,
                'pendingHeaders': pendingHeaders,
                'pendings': list(pending),
                'lendingHeaders': lendingHeaders,
                'lendings': list(lendings),
                'rooms': rooms,
            }
    template = loader.get_template('administrator/index.html')
    
    return HttpResponse(template.render(context, request))

def postPending(request):
    if request.method != 'POST':
        return HttpResponseRedirect('/administrator')

    selectedIds = request.POST.getlist('pre-selected')
    
    if len(selectedIds) == 0:
        return HttpResponseRedirect('/administrator')
    resvs = Reserve.objects.filter(pk__in=selectedIds)
    if 'accept' in request.POST : 
        for r in resvs:
            r.state = 'a'
            r.save()
    elif 'negate' in request.POST : 
        for r in resvs:
            r.state = 'r'
            r.save()
    
    return HttpResponseRedirect('/administrator')

# this method handles only post requests
# changes the 'state' of Reserves
def postPending(request):
    if request.method != 'POST':
        return HttpResponseRedirect('/administrator')

    selectedIds = request.POST.getlist('pre-selected')
    
    if len(selectedIds) == 0:
        return HttpResponseRedirect('/administrator')
    resvs = Reserve.objects.filter(pk__in=selectedIds)
    if 'accept' in request.POST : 
        for r in resvs:
            r.state = 'a'
            r.save()
    elif 'negate' in request.POST : 
        for r in resvs:
            r.state = 'r'
            r.save()
    
    return HttpResponseRedirect('/administrator')

# TODO: define behavior
def postLending(request):
    return HttpResponseRedirect('/administrator')


class MockSala():
    id = 1
    name = 'Sala #'
