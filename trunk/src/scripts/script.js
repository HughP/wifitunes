//    wifiTunes is a web based remote interface to your favorite music app
//    Copyright (C) 2008  Urs Kofmel
//
//    This file is part of wifiTunes.
//
//    wifiTunes is free software: you can redistribute it and/or modify
//    it under the terms of the GNU General Public License as published by
//    the Free Software Foundation, either version 3 of the License, or
//    (at your option) any later version.
//
//    wifiTunes is distributed in the hope that it will be useful,
//    but WITHOUT ANY WARRANTY; without even the implied warranty of
//    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//    GNU General Public License for more details.
//
//    You should have received a copy of the GNU General Public License
//    along with wifiTunes.  If not, see <http://www.gnu.org/licenses/>.

/**
/* Script Registrar from Simon Wilson 
*/
function addLoadEvent(func) {
	var oldonload = window.onload;
	if (typeof window.onload != 'function') {
		window.onload = func;
	} else {
		window.onload = function() {
			oldonload();
			func();
		}
	}
}

/** 
/* Event Listener des W3C
*/
function addEvent(obj, evType, fn, useCapture){
    if (obj.addEventListener){
        obj.addEventListener(evType, fn, useCapture);
        return true;
    } else if (obj.attachEvent){
        var retVal = obj.attachEvent("on"+evType, fn);
        return retVal;
    } else {
        return false;
    }
}

var Artist;
var TrackTitle;
var Album;

var ArtistScroll = false;
var TitleScroll = false;
var AlbumScroll = false;
var DoScroll = false;

var MobileSafari = false;
var Firefox = false;

addLoadEvent(init);
addLoadEvent(tracktime);
addLoadEvent(initrefresh);

function init () {
    window.scrollTo(0, 1);
    window.scrollTo(0, 0);
    setbottomsize();
    getscrollvalues();
    if (navigator.platform == "iPhone" || navigator.platform == "iPod") {
        document.getElementById('fingerarea').disabled = true;
        MobileSafari = true;
    }
    if (navigator.userAgent.search(/Firefox/) != -1) {
        //window.alert("Firefox")
        document.getElementById('fingerarea').addEventListener('DOMMouseScroll', setvolbar, false);
        Firefox = true;
    }
}

var starttime = 0;
function tracktime () {
    var jetzt = new Date();
    starttime = jetzt.getTime();
}

function initrefresh () {
    if (currentstate == "playing") {
        setInterval("setrefresh()", 1000);
    }
}

function gotourl (targeturl) {
    window.location.href = targeturl;
}

function getActualStyleById (ElementID, Property) {
    var PropertyValue
    var Element = document.getElementById(ElementID);
    if(Element.style[Property]) { 
        PropertyValue = Element.style[Property];
    }
    else if (window.getComputedStyle) { // Opera, Firefox, Safari
        PropertyValue = window.getComputedStyle( Element, "" ).getPropertyValue(Property);
    }
    else if(Element.currentStyle) { // IE
        PropertyValue = Element.currentStyle[Property];
    }
    else {
        // unsupported browser
        PropertyValue = "";
    }
    return PropertyValue;
}

function setbottomsize () {
    var middleheight = getActualStyleById ('middle','height').replace("px", "");
    //var middleheight = window.getComputedStyle( document.getElementById('middle'), "" ).getPropertyValue('height').replace("px", "");
    var topheight = getActualStyleById ('topbar','height').replace("px", "");
    //var topheight = window.getComputedStyle( document.getElementById('topbar'), "" ).getPropertyValue('height').replace("px", "");
    var bottombarheight = getActualStyleById ('bottombar','height').replace("px", "");
    //var bottombarheight = window.getComputedStyle( document.getElementById('bottombar'), "" ).getPropertyValue('height').replace("px", "");
    //if (middleheight == "auto") middleheight = 320; // if IE can't get the height assume 320
    if (middleheight == "auto") {
        middleheight = document.getElementById('middle').offsetHeight;
    }
    var bottomheight = 416 - topheight - middleheight;
    document.getElementById("bottom").style.height = bottomheight;
    //document.getElementById("bottom").style["height"] = bottomheight + "px";
    var fillerheight = bottomheight - bottombarheight;
    if (fillerheight < 0) fillerheight = 0; // avoid negative height, if something goes wrong
    document.getElementById("bottomfiller").style.height = fillerheight + "px";
    //document.getElementById("bottomfiller").style["height"] = fillerheight + "px";
}

