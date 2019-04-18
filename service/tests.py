from django.test import SimpleTestCase

# Create your tests here.
class MainAppTest(SimpleTestCase):
    def test_prescription_view_exist(self):
        response = self.client.get('/newPres/')
        self.assertEqual(response.status_code,200)
