Little Lemon Restaurant API

This is the API documentation for the Little Lemon restaurant project.

API Endpoints for Testing:

Menu API:
/restaurant/menu/ - GET, POST (List and create menu items)
/restaurant/menu/<id> - GET, PUT, DELETE (Retrieve, update, delete specific menu item)

Booking API (requires authentication):
/restaurant/booking/tables/ - GET, POST (List and create bookings)
/restaurant/booking/tables/<id> - GET, PUT, DELETE (Retrieve, update, delete specific booking)

Authentication API:
/auth/users/ - POST (User registration)
/auth/token/login/ - POST (Login to get authentication token)
/auth/token/logout/ - POST (Logout)

Admin Interface:
/admin/ - Django admin interface

Note: For booking endpoints, you need to include the authentication token in the request header:
Authorization: Token <your_token_here> 