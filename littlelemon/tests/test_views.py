from django.test import TestCase
from restaurant.models import MenuItem

class MenuViewTest(TestCase):
    def setUp(self):
        MenuItem.objects.create(title="IceCream", price=80, inventory=100)
    
    def test_getall(self):
        items = MenuItem.objects.all()
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].title, "IceCream")
        self.assertEqual(items[0].price, 80)
        self.assertEqual(items[0].inventory, 100)
