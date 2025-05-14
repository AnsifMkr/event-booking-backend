from django.urls import path
from .views import event_list, book_event, my_bookings, register, EventCreateView

urlpatterns = [
    path('events/', event_list, name='event-list'),
    path('book-event/', book_event, name='book-event'),
    path('my-bookings/', my_bookings, name='my-bookings'),
    path('register/', register, name='register'),
    path('create-event/', EventCreateView.as_view(), name='create-event'),  # 👈 Add this
]
