from django.contrib import admin
from . import models


@admin.register(models.reservation)
class reservationAdmin(admin.ModelAdmin):

    """Reservation Admin Definition"""

    list_display = (
        "room",
        "status",
        "check_in",
        "check_out",
        "guest",
        "in_progress",
        "is_finished",
    )

    list_filter = ("status",)
