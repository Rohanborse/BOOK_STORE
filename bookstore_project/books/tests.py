from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book

class BookAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.book_data = {
            'title': 'Test Book',
            'author': 'Test Author',
            'publication_date': '2023-01-01',
            'price': '25.99',
        }

        self.book = Book.objects.create(**self.book_data)

    def test_create_book(self):
        response = self.client.post('/api/books/', self.book_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_single_book(self):
        response = self.client.get(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_book(self):
        updated_data = {
            'title': 'Updated Book Title',
            'author': 'Updated Author',
            'publication_date': '2023-02-01',
            'price': '29.99',
        }
        response = self.client.put(f'/api/books/{self.book.id}/', updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        response = self.client.delete(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