var reloadid = 0;
var previousreloadtime = 1;
function setrefresh () {
    if (currentstate == "playing") {
        var jetzt = new Date();
        var currenttime = jetzt.getTime();
        runningsec = parseInt((currenttime - starttime) / 1000)
        currentposition = initialposition + runningsec;
        var reloadtime = (trackduration - currentposition + 1) * 1000;
        if (reloadtime < 0) reloadtime = 0;
        if (reloadid != 0) clearTimeout(reloadid);
        if (reloadtime == 0 && previousreloadtime == 0) { // avoid reload loop when wakeing up and connection is lost
        }
        else {
            //reloadid = setTimeout('window.location.href = "index.html"', reloadtime);
            reloadid = setTimeout('pagereload()', reloadtime);
            previousreloadtime = reloadtime;
        }
    }
}

function pagereload () {
    if ((outputsvisible && extendedinfosvisible) || volumeformvisible) {
        setTimeout('pagereload()', 1000);
    }
    else {
        window.location.href = "index.html";
    } 
}

var lasttime = 0;
function setcounters () {
    if (currentstate == "playing") {
        var jetzt = new Date();
        var currenttime = jetzt.getTime();
        runningsec = parseInt((currenttime - starttime) / 1000);
        currentposition = initialposition + runningsec;
        if (currentposition >= trackduration) currentposition = trackduration;
        //document.getElementById("playlist").firstChild.nodeValue = starttime;
    }
    else {
        currentposition = initialposition;
    }
    var posbarwidth = getActualStyleById('posbarbg', 'width').replace("px", "");
    //var posbarwidth = window.getComputedStyle( document.getElementById('posbarbg'), "" ).getPropertyValue('width').replace("px", "");
    var posbaractwidth = posbarwidth / trackduration * currentposition;
    document.getElementById("posbaract").style.width = posbaractwidth + "px";
    var remaining = trackduration - currentposition;
    var PosMin = parseInt(currentposition / 60);
    var PosSec = currentposition % 60;
    if (PosSec < 10) PosSec = "0" + PosSec;
    var RemMin = parseInt(remaining / 60);
    var RemSec = remaining % 60;
    if (RemSec < 10) RemSec = "0" + RemSec;
    document.getElementById("counterup").firstChild.nodeValue = PosMin + ":" + PosSec;
    document.getElementById("counterdown").firstChild.nodeValue = "-" + RemMin + ":" + RemSec;
}

var timerid;
var extendedinfosvisible = false;
function showextendedinfos () {
    var state;
    state = document.getElementById("extendedinfos").style.display;
    if (state != "inline") {
        state = "inline";
        if (currentstate == "playing") timerid = window.setInterval("setcounters()", 1000);
        extendedinfosvisible = true;
        if (volumeformvisible) showevolumeform();
    }
    else {
        state = "none";
        if (currentstate == "playing") window.clearInterval(timerid);
        extendedinfosvisible = false;
    }
    document.getElementById("extendedinfos").style.display = state;
    setcounters(); // iphone workaround. posbar has to be updated after made visible
}

var ajaxvolumeid;
var volumeformvisible = false;
function showvolumeform () {
    var state;
    state = document.getElementById("volumelayer").style.display;
    if (state != "inline") {
        state = "inline";
        ajaxvolumeid = window.setTimeout("ajaxsendvolume()", 0);
        volumeformvisible = true;
        if (extendedinfosvisible) showextendedinfos();
        ajaxgetvolume(); // set volume via ajax
        // TODO: perhaps wait until we got the volume before proceeding
    }
    else {
        state = "none";
        window.clearTimeout(ajaxvolumeid);
        volumeformvisible = false;
    }
    document.getElementById("volumelayer").style.display = state;
    updatevolbar(); // volbar has to be updated after made visible
}

