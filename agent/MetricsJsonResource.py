# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
from twisted.web import server, resource
from CPUMetrics import CPUResource
import linux_metrics as lm

class RootResource(resource.Resource):
    numberRequests = 0
    child_rec = {}

    def __init__(self):
        resource.Resource.__init__(self)
        print "initing root resource"
        self.child_rec['cpu_utilization'] = CPUResource()
        for path in self.child_rec:
            self.putChild(path, self.child_rec[path])

    def getChild(self, path, request):
        if path == "":
            return self
        if path in self.children:
            return self.children[path]
        return resource.NoResource()
        
    
    def render_GET(self, request):
        self.numberRequests += 1
        request.setHeader("content-type", "text/plain")
        res = "I am request #" + str(self.numberRequests) + "\n"
        for path in self.child_rec:
            res += path + ": " + self.child_rec[path].description + "\n"
        return res

