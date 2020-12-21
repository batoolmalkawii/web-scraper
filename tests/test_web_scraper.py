from web_scraper import __version__
from web_scraper.scraper import get_citations_needed_count, get_citations_needed_report
import json



def test_version():
    assert __version__ == '0.1.0'

def test_citation_count():
    assert get_citations_needed_count("https://en.wikipedia.org/wiki/Mindset") == 3

def test_citation_report():
    with open('test.json') as f:
        expectedResult = json.load(f)
    get_citations_needed_report("https://en.wikipedia.org/wiki/Mindset")
    with open('data.json') as f:
        actualResult = json.load(f)
    assert actualResult == expectedResult
    

