import unittest
from scripts.read_write_files import logging, create_logger


class TestCreateLogger(unittest.TestCase):

    def test_create_logger(self):
        """Test the creation of the logger"""
        logger = create_logger()
        assert isinstance(logger, logging.Logger)

    def test_logger(self):
        """Test the attribute level and handlers"""
        logger = create_logger()
        assert logger.level == logging.DEBUG
        assert logger.hasHandlers()
