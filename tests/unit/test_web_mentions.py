from WebMentionApp import WebMentionApp
from test_doubles import SearchAdaptorStub, StorageAdaptorSpy
from tests.SampleData import sample_search



def test_gather_collate_store_webmentions ():
    spy = StorageAdaptorSpy()
    searchAdaptor = SearchAdaptorStub()
    searchAdaptor.data = sample_search
    app = WebMentionApp(searchAdaptor, spy)
    app.gather_and_store()
    assert spy.stored == sample_search



