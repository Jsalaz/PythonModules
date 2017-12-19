'''
Created on Oct 8, 2017

@author: j_sal
'''
import sys
from math import log


def convert(s):
    '''Convert to an integer.'''
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print('Conversion Error: {}'.format(str(e)),
              file=sys.stderr)
        raise


def string_log(s):
    v = convert(s)
    return log(v)