import networkx as nx
# seed=1208           # seed the graph for reproducibility, you should be doing this  
# G = nx.erdos_renyi_graph (100, .025, seed=seed )       # here we create a random binomial graph with 10 nodes and an average (expected) connectivity of 10*.3= 3.
seed=1000           # seed the graph for reproducibility, you should be doing this  
G = nx.erdos_renyi_graph (10, .3, seed=seed )       # here we create a random binomial graph with 10 nodes and an average (expected) connectivity of 10*.3= 3.
print ( G.nodes() )

nx.is_connected(G)      # check whether which has at least one path between each pair of nodes. 
print(G.edges())

# **************************************************************************************************************************************************************

import matplotlib.pyplot as plt
import time

cust_queue = []
tot_num_cust = 0

# test shortest path
path_test = find_shortest_path(2, 9)
# print(path_test)

# create the list of vans
van_list = {"location": 2, "path": [], "cust": [], "new_cust": 0}
van_list["path"] = path_test

# create 35 to 40 initial customers in queue
add_to_queue(cust_queue, tot_num_cust)

# set node colors
color_map = ["green"] * len(G)
for van in van_list:
  color_map[van_list["location"]] = "red"

# get list of edges and node positions
links = [(u, v) for (u, v, d) in G.edges(data=True)]
pos = nx.nx_pydot.graphviz_layout(G) 

# create a loop that tracks the vans by changing the color of the current node they are on
# vans travel 30 mph
# distance between nodes is 1 mile
# to speed up time, vans will travel 1 mile every 2 seconds
count = 0
while van_list["path"]:
  # plt.clf()
  color_map[van_list["location"]] = "green"
  i = van_list["path"].pop(0)
  van_list["location"] = i
  color_map[van_list["location"]] = "red"
  nx.draw_networkx_nodes(G, pos, node_size=200, node_color=color_map, linewidths=0.25)
  nx.draw_networkx_edges(G, pos, edgelist=links, width=2)
  nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")
  plt.show()
  time.sleep(2)
  count += 2
  if count == 4:
    add_to_queue(cust_queue, tot_num_cust)
    count = 0
  
# display graph
# nx.draw(G, node_color=color_map, with_labels=True)
# plt.show()

# **************************************************************************************************************************************************************

def add_cust_to_vans():
  # CASE 1: one customer added to van queue
# van path queue is empty
if not van_list["path"]:
    # calculate from vans current location to customer pickup
    temp_list = find_shortest_path(van_curr_location, customer pickup location)
    temp_list.pop(0)
    van_list["path"] += temp_list
# van path queue is not empty
else:
    temp_list = find_shortest_path(van_final_location, customer pickup location)
    temp_list.pop(0)
    van_list["path"] += temp_list

