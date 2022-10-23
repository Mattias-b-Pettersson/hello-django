from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):
   
    def test_item_name_is_requierd(self):
        form = ItemForm({"name": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("name", forms.errors.key())
        self.assertEqual(forms.errors["error"][0], "This field is requierd.")

    def test_item_name_is_requierd(self):
        form = ItemForm({"name": "Test ToDo item"})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ItemForm({"name": "Test ToDo item"})
        self.assertTrue(form.Meta.fields, ["name", "done"])
