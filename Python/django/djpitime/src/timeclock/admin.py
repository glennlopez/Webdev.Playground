from django.contrib import admin

# Register your models here.
from .models import UserActivity

class UserActivityAdmin(admin.ModelAdmin):
	search_fields = ['user__username', 'user__email']
	list_display = ['__unicode__', 'timestamp']
	list_filter = ['timestamp']
	class Meta:
		model = UserActivity

admin.site.register(UserActivity, UserActivityAdmin)
