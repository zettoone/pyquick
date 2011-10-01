#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

def get_special_paths(dir):
    #print dir
    filenames = os.listdir(dir)
    rst_list = []
    for filename in filenames:
        match = re.search(r'__(\w+)__', filename)
        if match:
            #print match.group()
            rst_list.append(os.path.abspath(os.path.join(dir, filename)))
    return rst_list

def copy_to(paths, dir):
    if os.path.exists(dir) != True:
        os.makedirs(dir)
    for filename in paths:
        shutil.copy(filename, dir)
    return

def zip_to(paths, zippath):
    zipabspath = os.path.abspath(zippath)
    if os.path.exists(os.path.dirname(zipabspath)) != True:
        os.makedirs(os.path.dirname(zippath))
    cmd = 'tar -cf ' + zippath + ' '
    for filename in paths:
        cmd = cmd + os.path.basename(filename) + ' '
    print 'Command to run:', cmd
    (status, output) = commands.getstatusoutput(cmd)
    if status:
        sys.stderr.write(output)
        sys.exit(1)
    print output
    return               


def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    tozip = ''
    #print args
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]
    
    elif args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]

    elif len(args) == 0:
        print "error: must specify one or more dirs"
        sys.exit(1)

    # +++your code here+++
    # Call your functions

    if todir:
        dirlist = get_special_paths('.')
        copy_to(dirlist, todir)
    elif tozip:
        dirlist = get_special_paths('.')
        zip_to(dirlist, tozip)
    else:
        dirlist = get_special_paths(args[0])
        for dir in dirlist:
            print dir
      
  
if __name__ == "__main__":
    main()
