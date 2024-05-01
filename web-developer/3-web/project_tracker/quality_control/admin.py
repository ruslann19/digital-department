from django.contrib import admin
from .models import BugReport, FeatureRequest

@admin.action(description='Поменять статус на "Завершена"')
def change_status_to_Completed(self, request, queryset):
    queryset.update(status='Completed')
    self.message_user(request, f"Статус изменён на 'Завершено' у {queryset.count()} записи(ей).")

@admin.action(description='Поменять статус на "Новая"')
def change_status_to_New(self, request, queryset):
    queryset.update(status='New')
    self.message_user(request, f"Статус изменён на 'Новая' у {queryset.count()} записи(ей).")

@admin.action(description='Поменять статус на "В работе"')
def change_status_to_In_progress(self, request, queryset):
    queryset.update(status='In_progress')
    self.message_user(request, f"Статус изменён на 'В работе' у {queryset.count()} записи(ей).")

@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'created_at')
    list_filter = ('status', 'project')
    search_fields = ('title', 'description')
    actions = [change_status_to_Completed, change_status_to_New, change_status_to_In_progress]
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'created_at',)
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('project', 'task', 'status', 'priority',),
        }),
    )
    readonly_fields = ('created_at', 'updated_at',)

@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'created_at')
    list_filter = ('status', 'project')
    search_fields = ('title', 'description')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'created_at',)
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('project', 'task', 'status', 'priority',),
        }),
    )
    readonly_fields = ('created_at', 'updated_at',)
