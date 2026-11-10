from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def get_all_generi(self):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            return result

        cursor = cnx.cursor(dictionary=True)
        query = """SELECT DISTINCT genere FROM libro WHERE genere IS NOT NULL AND genere != '' ORDER BY genere"""

        try:
            cursor.execute(query)
            for row in cursor:
                result.append(row["genere"])
        except Exception as e:
            print(f"Errore nella query get_all_generi: {e}")
        finally:
            cursor.close()
            cnx.close()

        return result

    def get_libri_filtrati(self, biblioteca: str, genere: str):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            return result

        cursor = cnx.cursor(dictionary=True)
        query = """
            SELECT DISTINCT l.id, l.titolo, l.autore, l.genere, l.anno
            FROM libro l
            JOIN detiene d ON l.id = d.id_libro
            JOIN biblioteca b ON d.id_biblioteca = b.id
            WHERE b.nome = COALESCE(%s, b.nome)
              AND l.genere = COALESCE(%s, l.genere)
        """

        try:
            cursor.execute(query, (biblioteca, genere))
            for row in cursor:
                result.append(Libro(row["id"], row["titolo"], row["autore"], row["genere"], row["anno"]))
        except Exception as e:
            print(f"Errore nella query get_libri_filtrati: {e}")
        finally:
            cursor.close()
            cnx.close()

        return result
