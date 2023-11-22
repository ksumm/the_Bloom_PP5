from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import ArtClass, Booking
from .forms import ArtClassBookingForm


def art_class_list(request):
    artclasses = ArtClass.objects.all()

    # Print titles of art classes for debugging
    for art_class in artclasses:
        print(art_class.title)

    return render(request, 'artclass/art_class_list.html', {'artclasses': artclasses})



def art_class_detail(request, art_class_id):
    art_class = get_object_or_404(ArtClass, pk=art_class_id)
    return render(request, 'artclass/art_class_detail.html', {'art_class': art_class})



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

            return HttpResponseRedirect('/success/')
    else:
        form = ArtClassBookingForm()

    return render(request, 'artclass/book_art_class.html', {'art_class': art_class, 'form': form})