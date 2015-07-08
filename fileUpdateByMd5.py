#!/usr/bin python
# -*- encoding:utf8 -*-

import os
import sys
import hashlib
import shutil
   
pathnew = "C:\Users\sunlianqiang\pythontest\dir1"
pathold = "C:\Users\sunlianqiang\pythontest\dir2"

def gci(path):
    "gci start"
    parents = os.listdir(path)
    for parent in parents:
        child = os.path.join(path, parent)
        if os.path.isdir(child):
            print(child)
            gci(child)
        else:
            print(child)
            fileMd5(child)
           

           
def fileMd5(filename):
    fd = open(filename,"rb")  #rb, read only
    fcont = fd.read()
    fd.close()
    fmd5 = hashlib.md5(fcont)
    #print fmd5.hexdigest()
    return fmd5.hexdigest()
   
def gciOld(path):
    "gci old start"
    parents = os.listdir(path)
    for parent in parents:
        child = os.path.join(path, parent)
        if os.path.isdir(child):
            #print "Old dir: " +child
            child1=child.replace(pathold,pathnew)
            #print "New dir: " +child1
            if not os.path.exists(child1):
                shutil.rmtree(child,True)
                print "remove: " + child
            else:
                gciOld(child)
        else:
            #print "Old file: " +child
            child1=child.replace(pathold,pathnew)
            #print "New file: " +child1
            if not os.path.exists(child1):
                os.remove(child)
                print "remove: " + child
           
def gciNew(path):
    "gci new start"
    parents = os.listdir(path)
    for parent in parents:
        newFile = os.path.join(path, parent)
        if os.path.isdir(newFile):
            #dir
            #print "New dir: " +newFile
            oldFile = newFile.replace(pathnew, pathold)
            #print "Old dir: " +oldFile
            if not os.path.exists(oldFile):
                shutil.copytree(newFile,oldFile)
                print "copy Recursively: " + newFile + " to " + oldFile
            else:
                gciNew(newFile)
        else:
            #file
            #print "New file: " +newFile
            oldFile = newFile.replace(pathnew, pathold)
            #print "Old file: " +oldFile
            if not os.path.exists(oldFile):
                shutil.copyfile(newFile,oldFile)
                print "copy file: " + newFile + " to " + oldFile
            else:
            #check md5
                newFileMd5 = fileMd5(newFile)
                oldFileMd5 = fileMd5(oldFile)
                if ( newFileMd5 != oldFileMd5 ):
                    print "newFileMd5: " + newFileMd5
                    print "oldFileMd5: " + oldFileMd5
                    shutil.copyfile(newFile,oldFile)
                    print "replace file: " + newFile + " to " + oldFile
               
def updateDir(pathnew, pathold):
    print "update path: " + pathold + " from " + pathnew
    print "Gci search path: " + pathold + " start, delete file don't need"
    gciOld(pathold)
    print "Gci search path: " + pathnew + " start, copy new files and update files which have been modified"
    gciNew(pathnew)
    print "update complete!"
   
if __name__ == "__main__":
    #print(gci.__doc__)  #显示函数声明部分内容
    if 3 == len(sys.argv):
        pathnew = sys.argv[1]
        pathold = sys.argv[2]
        updateDir(pathnew,pathold)
   
   
