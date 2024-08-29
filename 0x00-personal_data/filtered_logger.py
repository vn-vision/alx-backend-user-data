#!/usr/bin/env python3
"""
Return log message with sensitive fields obfuscated.

    fields: list of strings - the names of the fields to obfuscate
    redaction: string - the string to replace the sensitive information with
    message: string - the log message to be obfuscated
    separator: string - the character used to separate
    the fields in the log message

Regex: f'({"|".join(fields)})=[^{separator}]*'
    {"|".join(fields)} creates a group of fields that are matched by the regex
    =[^{separator}]* matches the value of the field, stopping at the separator
    or the end of the string.
"""
import re
def filter_datum(fields, redaction, message, separator):
    """ return log message obfuscated """
    return re.sub(f'({"|".join(fields)})=[^{separator}]*',
                  lambda m: f"{m.group(1)}={redaction}", message)
