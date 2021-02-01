from Model.pgConnector import pgConnector
from Utils import config
class userCountryStatistics(object):
  USERCOUNTRYTABLE = config.getConfig('tables')['user_country_table']

  def __init__(self, id, date, userid, countrycode, country, count):
    self.id = id
    self.date = date
    self.userid = userid
    self.countrycode = countrycode
    self.country = country
    self.count = count

  @classmethod
  def getLastDate(self):
    pgConn = pgConnector()
    result = pgConn.execute_select("SELECT max(date::date) FROM {0}".format(userCountryStatistics.USERCOUNTRYTABLE))
    return result

  @classmethod
  def save(self, userCountryStatistics):
    pgConn = pgConnector()
    print(userCountryStatistics.date)
    print("INSERT INTO {0}(date, userid, countrycode, country, count) VALUES ('{1}', '{2}', '{3}', '{4}', {5}) ON CONFLICT (date, userid, countrycode) DO UPDATE SET count = statistics_country.count + 1".format(userCountryStatistics.USERCOUNTRYTABLE, userCountryStatistics.date, userCountryStatistics.userid, userCountryStatistics.countrycode, userCountryStatistics.country, 1))
    pgConn.execute_insert(
      "INSERT INTO {0}(date, userid, countrycode, country, count) VALUES ('{1}', '{2}', '{3}', '{4}', {5}) ON CONFLICT (date, userid, countrycode) DO UPDATE SET count = statistics_user_country.count + 1".format(userCountryStatistics.USERCOUNTRYTABLE, userCountryStatistics.date, userCountryStatistics.userid, userCountryStatistics.countrycode, userCountryStatistics.country, 1)
    )

  @classmethod
  def saveAll(self, userCountryStatisticsList):
    pgConn = pgConnector()
    values = ''
    for item in userCountryStatisticsList:
      values += "INSERT INTO {0}(date, userid, countrycode, country, count) VALUES ('{1}', '{2}', '{3}', '{4}', {5}) ON CONFLICT (date, userid, countrycode) DO UPDATE SET count = {0}.count + 1;".format(userCountryStatistics.USERCOUNTRYTABLE, item.date, item.userid, item.countrycode, item.country, item.count)
    pgConn.execute_insert(values)