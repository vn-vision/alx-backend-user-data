#!/usr/bin/env python3
"""
Return log message with sensitive fields obfuscated.

    fields: list of strings - the names of the fields to obfuscate
    redaction: string - the string to replace the sensitive information with
    message: string - the log message to be obfuscated
    separator: string - the character used to separate
    the fields in the log message

Regex Pattern:
    pattern = f'{field}=.*?(?={separator}|$)'
    This pattern matches field=value where value is any sequence of characters
    until it hits either the separator or the end of the string.
"""
import re


def filter_datum(fields, redaction, message, separator):
    """ return log message obfuscated """
    for field in fields:
        pattern = f'{field}=.*?(?={separator}|$)'
        message = re.sub(pattern, f'{field}={redaction}', message)
    return message
