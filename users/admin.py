from django.contrib import admin
from .models import Transactions,Expenses
# Register your models here.
admin.site.register(Transactions)


class ExpenseAdmin(admin.ModelAdmin):
    list_fields=['expense_name','expense_amount']
    
admin.site.register(Expenses,ExpenseAdmin)
