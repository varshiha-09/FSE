import unittest

from git_exercise.users.user import User
from git_exercise.users.users_gateway import UsersGateway


class TestUsersGateway(unittest.TestCase):
    def test_list(self):
        gateway = UsersGateway()

        result = gateway.list()

        self.assertEqual(4, len(result))
        self.assertIn(User(id=1, name="Fred Derf",email="fred@gmail.com",is_admin=True), result)

    def test_find(self):
        gateway = UsersGateway()

        self.assertEqual(User(id=2, name="Mary Yram",email="mary@gmail.com",is_admin=False), gateway.find(2))
        self.assertIsNone(gateway.find(1234))
    def test_add_user(self):
        gateway = UsersGateway()
        new_user_data = {
            "name": "Kate Etak",
            "email": "kate@example.com",
            "is_admin": False,
        }

        new_user_id = gateway.add_user(new_user_data["name"], new_user_data["email"], new_user_data["is_admin"])
        response = {"id": new_user_id}

        self.assertIn("id", response)
        self.assertIsInstance(response["id"], int)

        added_user = gateway.find(response["id"])
        self.assertIsNotNone(added_user)
        self.assertEqual(added_user.name, new_user_data["name"])
        self.assertEqual(added_user.email, new_user_data["email"])


        self.assertEqual(len(gateway.list()), 5)
    
    def test_update_user(self):
        gateway = UsersGateway()
        updated_user_data = {
            "name": "Kate Etak Updated",
            "email": "kateupdated@example.com"
        }

        gateway.update_user(2, updated_user_data["name"], updated_user_data["email"])
        updated_user = gateway.find(2)

        self.assertIsNotNone(updated_user)
        self.assertEqual(updated_user.name, updated_user_data["name"])
        self.assertEqual(updated_user.email, updated_user_data["email"])


