from django.test import TestCase
from django.urls import reverse


class NewsViewsTests(TestCase):
    def test_news_list_view__when_no_news__expect_empty_list(self):
        response = self.client.get(reverse('list news'))

        return self.assertEqual(0, len(response.context['news']))
