#!/usr/bin/python
from Controller.countryStatisticsController import countryStatisticsController
from Model.countryStatistics import countryStatistics
from Model.geoipDatabase import geoipDatabase
import ipaddress

class ipToCountry:
  @classmethod
  def mapIpToCountry(self):
    # handler for ip databases
    databaseHandler = geoipDatabase()
    ipData = countryStatisticsController.getDataNotMapped()
    for item in ipData:
      # get network address
      ipaddr = ipaddress.ip_network(item.ip).network_address
      # print(ipaddr)
      # get country code
      countryCode = databaseHandler.getCountryFromIp(str(ipaddr), item.ipVersion)
      if(countryCode != None):
        countryStatisticsItem = countryStatistics(None, item.accessed, item.sourceIdp, item.service, countryCode, 1)
        countryStatistics.save(countryStatisticsItem)


      


ipToCountry.mapIpToCountry()
    