var httpgetvol = null;
var httpgetvolgo = true;
function ajaxgetvolume () {
    if (httpgetvolgo) { // don't do if if we're busy
        httpgetvolgo = false;
        if (window.XMLHttpRequest) {
            httpgetvol = new XMLHttpRequest();
        } else if (window.ActiveXObject) {
            httpgetvol = new ActiveXObject("Microsoft.XMLHTTP");
        }
        if (httpgetvol != null) {
            httpgetvol.open("GET", "volume.html?cmd=getvol", true); // has to be async for firefox
            httpgetvol.onreadystatechange = getvolume;
            httpgetvol.send(null);
        }
    }
}

var currentvolume = 0;
function getvolume () {
    if( 4 == httpgetvol.readyState ) {
        if( 200 != httpgetvol.status ) {
            alert( "Fehler " + httpgetvol.status + ": " + httpgetvol.statusText );
        }
        else {
            currentvolume = httpgetvol.responseText;
            updatevolbar();
        }
        httpgetvolgo = true;
    }
}


var ArtistWidth;
var ArtistWidthDiff;
var TitleWidth;
var TitleWidthDiff;
var AlbumWidth;
var AlbumWidthDiff;
function getscrollvalues () {
    if (document.getElementById) {
        var TextMessung = document.getElementById('textmessung');

        var Artistfield = document.getElementById('artist');
        if (Artistfield.innerHTML != "") {
            Artist = Artistfield.firstChild.nodeValue;
        }
        else {
            Artist = "";
        }
        TextMessung.innerHTML = Artist;
        ArtistWidth = TextMessung.offsetWidth;
        TextMessung.innerHTML = '';
        var ArtistDivWidth = getActualStyleById('artist', 'width').replace("px", "");
        ArtistWidthDiff = ArtistWidth - ArtistDivWidth;
        if (ArtistWidth > ArtistDivWidth) {
            ArtistScroll = true;
        }
        else {
            ArtistScroll = false;
        }

        var Titlefield = document.getElementById('title');
        if (Titlefield.innerHTML != "") {
            TrackTitle = Titlefield.firstChild.nodeValue;
        }
        else {
            TrackTitle = "";
        }
        TextMessung.innerHTML = TrackTitle;
        TitleWidth = TextMessung.offsetWidth;
        TextMessung.innerHTML = '';
        var TitleDivWidth = getActualStyleById('title', 'width').replace("px", "");
        TitleWidthDiff = TitleWidth - TitleDivWidth;
        if (TitleWidth > TitleDivWidth) {
            TitleScroll = true;
        }
        else {
            TitleScroll = false;
        }

        var Albumfield = document.getElementById('album');
        if (Albumfield.innerHTML != "") {
            Album = Albumfield.firstChild.nodeValue;
        }
        else {
            Album = "";
        }
        TextMessung.innerHTML = Album;
        AlbumWidth = TextMessung.offsetWidth;
        TextMessung.innerHTML = '';
        var AlbumDivWidth = getActualStyleById('album', 'width').replace("px", "");
        AlbumWidthDiff = AlbumWidth - AlbumDivWidth;
        if (AlbumWidth > AlbumDivWidth) {
            AlbumScroll = true;
        }
        else {
            AlbumScroll = false;
        }
    }
}

var scrollid = 0;
var ArtistPosition = 0;
var ArtistWait = 0;
var TitlePosition = 0;
var TitleWait = 0;
var AlbumPosition = 0;
var AlbumWait = 0;
function scrollleft() {
    var pixelcount = 2;
    var timeout = 100;
    var WaitFactor = 7;

    if (ArtistScroll) {
        if (ArtistWait != 0) {
            ArtistWait = ArtistWait - 1;
            if (ArtistWait == 0) {
                if (ArtistPosition > ArtistWidthDiff) {
                    ArtistPosition = 0;
                    document.getElementById('artist').style.textIndent = "-" + ArtistPosition;
                    ArtistWait = WaitFactor;
                }
            }
        }
        else {
            ArtistPosition = ArtistPosition + pixelcount;
            if (ArtistPosition > ArtistWidthDiff) {
                ArtistWait = WaitFactor;
            }
            else {
                document.getElementById('artist').style.textIndent = "-" + ArtistPosition;
            }
        }
    }

    if (TitleScroll) {
        if (TitleWait != 0) {
            TitleWait = TitleWait - 1;
            if (TitleWait == 0) {
                if (TitlePosition > TitleWidthDiff) {
                    TitlePosition = 0;
                    document.getElementById('title').style.textIndent = "-" + TitlePosition;
                    TitleWait = WaitFactor;
                }
            }
        }
        else {
            TitlePosition = TitlePosition + pixelcount;
            if (TitlePosition > TitleWidthDiff) {
                TitleWait = WaitFactor;
            }
            else {
                document.getElementById('title').style.textIndent = "-" + TitlePosition;
            }
        }
    }
    
    if (AlbumScroll) {
        if (AlbumWait != 0) {
            AlbumWait = AlbumWait - 1;
            if (AlbumWait == 0) {
                if (AlbumPosition > AlbumWidthDiff) {
                    AlbumPosition = 0;
                    document.getElementById('album').style.textIndent = "-" + AlbumPosition;
                    AlbumWait = WaitFactor;
                }
            }
        }
        else {
            AlbumPosition = AlbumPosition + pixelcount;
            if (AlbumPosition > AlbumWidthDiff) {
                AlbumWait = WaitFactor;
            }
            else {
                document.getElementById('album').style.textIndent = "-" + AlbumPosition;
            }
        }
    }
    
    scrollid = window.setTimeout("scrollleft()", timeout);
}

