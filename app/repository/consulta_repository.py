from app.database.connection import get_db
from app.models.consulta_model import ConsultaModel

class ConsultaRepository:
    
    def get_all_consultas(self):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT c.id, c.data, c.especialidade, c.id_paciente, p.nome
            FROM consulta c
            JOIN paciente p ON c.id_paciente = p.id
        """)
        rows = cursor.fetchall()
        consultas = []
        for row in rows:
            consulta = ConsultaModel(id=row[0], data=row[1], especialidade=row[2], id_paciente=row[3])
            consulta.paciente_nome = row[4]
            consultas.append(consulta)
        return consultas
    
    def get_consulta_by_id(self, id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT c.id, c.data, c.especialidade, c.id_paciente, p.nome
            FROM consulta c
            JOIN paciente p ON c.id_paciente = p.id
            WHERE c.id = ?
        """, (id,))
        row = cursor.fetchone()
        if row:
            consulta = ConsultaModel(
                id=row[0],
                data=row[1],
                especialidade=row[2],
                id_paciente=row[3]
            )
            consulta.paciente_nome = row[4]
            return consulta
        return None
        
    def create_consulta(self, consulta):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO consulta (data, especialidade, id_paciente)
            VALUES (?, ?, ?)
        """, (consulta.get_data(), consulta.get_especialidade(), consulta.get_id_paciente()))
        connection.commit()
        
    def update_consulta(self, consulta):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("""
            UPDATE consulta
            SET data = ?, especialidade = ?, id_paciente = ?
            WHERE id = ?
        """, (consulta.get_data(), consulta.get_especialidade(), consulta.get_id_paciente(), consulta.get_id()))
        connection.commit()
        
    def delete_consulta(self, consulta_id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM consulta WHERE id = ?", (consulta_id,))
        connection.commit()
        