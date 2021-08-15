import time
import os
import subprocess


def wait(seconds):
    time.sleep(seconds) 


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
