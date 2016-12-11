#!/usr/bin/env python

import re
import os
import win32api

def listAllDrives():
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    return drives

def openDataFile(volume):
    try:
        with open(volume, 'rb') as file_image:
            data = file_image.read()
    except IOError:
        print("Can't open file!")
    else:
        print("File opened successfully!")

        return data

def retrieveJPEG(data):
    # ########## JPEG ########### #
    jpegheaders = getJPEGHeader(data)
    jpegtailers = getJPEGTrailer(data)
    jpeglist = buildJPEGList(jpegheaders, jpegtailers, data)
    buildJPEGImage(jpeglist)



def retrievePNG(data):
    # ########## PNG ########### #
    pngheaders = getPNGHeader(data)
    pngtailers = getPNGTrailer(data)
    pnglist = buildPNGList(pngheaders, pngtailers, data)
    buildPNGImage(pnglist)



def retrieveDOC(data):
    # ########## DOC ########### #
    docheaders = getDOCHeader(data)
    doctailers = getDOCTrailer(data)
    doclist = buildDOCList(docheaders, doctailers, data)
    buildDOCImage(doclist)


def retrieveXLS(data):
    # ########## XLS ########### #
    xlsheaders = getPNGHeader(data)
    xlstailers = getPNGTrailer(data)
    xlslist = buildXLSList(xlsheaders, xlstailers, data)
    buildXLSImage(xlslist)

def buildJPEGList(headers, tailers, data):
    jpeglist = []

    for i in range(0, len(headers)):
        jpeglist.append(data[headers[i].start(0):tailers[i].start(0) + 2])

    return jpeglist


def buildPNGList(headers, tailers, data):
    pnglist = []

    for i in range(0, len(headers)):
        pnglist.append(data[headers[i].start(0):tailers[i].start(0) + 8])

    return pnglist


def buildDOCList(headers, tailers, data):
    doclist = []

    for i in range(0, len(headers)):
        doclist.append(data[headers[i].start(0):tailers[i].start(0) + 2])

    return doclist


def buildXLSList(headers, tailers, data):
    xlslist = []

    for i in range(0, len(headers)):
        xlslist.append(data[headers[i].start(0):tailers[i].start(0) + 8])

    return xlslist

def getJPEGHeader(data):

    headers = re.finditer(b'\xff\xd8', data)
    listed = list(headers)
    iterator = 0
    for m in listed:
        iterator += 1
    print('Number of JPEG headers found: ', iterator)

    return listed


def getJPEGTrailer(data):

    tailers = re.finditer(b'\xff\xd9', data)
    listed = list(tailers)
    iterator = 0
    for m in listed:
        iterator += 1
    print('Number of JPEG footers found: ', iterator)

    return listed

    # ##### GET PNG HEADER & TRAILER ######


def getPNGHeader(data):

    headers = re.finditer(b'\x89\x50\x4E\x47', data)
    listed = list(headers)
    iterator = 0
    for m in listed:
        iterator += 1
    print('Number of PNG headers found: ', iterator)

    return listed


def getPNGTrailer(data):

    tailers = re.finditer(b'\x49\x45\x4E\x44\xAE\x42\x60\x82', data)
    listed = list(tailers)
    iterator = 0
    for m in listed:
        iterator += 1
    print('Number of PNG footers found: ', iterator)

    return listed



    # ##### GET DOC HEADER & TRAILER ######

def getDOCHeader(data):
                           ##CHANGE THIS CODE##
    headers = re.finditer(b'\x89\x50\x4E\x47', data)
    listed = list(headers)
    iterator = 0
    for m in listed:
        iterator += 1
    print('Number of DOC headers found: ', iterator)

    return listed


def getDOCTrailer(data):
                            ##CHANGE THIS CODE##
    tailers = re.finditer(b'\x49\x45\x4E\x44\xAE\x42\x60\x82', data)
    listed = list(tailers)
    iterator = 0
    for m in listed:
        iterator += 1
    print('Number of DOC footers found: ', iterator)

    return listed



    # ##### GET XLS HEADER & TRAILER ######


def getXLSHeader(data):
                           ##CHANGE THIS CODE##
    headers = re.finditer(b'\x89\x50\x4E\x47', data)
    listed = list(headers)
    iterator = 0
    for m in listed:
        iterator += 1
    print('Number of XLS headers found: ', iterator)

    return listed


def getXLSTrailer(data):
                            ##CHANGE THIS CODE##
    tailers = re.finditer(b'\x49\x45\x4E\x44\xAE\x42\x60\x82', data)
    listed = list(tailers)
    iterator = 0
    for m in listed:
        iterator += 1
    print('Number of XLS footers found: ', iterator)

    return listed

def buildJPEGImage(jpeglist):
    iterator = 0
    if len(jpeglist) > 0:
        for i in jpeglist:
            with open(os.path.join(os.path.expanduser('~'),'Desktop\\Retrieva Retrieved Files', 'JPEGIMAGE' + str(iterator) + '.jpg'), "wb") as f:
                f.write(i)
                iterator += 1
    else:
        print("No JPEG files recovered.")


def buildPNGImage(pnglist):
    iterator = 0
    if len(pnglist) > 0:
        for i in pnglist:
            with open(os.path.join(os.path.expanduser('~'),'Desktop\\Retrieva Retrieved Files', 'PNGIMAGE' + str(iterator) + '.png'), "wb") as f:
                f.write(i)
                iterator += 1
    else:
        print("No PNG files recovered.")


def buildDOCImage(doclist):
    iterator = 0
    if len(doclist) > 0:
        for i in doclist:
            with open(os.path.join(os.path.expanduser('~'),'Desktop\\Retrieva Retrieved Files', 'DOCIMAGE' + str(iterator) + '.doc'), "wb") as f:
                f.write(i)
                iterator += 1
    else:
        print("No DOC files recovered.")


def buildXLSImage(xlslist):
    iterator = 0
    if len(xlslist) > 0:
        for i in xlslist:
            with open(os.path.join(os.path.expanduser('~'),'Desktop\\Retrieva Retrieved Files', 'XLSIMAGE' + str(iterator) + '.xls'), "wb") as f:
                f.write(i)
                iterator += 1
    else:
        print("No XLS files recovered.")


def makeDirectory():
    os.makedirs(os.path.join(os.path.expanduser('~'),'Desktop\\Retrieva Retrieved Files'),exist_ok=True)
