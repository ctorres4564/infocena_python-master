from django.contrib import admin

from siteweb.models import MotivoContato, FaleConosco, Aluguel, Cliente

# Register your models here.
admin.site.register(MotivoContato)
admin.site.register(FaleConosco)
admin.site.register(Aluguel)
admin.site.register(Cliente)
