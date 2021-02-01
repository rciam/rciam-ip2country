from abc import ABC, abstractmethod
from Model.ipStatistics import ipStatistics
import GeoIP

class ipDatabase(ABC):
  @abstractmethod
  def getCountryFromIp(self): 
    pass

class geoipDatabase(ipDatabase):
  @classmethod
  def getCountryFromIp(self, ip, ipVersion):
    gi = GeoIP.open("../databases/GeoIP.dat",GeoIP.GEOIP_STANDARD)
    giV6 =  GeoIP.open("../databases/GeoIPv6.dat",GeoIP.GEOIP_STANDARD)
    if ipVersion == 'ipv4':
      print(gi.country_code_by_addr(ip))
      return [gi.country_code_by_addr(ip),gi.country_name_by_addr(ip)]
    else:
      print(giV6.country_code_by_addr_v6(ip))
      return [giV6.country_code_by_addr_v6(ip),giV6.country_name_by_addr_v6(ip)]

