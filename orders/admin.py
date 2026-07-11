from django.contrib import admin
from .models import Customer, Product, Order, OrderItem

admin.site.site_header = "Order Management Admin"
admin.site.site_title = "Order Management"
admin.site.index_title = "Welcome to Order Management"

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'created_at')
    search_fields = ('user__username', 'user__email', 'phone_number')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock_quantity', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'status', 'total_amount', 'created_at')
    list_filter = ('status',)
    inlines = [OrderItemInline]
