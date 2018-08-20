#!/usr/bin/python
# -*- coding: utf-8 -*-

import pyxstr2swift.pyxstr2swift as converter
import os
import pytest
import tempfile


@pytest.fixture
def input_file_and_output_file():
    test_base_dir_path = os.path.dirname(os.path.realpath(__file__))
    input_file_path = os.path.join(test_base_dir_path, "resources", "Strings.strings")
    id, output_file_path = tempfile.mkstemp()
    yield input_file_path, output_file_path

    if os.path.exists(output_file_path) == True:
        os.remove(output_file_path)


def test_get_keys_and_values_from_strings_file(input_file_and_output_file):
    input_file_path, output_file_path = input_file_and_output_file
    keys = converter.get_keys_and_values_from_strings_file(input_file_path)
    assert len(keys) == 1


def test_write_keys_to_swift_file(input_file_and_output_file):
    input_file_path, output_file_path = input_file_and_output_file
    converter.write_keys_to_swift_file({'test': 'testvalue'}, output_file_path)

    assert os.path.exists(output_file_path)
    assert os.path.getsize(output_file_path) > 0


def test_xstr2swift(input_file_and_output_file):
    input_file_path, output_file_path = input_file_and_output_file
    converter.xstr2swift(input_file_path, output_file_path, "TEST")

    assert os.path.exists(output_file_path)
    assert os.path.getsize(output_file_path) > 0
