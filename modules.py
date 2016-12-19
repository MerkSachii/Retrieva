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

def retrievePDF(data):
    # ########## JPEG ########### #
    pdfheaders = getPDFHeader(data)
    pdftailers = getPDFTrailer(data)
    pdflist = buildPDFList(pdfheaders, pdftailers, data)
    buildPDFImage(pdflist)


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

def buildPDFList(headers, tailers, data):
    pdflist = []

    for i in range(0, len(headers)):
        pdflist.append(data[headers[i].start(0):tailers[i].start(0) + 2])

    return pdflist


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

def getPDFHeader(data):

    headers = re.finditer(b'\x25\x50\x44\x46', data)
    listed = list(headers)
    iterator = 0
    for m in listed:
        iterator += 1
    print('Number of JPEG headers found: ', iterator)

    return listed


def getPDFTrailer(data):

    tailers = re.finditer(b'\x45\x4F\x46', data)
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
    headers = re.finditer(b'\xD0\xCF\x11\xE0', data)
    listed = list(headers)
    iterator = 0
    for m in listed:
        iterator += 1
    print('Number of DOC headers found: ', iterator)

    return listed


def getDOCTrailer(data):
                            ##CHANGE THIS CODE##
    tailers = re.finditer(b'\xF4\x39\xB2\x71', data)
    listed = list(tailers)
    iterator = 0
    for m in listed:
        iterator += 1
    print('Number of DOC footers found: ', iterator)

    return listed



    # ##### GET XLS HEADER & TRAILER ######


def getXLSHeader(data):
                           ##CHANGE THIS CODE##
    headers = re.finditer(b'\xD0\xCF\x11\xE0', data)
    listed = list(headers)
    iterator = 0
    for m in listed:
        iterator += 1
    print('Number of XLS headers found: ', iterator)

    return listed


def getXLSTrailer(data):
                            ##CHANGE THIS CODE##
    tailers = re.finditer(b'\x28\x00\x00\x00\x00\x10', data)
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

def buildPDFImage(pdflist):
    iterator = 0
    if len(pdflist) > 0:
        for i in pdflist:
            with open(os.path.join(os.path.expanduser('~'),'Desktop\\Retrieva Retrieved Files', 'PDFFILE' + str(iterator) + '.pdf'), "wb") as f:
                f.write(i)
                iterator += 1
    else:
        print("No PDF files recovered.")

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


# ============= Straight USB Read ==============

def smallScanJPEG(driveLetter):
    print("Small scan")
    volume = r'\\.\F:'
    volume = volume.replace('F', driveLetter[:1])
    chunk = 1048576
    iterator = 1
    listed = []
    listedH = []
    listedT = []
    fileList = []
    fileiter = 1
    bytes = 0

    firstRun = True
    g = os.fdopen(os.open(volume, os.O_RDONLY | os.O_BINARY), "rb")
    g.seek(0)
    data = g.read(chunk)
    while data:
        listed = []
        if not firstRun:
            data = g.read(chunk)
        firstRun = False
        iterNo = 1
        listedH = []
        listedT = []
        # JPEG Files
        headers = re.finditer(b'\xff\xd8', data)
        tailers = re.finditer(b'\xff\xd9', data)
        listedH.append(list(headers))
        listedT.append(list(tailers))
        listedH = list(filter(None, listedH))
        listedT = list(filter(None, listedT))

        if len(listedH) != 0 and len(listedT) != 0:
            for m in range(0, len(listedH)):
                for n in range(0, len(listedH[m])):
                    # print('H: ', data[listedH[m][n].start()])
                    # print('T: ', data[listedT[0][n].start()])
                    try:
                        headTup = listedH[m][n].span()
                        tailTup = listedT[0][n].span()
                        for l in range(0, len(listedT[0])):
                            fileList.append(data[listedH[m][n].start():listedT[0][l].start()])
                    except:
                        pass
        fileList = list(filter(None, fileList))
        if len(fileList) != 0:
            for k in fileList:
                with open(os.path.join(os.path.expanduser('~'),'Desktop\\Retrieva Retrieved Files', 'probablepic' + str(fileiter) + '.jpg'), 'wb') as fp:
                    fp.write(k)
                fileiter += 1
                print('JPEGNUMBER ', fileiter)
        iterator += 1
        fileList = []

