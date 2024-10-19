#!/usr/bin/env python3
'''
Write a function called filter_datum
that returns the log message obfuscated
'''

import re

def filter_datum(fields, redaction, message, separator):
    '''
    Returns the log message with fields obfuscated
    '''
    pattern = f"({'|'.join(fields)})=([^\\{separator}]+)"
    return re.sub(pattern, lambda match: f"{match.group(1)}={redaction}", message)
