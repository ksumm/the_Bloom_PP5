from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import ArtClass
from .forms import ArtClassBookingForm


def art_class_list(request):
    artclasses = ArtClass.objects.all()

    # Print titles of art classes for debugging
    for art_class in artclasses:
        print(art_class.title)

    return render(request, 'artclass/art_class_list.html', {'artclasses': artclasses})  # noqa


def art_class_detail(request, art_class_id):
    art_class = get_object_or_404(ArtClass, pk=art_class_id)
    return render(request, 'artclass/art_class_detail.html', {'art_class': art_class})  # noqa


@login_required
def book_art_class(request, art_class_id):
    art_class = get_object_or_404(ArtClass, pk=art_class_id)

    if request.method == 'POST':
        form = ArtClassBookingForm(request.POST)
        if form.is_valid():
            # Create a Booking object
            booking = form.save(commit=False)
            booking.art_class = art_class
            booking.user = request.user  # Set the user to the logged-in user
            booking.save()

            # Mark the art class as booked
            art_class.is_booked = True
            art_class.save()

            return HttpResponseRedirect(reverse('artclass:success_view'))
    else:
        form = ArtClassBookingForm()

    return render(request, 'artclass/book_art_class.html', {'art_class': art_class, 'form': form})  # noqa


def success_view(request):
    return render(request, 'artclass/success.html')
