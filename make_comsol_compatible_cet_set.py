#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Create COMSOL compatible color encodings for the CET perceptually uniform
colour maps available at: http://peterkovesi.com/projects/colourmaps/

To install to COMSOL, copy the unzipped tsv files to the
comsol\data\colormap directory

Works at least for COMSOL 4.2a.

Credit for those maps below:
Peter Kovesi. Good Colour Maps: How to Design Them.
arXiv:1509.03700 [cs.GR] 2015

This is a quick one-off script, use as you will.
Joseph E. Weaver, jeweave4@ncsu.edu 

"""

import os.path
import urllib.request
import zipfile
import re
import io

# Location of the csv file we want to convert.  COMSOL expects a tab-delimited
# file, with RGB values in the range of 0-1.  On my windows box, it also uses
# CR/LF endings.

# File below is the closest thing to what we want, let's download and convert.
csv_0_1_url = 'http://peterkovesi.com/projects/colourmaps/CETperceptual_csv_0_1.zip'  # noqa
filename = 'CETperceptual_csv_0_1.zip'

# I can never remember how to do this right, so stackoverflow is my friend
# https://stackoverflow.com/questions/3173372/download-files-from-a-list-if-not-already-downloaded   # noqa
# https://stackoverflow.com/questions/45247983/urllib-urlretrieve-with-custom-header   # noqa

# set the headers to avoid a 403 forbidden
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0')]  # noqa
urllib.request.install_opener(opener)

# actually download the file
if not os.path.isfile(filename):
        print('Downloading: ' + filename)
        try:
            urllib.request.urlretrieve(csv_0_1_url, filename)
        except Exception as inst:
            print(inst)
            print('  Encountered unknown error.')

# read in the downloaded zipfile
zfile = zipfile.ZipFile(filename)

# zipfile we're going to write
out_zip = zipfile.ZipFile(re.sub('csv', 'tsv', filename),
                          mode='w',
                          compression=zipfile.ZIP_DEFLATED,
                          )

# rummage thru the zip file, any time we find a csv, convert it to TSV in
# memory then pop it intot he output zip
# this is not pretty nor exception-proof, but it seems to work
for finfo in zfile.infolist():
    infile, file_extension = os.path.splitext(finfo.filename)
    if(".csv" == file_extension):
        ifile = zfile.open(finfo)
        # using StringIO to avoid writing/cleaning up temp files.
        # These are short, so there's no memory issue
        ofile = io.StringIO()
        line_list = ifile.readlines()
        # the actual substitutions
        for line in line_list:
            tabbed = (re.sub(b'\,', b'\t', line))
            termed = (re.sub(b'\n', b'\r\n', tabbed))
            ofile.write(termed.decode("ascii"))
        # getting a little hacky with the new filename
        newname = re.sub('csv', 'tsv', finfo.filename)
        out_zip.writestr(newname, ofile.getvalue())
        ofile.close()
