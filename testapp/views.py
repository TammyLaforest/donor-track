from django.shortcuts import render

#views.py
def all_json_models(request, brand):
    current_brand = VehicleBrand.objects.get(code=brand)
    name = 'brand_model_select'
    models = VehicleModel.objects.all().filter(brand=current_brand)
    json_models = serializers.serialize("json", models)
    return HttpResponse(json_models, mimetype="application/javascript")
