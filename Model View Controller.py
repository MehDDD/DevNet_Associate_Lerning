class Device:

    ipAddress = ""
    port = ""

    @staticmethod
    def findDevices():
        devices = []

        d = Device()
        d.ipAddress = "192.168.1.1"
        d.port = "2001"

        devices.append(d)

        d = Device()
        d.ipAddress = "192.168.1.50"
        d.port = "3500"

        devices.append(d)

        d = Device()
        d.ipAddress = "192.168.1.100"
        d.port = "4500"

        devices.append(d)

        return devices
    

class DevicesView:

    def showDevices(self, devices):
        for d in devices:
            print("--------------------")
            print("IP Address: " + d.ipAddress)
            print("Port: " + str(d.port) )
            print("--------------------")


class DeviceController:

    def __init__(self) -> None:
        devices = Device.findDevices()

        v = DevicesView()
        v.showDevices(devices)


c = DeviceController()

