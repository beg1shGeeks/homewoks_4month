
from django.shortcuts import render, get_object_or_404
from phone_app.models import Phones

# Create your views here.

# не полная информация
def phone_all_view(request):
    phone_list = Phones.objects.all()
    context = {
        'phone_list': phone_list
    }
    return render(request, 'phone_list.html', context)

# детальная информация
def phone_detail_view(request,id):
    phone_id = get_object_or_404(Phones, id=id)
    context = {
        'phone_id': phone_id
    }
    return render(request, 'phone_detail.html', context)