from crawler import SecCrawler
import re
import requests
from datetime import datetime


def find_and_save_10K_to_folder(ticker, from_date=None, number_of_documents=40, doc_format='xbrl'):
    if from_date is None:
        from_date = datetime.today().strftime('%Y%m%d')
    crawler = SecCrawler()
    cik, company_name = get_cik_and_name_from_ticker(ticker)
    crawler.filing_10K(ticker, cik, company_name, from_date,
                       number_of_documents, doc_format)


def find_and_save_10Q_to_folder(ticker, from_date=None, number_of_documents=40, doc_format='xbrl'):
    if from_date is None:
        from_date = datetime.today().strftime('%Y%m%d')
    crawler = SecCrawler()
    cik, company_name = get_cik_and_name_from_ticker(ticker)
    crawler.filing_10Q(ticker, cik, company_name, from_date,
                       number_of_documents, doc_format)


def find_and_save_20F_to_folder(ticker, from_date=None, number_of_documents=40, doc_format='xbrl'):
    if from_date is None:
        from_date = datetime.today().strftime('%Y%m%d')
    crawler = SecCrawler()
    cik, company_name = get_cik_and_name_from_ticker(ticker)
    crawler.filing_20F(ticker, cik, company_name, from_date,
                       number_of_documents, doc_format)


def get_cik_and_name_from_ticker(ticker):
    URL = 'http://www.sec.gov/cgi-bin/browse-edgar?CIK=%s&Find=Search&owner=exclude&action=getcompany' % ticker
    data = requests.get(URL).content.decode('utf-8')
    CIK_RE = re.compile(r'.*CIK=(\d{10}).*')
    cik_find = CIK_RE.findall(data)
    if type(cik_find) == str:
        pass
    elif type(cik_find) == list:
        cik_find = str(cik_find[0])
    else:
        print('could not find cik number...')
        cik_find = None

    name_RE = re.compile(r'companyName">(.+?)<')
    name_find = name_RE.findall(data)
    if type(name_find) == str:
        pass
    elif type(name_find) == list:
        name_find = str(name_find[0])
    else:
        print('could not find company name...')
        name_find = None

    return cik_find, name_find
