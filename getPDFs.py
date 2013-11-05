import sys
import os
from selenium import webdriver
import time
import glob

def spinWaitOnDownload(document):
    while 1:
        retrieved = glob.glob('pdf_files/ReterivePdf*')
        if not retrieved:
            break
        os.rename(retrieved[0],'pdf_files/'+document+'.pdf')
        time.sleep(1)

def downloadLastN(n):
    fp = webdriver.FirefoxProfile()
    fp.set_preference("browser.download.folderList", 2)
    fp.set_preference("browser.download.manager.showWhenStarting", True)
    fp.set_preference("browser.download.dir", os.getcwd()+'/pdf_files/')
    fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
    fp.set_preference("pdfjs.disabled", True)
    fp.update_preferences()
    browser = webdriver.Firefox(firefox_profile=fp)
    browser.get('http://e-foia.uspto.gov/Foia/DispatchBPAIServlet?RetrieveRecent='+str(n))

    links = browser.find_elements_by_tag_name('a')
    names = [link.get_attribute('name') if link else '' for link in links]
    documents = [doc if doc.isdigit() else '' for doc in names] 
    documents = filter(lambda x: x, documents)
    for document in documents:
        browser.get('http://e-foia.uspto.gov/Foia/DispatchBPAIServlet?RetrieveRecent='+str(n))
        downloadlink = browser.find_element_by_partial_link_text(document)
        downloadlink.click()
        spinWaitOnDownload(document)

if __name__=='__main__':
    if len(sys.argv) < 2:
        print 'Usage: python getPDFs.py <number-of-days-to-download>'
        sys.exit(0)
    num = sys.argv[1]
    if not num.isdigit():
        print 'Usage: python getPDFs.py <number-of-days-to-download>'
        sys.exit(0)
    if not os.path.exists('pdf_files'):
        os.mkdir('pdf_files')
    downloadLastN(int(num))
