from re import A
from django.contrib import admin
from account.models import Account
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('email', 'phone', 'username', 'first_name',
                    'last_name', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'phone', 'username', 'first_name',
                     'last_name')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
