import argparse

from utils import find_and_save_all_reports

parser = argparse.ArgumentParser(description='Description of optional arguments')
parser.add_argument('--ticker', '-t', type=str,
                    help='The ticker of a certain company')
parser.add_argument('--n_documents', '-n', type=int, default=40,
                    help='number of documents to download')
parser.add_argument('--txt', '-txt', action='store_true',
                    help='Set downloaded reports type as .txt')
parser.add_argument('--xbrl', '-xbrl', action='store_true',
                    help='Set downloaded reports type as .xbrl')
parser.add_argument('--doc_10k', '-k', action='store_true',
                    help='download 10-K reports')
parser.add_argument('--doc_10q', '-q', action='store_true',
                    help='download 10-Q reports')
parser.add_argument('--doc_20f', '-f', action='store_true',
                    help='download 20-F reports')

args = parser.parse_args()


def main():
    ticker = args.ticker
    n_documents = args.n_documents
    xbrl = args.xbrl
    txt = args.txt
    doc_10k = args.doc_10k
    doc_10q = args.doc_10q
    doc_20f = args.doc_20f
    find_and_save_all_reports(ticker, n_documents, txt, xbrl, doc_10k, doc_10q, doc_20f)

if __name__ == "__main__":
    main()
