'''
Takes command line arg of a finding aid pdf, tesseracts it to html.hocr
'''

import subprocess
import sys

subprocess.check_output(["convert", "-density", "400", sys.argv[1], "out.png"])
subprocess.check_output(["tesseract", "out-1.png", "html", "hocr"])
