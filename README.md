# DHT
It is an implementatioin of content sharing network implented using a Circular Distributed Hash Table.

# Initializing the Netwrok:
To initialize the network i.e to setup the first node in the network, you have to run the following commands:
```
python node.py 0 0
```
The system would use the to start listening for other nodes, and would ask you to set up a port for listening.
Choose the port in the command line. And then the client GUI will open up.

# Connecting to a network of node/s
To connect to an already set up network i.e a network that has atleast one node in it, you have to use following commands:
```
python node.py 0 portOfANodeInNetwork
```
The system will then ask for your port and then client GUI will open up.

Client GUI looks like this:
![Image description](https://github.com/Martian1998/DHT/blob/master/dht.png)

*Disclaimer: This code is written for python3
