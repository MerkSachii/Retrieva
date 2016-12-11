#!/usr/bin/env python
from __future__ import print_function
from time import sleep
import sys
import modules
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


@app.route("/Retrieva/", methods=['GET'])
def Retrieva():
    job = request.args.get('job')
    drive = request.args.get('drive')

    if job == 'media':
        return render_template('retrievaMedia.html', drives = drive)

    elif job == 'image':
        return render_template('retrievaImage.html', drives = drive)

    elif job == 'backup':
        return render_template('retrievaBackup.html', drives = drive)

    return render_template('home.html')

@app.route("/chooseFile")
def chooseFile():

    return render_template('chooseFile.html')

@app.route("/retrieveFromImage", methods=['GET'])
def retrieveFromImage():

    file_path = request.args['path']
    file_path = file_path.encode('unicode-escape')
    modules.makeDirectory()

    imageData = modules.openDataFile(file_path)

    modules.retrieveJPEG(imageData)
    modules.retrievePNG(imageData)
    modules.retrieveDOC(imageData)
    modules.retrieveXLS(imageData)
    return jsonify('Success!')

if __name__ == "__main__":
    handler = RotatingFileHandler('foo.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run()
