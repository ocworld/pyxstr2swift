#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import os
import io

def _get_keys_and_values_from_strings_file(strings_file_path):
    """
    get keys_and_values from xcode strings file
    :param strings_file_path: str. xcode strings file full path
    :return:
    """

    def _comment_remover(text):

        import re

        def replacer(match):
            s = match.group(0)
            if s.startswith('/'):
                return " "  # note: a space and not an empty string
            else:
                return s

        pattern = re.compile(
            r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
            re.DOTALL | re.MULTILINE
        )
        return re.sub(pattern, replacer, text)

    with io.open(strings_file_path, mode='r', encoding='utf-8') as f:
        contents = f.read()

    lines = _comment_remover(contents).splitlines()
    key_index = 0
    value_index = 1
    kv_list = list(filter(lambda kv: kv[key_index].strip() != "", [line.split('=') for line in lines]))
    kv_dic = {kv[key_index].strip(): kv[value_index].strip('"; ') for kv in kv_list}
    return kv_dic


def _write_keys_to_swift_file(kv_dic, out_file_path, tablename="", swift_struct_name="", is_write_values_as_comment=False):
    '''
    write string keys to swift file.
    :param kv_dic: dictionary for keys and values
    :param out_file_path: a target swift file path including .swift extension
    :param swift_struct_name: swift struct name in a target swift file path.
                              if "" outfile filename is used.
    :return:
    '''
    from os.path import basename, splitext

    default_struct_name = splitext(basename(out_file_path))[0]
    struct_name = swift_struct_name if swift_struct_name != "" else default_struct_name
    headlines = ["import Foundation", "", "struct %s {" % struct_name]
    taillines = ["}", ""]

    if is_write_values_as_comment:
        bodylines = ["  static let %s = NSLocalizedString(\"%s\", tableName: \"%s\", comment: \"\") // %s" % (key, key, tablename, value) for key, value in kv_dic.items()]
    else:
        bodylines = ["  static let %s = NSLocalizedString(\"%s\", tableName: \"%s\", comment: \"\")" % (
        key, key, tablename) for key in kv_dic.keys()]

    lines = headlines + bodylines + taillines

    with io.open(out_file_path, mode='w+', encoding='utf-8') as f:
        f.write(u'%s' % '\n'.join(lines))


def xstr2swift(strings_file_path, out_file_path,
               swift_struct_name="",
               overwrite_if_out_path_exist=True,
               is_write_values_as_comment=False):
    '''
    Generating swift file from xcode strings file.

    for example,

    import Foundation

    struct StringKeys {
        static let key1 = NSLocalizedString("key1", tableName: "Localizable.strings", comment: "")  // value
    }

    :param is_write_values_as_comment:
    :param strings_file_path: str. xcode strings file full path
    :param out_file_path: a target swift file path including .swift extension
    :param swift_struct_name: swift struct name in a target swift file path.
                              if "" outfile filename is used.
    :param overwrite_if_out_path_exist: overwrite if a outpath already exist.
    :return:
    '''
    if not os.path.exists(strings_file_path):
        logging.error('xstr2swift: %s is not exist' % strings_file_path)
        raise OSError(2)  # ENOENT

    if os.path.exists(out_file_path):
        if overwrite_if_out_path_exist:
            logging.info('xstr2swift: %s is removed' % out_file_path)
            os.remove(out_file_path)
        else:
            logging.error('xstr2swift: %s is not exist' % out_file_path)
            raise OSError(17)  # EEXIST

    logging.info('xstr2swift: try to get_keys_from_strings_file(%s)' % out_file_path)

    try:
        kv_dic = _get_keys_and_values_from_strings_file(strings_file_path)
    except IOError as err:
        logging.error('xstr2swift: failed to get_keys_from_strings_file %s with IOError (no: %d)(err: %s)' % (
            strings_file_path, err.errno, err.message))
        raise err
    except OSError as err:
        logging.error('xstr2swift: failed to get_keys_from_strings_file %s with OSError (no: %d)(err: %s)' % (
            strings_file_path, err.errno, err.message))
        raise err
    except Exception as ex:
        logging.error('xstr2swift: failed to get_keys_from_strings_file %s with Exception (no: %d)(err: %s)' % (
            strings_file_path, ex.errno, ex.message))
        raise ex

    logging.info('xstr2swift: try to write_keys_to_swift_file(%s)' % out_file_path)

    from os.path import basename, splitext
    tablename = splitext(basename(strings_file_path))[0]

    if swift_struct_name == "":
        swift_struct_name = tablename

    try:
        _write_keys_to_swift_file(kv_dic, out_file_path, tablename, swift_struct_name, is_write_values_as_comment)
    except OSError as err:
        logging.error('xstr2swift: failed to write_keys_to_swift_file %s with os error (no: %d)(err: %s)' % (
            strings_file_path, err.errno, err.message))
        raise err
    except Exception as ex:
        logging.error('xstr2swift: failed to write_keys_to_swift_file %s with exception (no: %d)(err: %s)' % (
            strings_file_path, ex.errno, ex.message))
        raise ex


def main():
    import argparse

    parser = argparse.ArgumentParser(description='pyxstr2swift needs arguments')

    parser.add_argument('source', type=str, help='source: a strings file')
    parser.add_argument('target', type=str, help='target: a swift file')
    parser.add_argument('--structname', type=str, default="", help='structname: a struct name in a target file')
    parser.add_argument('-f', '--force', action='store_true', help='force to write a target file if already exist')
    parser.add_argument('-m', '--comment', action='store_true', help='values are added as comment')
    args = parser.parse_args()

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
