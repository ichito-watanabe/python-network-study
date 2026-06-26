import sys
import subprocess

subprocess.run(["git", "clone", "https://github.com/flyby-yunakayama/network-simulator.git"])
sys.path.insert(0, "network-simulator")

from sec1.NetworkGraph import NetworkGraph
from sec1.Node import Node
from sec1.Link import Link
from sec1.Packet import Packet

network_graph = NetworkGraph()


node1 = Node(node_id = 1, address = "00:01", network_graph = network_graph)
node2 = Node(node_id = 2, address = "00:02", network_graph = network_graph)
node3 = Node(node_id = 3, address = "00:03", network_graph = network_graph)


link1 = Link(node1,node2,network_graph = network_graph)
link2 = Link(node2,node3,network_graph = network_graph)
link3 = Link(node1,node3,network_graph = network_graph)

packet = Packet(source = node1.address, destination = node2.address, payload = "hello2")
packet2 = Packet(source = node2.address, destination = node3.address, payload = "hello3")
packet3 = Packet(source = node3.address, destination = node1.address, payload = "hello1")

network_graph.draw()
