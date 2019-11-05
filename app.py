# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 18:27:46 2019

@authors: jaydeep thik , Vasudev Purandare

"""

import flask
import os
import pandas as pd
#import tk_webcam as tk
import cv_cam_facial_expression as tk
import Rec as recmod
import scipy
import warnings
import flask
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1
video_id=""
sub1 = ""

@app.route("/", methods = ['GET', 'POST'])
def start():
    return render_template("homepage.html")


@app.route("/render", methods = ['GET'])
def home():
    
    if request.method == 'GET':
      sub1 = request.args.get('subject')
      video_id = request.args.get('video_id')
      print(sub1)
      print(video_id)
      
      return render_template("new.html", state="NONE", wl="NONE", seek_time = "NONE",sub=sub1, you_vid=video_id)

@app.route("/launch", methods = ['GET', 'POST'])
def launch():
     if request.method == 'GET':
      sub1 = request.args.get('subject')
      video_id = request.args.get('video_id')
      state, seek_time =  tk.cam_run()
      print("SEEK :", seek_time)
      print(video_id, sub1)
      return render_template("new.html", state=state, wl="NONE", seek_time=seek_time, you_vid=video_id, sub=sub1)

@app.route("/rec", methods = ['GET'])
def perform_rec():
    print("call for perform")
    if request.method == 'GET':
      sub1 = request.args.get('subject')
      vid_id = request.args.get('video_id')
      skt = request.args.get('seek_time')
      id = skt.find('.')
      skt = skt[:id]
      val = recmod.call_rec(sub1, vid_id, skt)
      #val = " ".join(val)
      return render_template("new.html", state="NONE", wl = val,seek_time = skt, you_vid=vid_id, sub=sub1)
if __name__ =="__main__":
    app.run(debug=True)