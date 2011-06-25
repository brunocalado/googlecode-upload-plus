#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# --------------------------------------------------------------------------------
# Libraries
# --------------------------------------------------------------------------------
import os
import sys


# --------------------------------------------------------------------------------
# Variables and Constants
# --------------------------------------------------------------------------------
debug = 1
googlecodeproject = '' 
googlecodeuser = ''
googlecodepassword = ''
projectFiles = []
projectFileList = ''
changeset = ''

# ------------------------------------------------------------
# Package Type
# Available options:
# 1 - tar.7z (default)
# 2 - 7z
# 3 - tar 
# 4 - compressed tar gzip2
# 5 - compressed tar gzip
# ------------------------------------------------------------
packageType = 1
packageSummary = '"Packaged Source Code"'

 
# ------------------------------------------------------------
# Functions
# ------------------------------------------------------------
def returnFile(fileName): 
	fileHandle = open(fileName, "r") 
	lines = (fileHandle.read()).splitlines() 
	fileHandle.close() 
	return lines

def message(msg):
    print( '\n\n' )
    print( '#' + 80*'-' )
    print( '# ' + msg )
    print( '#' + 80*'-' )

def packageExtensionSelection():
    global packagedFilename
    global changeset
    tmp = ''

    # 1 - tar.7z (default)
    if packageType == 1:
        packageExtension_a = '.tar'
        packageExtension_b = '.7z'
        packageCompressCommand_a = 'tar --update --verbose --verify --file'
        packageCompressCommand_b = '7z a'

        packagedFilenameTemp = 'sourceV' + changeset[0].zfill(4) + packageExtension_a
        tmp = packageCompressCommand_a + ' ' + packagedFilenameTemp + ' ' + projectFileList

        packagedFilename  = 'sourceV' + changeset[0].zfill(4) + packageExtension_a + packageExtension_b
        tmp = tmp + ' ; ' + packageCompressCommand_b + ' ' + packagedFilename + ' ' + packagedFilenameTemp
        
    # 2 - 7z        
    elif packageType == 2:
        packageExtension_a = '.7z'
        packageCompressCommand_a = '7z a'
        
        packagedFilename  = 'sourceV' + changeset[0].zfill(4) + packageExtension_a
        tmp = packageCompressCommand_a + ' ' + packagedFilename + ' ' + projectFileList
        
    # 3 - tar         
    elif packageType == 3:
        packageExtension_a = '.tar'
        packageCompressCommand_a = 'tar --update --verbose --verify --file'

        packagedFilename = 'sourceV' + changeset[0].zfill(4) + packageExtension_a
        tmp = packageCompressCommand_a + ' ' + packagedFilename + ' ' + projectFileList
        
    # 4 - compressed tar gzip2
    elif packageType == 4:
        packageExtension_a = '.tar.bz2'
        packageCompressCommand_a = 'tar --update --gzip2 --verbose --verify --file'

        packagedFilename = 'sourceV' + changeset[0].zfill(4) + packageExtension_a
        tmp = packageCompressCommand_a + ' ' + packagedFilename + ' ' + projectFileList
        
    # 5 - compressed tar gzip
    elif packageType == 5:
        packageExtension_a = '.tar.gz'
        packageCompressCommand_a = 'tar --update --gzip --verbose --verify --file'

        packagedFilename = 'sourceV' + changeset[0].zfill(4) + packageExtension_a
        tmp = packageCompressCommand_a + ' ' + packagedFilename + ' ' + projectFileList
    else:
        message('bad option')

    return tmp


# ------------------------------------------------------------
# Main
# ------------------------------------------------------------
if __name__ == "__main__":

    # ------------------------------------------------------------
    # Start message
    # ------------------------------------------------------------
    os.system('clear')
    message( 'Google Code Upload Plus' )


    # ------------------------------------------------------------
    # Get project information
    # ------------------------------------------------------------
    # Get project name
    tmp = 'cat .hg/hgrc | grep prefix | cut --delimiter="/" -f 3 | cut --delimiter="." --fields=1 > .tmp'
    if debug: print( tmp )
    os.system( tmp )
    googlecodeproject = str(returnFile('.tmp')[0])

    # Get username
    tmp = 'cat .hg/hgrc | grep .username | cut --delimiter=" " -f 3 | cut --delimiter=" " --fields=2 > .tmp'
    if debug: print( tmp )
    os.system( tmp )
    googlecodeuser = str(returnFile('.tmp')[0])

    # Get password
    tmp = 'cat .hg/hgrc | grep .password | cut --delimiter=" " -f 3 | cut --delimiter=" " --fields=2 > .tmp'
    if debug: print( tmp )
    os.system( tmp )
    googlecodepassword = str(returnFile('.tmp')[0])


    # ------------------------------------------------------------
    # Show project
    # ------------------------------------------------------------
    message( 'Project ' + googlecodeproject.upper() + ' will be commited, pushed, compressed and uploaded' )


    # ------------------------------------------------------------
    # Commit changes
    # ------------------------------------------------------------
    if debug == 0: os.system('hg commit')
    if debug == 0: os.system('hg push')


    # ------------------------------------------------------------
    # Get current version
    # ------------------------------------------------------------
    tmp = "hg log | grep changeset | head -n 1 | awk -F : '{print $2}' | sed 's/ //g' > .tmp"
    if debug: print( tmp )
    os.system( tmp )
    changeset = returnFile('.tmp')


    # ------------------------------------------------------------
    # Get project files
    # ------------------------------------------------------------
    tmp = "hg locate > .tmp"
    if debug: print( tmp )
    os.system( tmp )
    projectFiles = returnFile('.tmp')
    
    projectFileList = ''
    for line in projectFiles:
        projectFileList = projectFileList + line + ' '
    if debug: print( projectFileList )


    # ------------------------------------------------------------
    # Compress project files
    # ------------------------------------------------------------
    tmp = packageExtensionSelection()
    if debug: print( tmp )
    if debug == 0: os.system( tmp )


    # ------------------------------------------------------------
    # Upload the packaged file
    # ------------------------------------------------------------
    tmp = './tools/googlecode_upload.py --summary=' + packageSummary + ' --project=' + googlecodeproject + ' --user=' + googlecodeuser + ' --password=' + googlecodepassword + ' ' +  packagedFilename 
    if debug: print( tmp )
    if debug == 0: os.system( tmp )


    # ------------------------------------------------------------
    # Clean
    # ------------------------------------------------------------
    tmp = 'rm -f .tmp ' + packagedFilename.split('.')[0] + '*'
    if debug: print( tmp )
    if debug == 0: os.system( tmp )







