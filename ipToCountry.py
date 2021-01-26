#!/usr/bin/python
from Controller.countryStatisticsController import countryStatisticsController
from Model.countryStatistics import countryStatistics
from Service.ipDatabase import geoipDatabase
import ipaddress
import log

class ipToCountry:
  logger = log.get_logger("ipToCountry")

  @classmethod
  def mapIpToCountry(self):
    # handler for ip databases
    ipDatabaseHandler = geoipDatabase()
    ipData = countryStatisticsController.getDataNotMapped()
    savedItems = 0 
    for item in ipData:
      # get network address
      ipaddr = ipaddress.ip_network(item.ip).network_address
      # print(ipaddr)
      # get country code
      countryCode = ipDatabaseHandler.getCountryFromIp(str(ipaddr), item.ipVersion)
      if(countryCode != None):
        countryStatisticsItem = countryStatistics(None, item.accessed, item.sourceIdp, item.service, countryCode, 1)
        countryStatistics.save(countryStatisticsItem)
        savedItems +=1
      else:
        self.logger.warning("ip {0} not found at database".format(ipaddr))
    self.logger.info("{0} ips mapped to countries".format(savedItems))

      


#ipToCountry.mapIpToCountry()
    
