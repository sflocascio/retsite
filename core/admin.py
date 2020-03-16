from django.contrib import admin

from core.models import  *


class RetSectionAdmin(admin.ModelAdmin):
    model = Ret

class TechnologyAdmin(admin.ModelAdmin):
    model = Technology

class DocumentAdmin(admin.ModelAdmin):
    model = Document


# class DocumentInLine(admin.StackedInline):
#     model = Document
#     list_display = ("document", "position", "process", )


# class DocumentAdmin(admin.ModelAdmin):
#     model = Document
#     list_display = ("document", "position", "process", )

class ProcessAdmin(admin.ModelAdmin):
    model = Process


class ScreenshotAdmin(admin.ModelAdmin):
    model = Screenshot

# class ProcessAdmin(admin.ModelAdmin):
#     model = Process
#     list_display = ("ref_number", "session_name",)
#     inlines = [DocumentInLine,]




#admin.site.register(Event, EventAdmin)
# admin.site.register(Process, ProcessAdmin)
# admin.site.register(Document, DocumentAdmin)

# admin.site.register(Unrelated)
admin.site.register(Ret)
admin.site.register(Document)
admin.site.register(Process)
admin.site.register(Technology)
admin.site.register(Screenshot)