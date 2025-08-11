from datetime import datetime, date
from app.repository.consulta_repository import ConsultaRepository
from app.models.consulta_model import ConsultaModel
from app.repository.paciente_repository import PacienteRepository

class ConsultaService:
    def __init__(self):
        self.consulta_repository = ConsultaRepository()
        self.paciente_repository = PacienteRepository()

    def validar_data_consulta(self, data_consulta):
        """Valida se a data da consulta não é no passado."""
        # Se vier como string no formato YYYY-MM-DD (padrão HTML)
        if isinstance(data_consulta, str):
            try:
                data_consulta = datetime.strptime(data_consulta, "%Y-%m-%d").date()
            except ValueError:
                raise ValueError("Formato de data inválido. Use o formato YYYY-MM-DD.")

        if not isinstance(data_consulta, date):
            raise ValueError("A data da consulta deve ser um objeto date válido.")

        hoje = date.today()
        if data_consulta < hoje:
            raise ValueError("Não é possível marcar consultas para datas que já passaram.")

        return data_consulta

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

        # Validação da data
        consulta.set_data(self.validar_data_consulta(consulta.get_data()))

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

        consulta.set_data(self.validar_data_consulta(consulta.get_data()))

        self.consulta_repository.update_consulta(consulta)
        
    def delete_consulta(self, consulta_id):
        if consulta_id is None:
            raise ValueError("O ID da categoria não pode ser None")
        self.consulta_repository.delete_consulta(consulta_id)
