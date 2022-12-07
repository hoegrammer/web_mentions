from FileWriterAdaptor import FileWriterAdaptor
from tests.SampleData import sample_search as sample_search
import json

def test_write_to_file():
    fileWriterAdaptor = FileWriterAdaptor()
    filename = "stored_search_results/testfile.json"
    fileWriterAdaptor.store(sample_search, filename)
    with open (filename, 'r') as f:
        saved = json.load(f)
    assert saved == sample_search