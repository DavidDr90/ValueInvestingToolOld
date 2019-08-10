import argparse

from utils import find_and_save_10K_to_folder, find_and_save_10Q_to_folder, find_and_save_20F_to_folder

parser = argparse.ArgumentParser(description='Description of optional arguments')
parser.add_argument('--ticker', '-t', type=str,
                    help='The ticker of a certain company')
parser.add_argument('--n_documents', '-n', type=int, default=40,
                    help='number of documents to download')
parser.add_argument('--txt', action='store_true',
                    help='Set downloaded reports type as .txt')
parser.add_argument('--xbrl', action='store_true',
                    help='Set downloaded reports type as .xbrl')
parser.add_argument('--doc_10k', '-k', action='store_true',
                    help='download 10-K reports')
parser.add_argument('--doc_10q', '-q', action='store_true',
                    help='download 10-Q reports')
parser.add_argument('--doc_20f', '-f', action='store_true',
                    help='download 20-F reports')

args = parser.parse_args()


def main():
    downloaded = False
    ticker = args.ticker
    if args.xbrl:
        doc_format = 'xbrl'
    else:
        doc_format = 'txt'
    if args.doc_10k:
        find_and_save_10K_to_folder(
            ticker, number_of_documents=args.n_documents, doc_format=doc_format)
        downloaded = True
    if args.doc_10q:
        find_and_save_10Q_to_folder(
            ticker, number_of_documents=args.n_documents, doc_format=doc_format)
        downloaded = True
    if args.doc_20f:
        find_and_save_20F_to_folder(
            ticker, number_of_documents=args.n_documents, doc_format=doc_format)
        downloaded = True
    if not downloaded:
        print('Supported document types are "10-K", "10-Q", "20-F", you should add '
              'one of the following arguments: "-k", "-q", "-f"')


if __name__ == "__main__":
    main()
