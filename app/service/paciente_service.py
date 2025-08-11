from datetime import datetime, date
from app.repository.paciente_repository import PacienteRepository
from app.models.paciente_model import PacienteModel

class PacienteService:
    def __init__(self):
        self.paciente_repository = PacienteRepository()
        
    def validate_date(self, date_str):
        try:
            data_nascimento = datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError("Data inválida. Use o formato YYYY-MM-DD.")
        
        hoje = date.today()
        if data_nascimento > hoje:
            raise ValueError("A data de nascimento não pode ser no futuro.")

        idade = hoje.year - data_nascimento.year - (
            (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day)
        )
        if idade > 130:
            raise ValueError("Idade inválida. Por favor, verifique a data de nascimento.")

        return data_nascimento

    def validate_paciente(self, paciente: PacienteModel):
        if not paciente.get_nome() or not paciente.get_data_nascimento() or not paciente.get_telefone():
            raise ValueError("Nome, data de nascimento e telefone são obrigatórios.")
        if len(paciente.get_nome()) < 3:
            raise ValueError("O nome do paciente deve ter pelo menos 3 caracteres.")
        if paciente.get_nome().isdigit():
            raise ValueError("O nome do paciente não pode ser apenas numérico.")
        paciente.set_data_nascimento(self.validate_date(paciente.get_data_nascimento()))

    def get_all_pacientes(self):
        return self.paciente_repository.get_all_pacientes()
    
    def get_paciente_by_id(self, paciente_id):
        if paciente_id is None:
            raise ValueError("O ID do paciente não pode ser None.")
        return self.paciente_repository.get_paciente_by_id(paciente_id)
    
    def create_paciente(self, paciente: PacienteModel):
        if paciente.get_id() is not None:
            raise ValueError("Não é possível criar um paciente com ID já definido.")
        self.validate_paciente(paciente)
        self.paciente_repository.create_paciente(paciente)
        
    def update_paciente(self, paciente: PacienteModel):
        if paciente.get_id() is None:
            raise ValueError("O ID do paciente não pode ser None.")
        self.validate_paciente(paciente)
        self.paciente_repository.update_paciente(paciente)
        
    def delete_paciente(self, paciente_id):
        if paciente_id is None:
            raise ValueError("O ID do paciente não pode ser None.")
        consultas = self.paciente_repository.get_consulta_by_paciente_id(paciente_id)
        if consultas:
            raise ValueError("Não é possível excluir um paciente que possui consultas agendadas.")
        self.paciente_repository.delete_paciente(paciente_id)
