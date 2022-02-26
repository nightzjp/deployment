# -*- coding: utf-8 -*-

"""
@author: Mr_zhang
@software: PyCharm
@file: build.py
@time: 2022/2/8 21:13
"""

import os
import time
import shutil
from distutils.core import setup
from Cython.Build import cythonize

ROOT_PATH = os.path.abspath('.')
PROJECT_NAME = ROOT_PATH.split('/')[-1]

# Ignore
EXCEPT_FILES = {
    'build.py'
}

# Only copy
IGNORE_FILES = {
    'manage.py',
}

IGNORE_HIDE_FILES = ('.env', '.env_example')

PY_FILE_EXCEPT_SUF = ('.pyc', '.pyx')
PY_FILE_SUF = ('.py', )


def ls(_dir=''):
    """Return all relative path under the current folder."""
    dir_path = os.path.join(ROOT_PATH, _dir)
    for filename in os.listdir(dir_path):
        absolute_file_path = os.path.join(dir_path, filename)
        file_path = os.path.join(_dir, filename)
        if filename.startswith('.') and filename not in IGNORE_HIDE_FILES:
            continue
        if os.path.isdir(absolute_file_path) and not filename.startswith('__'):
            for file in ls(file_path):
                yield file
        else:
            yield file_path
            

def copy_ignore(dist='dist'):
    """Copy exclude files"""
    files = ls()
    for file in files:
        file_arr = file.split('/')
        if file_arr[0] == dist:
            continue
        suffix = os.path.splitext(file)[1]
        if not suffix and file not in IGNORE_HIDE_FILES:
            continue
        if file_arr[0] not in IGNORE_FILES and file not in IGNORE_FILES:
            if suffix in PY_FILE_EXCEPT_SUF:
                continue
            elif suffix in PY_FILE_SUF:
                continue
        src = os.path.join(ROOT_PATH, file)
        dst = os.path.join(ROOT_PATH, os.path.join(dist, file.replace(ROOT_PATH, '', 1)))
        _dir = '/'.join(dst.split('/')[:-1])
        if not os.path.exists(_dir):
            os.makedirs(_dir)
        shutil.copyfile(src, dst)


def build(dist='dist'):
    """py -> c -> so"""
    start = time.time()
    files = list(ls())
    module_list = list()
    for file in files:
        if file in EXCEPT_FILES or file in IGNORE_FILES:
            continue

        suffix = os.path.splitext(file)[1]
        if not suffix:
            continue
        elif suffix in PY_FILE_EXCEPT_SUF:
            continue
        elif suffix in PY_FILE_SUF:
            module_list.append(file)

    dist = os.path.join('.', dist)
    dist_temp = os.path.join(dist, 'temp')
    try:
        setup(ext_modules=cythonize(module_list, language_level="3"),
              script_args=["build_ext", "-b", dist, "-t", dist_temp])
    except Exception as e:
        print('Error: ', e)
        if os.path.exists(dist_temp):
            shutil.rmtree(dist_temp)
        for file in ls():
            if not file.endswith('.c'):
                continue
            os.remove(os.path.join(ROOT_PATH, file))
        return

    if os.path.exists(dist_temp):
        shutil.rmtree(dist_temp)
    for file in ls():
        if not file.endswith('.c'):
            continue
        os.remove(os.path.join(ROOT_PATH, file))

    copy_ignore()
    end = time.time()
    print('Complete, %.2fs !' % (end - start))
    
    
if __name__ == '__main__':
    # build()
    copy_ignore()