# CASE 2: two customers added to van queue
# van path queue is empty
if not van_list["path"]:
    distance1 = find_path_length(van curr location, cust1 pickup)
    distance2 = find_path_length(van curr location, cust2 pickup)

    if distance1 < distance2:
        # calculate from cust1 pickup to cust1 dropoff
        # calculate from cust1 dropoff to cust2 pickup
        # calculate from cust1 pickup to cust2 pickup
        distance3 = find_path_length(cust1 pickup, cust1 dropoff)
        distance4 = find_path_length(cust1 dropoff, cust2 pickup)
        distance5 = find_path_length(cust1 pickup, cust2 pickup)

        if(distance3 + distance4) <= distance5:
            # dropoff cust1, then pickup cust2 //OP more detailed psuedocode
            #OP pickup customer 1
            temp_list = find_shortest_path(van_curr_location, cust1 pickup location)
            temp_list.pop(0)
            van_list["path"] += temp_list
            #OP dropoff customer 1
            temp_list = find_shortest_path(cust1 pickup location, cust1 dropoff location)
            temp_list.pop(0)
            van_list["path"] += temp_list
            #OP pickup customer 2
            temp_list = find_shortest_path(cust1 dropoff location, cust2 pickup location)
            temp_list.pop(0)
            van_list["path"] += temp_list
            #OP dropoff customer 2
            temp_list = find_shortest_path(cust2 pickup location, cust2 dropoff location)
            temp_list.pop(0)
            van_list["path"] += temp_list

        else:
            # pickup cust1, then pickup cust2 //OP more detailed pseudocode
            #OP pickup customer 1
            temp_list = find_shortest_path(van_curr_location, cust1 pickup location)
            temp_list.pop(0)
            van_list["path"] += temp_list
            #OP pickup customer 2
            temp_list = find_shortest_path(cust1 pickup location, cust2 pickup location)
            temp_list.pop(0)
            van_list["path"] += temp_list
            #OP dropoff customer 1
            temp_list = find_shortest_path(cust2 pickup location, cust1 dropoff location)
            temp_list.pop(0)
            van_list["path"] += temp_list
            #OP dropoff customer 2
            temp_list = find_shortest_path(cust1 dropoff location, cust2 dropoff location)
            temp_list.pop(0)
            van_list["path"] += temp_list

    else:
        # distance2 < distance1
        # calculate from cust2 pickup to cust2 dropoff
        # calculate from cust2 dropoff to cust1 pickup
        # caluclate from cust2 pickup to cust1 pickup
        distance3 = find_path_length(cust2 pickup, cust2 dropoff)
        distance4 = find_path_length(cust2 dropoff, cust1 pickup)
        distance5 = find_path_length(cust2 pickup, cust1 pickup)

        if(distance3 + distance4) <= distance5:
            # dropoff cust2, then pickup cust1 //OP more detailed psuedocode
            #OP pickup customer 2
            temp_list = find_shortest_path(van_curr_location, cust2 pickup location)
            temp_list.pop(0)
            van_list["path"] += temp_list
            #OP dropoff customer 2
            temp_list = find_shortest_path(cust 2 pickup location, cust2 dropoff location)
            temp_list.pop(0)
            van_list["path"] += temp_list
            #OP pickup customer 1
            temp_list = find_shortest_path(cust2 dropoff location, cust1 pickup location)
            temp_list.pop(0)
            van_list["path"] += temp_list
            #OP dropoff customer 1
            temp_list = find_shortest_path(cust1 pickup location, cust1 dropoff location)
            temp_list.pop(0)
            van_list["path"] += temp_list

        else:
            # pickup cust2, then pickup cust1 //OP more detailed pseudocode
            #OP pickup customer 2
            temp_list = find_shortest_path(van_curr_location, cust2 pickup location)
            temp_list.pop(0)
            van_list["path"] += temp_list
            #OP pickup customer 1
            temp_list = find_shortest_path(cust 2 pickup location, cust1 pickup location)
            temp_list.pop(0)
            van_list["path"] += temp_list
            #OP dropoff customer 2
            temp_list = find_shortest_path(cust1 pickup location, cust2 dropoff location)
            temp_list.pop(0)
            van_list["path"] += temp_list
            #OP dropoff customer 1
            temp_list = find_shortest_path(cust 2 dropoff location, cust1 dropoff location)
            temp_list.pop(0)
            van_list["path"] += temp_list

# van path queue is not empty   
else:
# drop off current customers before pickup up new customers
    distance1 = find_path_length(van final location, cust1 pickup)
    distance2 = find_path_length(van final location, cust2 pickup)

    if distance1 < distance2:
        # calculate from cust1 pickup to cust1 dropoff
        # calculate from cust1 dropoff to cust2 pickup
        # caluclate from cust1 pickup to cust2 pickup
        distance3 = find_path_length(cust1 pickup, cust1 dropoff)
        distance4 = find_path_length(cust1 dropoff, cust2 pickup)
        distance5 = find_path_length(cust1 pickup, cust2 pickup)

        if(distance3 + distance4) <= distance5:
            # dropoff cust1, then pickup cust2 //OP more detailed pseudocode
            #OP pickup customer 1
            temp_list = find_shortest_path(van_final_location, cust1 pickup location)
            temp_list.pop(0)
            van_list["path"] += temp_list
            #OP dropoff customer 1
            temp_list = find_shortest_path(cust1 pickup location, cust1 dropoff location)
            temp_list.pop(0)
            van_list["path"] += temp_list
            #OP pickup customer 2
            temp_list = find_shortest_path(cust1 dropoff location, cust2 pickup location)
            temp_list.pop(0)
            van_list["path"] += temp_list
            #OP dropoff customer 2
            temp_list = find_shortest_path(cust2 pickup location, cust2 dropoff location)
            temp_list.pop(0)
            van_list["path"] += temp_list
        else:
            # pickup cust1, then pickup cust2 //OP more detailed psuedocode
            #OP pickup customer 1
            temp_list = find_shortest_path(van_final_location, cust1 pickup location)
            temp_list.pop(0)
            van_list["path"] += temp_list
            #OP pickup customer 2
            temp_list = find_shortest_path(cust1 pickup location, cust2 pickup location)
            temp_list.pop(0)
            van_list["path"] += temp_list
            #OP dropoff customer 1
            temp_list = find_shortest_path(cust2 pickup location, cust1 dropoff location)
            temp_list.pop(0)
            van_list["path"] += temp_list
            #OP dropoff customer 2
            temp_list = find_shortest_path(cust1 dropoff location, cust2 dropoff location)
            temp_list.pop(0)
            van_list["path"] += temp_list

    else:
        # distance2 < distance1
        # calculate from cust2 pickup to cust2 dropoff
        # calculate from cust2 dropoff to cust1 pickup
        # caluclate from cust2 pickup to cust1 pickup
        distance3 = find_path_length(cust2 pickup, cust2 dropoff)
        distance4 = find_path_length(cust2 dropoff, cust1 pickup)
        distance5 = find_path_length(cust2 pickup, cust1 pickup)

        if(distance3 + distance4) <= distance5:
            # dropoff cust2, then pickup cust1 //OP more detailed pseudocode
            #OP pickup customer 2
            temp_list = find_shortest_path(van_final_location, cust2 pickup location)
            temp_list.pop(0)
            van_list["path"] += temp_list
            #OP dropoff customer 2
            temp_list = find_shortest_path(cust 2 pickup location, cust2 dropoff location)
            temp_list.pop(0)
            van_list["path"] += temp_list
            #OP pickup customer 1
            temp_list = find_shortest_path(cust2 dropoff location, cust1 pickup location)
            temp_list.pop(0)
            van_list["path"] += temp_list
            #OP dropoff customer 1
            temp_list = find_shortest_path(cust1 pickup location, cust1 dropoff location)
            temp_list.pop(0)
            van_list["path"] += temp_list
        else:
            # pickup cust2, then pickup cust1 //OP more detailed pseudocode
            #OP pickup customer 2
            temp_list = find_shortest_path(van_final_location, cust2 pickup location)
            temp_list.pop(0)
            van_list["path"] += temp_list
            #OP pickup customer 1
            temp_list = find_shortest_path(cust 2 pickup location, cust1 pickup location)
            temp_list.pop(0)
            van_list["path"] += temp_list
            #OP dropoff customer 2
            temp_list = find_shortest_path(cust1 pickup location, cust2 dropoff location)
            temp_list.pop(0)
            van_list["path"] += temp_list
            #OP dropoff customer 1
            temp_list = find_shortest_path(cust 2 dropoff location, cust1 dropoff location)
            temp_list.pop(0)
            van_list["path"] += temp_list

