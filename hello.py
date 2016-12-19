#!/usr/bin/env python
from __future__ import print_function
from time import sleep
import sys
import modules
import encryptdecrypt as ed
import logging
import os
from logging.handlers import RotatingFileHandler
from flask import Flask, render_template, request, redirect, jsonify, flash
UPLOAD_FOLDER = '/Uploads'
ALLOWED_EXTENSIONS = set(['raw', 'img', 'png', 'jpg', 'jpeg', 'gif'])
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def foo():
    app.logger.warning('A warning occurred (%d apples)', 42)
    app.logger.error('An error occurred')
    app.logger.info('Info')
    return "foo"

@app.route("/")
def hello():

    return render_template('landing.html')

@app.route("/menu")
def menu():
    return render_template('home.html')


@app.route("/chooseDrive/<action>")
def chooseDrive(action):
    drives = modules.listAllDrives();

    return render_template('chooseDrive.html', drive = drives, job = action)

@app.route("/chooseDrive")
def chooseDrive():
    drives = modules.listAllDrives();

    return render_template('chooseDrive.html', drive = drives)


@app.route("/Retrieva/", methods=['GET'])
def Retrieva():
    # job = request.args.get('job')
    # drive = request.args.get('drive')
    #
    # if job == 'media':
    #     return render_template('retrievaMedia.html', drives = drive)
    #
    # elif job == 'image':
    #     return render_template('retrievaImage.html', drives = drive)
    #
    # elif job == 'backup':
    #     return render_template('retrievaBackup.html', drives = drive)

    return render_template('home.html')

@app.route("/chooseFile")
def chooseFile():

    return render_template('chooseFile.html')

@app.route("/retrieveFromImage", methods=['POST'])
def retrieveFromImage():

    file_path = request.form.get('path')
    # if_jpeg = request.form.get('jpeg')
    # if_png = request.form.get('png')
    # if_doc = request.form.get('doc')
    # if_xls = request.form.get('xls')
    # if_pdf = request.form.get('pdf')
    file_path = file_path.encode('unicode-escape')
    modules.makeDirectory()

    imageData = modules.openDataFile(file_path)
    modules.retrieveJPEG(imageData)
    modules.retrievePNG(imageData)
    modules.retrieveDOC(imageData)
    modules.retrieveXLS(imageData)
    modules.retrievePDF(imageData)
    # if if_jpeg != None:
    #     modules.retrieveJPEG(imageData)
    # if if_png != None:
    #     modules.retrievePNG(imageData)
    # if if_doc != None:
    #     modules.retrieveDOC(imageData)
    # if if_xls != None:
    #     modules.retrieveXLS(imageData)
    # if if_pdf != None:
    #     modules.retrievePDF(imageData)
    return render_template("loading.html")


@app.route("/retrievaMedia/", methods=['GET'])
def retrievaMedia():
    drivers = request.args.get('drive')

    return render_template("retrievaMedia.html", drive = drivers)

@app.route("/shredMedia", methods=['GET'])
def shredMedia():
    drivers = request.args.get('drive')

    return render_template("shredSelect.html", drive = drivers)

@app.route("/doShredMedia", methods=['POST','GET'])
def doshredMedia():
    zero = request.form.get('zero')
    one = request.form.get('one')
    face = request.form.get('face')
    brit = request.form.get('brit')
    schn = request.form.get('schn')
    drive = request.form['drive']

    if zero != None:

    if one != None:

    if face != None:

    if brit != None:

    if schn != None:
    

    return render_template("loading.html", drive = drivers)

@app.route("/scanExtract/", methods=['GET'])
def scanExtract():
    job = request.args.get('job')
    driver = request.args.get('drivers')

    # if job == 'full':
    #     modules.fullScan(driver)
    # elif job == 'slow':
    #     modules.smallScan(driver)

    return render_template("scanExtract.html", jobs = job, drivers = driver)

