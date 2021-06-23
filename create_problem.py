#!/usr/local/bin/python3

from os import path, mkdir
import sys
import shutil


name = sys.argv[1]
print('Problem name: {}'.format(name))

# first check if directory exists, and create one if it doesn't
dir_name = name.replace('_', '-')
if path.isdir(dir_name):
    print('dir {} exists'.format(dir_name))
else:
    print('dir {} does not exist'.format(dir_name))
    print('creating dir {}'.format(dir_name))
    mkdir(dir_name)

# now copy template answer to new directory
file_name = name.replace('-', '_')
print('creating {}.py and {}.txt files from template'.format(file_name,file_name))
newPath = shutil.copy('template-solution/template_solution.py', dir_name + '/' + file_name + '.py')
newPath = shutil.copy('template-solution/template_solution.txt', dir_name + '/' + file_name + '.txt')

