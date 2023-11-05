import sqlite3

def create_table():
    connection = sqlite3.connect('Reservation.db')
    cursor = connection.cursor()
    
    cursor.execute('''
        CREAT TABLE IF NOT EXISTS Tickets (
            ticket_id TEXT PRIMARY KEY,
            movie_name TEXT,
            ticket_quantity INTEGER,
            ticket_price INTEGER)''')
    
    connection.commit()
    connection.close()
    
def insert_Tickets():
    connection = sqlite3.connect('Reservation.db')
    cursor = connection.cursor()
    
    Tickets_data = [
        ('T1','Movie1',3,50),
        ('T1','Movie2',2,50),
        ('T1','Movie3',4,50),
        ('T1','Movie4',5,50),
        ('T1','Movie5',1,50)
    ]
    
    cursor.executemany('INSERT OR IGNORE INTO Tickets (ticket_id, movie_name, ticket_quantity, ticket_price) VALUES (?, ?, ?, ?)', Tickets_data)
    connection.commit()
    connection.close()
    
def get_tickets():
    connection = sqlite3.connect('Reservation.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Tickets')
    tickets = cursor.fetchall()
    connection.close()
    
    return tickets

def update_quantity(id, reserved_quantity):
    connection = sqlite3.connect('Reservation.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE Tickets SET ticket_quantity = ticket_quantity - ? WHERE ticket_id = ?', (reserved_quantity,id))
    connection.commit()
    connection.close()
    
create_table()
insert_Tickets()