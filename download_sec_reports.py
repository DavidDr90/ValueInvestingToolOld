import argparse

from utils import find_and_save_10K_to_folder, find_and_save_10Q_to_folder, find_and_save_20F_to_folder

parser = argparse.ArgumentParser(description='Optional app description')
parser.add_argument('--symbol', '-s', type=str,
                    help='The symbol (ticker) of a company you are interested in their reports')
parser.add_argument('--type', '-t', type=str, default='10-K',
                    help='report type, can be 10-K, 10-Q or 20-F')
parser.add_argument('--num', '-n', type=int, default=40,
                    help='number of documents to download')
parser.add_argument('--xbrl', action='store_true',
                    help='download xbrl reports')

args = parser.parse_args()


def main():
    ticker = args.symbol
    if args.xbrl:
        doc_format = 'xbrl'
    else:
        doc_format = 'txt'
    if args.type == '10-K':
        find_and_save_10K_to_folder(
            ticker, number_of_documents=args.num, doc_format=doc_format)
    elif args.type == '10-Q':
        find_and_save_10Q_to_folder(
            ticker, number_of_documents=args.num, doc_format=doc_format)
    elif args.type == '20-F':
        find_and_save_20F_to_folder(
            ticker, number_of_documents=args.num, doc_format=doc_format)
    else:
        print('Supported document types are "10-K", "10-Q", "20-F"')

if __name__ == "__main__":
    main()