import sqlite3 as DB

try:
    
    connect = DB.connect("./banco.db")
    cursor = connect.cursor()
    
    comand = """
    
    """;
    cursor.execute(comand)
    
    connect.commit()
    
except  DB.DatabaseError as Err:
    print("Erro banco", Err)
    
finally:
    if connect:
        cursor.close()
        connect.close()
    
