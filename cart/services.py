from .models import Cart, CartItem

from restaurants.models import RestaurantMeal





def get_or_create_cart(user):

    cart, created = Cart.objects.get_or_create(
        user=user
    )

    return cart





def add_to_cart(
        user,
        restaurant_meal_id,
        quantity=1,
        consumed_by="self"
):


    cart = get_or_create_cart(user)



    restaurant_meal = RestaurantMeal.objects.get(

        id=restaurant_meal_id,

        is_available=True,

        restaurant__is_active=True

    )



    item, created = CartItem.objects.get_or_create(

        cart=cart,

        restaurant_meal=restaurant_meal,

        consumed_by=consumed_by,


        defaults={

            "quantity": quantity,

            "price": restaurant_meal.price,

        }

    )



    if not created:


        item.quantity += quantity

        item.price = restaurant_meal.price

        item.save()



    return item





def remove_from_cart(
        user,
        item_id
):


    cart = get_or_create_cart(user)



    CartItem.objects.filter(

        id=item_id,

        cart=cart

    ).delete()





def update_quantity(
        user,
        item_id,
        quantity
):


    cart = get_or_create_cart(user)



    item = CartItem.objects.get(

        id=item_id,

        cart=cart

    )



    if quantity <= 0:

        item.delete()

        return None



    item.quantity = quantity

    item.save()



    return item





def get_cart_total(user):


    cart = get_or_create_cart(user)



    total = 0



    for item in cart.items.all():

        total += item.subtotal()



    return total





def clear_cart(user):


    cart = get_or_create_cart(user)


    cart.items.all().delete()