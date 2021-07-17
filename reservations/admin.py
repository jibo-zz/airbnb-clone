from django.contrib import admin
from . import models


@admin.register(models.reservation)
class reservationAdmin(admin.ModelAdmin):

    """Reservation Admin Definition"""

    pass