# CASE 3: three customers added to van queue
distance1 = find_path_length(van curr location, cust1 pickup)
distance2 = find_path_length(van curr location, cust2 pickup)
distance3 = find_path_length(van curr location, cust3 pickup)

# picking up cust1 first
if distance1 <= distance2:
    if distance1 < distance3:
        # add path from van to cust1 to queue
        # then calculate distance from cust1 pickup to cust2 pickup
        # then calculate distance from cust1 pickup to cust3 pickup
        # then find who is closer: cust2 or cust3
        if cust2 closer:
            # check if we can dropoff cust1 before picking up cust2
            # else, pickup cust2
                # check if we can dropff cust1 before picking up cust3
                # else check if we can dropoff cust2 before picking up cust3
                # else check if we can dropoff cust1 & cust2 before picking up cust3
                # else pickup cust3   
        elif cust3 closer:
            # check if we can dropoff cust1 before picking up cust3
            # else, pickup cust3
                # check if we can dropff cust1 before picking up cust2
                # else check if we can dropoff cust3 before picking up cust2
                # else check if we can dropoff cust1 & cust3 before picking up cust2
                # else pickup cust2   

        # dropoff cust1, then cust3, then cust2 if they haven't been dropped off yet

# picking up cust2 first
if distance2 <= distance1:
    if distance2 <= distance3:
        if cust1 closer:

        if cust3 closer:

    # dropoff cust1, then cust3, then cust2 if they haven't been dropped off yet

# picking up cust3 first
if distance3 <= distance1:
    if distance3 <= distance2:
        if cust1 closer:

        if cust2 closer:

    # dropoff cust1, then cust3, then cust2 if they haven't been dropped off yet

# **************************************************************************************************************************************************************

# add 35 to 40 customers to queue
import random
import time

def add_to_queue(cust_queue, tot_num_cust):
  for i in range(0,4):
    num_gen_cust = random.randint(7,10)
    tot_num_cust += num_gen_cust
    for i in range(0,num_gen_cust):
      pickup = random.randint(0,99)
      dropoff = random.randint(0,99)
      while pickup == dropoff:
        dropoff = random.randint(0,99)
      cust_queue.append((pickup, dropoff))

# **************************************************************************************************************************************************************

# find the shortest path between 2 nodes
def find_shortest_path(startNode, endNode):
  return nx.shortest_path(G,startNode,endNode,weight='weight',method='dijkstra')

# **************************************************************************************************************************************************************

# find the path length between 2 nodes
def find_path_length(startNode, endNode):
  return nx.dijkstra_path_length(G,startNode,endNode)



