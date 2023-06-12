from django.contrib import admin
from .models import UserProfile, HappyDay, Message

admin.site.register(UserProfile)

admin.site.register(HappyDay)




class MessageAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        # Filtrar apenas as mensagens principais (sem respostas)
        queryset = queryset.filter(parent_message=None)
        return queryset

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'parent_message':
            # Filtrar as opções de parent_message para mostrar apenas o parente do tópico principal
            kwargs['queryset'] = Message.objects.filter(parent_message=None)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Message, MessageAdmin)