from app.repository.consulta_repository import ConsultaRepository
from app.models.consulta_model import ConsultaModel
from app.repository.paciente_repository import PacienteRepository

class ConsultaService:
    def __init__(self):
        self.consulta_repository = ConsultaRepository()
        self.paciente_repository = PacienteRepository()
        
    def get_all_consultas(self):
        return self.consulta_repository.get_all_consultas()
    
    def get_consulta_by_id(self, consulta_id):
        if consulta_id is None:
            raise ValueError("O ID da consulta não pode ser None.")
        return self.consulta_repository.get_consulta_by_id(consulta_id)
    
    def create_consulta(self, consulta: ConsultaModel):
        if consulta.get_id() is not None:
            raise ValueError("Não é possível criar uma consulta com ID já definido.")
        if not consulta.get_data() or not consulta.get_especialidade():
            raise ValueError("Data e especialidade da consulta são obrigatórias.")
        if len(consulta.get_especialidade()) < 3:
            raise ValueError("A especialidade deve ter pelo menos 3 caracteres.")
        if not self.paciente_repository.get_paciente_by_id(consulta.get_id_paciente()):
            raise ValueError("O paciente informado não existe.")
        self.consulta_repository.create_consulta(consulta)
        
    def update_consulta(self, consulta: ConsultaModel):
        if consulta.get_id() is None:
            raise ValueError("O ID da consulta não pode ser None.")
        if not consulta.get_data() or not consulta.get_especialidade():
            raise ValueError("Data e especialidade da consulta são obrigatórias.")
        if len(consulta.get_especialidade()) < 3:
            raise ValueError("A especialidade deve ter pelo menos 3 caracteres.")
        if not self.paciente_repository.get_paciente_by_id(consulta.get_id_paciente()):
            raise ValueError("O paciente informado não existe.")
        self.consulta_repository.update_consulta(consulta)
        
    def delete_consulta(self, consulta_id):
        if consulta_id is None:
            raise ValueError("O ID da categoria não pode ser None")
        self.consulta_repository.delete_consulta(consulta_id)
