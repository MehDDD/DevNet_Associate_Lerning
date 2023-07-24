# Print operational Data of a RouterInterface
from ncclient import manager
# You get the LoginInformation from CiscoDevNetSandbox
router = {"host": "10.10.20.48", "port": "830", "username": "developer", "password": "C1sco12345"}
# This is the Netconf filter, to show the GigabitEthernet2 Information. This is an XML Structure
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