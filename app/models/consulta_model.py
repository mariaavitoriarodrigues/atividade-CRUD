class ConsultaModel:
    def __init__(self, id, data, especialidade, id_paciente):
        self.__id = id
        self.__data = data
        self.__especialidade = especialidade
        self.__id_paciente = id_paciente
        
    def get_id(self):
        return self.__id
    
    def get_data(self):
        return self.__data
    
    def get_especialidade(self):
        return self.__especialidade
    
    def get_id_paciente(self):
        return self.__id_paciente
    
    def set_id(self, id):
        self.__id = id
        
    def set_data(self, data):
        self.__data = data
        
    def set_especialidade(self, especialidade):
        self.__especialidade = especialidade
    
    def set_id_paciente(self, id_paciente):
        self.__id_paciente = id_paciente