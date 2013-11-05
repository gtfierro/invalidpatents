Invalid Patents
===============

There are several modules to this repository.

The first part attempt to download decisions from the Patent Trial and Appeal
Board.  These are found
[here](http://e-foia.uspto.gov/Foia/PTABReadingRoom.jsp). We can easily get
decisions from the past N days by visting
[http://e-foia.uspto.gov/Foia/DispatchBPAIServlet?RetrieveRecent=30](http://e-foia.uspto.gov/Foia/DispatchBPAIServlet?RetrieveRecent=30),
and replacing the '30' in the URL with the number we want.

Using Selenium we download the decision PDFs, run Tesseract OCR on the
documents, and insert the full text into a RethinkDB database.

To run RethinkDB, start the following process in a window:

```
rethinkdb -d data
```
