import sys
import os
from pyocr import tesseract
import wand.image
from PIL import Image
from selenium import webdriver

def convertPDF(filename):
    img = wand.image.Image(filename=filename, resolution=200)
    img.compression = 99
    img.save(filename=filename+'.jpg')
    return filename+'.jpg' 

def getText(filename):
    img = Image.open(filename)
    text = tesseract.image_to_string(img)
    return text


def downloadLastN(n)
    fp = webdriver.FirefoxProfile()
    fp.set_preference("browser.download.folderList", 2)
    fp.set_preference("browser.download.manager.showWhenStarting", True)
    fp.set_preference("browser.download.dir", os.getcwd()+'/pdf_files/')
    fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
    fp.set_preference("pdfjs.disabled", True)
    fp.update_preferences()
    browser = webdriver.Firefox(firefox_profile=fp)
    browser.get('http://e-foia.uspto.gov/Foia/DispatchBPAIServlet?RetrieveRecent='+n)

    links = browser.find_elements_by_tag_name('a')
    names = [link.get_attribute('name') if link else '' for link in links]
    documents = [doc if doc.isdigit() else '' for doc in names] 
    documents = filter(lambda x: x, documents)
    for document in documents:
        browser.get('http://e-foia.uspto.gov/Foia/DispatchBPAIServlet?RetrieveRecent=30')
        downloadlink = browser.find_element_by_partial_link_text(document)
        downloadlink.click()
        os.rename('ReterivePdf',document+'.pdf')



if __name__=='__main__':
    if len(sys.argv) < 2:
        print 'Usage: python getPDFs.py <number-of-days-to-download>'
    num = sys.argv[1]
    if not num.isdigit():
        print 'Usage: python getPDFs.py <number-of-days-to-download>'
    if not os.path.exists('pdf_files'):
        os.mkdir('pdf_files')
    downloadLastN(int(num))
