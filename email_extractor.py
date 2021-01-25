#! /usr/bin/python3
# --*-- coding:UTF-8 --*--

import re
import argparse
import sys

parser = argparse.ArgumentParser(description="Extract file")
parser.add_argument('-i', '--input_file')
parser.add_argument('-o', '--output_file')
args = parser.parse_args()
if not args.input_file and not args.output_file:
    parser.print_help()
    sys.exit()

regex = re.compile(r'[\w\.-]+@[\w\.-]+')

# The input file
input_file = args.input_file

# The output file.
output_file = args.output_file

try:
    with open(input_file, 'r') as emailfile:
        email_list = emailfile.read().lower()
        # Here re.findall() returns a list of all the found email strings
        emails = re.findall(regex, email_list)
        # Write the emails into the file, one per line
        with open(output_file, 'w') as output_file:
            for email in emails:
                output_file.write(email + '\n')

except FileNotFoundError:
    print('this file doesn\'t exist')
