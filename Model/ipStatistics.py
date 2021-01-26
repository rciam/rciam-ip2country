#!/usr/bin/python
from Model.pgConnector import pgConnector

class ipStatistics(object):

  def __init__(self, accessed, sourceIdp, service, user, ip, ipVersion):
    self.accessed = accessed
    self.sourceIdp = sourceIdp
    self.service = service
    self.user = user
    self.ip = ip
    self.ipVersion = ipVersion
  
  @classmethod
  def getIpStatisticsByDate(self, dateFrom, dateTo):
    pgConn = pgConnector()
    
    result = list(pgConn.execute_select("SELECT accessed::date, sourceidp, service, user, ip, ipversion FROM statistics_ip WHERE accessed BETWEEN  '{0}' AND '{1}'".format(dateFrom, dateTo)))
    data = []
    for row in result:
      #print(row)
      ipData = ipStatistics(row[0], row[1], row[2], row[3], row[4], row[5])
      data.append(ipData)
    return data

  @classmethod
  def getAllIpStatistics(self):
    pgConn = pgConnector()
    result = list(pgConn.execute_select("SELECT accessed::date, sourceidp, service, user, ip, ipversion FROM statistics_ip"))
    data = []
    for row in result:
      print(row[0])
      ipData = ipStatistics(row[0], row[1], row[2], row[3], row[4], row[5])
      data.append(ipData)
    return data

      



#ipStat = ipStatistics.getIpStatisticsByDate('2021-01-01 00:00:00','2021-01-01 23:59:59')
#print(ipStat)


