import unittest
from scripts.read_write_files import ReadingWorker


class TestReadingWorker(unittest.TestCase):

    def test__init__(self):
        """Test attributes initialization"""
        r_worker = ReadingWorker()
        assert r_worker.file_pattern == "input"
        assert r_worker.number == 0

    def test_inheritance(self):
        """Test correct inheritance"""
        r_worker = ReadingWorker()
        assert isinstance(r_worker, ReadingWorker)
