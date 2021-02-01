from Model.pgConnector import pgConnector
from Utils import config
class countryStatistics(object):
  STATISTICSTABLE = config.getConfig('tables')['country_table']

  def __init__(self, id, date, sourceIdp, service, countryCode, country, count):
    self.id = id
    self.date = date
    self.service = service
    self.sourceIdp = sourceIdp
    self.countrycode = countryCode
    self.country = country
    self.count = count

  @classmethod
  def getLastDate(self):
    pgConn = pgConnector()
    result = pgConn.execute_select("SELECT max(date::date) FROM {0}".format(countryStatistics.STATISTICSTABLE))
    return result

  @classmethod
  def save(self, countryStatistics):
    pgConn = pgConnector()
    
    print("INSERT INTO statistics_country(date, sourceidp, service, countrycode, country, count) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', {5}) ON CONFLICT (date, sourceidp, service, countrycode) DO UPDATE SET count = statistics_country.count + 1".format(countryStatistics.date, countryStatistics.sourceIdp, countryStatistics.service, countryStatistics.countrycode,  countryStatistics.country, 1))
    pgConn.execute_insert(
      "INSERT INTO {0}(date, sourceidp, service, countrycode, country, count) VALUES ('{1}', '{2}', '{3}', '{4}', '{5}', {6}) ON CONFLICT (date, sourceidp, service, countrycode) DO UPDATE SET count = statistics_country.count + 1".format(countryStatistics.STATISTICSTABLE, countryStatistics.date, countryStatistics.sourceIdp, countryStatistics.service, countryStatistics.countrycode, countryStatistics.country, 1)
    )
  
  @classmethod
  def saveAll(self, countryStatisticsList):
    pgConn = pgConnector()
    values = ''
    for item in countryStatisticsList:
      values += "INSERT INTO {0}(date, sourceidp, service, countrycode, country, count) VALUES ('{1}', '{2}', '{3}', '{4}', '{5}', {6}) ON CONFLICT (date, sourceidp, service, countrycode) DO UPDATE SET count = {0}.count + 1;".format(countryStatistics.STATISTICSTABLE, item.date, item.sourceIdp, item.service, item.countrycode, item.country, 1)
    pgConn.execute_insert(values)
    

""" CREATE TABLE statistics_country (
id SERIAL PRIMARY KEY,
date DATE NOT NULL,
sourceidp character varying(255) NOT NULL,
service character varying(255) NOT NULL,
countrycode character varying(2) NOT NULL,
count int NOT NULL
);

CREATE INDEX statistics_country_i1 ON statistics_country (date);
CREATE INDEX statistics_country_i2 ON statistics_country (sourceidp);
CREATE INDEX statistics_country_i3 ON statistics_country (service);
CREATE INDEX statistics_country_i4 ON statistics_country (countrycode);
CREATE UNIQUE INDEX idx_statistics_country ON statistics_country(date, sourceidp, service, countrycode);
 """