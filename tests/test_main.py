from unittest import TestCase
from scripts.read_write_files import main


class TestMain(TestCase):

    def test_main(self):
        """Test correct return value of main"""
        assert main() == 0
