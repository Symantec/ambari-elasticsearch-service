#!/usr/bin/env python
"""
elasticsearch service params.

"""

from resource_management import *
from properties_config import properties_config
import sys
from copy import deepcopy

def slave():
    import params

    params.path_data = params.path_data.replace('"','')
    data_path = params.path_data.replace(' ','').split(',')
    data_path[:]=[x.replace('"','') for x in data_path]
    
    directories = [params.log_dir, params.pid_dir, params.conf_dir]
    directories = directories+data_path;
    
    Directory(directories,
              owner=params.elastic_user,
              group=params.elastic_user,
              recursive=True
          )
    
    File(format("{conf_dir}/elastic-env.sh"),
          owner=params.elastic_user,
          content=InlineTemplate(params.elastic_env_sh_template)
     )

    configurations = params.config['configurations']['elastic-site']

    File(format("{conf_dir}/elasticsearch.yml"),
       content=Template(
                        "elasticsearch.slave.yaml.j2",
                        configurations = configurations),
       owner=params.elastic_user,
       group=params.elastic_user
    )
    
    File(format("/etc/sysconfig/elasticsearch"),
       content=Template(
                        "elasticsearch.sysconfig.j2",
                        configurations = configurations),
       owner="root",
       group="root"
    )
