import getpass
import pymysql as db

# Innitiates connection to DB
connection = db.connect(host='192.168.1.210',
                        user='root',
                        password=getpass.getpass('What is the DB Password? '),
                        database='homebrew_proj',
                        charset='utf8mb4',
                        cursorclass=db.cursors.DictCursor)
# Grabs flavor table from DB and stores in flavors variable
sql_query = ('select honey_description, honey_name from honey')
with connection.cursor() as cursor:
    cursor.execute(sql_query)
    honeys = cursor.fetchall()

# Creates a query and converts the string to the corresponding
# primary key in flavor table to simplify sql query
query = input('What flavor are you looking for? ')
# for flavor in flavors:
#     if query == flavor['flavor_profile']:
#         query = flavor['flavor_id']

# builds a query that searches in honey_description field for a word or phrase
sql_query = ('select distinct honey.honey_name, flavors.flavor_profile ' +
             'FROM(honey inner join flavor_join as g ' +
             'on honey.honey_id=g.honey_id) ' +
             'inner join(flavor_join as f inner join flavors ' +
             'on f.flavor_id=flavors.flavor_id) ' +
             'on honey.honey_id=f.honey_id ' +
             f'where flavors.flavor_profile = \'{query}\' ' +
             'Order By honey_name; ')

# queries DB based on input search string and stores results in a list
# of Dictionaries
with connection.cursor() as cursor:
    cursor.execute(sql_query)
    results = cursor.fetchall()

# prints results of search or no result message
if len(results) == 0:
    print('No Results Found')
else:
    for result in results:
        print(result)
