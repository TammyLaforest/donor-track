from django.shortcuts import render


from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Person

class PersonListView(ListView):
    model = Person
    context_object_name = 'people'

class PersonCreateView(CreateView):
    model = Person
    fields = ('name', 'birthdate', 'country', 'city')
    success_url = reverse_lazy('person_changelist')

class PersonUpdateView(UpdateView):
    model = Person
    fields = ('name', 'birthdate', 'country', 'city')
    success_url = reverse_lazy('person_changelist')

    

#views.py
def all_json_models(request, brand):
    current_brand = VehicleBrand.objects.get(code=brand)
    name = 'brand_model_select'
    models = VehicleModel.objects.all().filter(brand=current_brand)
    json_models = serializers.serialize("json", models)
    return HttpResponse(json_models, mimetype="application/javascript")
