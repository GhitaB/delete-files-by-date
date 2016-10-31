""" Usage:
    $ python script.py
    will delete in all sub-folders of PARENT_FOLDER the files with type
    in FILES_TYPES and creation date between START_DATE and END_DATE.
"""

import os
import sys

FILES_TYPES = ['pdf']
START_DATE = 20100101
END_DATE = 20160630
PARENT_FOLDER = "/home/ghitabizau/ghita-work/test-delete"


def check_filetype(filename):
    """ Return True if filetype in FILES_TYPE
    """
    filetype = filename.split(".")[-1]
    if filetype in FILES_TYPES:
        return True
    else:
        return False


def check_delete(filename):
    """ Return True if this filename must be deleted

        I have a special case, the date is in filename. You can modify this
        to use creation date or something.
        Filename example: 1111_20160228-160658_etc_AA-0000_000_000_etc_.pdf
    """
    if check_filetype(filename):

        try:
            creation_date = int(filename.split("_")[1].split("-")[0])
            if creation_date >= START_DATE and creation_date <= END_DATE:
                return True
            else:
                return False
        except Exception:
            return False
    else:
        return False


def delete_file(filepath):
    """ Delete given file by path
    """
    try:
        os.remove(filepath)
    except Exception:
        print "ERROR deleting " + filepath


print "START."

for folder, subs, files in os.walk(PARENT_FOLDER):
    for filename in files:
        if check_delete(filename):
            filepath = folder + "/" + filename
            print "DELETING: " + filepath
            delete_file(filepath)

print "DONE."
