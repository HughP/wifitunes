#!/usr/bin/env python

#    wifiTunes is a web based remote interface to your favorite music app
#    Copyright (C) 2008  Urs Kofmel
#
#    This file is part of wifiTunes.
#
#    wifiTunes is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    wifiTunes is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with wifiTunes.  If not, see <http://www.gnu.org/licenses/>.

from socket import gethostname
import sys
import os
import time
import random
import SocketServer
import BaseHTTPServer

HOST_NAME = gethostname()
PORT_NUMBER = 5550
if len(sys.argv) == 2:
    PortNr = int(sys.argv[1])
    if PortNr > 0 and PortNr <= 65535:
        PORT_NUMBER = PortNr

if HOST_NAME == "":
    print "Invalid hostname"
    sys.exit(1)

HOST_NAME = ""

#WorkingDir = os.path.join(sys.path[0], "src")
WorkingDir = sys.path[0]
#print WorkingDir
MainFile = os.path.join(WorkingDir, "index.html")

singlequote = "'"

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    CommandID = ""
    def do_POST(s):
        s.send_response(200)
        s.end_headers()
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s):
        #"""Respond to a GET request."""
        # proccess request string
        RequestedPath = s.path.split("?",1)[0]
        try:
            Suffix = s.path.split("?",1)[1]
        except IndexError:
            Suffix = "none"
        SuffixVaribles = dict()
        if Suffix != "none":
            SuffixItems = Suffix.split("&")
            for SuffixItem in SuffixItems:
                try:
                    SuffixVaribles[SuffixItem.split("=",1)[0]] = SuffixItem.split("=",1)[1]
                except:
                    pass
        #print SuffixVaribles
        # do we have to change the volume
        if RequestedPath == "/volume.html" and SuffixVaribles.has_key("cmd") and SuffixVaribles["cmd"] != "":
            Command = SuffixVaribles["cmd"]
            if Command == "vol":
                try:
                    newvolume = int(SuffixVaribles["vol"])
                except:
                    s.send_error(404)
                    s.end_headers()
                    return
                if newvolume >= 0 and newvolume <=100:
                    os.system("osascript " + singlequote + os.path.join(WorkingDir, "setvol.scpt") + singlequote + " " + str(newvolume))
                    s.send_response(200)
                    s.send_header("Content-type", "text/html")
                    s.send_header("Cache-Control", "max-age=0")
                    s.end_headers()
                    s.wfile.write("done")
                else:
                    s.send_error(404)
                    s.end_headers()
                return
            elif Command == "getvol":
                #os.system("osascript " + os.path.join(WorkingDir, "getvolume.scpt"))
                volumescriptout = os.popen("osascript " + singlequote + os.path.join(WorkingDir, "getvolume.scpt") + singlequote, "r")
                newvolume = ""
                for line in volumescriptout:
                    newvolume = newvolume + line;
                volumescriptout.close
                s.send_response(200)
                s.send_header("Content-type", "text/html")
                s.send_header("Cache-Control", "max-age=0")
                s.end_headers()
                s.wfile.write(newvolume)
                return
            else:
                s.send_error(404)
                s.end_headers()
                return
        # do we have to change the player position
        if RequestedPath == "/position.html" and SuffixVaribles.has_key("cmd") and SuffixVaribles["cmd"] != "":
            Command = SuffixVaribles["cmd"]
            if Command == "pos":
                try:
                    newposition =  int(SuffixVaribles["pos"])
                except:
                    s.send_error(404)
                    s.end_headers()
                    return
                os.system("osascript " + singlequote + os.path.join(WorkingDir, "setpos.scpt") + singlequote + " " + str(newposition))
            s.send_response(200)
            s.send_header("Content-type", "text/html")
            s.send_header("Cache-Control", "max-age=0")
            s.end_headers()
            s.wfile.write("done")
            return
        # do we have to get/set the outputs
        if RequestedPath == "/outputs.html" and SuffixVaribles.has_key("cmd") and SuffixVaribles["cmd"] != "":
            Command = SuffixVaribles["cmd"]
            if Command == "getout":
                htmlout = []
