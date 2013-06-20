# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
# You can run this .tac file directly with:
#    twistd -ny service.tac

"""
This is an example .tac file which starts a webserver on port 8080 and
serves files from the current working directory.

The important part of this, the part that makes it a .tac file, is
the final root-level section, which sets up the object called 'application'
which twistd will look for
"""

import os
from twisted.application import service, internet
from twisted.web import static, server
from MetricsJsonResource import RootResource

def getWebService():
    """
    Return a service suitable for creating an application object.
    """
    # create a resource to serve static files
    root = RootResource()
    rootServer = server.Site(root)
    return internet.TCPServer(8080, rootServer)

# this is the core part of any tac file, the creation of the root-level
# application object
application = service.Application("Demo application")

# attach the service to its parent application
service = getWebService()
service.setServiceParent(application)
