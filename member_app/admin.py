from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin): 
  list_display = ('username', 'age', 'date')

admin.site.register(Member, MemberAdmin)