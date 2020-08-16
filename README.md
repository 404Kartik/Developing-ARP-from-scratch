
# Address Resolution Protocol (arp)
## Best IDE to implement the code in your Micro:Bit
Use the [MU code editor]([https://codewith.mu/](https://codewith.mu/))

## How ARP works?


The address resolution protocol (arp) is a protocol used by the  [Internet Protocol (IP)](https://erg.abdn.ac.uk/users/gorry/course/inet-pages/ip.html)  [[RFC826]](https://erg.abdn.ac.uk/users/gorry/course/inet-pages/arp.html#Anchor-49575), specifically IPv4, to map  [IP network addresses](https://erg.abdn.ac.uk/users/gorry/course/inet-pages/ip-address.html)  to the hardware addresses used by a data link protocol. The protocol operates below the network layer as a part of the interface between the OSI network and OSI link layer. It is used when  [IPv4 is used over Ethernet.](https://erg.abdn.ac.uk/users/gorry/course/inet-pages/ip-enet.html)

The term address resolution refers to the process of finding an address of a computer in a network. The address is "resolved" using a protocol in which a piece of information is sent by a client process executing on the local computer to a server process executing on a remote computer. The information received by the server allows the server to uniquely identify the network system for which the address was required and therefore to provide the required address. The address resolution procedure is completed when the client receives a response from the server containing the required address.

An  [Ethernet](https://erg.abdn.ac.uk/users/gorry/course/lan-pages/enet.html)  network uses two hardware addresses which identify the source and destination of each frame sent by the  [Ethernet](https://erg.abdn.ac.uk/users/gorry/course/lan-pages/enet.html). The destination address (all 1's) may also identify a  [broadcast](https://erg.abdn.ac.uk/users/gorry/course/intro-pages/uni-b-mcast.html)  packet (to be sent to all connected computers). The hardware address is also known as the  [Medium Access Control (MAC) address](https://erg.abdn.ac.uk/users/gorry/course/lan-pages/mac.html), in reference to the standards which define  [Ethernet](https://erg.abdn.ac.uk/users/gorry/course/lan-pages/enet.html). Each computer  [network interface card](https://erg.abdn.ac.uk/users/gorry/course/lan-pages/nic.html)  is allocated a globally unique 6 byte link address when the factory manufactures the card (stored in a PROM). This is the normal link source address used by an interface. A computer sends all packets which it creates with its own hardware source link address, and receives all packets which match the same hardware address in the destination field or one (or more) pre-selected broadcast/multicast addresses.

The Ethernet address is a link layer address and is dependent on the interface card which is used. IP operates at the network layer and is not concerned with the  [link addresses](https://erg.abdn.ac.uk/users/gorry/course/inet-pages/ip-address.html)  of individual nodes which are to be used.The address resolution protocol (arp) is therefore used to translate between the two types of address. The arp client and server processes operate on all computers using  [IP over Ethernet](https://erg.abdn.ac.uk/users/gorry/course/inet-pages/ip-enet.html). The processes are normally implemented as part of the software driver that drives the  [network interface card](https://erg.abdn.ac.uk/users/gorry/course/lan-pages/nic.html).

There are four types of arp messages that may be sent by the arp protocol. These are identified by four values in the "operation" field of an arp message. The types of message are:

1.  ARP-Request (Broadcast, source IP address of the requester)
2.  ARP-Reply (Unicast to requester, the target)

The format of an  arp message is shown below:

_![](https://erg.abdn.ac.uk/users/gorry/course/images/arp-header.gif)_

_Format of an arp message used to resolve the remote  [MAC Hardware Address](https://erg.abdn.ac.uk/users/gorry/course/lan-pages/mac.html) (HA)_

To reduce the number of address resolution requests, a client normally  **caches**  resolved addresses for a (short) period of time. The arp cache is of a finite size, and would become full of incomplete and obsolete entries for computers that are not in use if it was allowed to grow without check. The arp cache is therefore periodically flushed of all entries. This deletes unused entries and frees space in the cache. It also removes any unsuccessful attempts to contact computers which are not currently running.

If a host changes the MAC address it is using, this can be detected by other hosts when the cache entry is deleted and a fresh arp message is sent to establish the new association. The use of gratuitous arp (e.g. triggered when the new NIC interface is enabled with an IP address) provides a more rapid update of this information.

### Example of  use of the Address Resolution Protocol (arp)

The figure below shows the use of arp when a computer tries to contact a remote computer on the same  [LAN](https://erg.abdn.ac.uk/users/gorry/course/intro-pages/lan.html)  (known as "sysa") using the "[ping" program](https://erg.abdn.ac.uk/users/gorry/course/inet-pages/icmp.html). It is assumed that no previous IP datagrams have been received form this computer, and therefore arp must first be used to identify the  [MAC](https://erg.abdn.ac.uk/users/gorry/course/lan-pages/mac.html)  address of the remote computer.

![](https://erg.abdn.ac.uk/users/gorry/course/images/arp-encap.gif)

The  [arp request message](https://erg.abdn.ac.uk/users/gorry/course/inet-pages/arp.html#Anchor-arp-message)  ("who is X.X.X.X tell Y.Y.Y.Y", where X.X.X.X and Y.Y.Y.Y are  [IP addresses](https://erg.abdn.ac.uk/users/gorry/course/inet-pages/ip-address.html)) is sent using the Ethernet  [broadcast](https://erg.abdn.ac.uk/users/gorry/course/intro-pages/uni-b-mcast.html)  address, and an Ethernet protocol type of value 0x806. Since it is broadcast, it is received by all systems in the same collision domain ([LAN](https://erg.abdn.ac.uk/users/gorry/course/intro-pages/lan.html)). This is ensures that is the target of the query is connected to the network, it will receive a copy of the query. Only this system responds. The other systems discard the packet silently.

The target system forms an arp response ("X.X.X.X is hh:hh:hh:hh:hh:hh", where hh:hh:hh:hh:hh:hh is the  [Ethernet source address](https://erg.abdn.ac.uk/users/gorry/course/lan-pages/nic.html)  of the computer with the IP address of X.X.X.X). This packet is  [unicast](https://erg.abdn.ac.uk/users/gorry/course/intro-pages/uni-b-mcast.html)  to the address of the computer sending the query (in this case Y.Y.Y.Y). Since the original request also included the hardware address ([Ethernet source address)](https://erg.abdn.ac.uk/users/gorry/course/lan-pages/nic.html)  of the requesting computer, this is already known, and doesn't require another arp message to find this out.

### ![](https://erg.abdn.ac.uk/users/gorry/course/images/arp-eg.gif)

### Gratuitous ARP

Gratuitous ARP is used when a node (end system) has selected an IP address and then wishes to defend its chosen address on the local area network (i.e. to check no other node is using the same IP address). It can also be used to force a common view of the node's IP address (e.g. after the IP address has changed).

Use of this is common when an interface is first configured, as the node attempts to clear out any stale caches that might be present on other hosts. The node simply sends an arp request for itself.

### Proxy ARP

Proxy ARP is the name given when a node responds to an arp request on behalf of another node. This is commonly used to redirect traffic sent to one IP address to another system.

Proxy ARP can also be used to subvert traffic away from the intended recipient. By responding instead of the intended recipient, a node can pretend to be a different node in a network, and therefore force traffic directed to the node to be redirected to itself. The node can then view the traffic (e.g. before forwarding this to the originally intended node) or could modify the traffic. Improper use of Proxy ARP is therefore a significant security vulnerability and some networks therefore implement systems to detect this. Gratuitous ARP can also help defend the correct IP to MAC bindings.
