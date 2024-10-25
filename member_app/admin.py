from django.contrib import admin
from .models import Member


admin.site.register(Member)

class MemberAdmin(admin.ModelAdmin):
  list_display = ('username','age', 'date')

  admin.site.register(Member,MemberAdmin)