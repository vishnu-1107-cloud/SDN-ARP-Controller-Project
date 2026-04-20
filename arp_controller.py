from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.addresses import IPAddr

log = core.getLogger()

def _handle_ConnectionUp(event):
    msg = of.ofp_flow_mod()
    msg.priority = 300
    msg.match.dl_type = 0x0800
    msg.match.nw_src = IPAddr("10.0.0.1")
    msg.match.nw_dst = IPAddr("10.0.0.3")
    event.connection.send(msg)

    log.info("DROP rule installed for h1 -> h3")

def launch():
    log.info("Blocking Controller Started")
    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
