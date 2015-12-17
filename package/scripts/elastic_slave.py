"""
Elastic service script.

"""

from resource_management import *
import signal
import sys
import os
from os.path import isfile

from slave  import slave


class Elasticsearch(Script):
    def install(self, env):
        import params
        env.set_params(params)
        print 'Install the Slave'
        self.install_packages(env)
    def configure(self, env):
        import params
        env.set_params(params)
        slave()   
    def stop(self, env):
        import params
        env.set_params(params)
        stop_cmd = format("service elasticsearch stop")
        Execute(stop_cmd)
        print 'Stop the Slave'
    def start(self, env):
        import params
        env.set_params(params)
        self.configure(env)
        start_cmd = format("service elasticsearch start")
        Execute(start_cmd)
        print 'Start the Slave'
    def status(self, env):
        import params
        env.set_params(params)
        status_cmd = format("service elasticsearch status")
        Execute(status_cmd)
        print 'Status of the Slave'
if __name__ == "__main__":
    Elasticsearch().execute()


