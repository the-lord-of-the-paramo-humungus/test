#!/usr/bin/env python3
#import modules
import argparse

def n_args():
    arg=argparse.ArgumentParser(description="no-arguments or n-agurmets example")
    arg.add_argument("nom_args", nargs="?", default="gt", help="argumnets to parse")
    argument=arg.parse_args()

    if argument.nom_args:
        print(argument.nom_args)


n_args()
