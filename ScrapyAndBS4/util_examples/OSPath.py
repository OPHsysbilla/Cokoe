import os.path

def pathSplit(filepath):
    return os.path.split(filepath)

def pathJoin(parentpath, filename):
    return os.path.join(parentpath, filename)

def join(parentpath, filename):
    return pathJoin(parentpath, filename)

def split(filePath):
    return pathSplit(filePath)