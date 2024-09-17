from io import StringIO
from django.core.management import call_command
from django.test import TestCase

class GetDataTest(TestCase):
    def test_command_output(self):
        out = StringIO()
        fname = r"C:\Users\colli\Python\Mybo\yukidaruma_wordbank_data.txt"
        call_command("getdata", filename = fname, type = 'Word')