#                os.system("osascript " + os.path.join(WorkingDir, "getoutputs.scpt") + " " + os.path.join(WorkingDir, "") + " " + "outputs.txt")
                os.system("osascript " + singlequote + os.path.join(WorkingDir, "clickairtunes.scpt") + singlequote)
                os.system("osascript " + singlequote + os.path.join(WorkingDir, "getoutputs.scpt") + singlequote + " " + singlequote + os.path.join(WorkingDir, "") + singlequote + " " + "outputs.txt")
                OutputsFilePath = os.path.join(WorkingDir, "outputs.txt")
                if os.access(OutputsFilePath, os.R_OK):
                    OutputsFile = open(OutputsFilePath, "r")
                    for line in OutputsFile:
                        line = line.replace("\n","")
                        if line != "not enabled":
                            htmlout.append("<output>" + line + "</output>\n")
                    OutputsFile.close()
                #print htmlout
                if htmlout != []:
                    s.send_response(200)
                    s.send_header("Content-type", "text/xml")
                    s.send_header("Cache-Control", "max-age=0")
                    s.end_headers()
                    s.wfile.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
                    s.wfile.write('<document id="dokument">\n')
                    for line in htmlout:
                        s.wfile.write(line)
                    s.wfile.write("</document>\n")
                else:
                    s.send_response(204)
                    s.end_headers()
            elif Command == "setout":
                try:
                    newoutput = int(SuffixVaribles["name"])
                except:
                    s.send_error(404)
                    s.end_headers()
                    return
                os.system("osascript " + singlequote + os.path.join(WorkingDir, "clickairtunes.scpt") + singlequote)
                os.system("osascript " + singlequote + os.path.join(WorkingDir, "setoutput.scpt") + singlequote + " " + str(newoutput))
                s.send_response(200)
                s.send_header("Content-type", "text/html")
                s.send_header("Cache-Control", "max-age=0")
                s.end_headers()
                s.wfile.write("done")
            else:
                s.send_error(404)
                s.end_headers()
            return
        # do we have to change the playlist
        if RequestedPath == "/index.html" and SuffixVaribles.has_key("list") and SuffixVaribles["list"] != "" and SuffixVaribles["id"] == MyHandler.CommandID:
            script = ""
            # select a playlist
            try:
                PlaylistIndex = int(SuffixVaribles["list"])
            except:
                s.send_error(404)
                s.end_headers()
                return
            #print "Playlist index is " + PlaylistIndex
            os.system("osascript " + singlequote + os.path.join(WorkingDir, "selectlist.scpt") + singlequote + " " + str(PlaylistIndex))
            RequestedPath = "/index.html"
        # do we have to change the track
        if RequestedPath == "/index.html" and SuffixVaribles.has_key("track") and SuffixVaribles["track"] != "" and SuffixVaribles["id"] == MyHandler.CommandID:
            # select a track
            try:
                TrackId = int(SuffixVaribles["track"])
            except:
                s.send_error(404)
                s.end_headers()
                return
            #print "Track ID is " + TrackId
            os.system("osascript " + singlequote + os.path.join(WorkingDir, "settrack.scpt") + singlequote + " " + str(TrackId))
            RequestedPath = "/index.html"
        # do we have to execute a command
        elif RequestedPath == "/index.html" and SuffixVaribles.has_key("cmd") and SuffixVaribles["cmd"] != "" and SuffixVaribles["id"] == MyHandler.CommandID:
            script = ""
            Command = SuffixVaribles["cmd"]
            #print "Command is " + Command
            if Command == "prev":
                script = "prev"
            if Command == "playpause":
                script = "playpause"
            if Command == "next":
                script = "next"
            if Command == "shuffle":
                script = "toggleshuffle"
            if script != "":
                os.system("osascript " + singlequote + os.path.join(WorkingDir, script + ".scpt") + singlequote)
        # do we have to serve the main html
        if RequestedPath == "/index.html" or s.path == "" or s.path == "/":
            if RequestedPath == "" or RequestedPath == "/":
                RequestedPath = "/index.html"
            #if open file ok
            FileToServe = os.path.join(WorkingDir, RequestedPath[1:])
            MyHandler.CommandID = str(random.randint(1,9999))
            if os.access(FileToServe, os.R_OK):
                s.send_response(200)
                s.send_header("Content-type", "text/html")
                s.send_header("Cache-Control", "max-age=0")
                s.end_headers()
                os.system("osascript " + singlequote + os.path.join(WorkingDir, "getinfos.scpt") + singlequote + " " + singlequote + os.path.join(WorkingDir, "") + singlequote + " songinfo.txt")
                infos = dict()
                # initialise keys
                infos["artist"] = ""
                infos["title"] = ""
                infos["album"] = ""
                infos["duration"] = "missing value"
                infos["currentposition"] = "missing value"
                infos["hasartwork"] = ""
                infos["DBID"] = ""
                infofile = open(os.path.join(WorkingDir, "songinfo.txt"), "r")
                for line in infofile.readlines():
                    #print line
                    key = line.split(":")[0]
                    value = line.split(":",1)[1]
                    value = value.replace("\n","")
                    infos[key]=value
                #print infos
                infofile.close()
                #html = []
                #file = open(FileToServe, 'r')
                #for line in file.readlines():
                #    html.append(line)
                #file.close()
                for line in html:
                    if infos["state"] == "playing" and infos["duration"] != "missing value":
                        line = line.replace("STATE", '"playing"')
                        duration = infos["duration"].split(".")[0]
                        remaining = int(duration) - int(infos["currentposition"])
                        line = line.replace("PLAYPAUSE", "pause")
                        #line = line.replace("<!--RELOAD-->", '<meta id="reload" http-equiv="refresh" content="' + str(remaining) + '; URL=index.html">')
                    elif infos["state"] == "stopped" and infos["currentplaylist"] == "":
                        line = line.replace("<!--RELOAD-->", '<meta http-equiv="refresh" content="0; URL=playlists.html">')
                        line = line.replace("STATE", '"stopped"')
                        line = line.replace("PLAYPAUSE", "play")
                    else:
                        line = line.replace("STATE", '"stopped"')
                        line = line.replace("PLAYPAUSE", "play")
                    line = line.replace("ID", MyHandler.CommandID)
                    line = line.replace("ARTIST", infos["artist"])
                    line = line.replace("TITLE", infos["title"])
                    line = line.replace("ALBUM", infos["album"])
                    line = line.replace("PLAYLIST", infos["currentplaylist"])
                    if infos["shuffle"] == "true":
                        line = line.replace("SHUFFLE", "shuffleon")
                    else:
                        line = line.replace("SHUFFLE", "shuffleoff")
                    if infos["duration"] != "missing value":
                        line = line.replace("DURATION", infos["duration"].split(".")[0])
                    else:
                        line = line.replace("DURATION", "0")
                    if infos["currentposition"] != "missing value":
                        line = line.replace("POSITION", infos["currentposition"])
                    else:
                        line = line.replace("POSITION", "0")
                    if infos["hasartwork"] == "true":
                        line = line.replace("ARTWORK", infos["DBID"] + "cover")
                    elif infos["hasartwork"] == "ilegal":
                        line = line.replace("ARTWORK", "ilegalartwork")
                    else:
                        line = line.replace("ARTWORK", "noartwork")
                    #if infos["hasartwork"] == "true":
                    line = line.replace("MIRROR", infos["DBID"] + "mirror")
                    #if line.find("VOLUME") != -1:
                    #    line = line.replace("VOLUME", infos["volume"])
                    s.wfile.write(line)
                #file.close()
        elif (RequestedPath[:1] == "/" and RequestedPath[-4:] == ".png") or (RequestedPath[:1] == "/" and RequestedPath[-4:] == ".jpg") or (RequestedPath[:1] == "/" and RequestedPath[-4:] == ".css") or (RequestedPath[:1] == "/" and RequestedPath[-3:] == ".js"):
            #if open file ok
            if RequestedPath[:1] == "/" and (RequestedPath[-9:] == "cover.jpg" or RequestedPath[-10:] == "mirror.jpg"):
                contenttype = "image/jpg"
                sourcedir = ""
            elif RequestedPath[:1] == "/" and RequestedPath[-4:] == ".jpg":
                contenttype = "image/jpg"
                sourcedir = "images"
            elif RequestedPath[:1] == "/" and RequestedPath[-4:] == ".png":
                contenttype = "image/png"
                sourcedir = "images"
            elif RequestedPath[:1] == "/" and RequestedPath[-4:] == ".css":
                contenttype = "text/css"
                sourcedir = "css"
            elif RequestedPath[:1] == "/" and RequestedPath[-3:] == ".js":
                contenttype = "text/javascript"
                sourcedir = "scripts"
            ImageToServe = os.path.join(WorkingDir, sourcedir, RequestedPath[1:])
            if os.access(ImageToServe, os.R_OK):
                s.send_response(200)
                s.send_header("Content-type", contenttype)
                s.send_header("Cache-Control", "max-age=0")
                s.end_headers()
                imagefile = open(ImageToServe, 'r')
                s.wfile.write(imagefile.read())
                #for byte in imagefile.readlines():
                #    s.wfile.write(byte)
                imagefile.close()
            else:
                s.send_error(404)
                s.end_headers()
        elif RequestedPath == "/playlists.html":
            #if open file ok
            FileToServe = os.path.join(WorkingDir, RequestedPath[1:])
            MyHandler.CommandID = str(random.randint(1,9999))
            if os.access(FileToServe, os.R_OK):
                s.send_response(200)
                s.send_header("Content-type", "text/html")
                s.send_header("Cache-Control", "max-age=0")
                s.end_headers()
                os.system("osascript " + singlequote + os.path.join(WorkingDir, "getplaylists.scpt") + singlequote + " " + singlequote + os.path.join(WorkingDir, "") + singlequote + " " + "playlists.txt")
                normallists = dict()
                smartlists = dict()
                playlistfile = open(os.path.join(WorkingDir, "playlists.txt"), "r")
                for line in playlistfile.readlines():
                    playlistname = line.split(":",2)[2]
                    playlistindex = line.split(":",2)[1]
                    if line.split(":")[0] == "smart":
                        smartlists[playlistindex]=(playlistname.replace("\n", ""))
                    elif line.split(":")[0] == "normal":
                        normallists[playlistindex]=(playlistname.replace("\n", ""))
                #print normallists
                #print smartlists
                playlistfile.close()
                addline = False
                playlisthtml = []
                htmlfile = open(FileToServe, 'r')
                for line in htmlfile.readlines():
                    if line.find("<!--NORMALLISTS-END-->") != -1:
                        addline = False
                        for item in normallists.keys():
                            for codeline in playlisthtml:
                                codeline = codeline.replace("NAME", normallists[item])
                                codeline = codeline.replace("INDEX", item)
                                codeline = codeline.replace("ID", MyHandler.CommandID)
                                s.wfile.write(codeline)
                        playlisthtml = []
                    if line.find("<!--SMARTLISTS-END-->") != -1:
                        addline = False
                        for item in smartlists.keys():
                            for codeline in playlisthtml:
                                codeline = codeline.replace("NAME", smartlists[item])
                                codeline = codeline.replace("INDEX", item)
                                codeline = codeline.replace("ID", MyHandler.CommandID)
                                s.wfile.write(codeline)
                        playlisthtml = []
                    if addline:
                        playlisthtml.append(line)
                    else:
                        s.wfile.write(line)
                    if line.find("<!--NORMALLISTS-START-->") != -1 or line.find("<!--SMARTLISTS-START-->") != -1:
                        addline = True
                htmlfile.close()

        elif RequestedPath == "/tracklist.html":
            #if open file ok
            FileToServe = os.path.join(WorkingDir, RequestedPath[1:])
            MyHandler.CommandID = str(random.randint(1,9999))
            if os.access(FileToServe, os.R_OK):
                s.send_response(200)
                s.send_header("Content-type", "text/html")
                s.send_header("Cache-Control", "max-age=0")
                s.end_headers()
                os.system("osascript " + singlequote + os.path.join(WorkingDir, "gettracklist.scpt") + singlequote + " " + singlequote + os.path.join(WorkingDir, "") + singlequote + " " + "tracklist.txt")
                tracklist = []
                trackprops = dict()
                tracklistfile = open(os.path.join(WorkingDir, "tracklist.txt"), "r")
                for line in tracklistfile.readlines():
                    if line.split(":",1)[0] == "playlist":
                        PlaylistName = line.split(":",1)[1].replace("\n", "")
                    else:
                        #tracklist.append(line.replace("\n", ""))
                        DBID = line.split(":",1)[0]
                        if not trackprops.has_key(DBID): 
                            tracklist.append(DBID)
                            trackprops[DBID] = dict()
                        Key = line.split(":",2)[1]
                        Value= line.split(":",2)[2].replace("\n", "")
                        trackprops[DBID][Key] = Value
                #print tracklist
                tracklistfile.close()
                addline = False
                playlisthtml = []
                htmlfile = open(FileToServe, 'r')
                for line in htmlfile.readlines():
                    line = line.replace("PLAYLIST", PlaylistName)
                    if line.find("<!--TRACKLISTS-END-->") != -1:
                        addline = False
                        for DBID in tracklist:
                            TrackName = trackprops[DBID]["title"]
                            if trackprops[DBID].has_key("artist"):
                                TrackArtist = trackprops[DBID]["artist"]
                            else:
                                TrackArtist = ""
                            #TrackName = item.split(":",1)[1]
                            #TrackIndex =  item.split(":",1)[0]
                            if DBID == "current":
                                TrackCommandId = "0"
                                ArrowName = "arrow_white"
                            else:
                                TrackCommandId = str(MyHandler.CommandID)
                                ArrowName = "arrow"
                            for codeline in playlisthtml:
                                codeline = codeline.replace("NAME", TrackName)
                                codeline = codeline.replace("ARTIST", TrackArtist)
                                codeline = codeline.replace("INDEX", DBID)
                                codeline = codeline.replace("ID", TrackCommandId)
                                codeline = codeline.replace("ARROW", ArrowName)
                                s.wfile.write(codeline)
                        playlisthtml = []
                    if addline:
                        playlisthtml.append(line)
                    else:
                        s.wfile.write(line)
                    if line.find("<!--TRACKLISTS-START-->") != -1:
                        addline = True
                htmlfile.close()

        else:
            s.send_error(404)
            s.end_headers()
    def log_message(format, *args):
        #do nothing
        output = "none"
        
        
class ThreadingHTTPServer (SocketServer.ThreadingMixIn,
              BaseHTTPServer.HTTPServer):
    pass

if __name__ == '__main__':
    #server_class = BaseHTTPServer.HTTPServer
    #httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    httpd = ThreadingHTTPServer((HOST_NAME, PORT_NUMBER), MyHandler)
    html = []
    if os.access(MainFile, os.R_OK):
        file = open(MainFile, 'r')
        for line in file.readlines():
            html.append(line)
        file.close()
    #print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    #print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)