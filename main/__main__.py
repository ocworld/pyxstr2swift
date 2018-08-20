#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import logging


def main():
    parser = argparse.ArgumentParser(description='pyxstr2swift needs arguments')

    parser.add_argument('source', type=str, help='Input source a strings file')
    parser.add_argument('target', type=str, help='Input target a swift file')
    parser.add_argument('structname', type=str, help='Input target a swift struct name')
    parser.add_argument('-f', '--force', action='store_true', help='force to write a target file if already exist')
    parser.add_argument('-m', '--comment', action='store_true', help='values are added as comment')
    args = parser.parse_args()

    from pyxstr2swift.pyxstr2swift import xstr2swift

    is_forced = True if args.force else False
    is_comment_value = True if args.comment else False
    logging.info('source : %s' % args.source)
    logging.info('target : %s' % args.target)
    logging.info('structname : %s' % args.structname)
    logging.info('is_forced : %s' % 'True' if args.force else 'False')
    logging.info('is_comment_value : %s' % 'True' if args.comment else 'False')
    xstr2swift(args.source, args.target, args.structname, is_forced, is_comment_value)


if __name__ == "__main__":
    main()
