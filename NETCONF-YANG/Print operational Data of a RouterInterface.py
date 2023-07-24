# Print operational Data of a RouterInterface
from ncclient import manager
import xml.dom.minidom

# You get the LoginInformation from CiscoDevNetSandbox
router = {"host": "10.10.20.48", "port": "830", "username": "developer", "password": "C1sco12345"}
# This is the Netconf filter, to show the GigabitEthernet2 Information. This is an XML Structure.
netconf_filter = """
<filter>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>GigabitEthernet2</name>
    </interface>
  </interfaces>
  <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>GigabitEthernet2</name>
    </interface>
  </interfaces-state>
</filter>
"""

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
    for capability in m.server_capabilities:
        print('*' * 50)
        print(capability)

        # now we get the netconf data
        interface_netconf = m.get(netconf_filter)
        # we turn the response to a human readable xml data
        xmlDom = xml.dom.minidom.parseString(str(interface_netconf))
        print(xmlDom.toprettyxml(indent=" "))
        print('*' * 50 + 'break' + '*' * 50)
    m.close_session()