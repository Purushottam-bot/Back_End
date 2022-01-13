from django.contrib import admin
from first_app.models import Topic,webpage,AccessRecord

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(webpage)

# Register your models here.
