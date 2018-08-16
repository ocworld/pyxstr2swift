#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import os


def get_keys_from_strings_file(strings_file_path):
    """
    get keys from xcode strings file
    :param strings_file_path: str. xcode strings file full path
    :return:
    """
    def comment_remover(text):

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

    with open(strings_file_path, mode='r') as f:
        contents = f.read()

    lines = comment_remover(contents).splitlines()
    keys = [line.split('=')[0] for line in lines]
    filtered_keys = filter(lambda line: line.strip() != "", keys)
    return list(filtered_keys)


def write_keys_to_swift_file(keys, out_file_path, swift_struct_name=""):
    '''
    write string keys to swift file.
    :param keys: strings keys
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

    bodylines = ["  static let %s = \"%s\".localized" % (key, key) for key in keys]

    lines = headlines + bodylines + taillines

    with open(out_file_path, mode='w+') as f:
        f.write('\n'.join(lines))


def xstr2swift(strings_file_path, out_file_path, swift_struct_name="", overwrite_if_out_path_exist=True):
    '''
    Generating swift file from xcode strings file.

    for example,

    import Foundation

    struct StringKeys {
        static let key1 = "key1".localized
    }

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
        if overwrite_if_out_path_exist == True:
            logging.info('xstr2swift: %s is removed' % out_file_path)
            os.remove(out_file_path)
        else:
            logging.error('xstr2swift: %s is not exist' % out_file_path)
            raise OSError(17)  # EEXIST

    logging.info('xstr2swift: try to get_keys_from_strings_file(%s)' % out_file_path)

    try:
        keys = get_keys_from_strings_file(strings_file_path)
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

    try:
        write_keys_to_swift_file(keys, out_file_path, swift_struct_name)
    except OSError as err:
        logging.error('xstr2swift: failed to write_keys_to_swift_file %s with os error (no: %d)(err: %s)' % (
            strings_file_path, err.errno, err.message))
        raise err
    except Exception as ex:
        logging.error('xstr2swift: failed to write_keys_to_swift_file %s with exception (no: %d)(err: %s)' % (
            strings_file_path, ex.errno, ex.message))
        raise ex