@app.route("/doScanAndExtract", methods=['POST','GET'])
def doScanAndExtract():
    if request.method == 'POST':
        jpeg = request.form.get('jpeg')
        png = request.form.get('png')
        doc = request.form.get('doc')
        xls = request.form.get('xls')
        pdf = request.form.get('pdf')
        drive = request.form['drive']
        job = request.form['job']
    modules.makeDirectory()
    if job == 'full':
        if jpeg != None:
            modules.smallScanJPEG(drive)
        if png != None:
            modules.smallScanPNG(drive)
        if doc != None:
            modules.smallScanDOC(drive)
        if xls != None:
            modules.smallScanXLS(drive)
        if pdf != None:
            modules.smallScanPDF(drive)
        return render_template("loading.html")
    if job == "slow":
        modules.imager(drive)
        imageData = os.path.join(os.path.expanduser('~'),'Desktop\\Retrieva Retrieved Files', 'tempImage.raw')
        if jpeg != None:
            modules.retrieveJPEG(imageData)
        if png != None:
            modules.retrievePNG(imageData)
        if doc != None:
            modules.retrieveDOC(imageData)
        if xls != None:
            modules.retrieveXLS(imageData)
        if pdf != None:
            modules.retrievePDF(imageData)
        return render_template("loading.html")


@app.route("/encryptdecrypt", methods=['POST', 'GET'])
def encryptdecrypt():

    return render_template("encryptDec.html")

@app.route("/encCaesarMin1", methods=['POST'])
def encCaesarMin1():
    plainText = request.form.get('plainText')
    KeyMap = ed.appendKeyMapList()
    encryptedText = ed.encryptText(KeyMap, 0, plainText)
    return encryptedText

@app.route("/decCaesarMin1", methods=['POST'])
def decCaesarMin1():
    plainText = request.form.get('plainText')
    KeyMap = ed.appendReverseKeyMapList()
    decryptedText = ed.decryptText(KeyMap, 0, plainText)
    return decryptedText

@app.route("/encCaesarMin2", methods=['POST'])
def encCaesarMin2():
    plainText = request.form.get('plainText')
    KeyMap = ed.appendKeyMapList()
    encryptedText = ed.encryptText(KeyMap, 1, plainText)
    return encryptedText

@app.route("/decCaesarMin2", methods=['POST'])
def decCaesarMin2():
    plainText = request.form.get('plainText')
    KeyMap = ed.appendReverseKeyMapList()
    decryptedText = ed.decryptText(KeyMap, 1, plainText)
    return decryptedText

@app.route("/encCaesarMin3", methods=['POST'])
def encCaesarMin3():
    plainText = request.form.get('plainText')
    KeyMap = ed.appendKeyMapList()
    encryptedText = ed.encryptText(KeyMap, 2, plainText)
    return encryptedText

@app.route("/decCaesarMin3", methods=['POST'])
def decCaesarMin3():
    plainText = request.form.get('plainText')
    KeyMap = ed.appendReverseKeyMapList()
    decryptedText = ed.decryptText(KeyMap, 2, plainText)
    return decryptedText

@app.route("/encCaesarPlus1", methods=['POST'])
def encCaesarPlus1():
    plainText = request.form.get('plainText')
    KeyMap = ed.appendKeyMapList()
    encryptedText = ed.encryptText(KeyMap, 3, plainText)
    return encryptedText

@app.route("/decCaesarPlus1", methods=['POST'])
def decCaesarPlus2():
    plainText = request.form.get('plainText')
    KeyMap = ed.appendReverseKeyMapList()
    decryptedText = ed.decryptText(KeyMap, 3, plainText)
    return decryptedText

@app.route("/encEmoticon", methods=['POST'])
def encEmoticon():
    plainText = request.form.get('plainText')
    KeyMap = ed.appendKeyMapList()
    encryptedText = ed.encryptText(KeyMap, 4, plainText)
    print('Enc ',encryptedText)
    return encryptedText

@app.route("/decEmoticon", methods=['POST'])
def decEmoticon():
    plainText = request.form.get('plainText')
    KeyMap = ed.appendReverseKeyMapList()
    decryptedText = ed.decryptText(KeyMap, 4, plainText)
    print('Plain ', plainText)
    print('Dec ', decryptedText)
    return decryptedText

@app.route("/encRandom", methods=['POST'])
def encRandom():
    plainText = request.form.get('plainText')
    encryptedText = ed.encryptTextRandom(plainText)
    return encryptedText

@app.route("/decRandom", methods=['POST'])
def decRandom():
    plainText = request.form.get('plainText')
    decryptedText = ed.decryptTextRandom(plainText)
    return decryptedText

@app.route("/encMD5", methods=['POST'])
def encMD5():
    plainText = request.form.get('plainText')
    encryptedText = ed.md5Hash(plainText)
    return encryptedText

@app.route("/encSHA", methods=['POST'])
def encSHA():
    plainText = request.form.get('plainText')
    encryptedText = ed.sha512Hash(plainText)
    return encryptedText






if __name__ == "__main__":
    handler = RotatingFileHandler('foo.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run()
