import time
import os
import subprocess
import json


def wait(seconds):
    time.sleep(2) 


def openresults(filepath):
    """
    openresults function to open windows explorer when finished
    """
    subprocess.call(r"explorer {}".format(filepath), shell=True)


def createdir(filepath):
    """
    create directory for xlsx documents
    """
    try:
        os.makedirs(filepath)
    except FileExistsError:
        pass 


def readjson():
    """
    function for reading jason file. 
    the environments jason file holds the lists of sevrers.
    """
    try:
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        Json_file = open(os.path.join(__location__,"Environments.json"), "r")
        data = json.load(Json_file,encoding='utf8')
    except json.JSONDecodeError as e:
        print(e)
    return data