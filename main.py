import argparse
import csv
import datetime
import logging

import chevron as chevron


def setup():
    logging.basicConfig(level=logging.DEBUG, format='%(message)s')

    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--template-file", help="Template file")
    parser.add_argument("-i", "--input-csv", help="Input csv file")

    args = parser.parse_args()

    if args.input_csv is None:
        logging.error("input-csv not provided")
        exit(1)

    if args.template_file is None:
        logging.error("template-file not provided")
        exit(1)

    return args


def main():
    args = setup()

    logging.info("zomb bulk %s" % args)

    template_data = open(args.template_file).read()
    logging.info("template %s", template_data)

    rows = csv.DictReader(open(args.input_csv))

    for idx, row in enumerate(rows):
        row['now'] = datetime.datetime.utcnow().isoformat() + 'Z'
        logging.info('%d: %s', idx, row)

        zomb = chevron.render(template_data, row)
        logging.info("%s", zomb)


if __name__ == "__main__":
    main()
