#!/usr/bin/env python
"""
Elasticsearch  service params

"""

from resource_management import *

config = Script.get_config()

elastic_pid_dir = config['configurations']['elastic-env']['elastic_pid_dir']
elastic_pid_file = format("{elastic_pid_dir}/elasticsearch.pid")
