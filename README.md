SDN ARP-Aware Traffic Control using POX and Mininet
 Project Overview
This project demonstrates Software Defined Networking (SDN) with a focus on ARP-aware traffic control using the POX controller and Mininet emulator.

The controller enforces network policies by installing OpenFlow rules while leveraging ARP for host discovery and communication setup.


 Objectives
Understand SDN architecture (Control Plane vs Data Plane)
Demonstrate ARP role in network communication
Implement centralized control using POX
Apply OpenFlow match-action rules
Block communication between selected hosts (h1 → h3)


 Network Topology
1 Switch (s1)
3 Hosts:
h1 → 10.0.0.1
h2 → 10.0.0.2
h3 → 10.0.0.3


 Technologies Used
Mininet
POX Controller
OpenFlow
Ubuntu Linux


 SDN Architecture
Control Plane → POX Controller
Data Plane → Open vSwitch


 ARP Handling in SDN
In traditional networks, ARP (Address Resolution Protocol) is used to map IP addresses to MAC addresses.

In this project:

ARP is used for host discovery
Hosts use ARP before communication begins
The controller observes packet flow after ARP resolution
Policies are enforced centrally using OpenFlow rules


 Controller Logic
The controller installs a high-priority OpenFlow DROP rule:

Source IP: 10.0.0.1 (h1)
Destination IP: 10.0.0.3 (h3)
Action: DROP


 Packet Behavior
 Allowed
h2 → h3 → Works
h1 → h2 → Works
 Blocked
h1 → h3 → Blocked (100% packet loss)


 Why No "Destination Host Unreachable"?
Packets are silently dropped by the switch due to the DROP rule. No ICMP error is generated → results in packet loss instead of unreachable message.


 How to Run
Start Controller
cd ~/pox ./pox.py forwarding.l2_learning arp_controller
Start Mininet
sudo mn --topo single,3 --controller=remote,ip=127.0.0.1,port=6633 //inbuilt topology


 Testing
Ping
h1 ping h3 h2 ping h3 pingall
Iperf
h3 iperf -s -u & h2 iperf -c 10.0.0.3 -u


 Flow Rules
sudo ovs-ofctl dump-flows s1


 Screenshots


Ping_blocked.png

Ping_allowed.png

Pingall.png

Iperf.png

Flow_table.png

Controller_logs.png



 Conclusion
This project demonstrates how SDN enables centralized control while ARP supports host discovery. The controller enforces policies using OpenFlow rules.


 Author
Vishnu Maddirala

