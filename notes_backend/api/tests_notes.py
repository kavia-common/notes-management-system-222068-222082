from rest_framework.test import APITestCase
from django.urls import reverse


class NotesCrudTests(APITestCase):
    def setUp(self):
        self.list_url = reverse("notes-list-create")

    def test_create_and_list_notes(self):
        # Create
        payload = {"title": "Test Note", "content": "Body"}
        res = self.client.post(self.list_url, data=payload, format="json")
        self.assertEqual(res.status_code, 201)
        self.assertIn("id", res.data)

        # List
        res_list = self.client.get(self.list_url)
        self.assertEqual(res_list.status_code, 200)
        self.assertTrue(any(item["title"] == "Test Note" for item in res_list.data))
