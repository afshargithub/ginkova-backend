from django.contrib import admin

from .models import (
    Restaurant,
    RestaurantMeal,
    RestaurantTranslation,
)


class RestaurantTranslationInline(
    admin.TabularInline
):
    model = RestaurantTranslation

    extra = 0

    fields = (
        "language",
        "name",
        "address",
    )

    ordering = (
        "language",
    )


class RestaurantMealInline(
    admin.TabularInline
):
    model = RestaurantMeal

    extra = 1

    fields = (
        "meal",
        "price",
        "estimated_preparation_time",
        "is_available",
        "image",
    )


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "phone",
        "delivery_radius",
        "is_active",
        "created_at",
    )

    search_fields = (
        "name",
        "address",
        "phone",
        "manager_name",
        "translations__name",
        "translations__address",
    )

    list_filter = (
        "is_active",
        "created_at",
    )

    ordering = (
        "name",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    inlines = (
        RestaurantTranslationInline,
        RestaurantMealInline,
    )


@admin.register(RestaurantMeal)
class RestaurantMealAdmin(admin.ModelAdmin):
    list_display = (
        "id",
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
        "restaurant__translations__name",
        "meal__name",
        "meal__translations__name",
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
                ),
            },
        ),
        (
            "Preparation",
            {
                "fields": (
                    "estimated_preparation_time",
                    "is_available",
                ),
            },
        ),
        (
            "Dates",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                ),
            },
        ),
    )