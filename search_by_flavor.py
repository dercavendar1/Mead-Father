import pymysql as db

# Innitiates connection to DB
connection = db.connect(host='192.168.1.210',
                        user='root',
                        password='#d8K*omZWK%J9b6P',
                        database='homebrew_proj',
                        charset='utf8mb4',
                        cursorclass=db.cursors.DictCursor)
# Grabs flavor table from DB and stores in flavors variable
sql_query = ('select * from flavors')
with connection.cursor() as cursor:
    cursor.execute(sql_query)
    flavors = cursor.fetchall()

# Creates a query and converts the string to the corresponding
# primary key in flavor table to simplify sql query
query = input('What flavor are you looking for? ')
for flavor in flavors:
    if query == flavor['flavor_profile']:
        query = flavor['flavor_id']

sql_query = (f'select honey_name, flavors.flavor_profile, honey_description from honey ' +
             f'inner join flavors on honey.flavor_profile = flavor_id' +
             f' where flavors.flavor_id = {query}')

# queries DB based on input search string and stores results in a list of Dictionaries
with connection.cursor() as cursor:
    cursor.execute(sql_query)
    results = cursor.fetchall()

# prints results of search or no result message
if len(results) == 0:
    print('No Results Found')
else:
    for result in results:
        print(result)
