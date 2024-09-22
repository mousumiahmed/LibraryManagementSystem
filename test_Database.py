import unittest
from datetime import datetime

from Database import show_all_users


class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.data = [{'user_id': 2, 'user_name': 'Mark John', 'user_email': 'mark@gmail.com', 'user_type': 1,
                      'password': 'Mark@123', 'profile_created': datetime(2024, 8, 12, 16, 59, 1),
                      'confirm_password': 'Mark@123'},
                     {'user_id': 6, 'user_name': 'Mousumi Ara', 'user_email': 'mousumi@gmail.com', 'user_type': 2,
                      'password': 'Password@123', 'profile_created': datetime(2024, 8, 12, 19, 9, 18),
                      'confirm_password': 'Password@123'},
                     {'user_id': 7, 'user_name': 'Mousumi Ara ', 'user_email': 'user@gmail.com', 'user_type': 2,
                      'password': 'Password@123', 'profile_created': datetime(2024, 8, 13, 9, 52, 49),
                      'confirm_password': 'Password@123'},
                     {'user_id': 8, 'user_name': 'Admin', 'user_email': 'admin@gmail.com', 'user_type': 1,
                      'password': 'Admin@123', 'profile_created': datetime(2024, 8, 13, 9, 54, 58),
                      'confirm_password': 'Admin@123'},
                     {'user_id': 9, 'user_name': 'Faculty', 'user_email': 'faculty@gmail.com', 'user_type': 2,
                      'password': 'Password@123', 'profile_created': datetime(2024, 8, 13, 12, 49, 21),
                      'confirm_password': 'Password@123'},
                     {'user_id': 11, 'user_name': 'Mousumi_Admin', 'user_email': 'm_admin@gmail.com', 'user_type': 1,
                      'password': 'Password@123', 'profile_created': datetime(2024, 8, 22, 12, 17, 53),
                      'confirm_password': 'Password@123'}]

    def test_user_verification(self):
        res = show_all_users()
        print(self.data)
        print(res)
        self.assertEqual(res, self.data)

        # def tearDown(self):
        #     del self.data


if __name__ == '__main__':
    unittest.main()
