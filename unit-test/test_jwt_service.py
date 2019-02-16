import unittest
import uuid
import logging

from mock import patch
from src.jwt_service import JwtService
from freezegun import freeze_time


@freeze_time("2012-02-16")
class JwtServiceTest(unittest.TestCase):

    def setUp(self):
        logging.basicConfig(level=logging.INFO)
        self.service = JwtService('my-issuer', 'my-secret')

    @patch.object(uuid, 'uuid4', return_value=uuid.UUID('06335e84-2872-4914-8c5d-3ed07d2a2f16'))
    def test_should_generate_jwt_non_expiring_token(self, mock_uuid):
        token = self.service.create_non_expiring_token('my-subject')

        expected_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJteS1pc3N1ZXIiLCJpYXQiOjEzMjkzNTA0MDAsIm' \
                         'p0aSI6IjA2MzM1ZTg0LTI4NzItNDkxNC04YzVkLTNlZDA3ZDJhMmYxNiIsInN1YiI6Im15LXN1YmplY3QifQ.0I' \
                         'NZqTk20CFh6rbuFXcI1iy5OEVeFWQnCC21r5JXqos'
        self.assertEqual(expected_token, token)

    @patch.object(uuid, 'uuid4', return_value=uuid.UUID('06335e84-2872-4914-8c5d-3ed07d2a2f16'))
    def test_should_generate_jwt_expiring_token(self, mock_uuid):
        seconds_to_live = 60
        token = self.service.create_expiring_token('my-subject', seconds_to_live)

        expected_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJteS1pc3N1ZXIiLCJpYXQiOjEzMjkzNTA0MDAsIm' \
                         'p0aSI6IjA2MzM1ZTg0LTI4NzItNDkxNC04YzVkLTNlZDA3ZDJhMmYxNiIsInN1YiI6Im15LXN1YmplY3QiLCJle' \
                         'HAiOjEzMjkzNTA0NjB9.XitpF0TSkrD0l1xtSg7CrLx0Jno43JACRP5HA35N9Lw'
        self.assertEqual(expected_token, token)


if __name__ == '__main__':
    unittest.main()