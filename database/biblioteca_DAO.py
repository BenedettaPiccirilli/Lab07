from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    def get_all_biblioteche(self):
        cnx = DBConnect.get_connection()
        result=[]
        if cnx is None:
            print("Errore di connessione al database")
            return result
        cursor = cnx.cursor(dictionary=True)
        query= """ SELECT id, nome, indirizzo FROM biblioteca"""

        try:
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                result.append(Biblioteca(row["id"], row["nome"], row["indirizzo"]))
        except Exception as e:
            print(f"Errore nella query: {e}")
        finally:
            cursor.close()
        return result