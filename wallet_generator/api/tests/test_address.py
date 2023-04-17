from logging import INFO, basicConfig, getLogger
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from wallet_generator.api.models import Address

# from django.urls import reverse


logger = getLogger(__name__)
basicConfig(level=INFO)
# Create your tests here.
class AddressTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.address_url = reverse("address")
        self.acronym = ["BTC", "BTG", "BCH", "ETH", "LTC", "DASH", "DOGE"]

    def test_list_address(self):
        res = self.client.get(self.address_url, format="json")
        self.assertTrue(res.json()["success"])
        self.assertEqual(
            res.json()["message"], "All addresses are retrieved successfully!"
        )
        self.assertEqual(res.json()["account_details"], [])

    def test_list_address_with_address(self):
        request_data = {"network": self.acronym[0]}
        self.client.post(self.address_url, data=request_data, format="json")
        res = self.client.get(self.address_url, format="json")
        self.assertTrue(res.json()["success"])
        self.assertEqual(
            res.json()["message"], "All addresses are retrieved successfully!"
        )
        self.assertIsNotNone(res.json()["account_details"][0]["private_key"])
        self.assertIsNotNone(res.json()["account_details"][0]["public_key"])

    def test_get_address_by_id(self):
        request_data = {"network": self.acronym[0]}
        self.client.post(self.address_url, data=request_data, format="json")
        get_request_data = {"wallet_id": 1}
        res = self.client.get(self.address_url, data=get_request_data, format="json")
        self.assertTrue(res.json()["success"])
        self.assertEqual(
            res.json()["message"], "All addresses are retrieved successfully!"
        )
        self.assertEqual(res.json()["account_details"]["coin"], self.acronym[0])
        self.assertIsNotNone(res.json()["account_details"]["private_key"])
        self.assertIsNotNone(res.json()["account_details"]["public_key"])

    def test_address_creation_no_acronym(self):
        res = self.client.post(self.address_url, format="json")
        self.assertFalse(res.json()["success"])
        self.assertEqual(res.json()["error"], "Please specify the acronym!")

    def test_address_creation_btc(self):
        request_data = {"network": self.acronym[0]}
        res = self.client.post(self.address_url, data=request_data, format="json")
        self.assertTrue(res.json()["success"])
        self.assertEqual(
            res.json()["message"], "New wallet has been created successfully"
        )
        self.assertEqual(res.json()["account_details"]["coin"], self.acronym[0])
        self.assertIsNotNone(res.json()["account_details"]["private_key"])
        self.assertIsNotNone(res.json()["account_details"]["public_key"])

    def test_address_creation_btg(self):
        request_data = {"network": self.acronym[1]}
        res = self.client.post(self.address_url, data=request_data, format="json")
        self.assertTrue(res.json()["success"])
        self.assertEqual(
            res.json()["message"], "New wallet has been created successfully"
        )
        self.assertEqual(res.json()["account_details"]["coin"], self.acronym[1])
        self.assertIsNotNone(res.json()["account_details"]["private_key"])
        self.assertIsNotNone(res.json()["account_details"]["public_key"])

    def test_address_creation_bch(self):
        request_data = {"network": self.acronym[2]}
        res = self.client.post(self.address_url, data=request_data, format="json")
        self.assertTrue(res.json()["success"])
        self.assertEqual(
            res.json()["message"], "New wallet has been created successfully"
        )
        self.assertEqual(res.json()["account_details"]["coin"], self.acronym[2])
        self.assertIsNotNone(res.json()["account_details"]["private_key"])
        self.assertIsNotNone(res.json()["account_details"]["public_key"])

    def test_address_creation_eth(self):
        request_data = {"network": self.acronym[3]}
        res = self.client.post(self.address_url, data=request_data, format="json")
        self.assertTrue(res.json()["success"])
        self.assertEqual(
            res.json()["message"], "New wallet has been created successfully"
        )
        self.assertEqual(res.json()["account_details"]["coin"], self.acronym[3])
        self.assertIsNotNone(res.json()["account_details"]["private_key"])
        self.assertIsNotNone(res.json()["account_details"]["public_key"])

    def test_address_creation_ltc(self):
        request_data = {"network": self.acronym[4]}
        res = self.client.post(self.address_url, data=request_data, format="json")
        self.assertTrue(res.json()["success"])
        self.assertEqual(
            res.json()["message"], "New wallet has been created successfully"
        )
        self.assertEqual(res.json()["account_details"]["coin"], self.acronym[4])
        self.assertIsNotNone(res.json()["account_details"]["private_key"])
        self.assertIsNotNone(res.json()["account_details"]["public_key"])

    def test_address_creation_dash(self):
        request_data = {"network": self.acronym[5]}
        res = self.client.post(self.address_url, data=request_data, format="json")
        self.assertTrue(res.json()["success"])
        self.assertEqual(
            res.json()["message"], "New wallet has been created successfully"
        )
        self.assertEqual(res.json()["account_details"]["coin"], self.acronym[5])
        self.assertIsNotNone(res.json()["account_details"]["private_key"])
        self.assertIsNotNone(res.json()["account_details"]["public_key"])

    def test_address_creation_doge(self):
        request_data = {"network": self.acronym[6]}
        res = self.client.post(self.address_url, data=request_data, format="json")
        self.assertTrue(res.json()["success"])
        self.assertEqual(
            res.json()["message"], "New wallet has been created successfully"
        )
        self.assertEqual(res.json()["account_details"]["coin"], self.acronym[6])
        self.assertIsNotNone(res.json()["account_details"]["private_key"])
        self.assertIsNotNone(res.json()["account_details"]["public_key"])
