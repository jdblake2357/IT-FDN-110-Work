# ------------------------------------------------------------------------------- #
# Title: Test Processing Classes Module
# # Description: A collection of tests for the processing_classes module
# ChangeLog: (Who, When, What)
# JD Blake, 6/7/24, Created Test
# ------------------------------------------------------------------------------- #

import tempfile
import unittest
import json
import data_classes as data
from processing_classes import FileProcessor


class Test_File_Processor(unittest.TestCase):  # Create temporary test file
    def setUp(self):
        self.temp_file=tempfile.NamedTemporaryFile(delete=False)
        self.temp_file_name=self.temp_file.name

    def tearDown(self):  # Delete temporary test file
        self.temp_file.close()

    def test_read_data_from_file(self):  # Create sample data and populate temporary file
        sample_data = [
            {"FirstName": "Bob", "LastName": "Smith", "ReviewDate": "1911-01-21", "ReviewRating": 4},
            {"FirstName": "Sue", "LastName": "Jones", "ReviewDate": "1911-01-21", "ReviewRating": 4}
        ]

        with open(self.temp_file_name,'w') as file:
            json.dump(sample_data, file)
        # Call read_employee_data_from_file and verify it returns the expected data
        employees = FileProcessor.read_employee_data_from_file(self.temp_file_name, sample_data, data.Employee)
        self.assertEqual(len(sample_data),len(employees))
        self.assertEqual(sample_data[0]['FirstName'],employees[0]['FirstName'])
        self.assertEqual(sample_data