def smallScanPNG(driveLetter):
    print("Small scan")
    volume = r'\\.\F:'
    volume = volume.replace('F', driveLetter[:1])
    chunk = 1048576
    iterator = 1
    listed = []
    listedH = []
    listedT = []
    fileList = []
    fileiter = 1
    bytes = 0

    firstRun = True
    g = os.fdopen(os.open(volume, os.O_RDONLY | os.O_BINARY), "rb")
    g.seek(0)
    data = g.read(chunk)
    while data:
        listed = []
        if not firstRun:
            data = g.read(chunk)
        firstRun = False
        iterNo = 1
        listedH = []
        listedT = []
        # JPEG Files
        headers = re.finditer(b'\x89\x50\x4E\x47', data)
        tailers = re.finditer(b'\x49\x45\x4E\x44\xAE\x42\x60\x82', data)
        listedH.append(list(headers))
        listedT.append(list(tailers))
        listedH = list(filter(None, listedH))
        listedT = list(filter(None, listedT))

        if len(listedH) != 0 and len(listedT) != 0:
            for m in range(0, len(listedH)):
                for n in range(0, len(listedH[m])):
                    # print('H: ', data[listedH[m][n].start()])
                    # print('T: ', data[listedT[0][n].start()])
                    try:
                        headTup = listedH[m][n].span()
                        tailTup = listedT[0][n].span()
                        for l in range(0, len(listedT[0])):
                            fileList.append(data[listedH[m][n].start():listedT[0][l].start()])
                    except:
                        pass
        fileList = list(filter(None, fileList))
        if len(fileList) != 0:
            for k in fileList:
                with open(os.path.join(os.path.expanduser('~'),'Desktop\\Retrieva Retrieved Files', 'probablepng' + str(fileiter) + '.png'), 'wb') as fp:
                    fp.write(k)
                fileiter += 1
                print('PNGNUMBER ', fileiter)
        iterator += 1
        fileList = []

def smallScanDOC(driveLetter):
    print("Small scan")
    volume = r'\\.\F:'
    volume = volume.replace('F', driveLetter[:1])
    chunk = 1048576
    iterator = 1
    listed = []
    listedH = []
    listedT = []
    fileList = []
    fileiter = 1
    bytes = 0

    firstRun = True
    g = os.fdopen(os.open(volume, os.O_RDONLY | os.O_BINARY), "rb")
    g.seek(0)
    data = g.read(chunk)
    while data:
        listed = []
        if not firstRun:
            data = g.read(chunk)
        firstRun = False
        iterNo = 1
        listedH = []
        listedT = []
        # JPEG Files
        headers = re.finditer(b'\xD0\xCF\x11\xE0', data)
        tailers = re.finditer(b'\xF4\x39\xB2\x71', data)
        listedH.append(list(headers))
        listedT.append(list(tailers))
        listedH = list(filter(None, listedH))
        listedT = list(filter(None, listedT))

        if len(listedH) != 0 and len(listedT) != 0:
            for m in range(0, len(listedH)):
                for n in range(0, len(listedH[m])):
                    # print('H: ', data[listedH[m][n].start()])
                    # print('T: ', data[listedT[0][n].start()])
                    try:
                        headTup = listedH[m][n].span()
                        tailTup = listedT[0][n].span()
                        for l in range(0, len(listedT[0])):
                            fileList.append(data[listedH[m][n].start():listedT[0][l].start()])
                    except:
                        pass
        fileList = list(filter(None, fileList))
        if len(fileList) != 0:
            for k in fileList:
                with open(os.path.join(os.path.expanduser('~'),'Desktop\\Retrieva Retrieved Files', 'probabledoc' + str(fileiter) + '.doc'), 'wb') as fp:
                    fp.write(k)
                fileiter += 1
                print('DOCNUMBER ', fileiter)
        iterator += 1
        fileList = []

