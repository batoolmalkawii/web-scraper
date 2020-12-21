PR: https://github.com/batoolmalkawii/web-scraper/pull/1

# Web Scraper
In this project, we scraped a Wiki page and record which passages need citations. `BeautifulSoup` is used for parsing from web pages.
We implemented [Wiki History of Mexico](https://en.wikipedia.org/wiki/History_of_Mexico) page.


The notebook includes the following functions:

* `get_citations_needed_count`: takes in a url and returns an integer
* `get_citations_needed_report`: takes in a url and returns a string.
   The string is formatted with each citation needed on own line, in order found. 
   And result is exported to `data.json` file.

User acceptance tests are included on [Wiki Mindset](https://en.wikipedia.org/wiki/Mindset) page. 
We created a `test.json` that includes the ground-truth citations and compared it to `data.json` that is the output of `get_citations_needed_report` function.