import sqlite3

def create_database():
    # Connexion à la base de données (cela crée le fichier si nécessaire)
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # Créer la table Products si elle n'existe pas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')

    # Utiliser INSERT OR IGNORE pour éviter les doublons
    cursor.executemany('''
        INSERT OR IGNORE INTO Products (id, name, category, price)
        VALUES (?, ?, ?, ?)
    ''', [
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ])
    
    # Sauvegarder les modifications
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()
