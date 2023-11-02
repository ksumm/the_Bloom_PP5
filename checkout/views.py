from django.shortcuts import render, redirect, reverse
from django.contrib import messages


from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your shopping bag is empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51O80FTEf394j36LQ2QWpqWVZFxkj7IebHmEF2TeAQCG2JSdPkCBuOR7k8GmzMplrEy7IStlL5Ne1v9n2Licfs35E005vQSYj4A',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
