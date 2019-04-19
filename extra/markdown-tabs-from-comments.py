#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import argparse
import re

LOG = logging.getLogger(__name__)

def init_logger(verbose=False):
    "Init logger and handler"
    if verbose:
        LOG.setLevel(logging.INFO)
    else:
        LOG.setLevel(logging.WARNING)
    formatter = logging.Formatter('%(asctime)s %(levelname)s -: %(message)s')
    hdl = logging.StreamHandler(); hdl.setFormatter(formatter); LOG.addHandler(hdl)

def get_args():
    "Init and return args from argparse"
    parser = argparse.ArgumentParser()

    parser.add_argument('-f','--file',
            help='File to parse',
            default="pipeline/variables.sample.yml",
            type=argparse.FileType('r'),
            required=True)

    return parser.parse_args()

def safe_strip(var):
    if var is not None:
        return var.strip()
    return var

def is_required(var):
    var = safe_strip(var)
    if var is None:
        return False
    if var.lower() in ['required', 'require', 'true']:
        return True
    return False

def run(args):

    # Comment format exemple

    #. variable_name (required): default value 1
    #+ description: my long desc
    
    #. variable_name2 (optional, str): default value
    #+ description: my long description
    #+  On several lines indeed
    
    #. variable_name3: 
    #+ description: desc 3


    docs = {}

    re_var_doc = re.compile('^\s*#\.\s*([^ ]+)\s*(\(([^,]+)(,(.+))?\))?\s*:(.*)')
    # groups :
    # 1: var name
    # 2: ignored
    # 3: required string
    # 4: ignored
    # 5: type
    # 6: default value
    #re_var_doc = re.compile('^\s*#\.\s*([^ ]+)\s*(\(.+\))?\s*:(.*)')
    re_var_descrption = re.compile('^\s*#\+ ?(.*)')
    #re_var_details = re.compile('\((.+)(,(.+))?\)')
    for line in args.file.readlines():
        
        docstring = re_var_doc.match(line)

        if docstring is None:
            description = re_var_descrption.match(line)

        if docstring is not None:
            _var = safe_strip(docstring.group(1))
            _type = safe_strip(docstring.group(5)) or '-'
            _default = safe_strip(docstring.group(6))
            _require = is_required(docstring.group(3))

            docs[_var] = {
                'Name': '`%s`' % _var,
                'Default': '`%s`' % _default,
                'Type': '`%s`' % _type,
                'Required': '`%s`' % _require,
                'Description': '',
            }

        elif description is not None:
            # Adding description to the latest var
            if _var is not None:
                docs[_var]['Description'] += description.group(1)
        else:
            continue

    # Print
    template = "|{Name}|{Description}|{Type}|{Default}|{Required}|"
    print(template.format( # header
      Name='Name', Description='Description', Type='Type',
      Default='Default', Required='Required'
    ))
    print(template.format( # Alignement parameters
      Name='---', Description='---', Type=':---:',
      Default=':---:', Required=':---:'
    ))

    for key, value in sorted(docs.iteritems()):
      print template.format(**value)


if __name__ == '__main__':

    args = get_args()
    init_logger(verbose=True)
    run(args)
