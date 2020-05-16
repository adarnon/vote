import argparse
from lxml import html
import requests
import sys


def vote(args):
    sess = requests.Session()

    page = sess.get(args.url)
    tree = html.fromstring(page.content)
    token_el = tree.xpath('//input[@name="_token"]')
    form_token = token_el[0].value

    payload = {
        '_token': form_token,
        'school': args.school,
        'product': args.product,
    }
    req = sess.post(args.url, data=payload)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-s', '--school', default='4',
                        help="School")
    parser.add_argument('-p', '--product', default='truly',
                        choices=['truly', 'bud_light', 'white_claw', 'corona'], help="Product (default: truly).")
    parser.add_argument('url', help="URL.")

    vote(parser.parse_args())


if __name__ == '__main__':
    sys.exit(main())
