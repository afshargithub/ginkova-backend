from django.contrib import admin

from .models import (
    Restaurant,
    RestaurantMeal,
)


# =====================================================
# Restaurant Meal Inline
# =====================================================

class RestaurantMealInline(admin.TabularInline):

    model = RestaurantMeal

    extra = 1

    fields = (
        "meal",
        "price",
        "estimated_preparation_time",
        "is_available",
        "image",
    )



# =====================================================
# Restaurant Admin
# =====================================================

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "phone",
        "delivery_radius",
        "is_active",
        "created_at",
    )


    search_fields = (
        "name",
        "phone",
        "manager_name",
    )


    list_filter = (
        "is_active",
        "created_at",
    )


    readonly_fields = (
        "created_at",
        "updated_at",
    )


    inlines = [
        RestaurantMealInline
    ]



# =====================================================
# Restaurant Meal Admin
# =====================================================

@admin.register(RestaurantMeal)
class RestaurantMealAdmin(admin.ModelAdmin):

    list_display = (
        "restaurant",
        "meal",
        "price",
        "estimated_preparation_time",
        "is_available",
        "updated_at",
    )


    list_filter = (
        "restaurant",
        "is_available",
    )


    search_fields = (
        "restaurant__name",
        "meal__name",
    )


    readonly_fields = (
        "created_at",
        "updated_at",
    )


    fieldsets = (

        (
            "Meal Information",
            {
                "fields": (
                    "restaurant",
                    "meal",
                    "price",
                    "image",
                )
            }
        ),


        (
            "Preparation",
            {
                "fields": (
                    "estimated_preparation_time",
                    "is_available",
                )
            }
        ),


        (
            "Dates",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            }
        ),

    )