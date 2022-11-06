#!/usr/bin/env python3
from mininet.net import Mininet
from mininet.cli import CLI
net=Mininet(ipBase='10.0.0.0/24')
h1=net.addHost(name='h1',ip='10.0.0.1/24')
h2=net.addHost(name='h2',ip='10.0.0.2/24')
h3=net.addHost(name='h3',ip='10.0.0.3/24')
s1=net.addSwitch('s1')
print(net.addLink(s1,h1))
print(net.addLink(s1,h2))
print(net.addLink(s1,h3))
net.build()
net.start()
#sh ovs-ofctl add-flow s1 action=normal komanda koja se unosi u miniet>, kako bi se aktivirao switch i dodjelila mu se Flow tabela
print("Unosi se komanda: sh ovs-ofctl add-flow s1 action=normal kako bi se aktivirao switch\n i definisala dodjela Flow tabele")
CLI(net)
net.pingAll()
net.stop()
