#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from argparse import ArgumentParser
import fileinput
import os

from datetime import date
from constants import *
from utils import *
from config import REPLACEMENT

def addForm(form,description = '@TODO'):
    formInclude = form.upper()
    formUnderscore = camelToUnderscore(form)

    replacePlaceholders = {
        '%%FORM_NAME%%' : form,
        '%%FORM_INCLUDE%%' : formInclude,
        '%%FORM_TODAY%%' : date.today().strftime('%d %B %Y'),
        '%%FORM_DESCRIPTION%%' : description
    }


    # create the struct file

    generateFromTemplate(
        os.path.join(FORM_TMPL_DIR,FORM_H_TPL),
        replacePlaceholders,
        os.path.join(FORM_OUTPUT_DIR,form + '.h')
    )


if __name__ == '__main__' :

    parser = ArgumentParser(
        description = "Add a new form"
    )

    parser.add_argument(
        'form',
        metavar = 'FORM',
        help = 'name of form you want to add'
    )

    parser.add_argument(
        '-d',
        '--description',
        nargs='?',
        help = 'a description of what your form is supposed to do',
        default = '@TODO add a description'
    )


    args = parser.parse_args();


    description = args.description
#TODO maybe do some check if the user enter a non valid
# form name
    form = args.form
    addForm(form,description)

