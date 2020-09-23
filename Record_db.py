import sqlite3

#create and connect database
conn = sqlite3.connect('Records_db.sqlite')

#create table in database
conn.execute('CREATE TABLE IF NOT EXISTS record_holders(Name text, Country text, Number_of_catches int)')

#inserting the four record holders
conn.execute('INSERT INTO record_holders VALUES("Janne Mustonen", "Finland", 98)')
conn.execute('INSERT INTO record_holders VALUES("Ian Stewart", "Canada", 94)')
conn.execute('INSERT INTO record_holders VALUES("Aaron Gregg", "Canada", 88)')
conn.execute('INSERT INTO record_holders VALUES("Chad Taylor", "USA", 78)')
    
for row in conn.execute('select * from record_holders'):
    print(row)
conn.commit() 
   
#adding new record holder
print("Enter the new record holder you want to add below ")
name = input("Enter the full name of record holder: ")
country = input("Enter the country: ")
number_of_catches = int(input("Enter the number of catches: "))     

conn.execute('INSERT INTO record_holders VALUES (?,?,?)', (name, country, number_of_catches))
conn.commit()

#search record holder by name
record_holder_search ="Ian Stewart"
conn.execute("SELECT * FROM record_holders WHERE Name=?", (record_holder_search,))
conn.commit()

#update the number of catches
sql_update_query = 'Update record_holders set Name = ? where Number_of_catches = ?'
data = (name, number_of_catches)
conn.execute(sql_update_query, data)
conn.commit()
   
#delete a record by recordholder's name
deleted_name = "Chad Taylor"
conn.execute('DELETE FROM record_holders WHERE Name = ?', (deleted_name,))
conn.commit()
   

conn.close()

    








  