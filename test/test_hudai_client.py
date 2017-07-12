from mock import patch
from unittest import TestCase
from mock import patch, MagicMock

from test.helpers.test_util import TestUtil
from hudai.hudai_client import HudAiClient

class TestHudAiClient(TestCase):
    def test_client(self):
        self.assertTrue(HudAiClient.create)
        client = HudAiClient.create(TestUtil.get_key())
        self.assertIsInstance(client, HudAiClient)
