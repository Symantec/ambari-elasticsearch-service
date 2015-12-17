#!/usr/bin/env python
"""
Elasticsearch service checks.

"""
from __future__ import print_function
from resource_management import *
import  sys,subprocess,os
import requests
import time

class ServiceCheck(Script):
    def service_check(self, env):
        import params
        env.set_params(params)

	print("Running Elastic search  service check", file=sys.stdout)
        # There is a race condition by the time the BDSE server starts and service checks.  Hence added the below sleep for 20 seconds
        time.sleep(20)
    	payload = {'name': 'Buddy.  Dont Worry, I am Fine '} 
	r = requests.get('http://localhost:9200/',params=payload) 

        if r.status_code == 200:
	    print(r.json(), file=sys.stdout)
            sys.exit(0)
        else:
	    print("Elastic service is not running", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    ServiceCheck().execute()