def smallScanXLS(driveLetter):
    print("Small scan")
    volume = r'\\.\F:'
    volume = volume.replace('F', driveLetter[:1])
    chunk = 1048576
    iterator = 1
    listed = []
    listedH = []
    listedT = []
    fileList = []
    fileiter = 1
    bytes = 0

    firstRun = True
    g = os.fdopen(os.open(volume, os.O_RDONLY | os.O_BINARY), "rb")
    g.seek(0)
    data = g.read(chunk)
    while data:
        listed = []
        if not firstRun:
            data = g.read(chunk)
        firstRun = False
        iterNo = 1
        listedH = []
        listedT = []
        # JPEG Files
        headers = re.finditer(b'\xD0\xCF\x11\xE0', data)
        tailers = re.finditer(b'\x00\x00\x00\x00\x10', data)
        listedH.append(list(headers))
        listedT.append(list(tailers))
        listedH = list(filter(None, listedH))
        listedT = list(filter(None, listedT))

        if len(listedH) != 0 and len(listedT) != 0:
            for m in range(0, len(listedH)):
                for n in range(0, len(listedH[m])):
                    # print('H: ', data[listedH[m][n].start()])
                    # print('T: ', data[listedT[0][n].start()])
                    try:
                        headTup = listedH[m][n].span()
                        tailTup = listedT[0][n].span()
                        for l in range(0, len(listedT[0])):
                            fileList.append(data[listedH[m][n].start():listedT[0][l].start()])
                    except:
                        pass
        fileList = list(filter(None, fileList))
        if len(fileList) != 0:
            for k in fileList:
                with open(os.path.join(os.path.expanduser('~'),'Desktop\\Retrieva Retrieved Files', 'probablexls' + str(fileiter) + '.xls'), 'wb') as fp:
                    fp.write(k)
                fileiter += 1
                print('XLSNUMBER ', fileiter)
        iterator += 1
        fileList = []

def smallScanPDF(driveLetter):
    print("Small scan")
    volume = r'\\.\F:'
    volume = volume.replace('F', driveLetter[:1])
    chunk = 1048576
    iterator = 1
    listed = []
    listedH = []
    listedT = []
    fileList = []
    fileiter = 1
    bytes = 0

    firstRun = True
    g = os.fdopen(os.open(volume, os.O_RDONLY | os.O_BINARY), "rb")
    g.seek(0)
    data = g.read(chunk)
    while data:
        listed = []
        if not firstRun:
            data = g.read(chunk)
        firstRun = False
        iterNo = 1
        listedH = []
        listedT = []
        # JPEG Files
        headers = re.finditer(b'\x25\x50\x44\x46', data)
        tailers = re.finditer(b'\x45\x4F\x46', data)
        listedH.append(list(headers))
        listedT.append(list(tailers))
        listedH = list(filter(None, listedH))
        listedT = list(filter(None, listedT))

        if len(listedH) != 0 and len(listedT) != 0:
            for m in range(0, len(listedH)):
                for n in range(0, len(listedH[m])):
                    # print('H: ', data[listedH[m][n].start()])
                    # print('T: ', data[listedT[0][n].start()])
                    try:
                        headTup = listedH[m][n].span()
                        tailTup = listedT[0][n].span()
                        for l in range(0, len(listedT[0])):
                            fileList.append(data[listedH[m][n].start():listedT[0][l].start()])
                    except:
                        pass
        fileList = list(filter(None, fileList))
        if len(fileList) != 0:
            for k in fileList:
                with open(os.path.join(os.path.expanduser('~'),'Desktop\\Retrieva Retrieved Files', 'probablepdf' + str(fileiter) + '.pdf'), 'wb') as fp:
                    fp.write(k)
                fileiter += 1
                print('PDFNUMBER ', fileiter)
        iterator += 1
        fileList = []

