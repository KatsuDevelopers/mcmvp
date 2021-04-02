from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from .forms import PinChangeForm
from .models import PinModel
from .serializer import PinModelSerializer


@api_view(['GET'])
def return_pin(request):
    pin = PinModel.objects.last()
    pin = PinModelSerializer(pin)
    return Response({'pin-off': pin.data['pin_number']})

def change_pin(request):
    if request.method == 'POST':
        form = PinChangeForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            PinModel.objects.create(pin_number = cd['pin'])
            messages.success(request, 'Pin Saved')
            return render(request, 'command/pin_change/change.html', {'form': PinChangeForm()})

    else:
        form = PinChangeForm()
        return render(request, 'command/pin_change/change.html', {'form': form})

# Create your views here.
