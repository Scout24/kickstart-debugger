#!/usr/bin/python
'''\
Kickstart Debugger, written by Schlomo Schapiro.
Licensed under the <a href="http://www.gnu.org/licenses/gpl.html">GNU General Public License</a>.

The favicon.ico is taken from the XFCE project.
'''

__version__ = "$Id$"


import base64

# remember to use %% and \\ instead of % and \ !
builtinPages = {
                "/" : u'''\
<html><head><title>%(host)s - Kickstart Debugger</title>
<script language="javascript" type="text/javascript">
    
function scrollToBottom(el) {
    var l=document.getElementById(el);
    l.contentWindow.scrollTo(0,10000000000000);
    l.height=window.innerHeight-l.offsetTop-20;
}

function loadInContentPanel(uri, legend) {
    var el = document.getElementById('contentpanel');
    if (el != null) {
        var h = window.innerHeight - 100;
        el.innerHTML = "<legend>" + legend + "</legend><iframe id='contentframe' onload='scrollToBottom(\\"contentframe\\")' frameborder='0' height='" + h + "' width='100%%' src='" + uri + "'/>";
    }
    return(false);
}

</script>

</head>
<body>
    <h1>%(host)s - Kickstart Debugger</h1>
        <div style="float: left; width: 20%%;">
        <fieldset><legend>What do you want to see?</legend>
            <p><ul>
                %(screenshotLink)s
                <li><a onclick="return loadInContentPanel('/fs/tmp/ks.cfg','Kickstart File')" href="/fs/tmp/ks.cfg">kickstart file</a></li>

                <li><a onclick="return loadInContentPanel('/fs/mnt/sysimage/root/ks-post.log','Kickstart %%post Script Log')" href="/fs/mnt/sysimage/root/ks-post.log">%%post log</a></li>
                <li><a onclick="return loadInContentPanel('/fs/tmp/anaconda.log','Anaconda log file')" href="/fs/tmp/anaconda.log">anaconda.log</a></li>
                <li><a onclick="return loadInContentPanel('/fs/tmp/','Browse Installation System (<code>/tmp</code>)')" href="/fs/tmp/">/tmp of Installation System</a></li>
                <li><a onclick="return loadInContentPanel('/fs/mnt/sysimage/','Browse Installed System (<code>/mnt/sysimage</code>)')" href="/fs/mnt/sysimage/">Installed Root Filesystem</a></li>
            </ul></p>
        </fieldset>
        <fieldset><legend>Downloads:</legend>

            <p><ul>
                <li><a href="/download/tmp/ks.cfg">kickstart file</a></li>
                <li><a href="/download/mnt/sysimage/root/ks-post.log">Kickstart %%post log</a></li>
                <li><a href="/download/tmp/anaconda.log">anaconda.log</a></li>
                <li><a href="/download/tmp">/tmp of Installation System</a></li>
                <li><a href="/download/mnt/sysimage/root">Installed Root Filesystem (/root)</a></li>

            </ul></p>
        </fieldset>
    </div>
    <div id="logframe" style="float: right; width: 80%%;">
        <fieldset id="contentpanel" style="border: 2px solid grey;"><legend>Content</legend>
            <h2 style="color:red">%(error)s</h2>
            <p>Click on a link at the left to display the content here</p>
        </fieldset>
    </div>

    <hr/>
    <i style="font-size: 80%%">Kickstart Debugger, written by Schlomo Schapiro. Licensed under the <a href="http://www.gnu.org/licenses/gpl.html">GNU General Public License</a>. See my <a href="http://blog.schlomo.schapiro.org">BLOG</a> for news and updates.</i>
</body>
</html>
                ''',
                "/screenshot" : u'''\
<html>
<head><title>%(host)s - Kickstart Debugger Screenshot</title>
</head>
<body>
<img style="cursor:pointer;" onclick="this.src=this.src;" src="%(screenshotUrl)s"/>
</body>
</html>
                ''',
                "/favicon.ico.mimetype":"image/icon",
                "/favicon.ico":base64.decodestring('''\
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
P+EA+H/zAP///wA=''',
)}

# ignore popen2 deprecation warning
import warnings
warnings.filterwarnings("ignore")

import SimpleHTTPServer
import os
import posixpath
import BaseHTTPServer
import urllib
import cgi
import shutil
import string
import mimetypes
import popen2
import socket
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

class KickstartDebuggerRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    server_name= socket.gethostname()
    extensions_map = {
        '' : 'application/octet-stream', # default mime type
        '.log': 'text/plain',
        '.cfg': 'text/plain',
        '.ks': 'text/plain',
        '.txt': 'text/plain',
        }

    def list_directory(self, path):
        """Helper to produce a directory listing (absent index.html).

        Return value is either a file object, or None (indicating an
        error).  In either case, the headers are sent, making the
        interface the same as for send_head().

        """
        try:
            list = os.listdir(path)
        except os.error:
            self.send_error(404, "No permission to list directory")
            return None
        list.sort(key=lambda a: a.lower())
        f = StringIO()
        displaypath = cgi.escape(urllib.unquote(self.path))
        f.write('<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">')
        f.write("<html>\n<title>Directory listing for %s</title>\n" % displaypath)
        f.write("<body>\n<h2>Directory listing for %s</h2>\n" % displaypath)
        f.write("<hr>\n<table border=0>\n<tr><td colspan='2'><a href='../'>../<a></td></tr>\n")
        for name in list:
            linkHtml=""
            fullname = os.path.join(path, name)
            displayname = linkname = name
            # Append / for directories or @ for symbolic links
            if os.path.isdir(fullname):
                displayname = name + "/"
                linkname = name + "/"
            if os.path.islink(fullname):
                displayname = name + "@"
                linkHtml = "<br/>&nbsp;&nbsp;&rarr;&nbsp;<small>%s</small>" % os.path.realpath(fullname)
                # Note: a link to a directory displays with @ and links with /
            f.write('<tr valign="top"><td><a href="%s">%s</a>%s</td><td align="right">%d</td></tr>\n'
                    % (urllib.quote(linkname), cgi.escape(displayname), linkHtml, os.path.getsize(fullname)))
        f.write("</table>\n<hr>\n</body>\n</html>\n")
        length = f.tell()
        f.seek(0)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", str(length))
        self.end_headers()
        return f
    
    def getReplacements(self):
        '''Build a dictionary with some data that can be used in builtinPages '''
        replacements = {}
        replacements["host"] = KickstartDebuggerRequestHandler.server_name
        replacements["screenshotUrl"] = options.screenshotUrl
        if options.screenshotUrl:
            replacements["screenshotLink"] = '''<li><a onclick="return loadInContentPanel('/screenshot','Screenshot')" href="/screenshot">Screenshot</a></li>'''
        else:
            replacements["screenshotLink"] = ""
        replacements["error"] = ""
        error_file = "/dev/kickstart_debugger_error.txt"
        if os.path.isfile(error_file):
            f = None
            try:
                f = open(error_file)
                replacements["error"] = f.read()
            finally:
                if f:
                    f.close()
                else:
                   replacements["error"] = "Could not read from <code>%s</code>!" % error_file
        return replacements
    
    def do_GET(self,onlyHeaders = False):
        '''Serve a GET request'''
        f = None
        f_in = None
        # disable caching, found in http://stackoverflow.com/questions/49547/making-sure-a-web-page-is-not-cached-across-all-browsers
        if self.path in builtinPages:
            f = StringIO()
            f.write(builtinPages[self.path] % self.getReplacements())
            length = f.tell()
            f.seek(0)
            self.send_response(200)
            if self.path+".mimetype" in builtinPages:
                self.send_header("Content-type",builtinPages[self.path+".mimetype"])
            else:
                self.send_header("Content-type", "text/html")
            self.send_header("Content-Length", str(length))
            self.end_headers()        
        
        elif self.path.startswith("/fs"):
            self.path=self.path[3:] # strip leading /fs to map /fs to real /

        elif self.path.startswith("/download"):
            self.path=self.path[9:] # strip leading /download to map /download to real /
            try:
                isFile=False
                downloadSuffix = ""
                if os.path.isfile(self.path):
                    isFile=True
                    f = open(self.path)
            
                elif os.path.isdir(self.path):
                    downloadSuffix = ".tar.gz"
                    # not using builtin tarfile module because python 2.4 tarfile does not support add with exclusions
                    # also, I am not sure if the tarfile module would do real streaming of the resulting tar.gz or assemble it in memory
                    (f,f_in) = popen2.popen2("tar -C / -cz --ignore-failed-read --exclude \"*.img\" \"%s\"" % self.path[1:]) # skip leading /
                    f_in.close()
                else:
                    raise IOError("not a file and not a dir")
                
                self.send_response(200)
                self.send_header("Content-type", "application/octet-stream")
                # set filename to be like HOSTNAME_path_to_file.txt
                self.send_header("Content-Disposition:", "attachment; filename=\"%s%s\"" % (KickstartDebuggerRequestHandler.server_name, (string.replace(self.path,"/","_") + downloadSuffix)))
                if isFile:
                    self.send_header("Content-Length", str(os.path.getsize(self.path)))
                self.end_headers()
            except IOError ,e:
                self.send_error(404,"No permission or error while opening " + self.path + ": " + str(e))
                return None
                    

        if not f:       
            # default action from super class if no file set
            f = self.send_head()
            
        if f:
            if not onlyHeaders:
                self.copyfile(f, self.wfile)
            f.close()          

    def do_HEAD(self):
        """Serve a HEAD request."""
        self.doGET(True)
        
    def end_headers(self):
        """Send standard headers and end header sending"""
        self.send_header("Cache-Control","no-cache, no-store, must-revalidate")
        self.send_header("Pragma","no-cache")
        self.send_header("Expires:","0")
        SimpleHTTPServer.SimpleHTTPRequestHandler.end_headers(self)
        
if __name__ == "__main__":
    usage='''Kickstart Debugger is a simple web tool meant to run inside a kickstart/anaconda
installation system.'''
    import optparse
    import sys
    import SocketServer


    parser = optparse.OptionParser(usage=usage,version=__version__)
    parser.add_option("-p","--port",dest="listenPort",default="80",type="int",metavar="PORT",help="Listening port for web server [%default]")
    parser.add_option("-s","--screenshot",dest="screenshotUrl",default="",type="string",metavar="SCREENSHOT",help="URL to screenshot")
    options, arguments = parser.parse_args()

    os.chdir("/")        
    httpd = SocketServer.TCPServer(("", options.listenPort), KickstartDebuggerRequestHandler)

    #KickstartDebuggerRequestHandler.server_name = socket.gethostname()
    print "Starting Kickstart Debugger on port %s" % options.listenPort
    httpd.serve_forever()