function scrollinfos () {
    if (DoScroll) {
        DoScroll = false;
        if (scrollid != 0) window.clearTimeout(scrollid);
        if (ArtistScroll) scrollinfooff("artist");
        if (TitleScroll) scrollinfooff("title");
        if (AlbumScroll) scrollinfooff("album");
        ArtistPosition = 0;
        TitlePosition = 0;
        AlbumPosition = 0;

    }
    else {
        DoScroll = true;
        if (ArtistScroll) scrollinfoon("artist");
        if (TitleScroll) scrollinfoon("title");
        if (AlbumScroll) scrollinfoon("album");
        scrollid = window.setTimeout("scrollleft()", 50);
    }
}

function scrollinfoon (id) {
    var Element = document.getElementById(id);
    Element.style.textAlign = "left";
    Element.style.textIndent = "0px";
}

function scrollinfooff (id) {
    var Element = document.getElementById(id);
    Element.style.textAlign = "center";
    Element.style.textIndent = "0px";
}

function scrollinfos_old () {
    if (DoScroll) {
        DoScroll = false;
        if (ArtistScroll) removemarquee("artist");
        if (TitleScroll) removemarquee("title");
        if (AlbumScroll) removemarquee("album");
    }
    else {
        DoScroll = true;
        if (ArtistScroll) insertmarquee("artist");
        if (TitleScroll) insertmarquee("title");
        if (AlbumScroll) insertmarquee("album");
    }
}

function insertmarquee (id) {
    var Element = document.getElementById(id);
    var Marquee = document.createElement("marquee");
    var MarqueeText = document.createTextNode(Element.firstChild.nodeValue);
    Marquee.appendChild(MarqueeText);
    Element.replaceChild(Marquee, Element.firstChild);
    Element.firstChild.setAttribute("scrollamount", "4");
}

function removemarquee (id) {
    var Element = document.getElementById(id);
    var Text = document.createTextNode(Element.firstChild.firstChild.nodeValue);
    Element.replaceChild(Text, Element.firstChild);
}

function setvolbar (event) {
    if (Firefox) {
        difference = event.detail*-1;
    }
    else {
        difference = window.event.wheelDelta/150;
    }

    var tempvolume = currentvolume - (difference * volfactor);
    if (tempvolume > 100) {
        tempvolume = 100;
    }
    else if (tempvolume < 0) {
        tempvolume = 0;
    }
    currentvolume = tempvolume;

    updatevolbar();
}

