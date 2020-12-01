from django.test import TestCase
from django.urls import reverse

from .models import Category, Publisher, Author, Book


class BookTests(TestCase):

    category_name = "Comic"

    def setUp(self):
        Category.objects.create(name=self.category_name)

    def test_category_content(self):
        id=1
        category = Category.objects.get(pk=id)
        expected_object_name = f'{category.name}'
        self.assertEquals(expected_object_name, self.category_name)

    def test_category_list_view(self):
        response = self.client.get(reverse('category_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h2><a href="/category/">Category</a></h2>')
        self.assertTemplateUsed(response, 'book/category_list.html')