""" Module to fetch absolute path"""
import os
import sys
sys.path.insert(1, os.path.dirname(__file__))

print("Imported")
class FileUtilities:
    """ Class will return absolute path"""
    @classmethod
    def get_abs_path(cls, relative_path):
        """ Function will return absolute path"""
        dirname = os.path.dirname(__file__)
        return os.path.join(dirname, relative_path)
