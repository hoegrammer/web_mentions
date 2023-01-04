from SerpApiAdaptor import SerpApiAdaptor
from WebMention import WebMention



def test_gather():
    params: dict = {
        'q': "some random query"
    }
    adaptor = SerpApiAdaptor(params)
    results: list[WebMention] = adaptor.gather()
    assert len(results) > 0


