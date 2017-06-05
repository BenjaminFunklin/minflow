"""
No need to change anything here!

If all goes well, this should work after you
modify the Add class in miniflow.py.
"""

from miniflow import *

x, y, z = Input(), Input(), Input()

f = Add(x, y, z)
print (f.inbound_nodes[0].value,"f inbound nodes")
feed_dict = {x: 4, y: 5, z: 10}

# inside of topo_sort is where the magic happens 
# topo_sort calls
graph = topological_sort(feed_dict)
print (f.inbound_nodes[0].value,"f's inbound NODEEE at 0 and x's value",x.value)

output = forward_pass(f, graph)
print (f.inbound_nodes[1].value,"x's inbound NODEEE",x.value)

# should output 19
print("{} + {} + {} = {} (according to miniflow)".format(feed_dict[x], feed_dict[y], feed_dict[z], output))
