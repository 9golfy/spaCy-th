# encoding: utf8
from __future__ import unicode_literals

from ..symbols import *
from ..language_data import PRON_LEMMA


TOKENIZER_EXCEPTIONS = {
    "ม.ค.": [
        {ORTH: "ม.ค.", LEMMA: "มกราคม"}
    ],
    "ก.พ.": [
        {ORTH: "ก.พ.", LEMMA: "กุมภาพันธ์"}
    ]
}


# exceptions mapped to a single token containing only ORTH property
# example: {"string": [{ORTH: "string"}]}
# converted using strings_to_exc() util
'''
ORTH_ONLY = [
    "a.",
    "b.",
    "c.",
    "d.",
    "e.",
    "f.",
    "g.",
    "h.",
    "i.",
    "j.",
    "k.",
    "l.",
    "m.",
    "n.",
    "o.",
    "p.",
    "q.",
    "r.",
    "s.",
    "t.",
    "u.",
    "v.",
    "w.",
    "x.",
    "y.",
    "z."
]
'''