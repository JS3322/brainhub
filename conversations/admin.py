from django.contrib import admin
from . import models


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):

    """ Message Admin Definition conversations/admin list_display = ("__str__", "created") """

    list_display = ("__str__",)


@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):

    """ Conversation Admin Definition """

    list_display = ("__str__", "count_messages", "count_participants")