def fullScan():
    print("Full scan")


def imager(driveLetter):
    volume = r'\\.\F:'
    volume = volume.replace('F', driveLetter[:1])
    chunk = 32768
    firstRun = True
    iterator = 1

    g = os.fdopen(os.open(volume, os.O_RDONLY | os.O_BINARY), "rb")
    g.seek(0)
    data = g.read(chunk)
    while data:
        if not firstRun:
            data = g.read(chunk)
        firstRun = False

        with open(os.path.join(os.path.expanduser('~'),'Desktop\\Retrieva Retrieved Files', 'tempImage.raw'), 'ab+') as file:
            file.write(data)
            print('Bytes: ', chunk * iterator)
            iterator += 1


def allZero(driveLetter):
    print('All Zero')
    # Implement the All Zero Algorithm
    # Overwriting Rounds: 1
    # Pattern: All zeroes
    volume = r'\\.\F:'
    vol = 'F:\\'
    volume = volume.replace('F', driveLetter[:1])
    vol = vol.replace('F', driveLetter[:1])
    print('DRIVELETTER ', driveLetter)
    print('VOL!!!!!!!!!!!!!!!!', vol)
    overwritePass = 1
    chunk = 512
    blocknum = 0
    overwriter = b'\x00'
    volumeSizeInformation = win32api.GetDiskFreeSpaceEx(vol)
    totalSize = volumeSizeInformation[1]
    totalSector = int(totalSize/chunk)

    g = os.fdopen(os.open(volume, os.O_WRONLY | os.O_BINARY), "wb")
    g.seek(0)

    if overwritePass == 1:
        for i in range(0,512):
            overwriter += b'\x00'
    print('Is it seekable? ', g._checkSeekable())

    for j in range(0, totalSector):

        print(blocknum)
        print('chunk: ', chunk)
        print('blocknum', blocknum)

        try:
            g.seek(chunk * blocknum)
            g.write(overwriter)
        except:
            pass
        blocknum += 1

def allOne(driveLetter):
    print('All One')
    # Implement the All One Algorithm
    # Overwriting Rounds: 1
    # Pattern: All ones
    volume = r'\\.\F:'
    vol = 'F:\\'
    volume = volume.replace('F', driveLetter[:1])
    vol = vol.replace('F', driveLetter[:1])
    overwritePass = 1
    chunk = 512
    blocknum = 0
    overwriter = b'\xFF'
    volumeSizeInformation = win32api.GetDiskFreeSpaceEx(vol)
    totalSize = volumeSizeInformation[1]
    totalSector = int(totalSize/chunk)
    g = os.fdopen(os.open(volume, os.O_WRONLY | os.O_BINARY), "wb")
    if overwritePass == 1:
        for i in range(0,chunk - 1):
            overwriter += b'\xFF'
    print('Is it seekable? ', g._checkSeekable())
    g.write(overwriter)
    for j in range(1, totalSector):

        # print('chunk: ', chunk)
        # print('blocknum', blocknum)

        # g.seek(g.tell())

        print('Current byte pwesto: ', g.tell())

        try:
            # g.seek(chunk * blocknum)
            g.write(overwriter)
        except:
            isError = True
            print('Hello')
            pass
        blocknum += 1
        if isError:
            isError = False
            try:
                g.seek(chunk * blocknum)
            except:
                print('WOOOORLDD!!!!')

