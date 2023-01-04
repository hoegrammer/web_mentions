from FileWriterAdaptor import FileWriterAdaptor
from tests.SampleData import sample_search as sample_search
import json


def test_write_to_file():
    file_writer_adaptor = FileWriterAdaptor()
    file_writer_adaptor.store(sample_search)
    with open("stored_search_results/results.json", 'r') as f:
        saved = json.load(f)
    assert saved == sample_search
