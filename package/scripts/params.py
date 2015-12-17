#!/usr/bin/env python
"""
Elasticsearch Params configurations
"""

from resource_management.libraries.functions.version import format_hdp_stack_version, compare_versions
from resource_management import *
import status_params

# server configurations
config = Script.get_config()

elastic_home = '/etc/elasticsearch/'
elastic_bin = '/usr/share/elasticsearch/bin/'

conf_dir = "/etc/elasticsearch"
elastic_user = config['configurations']['elastic-env']['elastic_user']
user_group = config['configurations']['elastic-env']['user_group']
log_dir = config['configurations']['elastic-env']['elastic_log_dir']
pid_dir = '/var/run/elasticsearch'
pid_file = '/var/run/elasticsearch/elasticsearch.pid'
hostname = config['hostname']
java64_home = config['hostLevelParams']['java_home']
elastic_env_sh_template = config['configurations']['elastic-env']['content']

cluster_name = config['configurations']['elastic-site']['cluster_name']
seed_node1 = config['configurations']['elastic-site']['seed_node1']
seed_node2 = config['configurations']['elastic-site']['seed_node2']
seed_node3 = config['configurations']['elastic-site']['seed_node3']

path_data = config['configurations']['elastic-site']['path_data']
http_port = config['configurations']['elastic-site']['http_port']
transport_tcp_port = config['configurations']['elastic-site']['transport_tcp_port']

recover_after_time = config['configurations']['elastic-site']['recover_after_time']
recover_after_data_nodes = config['configurations']['elastic-site']['recover_after_data_nodes']
expected_data_nodes = config['configurations']['elastic-site']['expected_data_nodes']
discovery_zen_ping_multicast_enabled = config['configurations']['elastic-site']['discovery_zen_ping_multicast_enabled']
index_merge_scheduler_max_thread_count = config['configurations']['elastic-site']['index_merge_scheduler_max_thread_count']
index_translog_flush_threshold_size = config['configurations']['elastic-site']['index_translog_flush_threshold_size']
index_refresh_interval = config['configurations']['elastic-site']['index_refresh_interval']
index_store_throttle_type = config['configurations']['elastic-site']['index_store_throttle_type']
index_number_of_shards = config['configurations']['elastic-site']['index_number_of_shards']
index_number_of_replicas = config['configurations']['elastic-site']['index_number_of_replicas']
index_buffer_size = config['configurations']['elastic-site']['index_buffer_size']
mlockall = config['configurations']['elastic-site']['mlockall']
threadpool_bulk_queue_size = config['configurations']['elastic-site']['threadpool_bulk_queue_size']
cluster_routing_allocation_node_concurrent_recoveries = config['configurations']['elastic-site']['cluster_routing_allocation_node_concurrent_recoveries']
cluster_routing_allocation_disk_watermark_low = config['configurations']['elastic-site']['cluster_routing_allocation_disk_watermark_low']
cluster_routing_allocation_disk_threshold_enabled = config['configurations']['elastic-site']['cluster_routing_allocation_disk_threshold_enabled']
cluster_routing_allocation_disk_watermark_high = config['configurations']['elastic-site']['cluster_routing_allocation_disk_watermark_high']
indices_fielddata_cache_size = config['configurations']['elastic-site']['indices_fielddata_cache_size']
indices_cluster_send_refresh_mapping = config['configurations']['elastic-site']['indices_cluster_send_refresh_mapping']
threadpool_index_queue_size = config['configurations']['elastic-site']['threadpool_index_queue_size']

discovery_zen_ping_timeout = config['configurations']['elastic-site']['discovery_zen_ping_timeout']
discovery_zen_fd_ping_interval = config['configurations']['elastic-site']['discovery_zen_fd_ping_interval']
discovery_zen_fd_ping_timeout = config['configurations']['elastic-site']['discovery_zen_fd_ping_timeout']
discovery_zen_fd_ping_retries = config['configurations']['elastic-site']['discovery_zen_fd_ping_retries']

network_host = config['configurations']['elastic-site']['network_host']