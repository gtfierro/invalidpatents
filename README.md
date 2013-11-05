Invalid Patents
===============

We want to download decisions from the Patent Trial and Appeal
Board.  These are found
[here](http://e-foia.uspto.gov/Foia/PTABReadingRoom.jsp). We can easily get
decisions from the past N days by visting
[http://e-foia.uspto.gov/Foia/DispatchBPAIServlet?RetrieveRecent=30](http://e-foia.uspto.gov/Foia/DispatchBPAIServlet?RetrieveRecent=30),
and replacing the '30' in the URL with the number we want.

Using Selenium we download the decision PDFs, run Tesseract OCR on the
documents, and insert the full text into a RethinkDB database.


## Getting Set Up

You will need the following installed on your computer to get the below working:

* RethinkDB - [http://rethinkdb.com/](http://rethinkdb.com/)
* Python modules in [requirements.txt](https://github.com/gtfierro/invalidpatents/blob/master/requirements.txt)
  * you can run `pip install -r requirements.txt` to install these
* Firefox - [https://www.mozilla.org/en-US/firefox/new/](https://www.mozilla.org/en-US/firefox/new/)
  * any of the newer versions should work


## Running Scripts

To run RethinkDB, start the following process in a window:

```
rethinkdb -d data
```

Make sure the requisite db/table are setup:

```
python setupRethinkDB.py
```

Download the PDF files from the last N days by running (expects N as an integer):

```
python getPDFs.py N
```

This will open up Firefox on your computer and programatically direct the browser
to download all of the relevant PDFs, which will be placed in a newly created
folder `pdf_files` in the same directory. Each file will be named according
to its application number.

To run OCR on the PDFs, run

```
python insertTexts.py
```

which will automatically iterate through all the PDF documents in the
`pdf_files` directory and perform all the necessary operations. It will upload
these to the RethinkDB instance you started above, but the code is simple
enough that you should be able to alter the script to output the data however
you want.
