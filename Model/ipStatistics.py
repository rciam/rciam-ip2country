#!/usr/bin/python
from Model.pgConnector import pgConnector
from Utils import config

class ipStatistics(object):
  IPSTATISTICSTABLE = config.getConfig('tables')['ip_table']
  def __init__(self, accessed, sourceIdp, service, userid, ip, ipVersion):
    self.accessed = accessed
    self.sourceIdp = sourceIdp
    self.service = service
    self.userid = userid
    self.ip = ip
    self.ipVersion = ipVersion
  
  @classmethod
  def getIpStatisticsByDate(self, dateFrom, dateTo):
    pgConn = pgConnector()
    
    result = list(pgConn.execute_select("SELECT accessed::date, sourceidp, service, userid, ip, ipversion FROM {0} WHERE accessed BETWEEN  '{1}' AND '{2}'".format(ipStatistics.IPSTATISTICSTABLE, dateFrom, dateTo)))
    data = []
    for row in result:
      #print(row)
      ipData = ipStatistics(row[0], row[1], row[2], row[3], row[4], row[5])
      data.append(ipData)
    return data

  @classmethod
  def getAllIpStatistics(self):
    pgConn = pgConnector()
    result = list(pgConn.execute_select("SELECT accessed::date, sourceidp, service, userid, ip, ipversion FROM {0}".format(ipStatistics.IPSTATISTICSTABLE)))
    data = []
    for row in result:
      print(row[0])
      ipData = ipStatistics(row[0], row[1], row[2], row[3], row[4], row[5])
      data.append(ipData)
    return data

#ipStat = ipStatistics.getIpStatisticsByDate('2021-01-01 00:00:00','2021-01-01 23:59:59')
#print(ipStat)


