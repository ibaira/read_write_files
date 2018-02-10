import unittest
from scripts.read_write_files import logging, Worker


class TestWorker(unittest.TestCase):

    def test_extension(self):
        """Check correct extension format for files"""
        worker = Worker()
        assert worker.extension == ".txt"

    def test_default(self):
        """Test default initialization"""
        worker = Worker()
        assert worker.number == 0

    def test_non_default_number(self):
        """Test non-default initialization"""
        worker = Worker(10)
        assert worker.number == 10
