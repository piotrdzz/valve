from python.fileHandling.storage.LookupTableReadingsToPerc import LookupTableReadingsToPerc
from python.fileHandling.storage.MqttSettings import MqttSettings
from python.fileHandling.storage.ValveParams import ValveParams


class DbStructure:
    def __init__(self):
        self.lookupTable: LookupTableReadingsToPerc = LookupTableReadingsToPerc()
        self.valveParams: ValveParams = ValveParams()
        self.mqttSettings: MqttSettings = MqttSettings()
        self.wifiScriptPath: str = "/usr/sbin/setWifi.sh"
        self.accessPointScriptLocation: str = "/usr/sbin/startAP.sh"
        self.restartScriptLocation: str = "/usr/sbin/restartValve.sh"
