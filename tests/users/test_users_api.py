import unittest,json

from git_exercise.users.users_api import users_api
from git_exercise.users.users_gateway import UsersGateway
from tests.blueprint_test_support import test_client


class TestUsersApi(unittest.TestCase):
    def setUp(self):
        gateway = UsersGateway()
        self.client = test_client(users_api(gateway))

    def test_list(self):
        response = self.client.get("/users")

        self.assertEqual(200, response.status_code)
        self.assertIn({"id": 1, "name": "Fred Derf","email":"fred@gmail.com"}, response.json)

    def test_find(self):
        response = self.client.get("/users/2")

        self.assertEqual(200, response.status_code)
        self.assertEqual({"id": 2, "name": "Mary Yram","email":"mary@gmail.com"}, response.json)

    def test_find_not_found(self):
        response = self.client.get("/users/2345")

        self.assertEqual(404, response.status_code)

    def test_create_user(self):
        response = self.client.post(
            "/users", 
            data=json.dumps({"name": "Kate Etak", "email": "kate@example.com"}), 
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 201) 
        self.assertIn("id", response.json)  
        self.assertIsInstance(response.json["id"], int)
