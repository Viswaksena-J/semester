#!/usr/bin/python

"""

The topology creates two routers and three IP subnets:

    - 192.168.1.0/24 (r0-eth1, IP: 192.165.1.1)
    - 10.0.0.0/8 (r0-eth2, IP: 10.0.0.1, r1-eth1, IP: 10.0.0.2)
    - 172.16.0.0/12 (r1-eth2, IP: 170.12.0.1)

Each subnet consists of a single host connected to
a single switch:

    r0-eth1 - s1-eth1 - h1-eth0 (IP: 192.165.1.100)
    r1-eth1 - s2-eth1 - h2-eth0 (IP: 10.0.0.100)
    r1-eth2 - s3-eth1 - h3-eth0 (IP: 170.12.0.100)

The example relies on default routing entries that are
automatically created for each router interface, as well
as 'defaultRoute' parameters for the host interfaces.

Additional routes may be added to the router or hosts by
executing 'ip route' or 'route' commands on the router or hosts.
"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node, OVSBridge
from mininet.log import setLogLevel, info
from mininet.cli import CLI

class TestRouter( Node ):
    "A Node with IP forwarding enabled."

    def config( self, **params ):
        super( TestRouter, self).config( **params )
        # Enable forwarding on the router
        self.cmd( 'sysctl net.ipv4.ip_forward=1' )

    def terminate( self ):
        self.cmd( 'sysctl net.ipv4.ip_forward=0' )
        super( TestRouter, self ).terminate()


class NetworkTopo( Topo ):
    "Two Routers connecting three IP subnets"

    def build( self, **_opts ):

        subnet1IP = '192.165.1.1/24'  # IP address for r0-eth1
        router = self.addNode( 'r0', cls=TestRouter, ip=subnet1IP )


        self.addLink( s1, router, intfName2='r0-eth1',
                      params2={ 'ip' : subnet1IP } )  # for clarity

        h1 = self.addHost( 'h1', ip='192.165.1.100/24',
                           defaultRoute='via 192.165.1.1' )

        self.addLink( h1, s1 )


def run():
    "Test linux router"
    topo = NetworkTopo()
    net = Mininet( topo=topo, switch=OVSBridge)  # controller is used by s1-s3
    net.start()
    info( '*** Routing Table on Router:\n' )
    print net[ 'r0' ].cmd( 'route' )
    CLI( net )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    run()
