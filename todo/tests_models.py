from django.test import TestCase
from .models import Item


class TestItemForm(TestCase):

    def test_done_defaults_to_false(self):
        item = Item.objects.create(name="test Todo Item")
        self.assertFalse(item.done)

    def test_item_string_method_returns_name(self):
        item = Item.objects.create(name="test Todo Item")
        self.assertEqual(str(item), "test Todo Item")