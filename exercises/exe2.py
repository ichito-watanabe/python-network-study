import sys
import subprocess

subprocess.run(["git", "clone", "https://github.com/flyby-yunakayama/network-simulator.git"])
sys.path.insert(0, "network-simulator")

from sec2.Node import Node
from sec2.Link import Link
from sec2.NetworkEventScheduler import NetworkEventScheduler


network_event_scheduler = NetworkEventScheduler(log_enabled = True, verbose = True)
node_1 = Node(node_id = 1, address = "00:01", network_event_scheduler = network_event_scheduler)
node_2 = Node(node_id = 2, address = "00:02", network_event_scheduler = network_event_scheduler)

link1 = Link(node_1,node_2,bandwidth = 10000, delay = 0.001, loss_rate = 0.0, network_event_scheduler = network_event_scheduler)

header_size = 40
payload_size = 85
node_1.set_traffic(destination = "00:02",bitrate = 1000, start_time = 1.0 , duration = 10.0, burstiness =1.0,header_size =  header_size, payload_size = payload_size)

network_event_scheduler.run()

network_event_scheduler.generate_throughput_graph(network_event_scheduler.packet_logs)
network_event_scheduler.generate_delay_histogram(network_event_scheduler.packet_logs)