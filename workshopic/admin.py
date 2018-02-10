from django.contrib import admin
from .models import Workshop
from .models import Participant
from .models import Facilitator


# Register your models here.
admin.site.register(Workshop)
admin.site.register(Participant)
admin.site.register(Facilitator)
