#!/usr/bin/env python
# # -*- coding: utf-8 -*-

import gzip
import tarfile
import os
import re
import shutil
import sys

try:
    from StringIO import StringIO
except ImportError:
    print "Missing module: StringIO\n"
    os.system('python -m pip install StringIO')
from StringIO import StringIO

try:
    from pathlib2 import Path
except ImportError:
    print "Missing module: pathlib2\n"
    os.system('python -m pip install pathlib2')
from pathlib2 import Path

try:
    from lxml import etree
except ImportError:
    print "Missing module: lxml\n"
    os.system('python -m pip install lxml')

from lxml import etree

result_dir = './result'
temp_dir = './temp'


def extract_words(snode):
    word_nodes = snode.xpath('w')

    words = []

    for word_node in word_nodes:
        words.append(word_node.text)

    return ' '.join(words).encode('utf-8')


def create_subtitle_text_file(text, filename):

    filename_slash_pos = [pos for pos, char in enumerate(filename) if char == '/']
    result_subtitle_text_file = result_dir + filename[filename_slash_pos[2]:-7] + '.txt'

    print result_subtitle_text_file

    Path(os.path.dirname(result_subtitle_text_file)).mkdir(parents=True, exist_ok=True)

    with open(result_subtitle_text_file, "w") as f:
        f.seek(0)

        for line in text:
            f.write("%s\n" % line)

    f.close()

    pass


def open_and_extract(filename):

    opener, mode = tarfile.open, 'r:gz'

    cwd = os.getcwd()
    os.chdir(temp_dir)

    try:
        file = opener('../' + filename, mode)
        try:
            file.extractall()
        finally:
            file.close()
    finally:
        os.chdir(cwd)


def cleanup(dirname):
    if os.path.exists(dirname):
        shutil.rmtree(dirname)
    os.makedirs(dirname)


if len(sys.argv) != 2:
    print "Usage: python main.py file.tar.gz\n"
    exit(1)

cleanup(result_dir)
cleanup(temp_dir)

open_and_extract(sys.argv[1])

rx = re.compile(r'\.(gz)')

subtitles = []
for path, dnames, fnames in os.walk(temp_dir):
    subtitles.extend([os.path.join(path, x) for x in fnames if rx.search(x)])

for subtitle in subtitles:
    raw_text_content = gzip.open(subtitle).read()
    xml_file = etree.parse(StringIO(raw_text_content))
    string_nodes = xml_file.xpath('//document/s')

    subtitle_dialogue = []
    for string_node in string_nodes:
        subtitle_dialogue.append(extract_words(string_node))

    create_subtitle_text_file(subtitle_dialogue, subtitle)

shutil.rmtree(temp_dir)
