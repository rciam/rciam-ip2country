#!/usr/bin/python
from Model.pgConnector import pgConnector

class countryStatistics(object):

  def __init__(self, id, date, sourceIdp, service, countryCode, count):
    self.id = id
    self.date = date
    self.service = service
    self.sourceIdp = sourceIdp
    self.countrycode = countryCode
    self.count = count

  @classmethod
  def getLastDate(self):
    pgConn = pgConnector()
    result = pgConn.execute_select("SELECT max(date::date) FROM statistics_country")
    return result

  @classmethod
  def save(self, countryStatistics):
    pgConn = pgConnector()
    print(countryStatistics.date)
    print("INSERT INTO statistics_country(id, date, sourceidp, service, countrycode, count) VALUES (NULL, '{0}', '{1}', '{2}', '{3}', {4}) ON CONFLICT (date, sourceidp, service, countrycode) DO UPDATE SET count = statistics_country.count + 1".format(countryStatistics.date, countryStatistics.service, countryStatistics.sourceIdp, countryStatistics.countrycode, 1))
    pgConn.execute_insert(
      "INSERT INTO statistics_country(date, sourceidp, service, countrycode, count) VALUES ('{0}', '{1}', '{2}', '{3}', {4}) ON CONFLICT (date, sourceidp, service, countrycode) DO UPDATE SET count = statistics_country.count + 1".format(countryStatistics.date, countryStatistics.service, countryStatistics.sourceIdp, countryStatistics.countrycode, 1)
    )


  
 

#countryStatistics.getLastDate()

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