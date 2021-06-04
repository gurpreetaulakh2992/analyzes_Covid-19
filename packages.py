#! /usr/local/bin/python3

import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install("seaborn")
# install("numpy")
# install("scipy")
# install("matplotlib")
# install("ipython")
# install("pandas")
# install("sympy")
#install("nose")
#install("nose-warnings-filters")
#install("pytest")
#install("flaky")
#install("coverage")
#install("ipykernel")
#install("django")
#install("advertools")
#install("pyminifier")
#install("jupyter")
#install("pymongo")
#install("pypi")
#install("ssl")
#install("aws")
#install("srv")
#install("dnspython")
#install("certifi")