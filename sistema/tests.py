from django.test import TestCase, Client

class MetricsViewTests(TestCase):
    def test_index_loads(self):
        client = Client()
        resp = client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_api_metrics(self):
        client = Client()
        resp = client.get('/api/metrics/')
        self.assertEqual(resp.status_code, 200)
        self.assertIn('application/json', resp['Content-Type'])
