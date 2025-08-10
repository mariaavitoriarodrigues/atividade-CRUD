from app.repository.paciente_repository import PacienteRepository
from app.models.paciente_model import PacienteModel

class PacienteService:
    def __init__(self):
        self.paciente_repository = PacienteRepository()

    def get_all_pacientes(self):
        return self.paciente_repository.get_all_pacientes()
    
    def get_paciente_by_id(self, paciente_id):
        if paciente_id is None:
            raise ValueError("O ID do paciente não pode ser None.")
        return self.paciente_repository.get_paciente_by_id(paciente_id)
    
    def create_paciente(self, paciente: PacienteModel):
        if paciente.get_id() is not None:
            raise ValueError("Não é possível criar um paciente com ID já definido.")
        if not paciente.get_nome() or not paciente.get_data_nascimento() or not paciente.get_telefone():
            raise ValueError("Nome, data de nascimento e telefone são obrigatórios.")
        if len(paciente.get_nome()) < 3:
            raise ValueError("O nome do paciente deve ter pelo menos 3 caracteres.")
        if paciente.get_nome().isdigit():
            raise ValueError("O nome do paciente não pode ser apenas numérico.")
        self.paciente_repository.create_paciente(paciente)
        
    def update_paciente(self, paciente: PacienteModel):
        if paciente.get_id() is None:
            raise ValueError("O ID do paciente não pode ser None.")
        if not paciente.get_nome() or not paciente.get_data_nascimento() or not paciente.get_telefone():
            raise ValueError("Nome, data de nascimento e telefone são obrigatórios.")
        if len(paciente.get_nome()) < 3:
            raise ValueError("O nome do paciente deve ter pelo menos 3 caracteres.")
        if paciente.get_nome().isdigit():
            raise ValueError("O nome do paciente não pode ser apenas numérico.")
        self.paciente_repository.update_paciente(paciente)
        
    def delete_paciente(self, paciente_id):
        if paciente_id is None:
            raise ValueError("O ID do paciente não pode ser None.")
        paciente_consultas = self.paciente_repository.get_all_pacientes()
        for paciente in paciente_consultas:
            if paciente.get_id() == paciente_id:
                raise ValueError("Não é possível excluir um cliente com consultas associadas.")
        self.paciente_repository.delete_paciente(paciente_id)