function updatevolbar () {
    var volbarheight = getActualStyleById('volumebar', 'height').replace("px", "");
    var newheight = volbarheight / 100 * currentvolume;
    if (currentvolume > 0 && currentvolume <= 2) newheight = 0;
    else if (currentvolume > 2 && currentvolume <= 8) newheight = 14;
    else if (currentvolume > 8 && currentvolume <= 13) newheight = 27;
    else if (currentvolume > 13 && currentvolume <= 18) newheight = 37;
    else if (currentvolume > 18 && currentvolume <= 23) newheight = 49;
    else if (currentvolume > 23 && currentvolume <= 28) newheight = 63;
    else if (currentvolume > 28 && currentvolume <= 33) newheight = 72;
    else if (currentvolume > 33 && currentvolume <= 38) newheight = 84; 
    else if (currentvolume > 38 && currentvolume <= 43) newheight = 95;
    else if (currentvolume > 43 && currentvolume <= 48) newheight = 107;
    else if (currentvolume > 48 && currentvolume <= 53) newheight = 121;
    else if (currentvolume > 53 && currentvolume <= 58) newheight = 130;
    else if (currentvolume > 58 && currentvolume <= 63) newheight = 143;
    else if (currentvolume > 63 && currentvolume <= 68) newheight = 154;
    else if (currentvolume > 68 && currentvolume <= 73) newheight = 166;
    else if (currentvolume > 73 && currentvolume <= 78) newheight = 180;
    else if (currentvolume > 78 && currentvolume <= 83) newheight = 190;
    else if (currentvolume > 83 && currentvolume <= 88) newheight = 202;
    else if (currentvolume > 88 && currentvolume <= 93) newheight = 212;
    else if (currentvolume > 93 && currentvolume <= 97) newheight = 224;
    else if (currentvolume > 97 && currentvolume <= 100) newheight = volbarheight;
    document.getElementById('volumebaract').style.height = parseInt(String(newheight)) + "px";
    //document.getElementById('volumebarinact').style.height = parseInt(String(volbarheight - newheight)) + "px";
}

var volfactor = 1;
function reversevol () {
    volfactor = -1;
}

function normalvol () {
    volfactor = 1;
}

var oldvolume = 0;
function ajaxsendvolume () {
    if (currentvolume != oldvolume) {
        var AjaxString = parseInt(String(currentvolume));
        var http = null;
        if (window.XMLHttpRequest) {
           http = new XMLHttpRequest();
        } else if (window.ActiveXObject) {
           http = new ActiveXObject("Microsoft.XMLHTTP");
        }
        if (http != null) {
           http.open("GET", "volume.html?cmd=vol&vol=" + AjaxString, true); // has to be async for firefox
           http.onreadystatechange = function () {void(0)};
           http.send(null);
        }
    }
    oldvolume = currentvolume;
    ajaxvolumeid = window.setTimeout("ajaxsendvolume()", 300);
}

function ajaxsendposition (event, Sender) {
    if (currentstate == "playing") {
        var posbarwidth = getActualStyleById('posbarbg', 'width').replace("px", "");
        //var posbarwidth = window.getComputedStyle( document.getElementById('posbarbg'), "" ).getPropertyValue('width').replace("px", "");
        var Offset = 0;
        if (!event.offsetX) { // Firefox
            // get left position of element
            var CurrentObject = Sender;
            var ElementOffset = 0;
            while (CurrentObject) {
                ElementOffset = ElementOffset + CurrentObject.offsetLeft;
                CurrentObject = CurrentObject.offsetParent;
            }
            // calculate offset within element
            Offset =  event.pageX - ElementOffset;
        } // others
        else {
            Offset = event.offsetX;
        }
        var newposition = trackduration / posbarwidth * Offset;
        initialposition = parseInt(String(newposition));
        tracktime();
        var AjaxString = initialposition;
        
        var http = null;
        if (window.XMLHttpRequest) {
            http = new XMLHttpRequest();
        } else if (window.ActiveXObject) {
            http = new ActiveXObject("Microsoft.XMLHTTP");
        }
        if (http != null) {
            http.open("GET", "position.html?cmd=pos&pos=" + AjaxString, true); // has to be async for firefox
            http.onreadystatechange = function () {void(0)};
            http.send(null);
        }
        setcounters();
        setrefresh();
    }
}

function setview () {
    if (MobileSafari) {
        window.scrollTo(0, 1);
        window.scrollTo(0, 0);
    }
}

var outhttp = null;
var outhttpgo = true;
function ajaxgetoutputs () {
    if (outhttpgo) { // don't run if we're still busy
        outhttpgo = false;
        if (window.XMLHttpRequest) {
            outhttp = new XMLHttpRequest();
        } else if (window.ActiveXObject) {
            outhttp = new ActiveXObject("Microsoft.XMLHTTP");
        }
        if (outhttp != null) {
            outhttp.open("GET", "outputs.html?cmd=getout", true); // has to be async for firefox
            outhttp.onreadystatechange = insertoutputs;
            outhttp.send(null);
        }
    }
}

