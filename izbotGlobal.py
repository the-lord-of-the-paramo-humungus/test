#!/usr/bin/env python3
#optional argument converted in mandatory and default value 
#import modules
import argparse


def glParse():
    arg=argparse.ArgumentParser(description="optional argument converted in mandatory and default value  example")
    arg.add_argument("-c","--country", default="Guatemala", help="country name")
    argument=arg.parse_args()

    if argument.country:
        print(argument.country)

glParse()
