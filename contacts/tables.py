# # models.py
# class Person(models.Model):
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     user = models.ForeignKey('auth.User')
#     dob = models.DateField()

# tables.py
import django_tables2 as tables

class PersonTable(tables.Table):
    class Meta:
        model = Person

# # views.py
# def person_list(request):
#     table = PersonTable(Person.objects.all())
#
#     return render(request, 'person_list.html', {
#         'table': table
#     })
