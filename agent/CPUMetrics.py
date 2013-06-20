# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
from twisted.web import resource
import json
import linux_metrics as lm

class CPUResource(resource.Resource):
    isLeaf = True
    description = 'CPU utilization'

    def render_GET(self, request):
        cpu_pcts = lm.cpu_stat.cpu_percents(sample_duration=1)
        cpu_times = lm.cpu_stat.cpu_times()
        load_avgs = lm.cpu_stat.load_avg()

        cpu = { 'times':cpu_times, 'load':cpu_pcts, 'load_avg':load_avgs }
        return json.dumps(cpu)


