#!/usr/bin/env python3
#import modules
import argparse
import yaml


def argApp():
    arg=argparse.ArgumentParser(description="Pase yml file with mandatory argumet")
    arg.add_argument("nom_arg", nargs=2, help="Display secret tocken")
    argument=arg.parse_args()

    if argument.nom_arg:
        return argument.nom_arg[0],argument.nom_arg[1]


def ymlApp():
    secret,app_id=argApp()
    
    with open("application.yml", mode="r") as app_yml:
        data=yaml.load(app_yml)
        if secret == "secret" and app_id == "id":
            print(data["SECRET_TOKEN"])
            print(data["FACEBOOK_APP_ID"])
        else:
            print("Not found")

ymlApp()

