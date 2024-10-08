from django.contrib import admin
from.models import*

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Email', 'Phone', 'Message')


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('Name2', 'Email2', 'Phone2', 'Product2', 'Message2')
