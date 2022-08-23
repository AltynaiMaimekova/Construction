from django.contrib import admin

from .models import *


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):

    @admin.display(description='общее кол-во квартир')
    def total_apartments(self, obj):
        return obj.number_apartments * obj.floors

    @admin.display(description='итоговая стоимость всех квартир')
    def total_cost_all_apartments(self, obj):
        total_cost = 0
        for apartment in obj.apartment_set.all():
            total_cost += apartment.squire * obj.cost_per_sqm
        return total_cost

    list_display = ('number', 'entrances', 'floors', 'number_apartments',
                    'total_apartments', 'total_cost_all_apartments')


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):

    @admin.display(description='итоговая стоимость')
    def total_price(self, obj):
        return obj.squire * obj.block.cost_per_sqm

    date_hierarchy = 'date_purchase'
    list_display = ('surname', 'date_purchase', 'status', 'squire', 'total_price')
    list_editable = ('date_purchase',)
    empty_value_display = '--без хоз--'
    list_filter = ('block', 'status')
    search_fields = ['surname',]