var outputsvisible = false;
function insertoutputs () {
    if( 4 == outhttp.readyState ) {
        if (outhttp.status == 204) {
            alert("Not available");
        }
        else if( outhttp.status != 200 ) {
            alert( "Error. Status: " + outhttp.status + " / " + outhttp.statusText );
        }
        else {
            //var ResultXml = outhttp.responseXML;
            var TopDiv = document.getElementById('outputselect');
            var TopDivParent = TopDiv.parentNode;
            var NewOutSel = document.createElement("div");
            var IdAttr = document.createAttribute("id");
            IdAttr.nodeValue = "outputselect";
            NewOutSel.setAttributeNode(IdAttr);
            var Outputs = outhttp.responseXML.getElementsByTagName("output");
            var CountOfElements = Outputs.length;
            if (CountOfElements > 1) {
                // first element is assumed to be the computer
                var ThisOutputDiv = document.createElement("div");
                var idAttr = document.createAttribute("id");
                idAttr.nodeValue = "outputbuttoncomputer";
                ThisOutputDiv.setAttributeNode(idAttr);
                var clickAttr = document.createAttribute("onclick");
                //clickAttr.nodeValue = "setaoutput(\'" + Outputs[0].textContent + "\')";
                clickAttr.nodeValue = "setaoutput(\'1\')";
                ThisOutputDiv.setAttributeNode(clickAttr);
                //var ThisTextNode = document.createTextNode(Outputs[0].textContent);
                var ThisTextNode = document.createTextNode(Outputs[0].firstChild.nodeValue);
                ThisOutputDiv.appendChild(ThisTextNode);
                NewOutSel.appendChild(ThisOutputDiv);
                // remaining elements are airtunes outputs
                for (var i = 1 ; i < CountOfElements ; i++) {
                    var ThisOutputDiv = document.createElement("div");
                    var classAttr = document.createAttribute("class");
                    classAttr.nodeValue = "outputbuttonairtunes";
                    ThisOutputDiv.setAttributeNode(classAttr);
                    var clickAttr = document.createAttribute("onclick");
                    //clickAttr.nodeValue = "setaoutput(\'" + Outputs[i].textContent + "\')";
                    var OutputNumber = i + 1;
                    clickAttr.nodeValue = "setaoutput(\'" + OutputNumber + "\')";
                    ThisOutputDiv.setAttributeNode(clickAttr);
                    //var ThisTextNode = document.createTextNode(Outputs[i].textContent);
                    var ThisTextNode = document.createTextNode(Outputs[i].firstChild.nodeValue);
                    ThisOutputDiv.appendChild(ThisTextNode);
                    NewOutSel.appendChild(ThisOutputDiv);
                }
                TopDivParent.replaceChild(NewOutSel, TopDiv);
                outputsvisible = true;
            }
            else {
                alert("No remote speakers")
            }
        }
        outhttpgo = true;
    }
}

var setouthttp = null;
var setouthttpgo = true;
function setaoutput(outputName) {
    if (setouthttpgo) { // don't do it we're still busy
        setouthttpgo = false;
        if (window.XMLHttpRequest) {
            setouthttp = new XMLHttpRequest();
        } else if (window.ActiveXObject) {
            setouthttp = new ActiveXObject("Microsoft.XMLHTTP");
        }
        if (setouthttp != null) {
            setouthttp.open("GET", "outputs.html?cmd=setout&name=" + outputName, true); // has to be async for firefox
            setouthttp.onreadystatechange = resetoutputselect;
            setouthttp.send(null);
        }
    }
}

function resetoutputselect () {
    if( 4 == setouthttp.readyState ) {
        if( 200 != setouthttp.status ) {
            alert( "Fehler " + setouthttp.status + ": " + setouthttp.statusText );
        }
        else {
            var TopDiv = document.getElementById('outputselect');
            var TopDivParent = TopDiv.parentNode;
            var NewOutSel = document.createElement("div");
            var IdAttr = document.createAttribute("id");
            IdAttr.nodeValue = "outputselect";
            NewOutSel.setAttributeNode(IdAttr);
            TopDivParent.replaceChild(NewOutSel, TopDiv);
            outputsvisible = false;
        }
        setouthttpgo = true;
    }
}


