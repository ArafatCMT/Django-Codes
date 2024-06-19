from django.contrib import admin
from accounts.models import UserBankAccount, UserAddress, BankRupt

admin.site.register(UserBankAccount)
admin.site.register(UserAddress)
admin.site.register(BankRupt)