def FACEAlgorithm(driveLetter):
    print('Face')
    # Implement the FACE Wipe Algorithm
    # Overwriting Rounds: 1
    # Pattern: F A C E
    volume = r'\\.\F:'
    vol = 'F:\\'
    volume = volume.replace('F', driveLetter[:1])
    vol = vol.replace('F', driveLetter[:1])
    overwritePass = 1
    chunk = 512
    blocknum = 0
    overwriter = b'\x0F\x0A\x0C\x0E'
    volumeSizeInformation = win32api.GetDiskFreeSpaceEx(vol)
    totalSize = volumeSizeInformation[1]
    totalSector = int(totalSize/chunk)

    g = os.fdopen(os.open(volume, os.O_WRONLY | os.O_BINARY), "wb")
    g.seek(0)

    if overwritePass == 1:
        for i in range(0,127):
            overwriter += b'\x0F\x0A\x0C\x0E'
    print('Is it seekable? ', g._checkSeekable())

    for j in range(0, totalSector):

        print(blocknum)
        print('chunk: ', chunk)
        print('blocknum', blocknum)

        try:
            g.seek(chunk * blocknum)
            g.write(overwriter)
        except:
            pass
        blocknum += 1

def BritInfo5St5Enhanced(driveLetter):
    print('British')
    # British HMG Infosec Standard 5, Enhanced Standard
    # Overwriting Rounds: 3
    # Pattern: 	All ones, all zeros, random
    volume = r'\\.\F:'
    vol = 'F:\\'
    volume = volume.replace('F', driveLetter[:1])
    vol = vol.replace('F', driveLetter[:1])
    overwritePass = 1
    chunk = 512
    blocknum = 0
    overwriter = b'\x00'
    volumeSizeInformation = win32api.GetDiskFreeSpaceEx(vol)
    totalSize = volumeSizeInformation[1]
    totalSector = int(totalSize/chunk)

    g = os.fdopen(os.open(volume, os.O_WRONLY | os.O_BINARY), "wb")
    g.seek(0)

    if overwritePass == 1:
        for i in range(0,511):
            overwriter += b'\x00'
    print('Is it seekable? ', g._checkSeekable())

    for k in range(0, 2):
        for j in range(0, totalSector):

            print(blocknum)
            print('chunk: ', chunk)
            print('blocknum', blocknum)

            try:
                g.seek(chunk * blocknum)
                g.write(overwriter)
            except:
                pass
            blocknum += 1
        overwritePass += 1
        if overwritePass == 2:
            for i in range(0,511):
                overwriter += b'\x00'
            g.seek(0)
        if overwritePass == 3:
            overwriter = os.urandom(512)
            g.seek(0)
def SchneierAlgo(driveLetter):
    print('Schneier')
    # Bruce Schneier's Algorithm
    # Overwriting Rounds: 7
    # Pattern: 	All ones, all zeros, pseudo-random sequence five times
    volume = r'\\.\F:'
    vol = 'F:\\'
    volume = volume.replace('F', driveLetter[:1])
    vol = vol.replace('F', driveLetter[:1])
    overwritePass = 1
    chunk = 512
    blocknum = 0
    overwriter = b'\xFF'
    volumeSizeInformation = win32api.GetDiskFreeSpaceEx(vol)
    totalSize = volumeSizeInformation[1]
    totalSector = int(totalSize/chunk)

    g = os.fdopen(os.open(volume, os.O_WRONLY | os.O_BINARY), "wb")
    g.seek(0)
    # lock_volume(g)

    if overwritePass == 1:
        for i in range(0,511):
            overwriter += b'\xFF'
    print('Is it seekable? ', g._checkSeekable())

    for k in range(0, 7):
        for j in range(0, totalSector):
            print(overwriter)
            print(blocknum)
            print('Iteration: ', k)
            print('chunk: ', chunk)
            print('blocknum', blocknum)

            g.seek(chunk * blocknum)
            g.write(overwriter)
            try:
                print("Hello")
            except:
                pass
            blocknum += 1
        overwritePass += 1
        if overwritePass == 2:
            for i in range(0,511):
                overwriter += b'\x00'
            # g.seek(0)
            blocknum = 0
        if overwritePass >= 3:
            overwriter = os.urandom(512)
            blocknum = 0
            # g.seek(0)
