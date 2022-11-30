from pytest import *
from WebMentionApp import WebMentionApp
from test_doubles import SearchAdaptorStub, StorageAdaptorSpy


sample_search = [{
        "date": "2022-11-10",
        "title": "This is a title",
        "summary": "This page is more or less about what the title said.",
        "url": "https://www.somesite.cn/"
    },
    {
        "date": "2022-11-18",
        "title": "This is another title",
        "summary": "This page is more of the same.",
        "url": "https://www.somesite.cn/page2"
    },
    {
        "date": "2022-10-10",
        "title": "This is another title",
        "summary": "This one is terrible.",
        "url": "https://www.someothersite.cn/"
    }]

def test_gather_collate_store_webmentions ():
    spy = StorageAdaptorSpy()
    searchAdaptor = SearchAdaptorStub()
    searchAdaptor.data = sample_search
    app = WebMentionApp(searchAdaptor, spy)
    app.gather_and_store()
    assert spy.stored == sample_search



