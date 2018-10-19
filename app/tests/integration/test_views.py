from unittest import TestCase
from ..base import TestClient
from calculator.app import app


class ViewTests(TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = TestClient(app)

    def test_multiply(self):
        r = self.client.get("/calc/3*10")
        self.assertEquals(r.status_code, 200)
        self.assertEquals(r.body, "30")

    def test_multiply_out_of_bounds(self):
        r = self.client.get("/calc/3*10000")
        self.assertEquals(r.status_code, 403)

    def test_division(self):
        r = self.client.get("/calc/50/10")
        self.assertEquals(r.status_code, 200)
        self.assertEquals(r.body, "5")

    def test_division_out_of_bounds(self):
        r = self.client.get("/calc/-1001/10")
        self.assertEquals(r.status_code, 403)

    def test_division_zero(self):
        r = self.client.get("/calc/100/0")
        self.assertEquals(r.status_code, 403)
