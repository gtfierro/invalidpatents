import os
import glob
import rethinkdb as r
from pyocr import tesseract
import wand.image
from PIL import Image

r.connect().repl()
db = r.db('invalid')
table = db.table('invalid')

def convertPDF(filename):
    img = wand.image.Image(filename=filename, resolution=200)
    img.compression = 99
    img.save(filename=filename+'.jpg')
    return filename+'.jpg' 

def getText(filename):
    img = Image.open(filename)
    text = tesseract.image_to_string(img)
    return text

def getNumberFromFilename(filename):
    return filename.split('/')[-1].split('.')[0]

def getFileNames():
    pdfs = glob.glob('pdf_files/*.pdf')
    print pdfs
    return pdfs

def run():
    for filename in getFileNames():
        number = getNumberFromFilename(filename)
        convertPDF(filename)
        print filename
        for i, jpg in enumerate(glob.glob(filename+'-[0-9]*.jpg')):
            text = getText(jpg)
            table.insert({'filename': filename,
                          'sequence': i,
                          'number': number,
                          'text': text}).run()

if __name__=='__main__':
    print 'Converting PDFs to JPG, running tesseract OCR, inserting documents into RethinkDB'
    run()
