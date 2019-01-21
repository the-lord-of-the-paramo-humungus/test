#!/usr/bin/env python3
#mandatory choice argparse example
#import module
import argparse


def countryParse():
    arg=argparse.ArgumentParser(description="mandatory choice argparse example")
    arg.add_argument("country", choice=["Guatemala","Polonia","Francia"] help="Choice Country:  Guatemala, Polonia, Francia")

