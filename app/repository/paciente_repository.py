from app.database.connection import get_db
from app.models.paciente_model import PacienteModel

class PacienteRepository:
    def get_all_pacientes(self):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM paciente")
        rows = cursor.fetchall()
        return [
            PacienteModel(id=row[0], nome=row[1], data_nascimento=row[2], telefone=row[3]) for row in rows
        ]
    
    def get_paciente_by_id(self, id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM paciente WHERE id = ?", (id,))
        row = cursor.fetchone()
        if row:
            return PacienteModel(id=row[0], nome=row[1], data_nascimento=row[2], telefone=row[3])
        return None
    
    def create_paciente(self, paciente):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO paciente (nome, data_nascimento, telefone) VALUES (?, ?, ?)",
            (paciente.get_nome(), paciente.get_data_nascimento(), paciente.get_telefone())
        )
        connection.commit()

    def update_paciente(self, paciente):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE paciente SET nome = ?, data_nascimento = ?, telefone = ? WHERE id = ?",
            (paciente.get_nome(), paciente.get_data_nascimento(), paciente.get_telefone(), paciente.get_id())
        )
        connection.commit()
        
    def delete_paciente(self, id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM paciente WHERE id = ?", (id,))
        connection.commit()
        
    def get_consulta_by_paciente_id(self, paciente_id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM consulta WHERE id_paciente = ?", (paciente_id,))
        return cursor.fetchall()