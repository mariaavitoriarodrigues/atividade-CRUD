CREATE TABLE paciente (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    data_nascimento DATE,
    telefone TEXT
);

CREATE TABLE consulta (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data DATE NOT NULL,
    especialidade TEXT NOT NULL,
    id_paciente INTEGER NOT NULL,
    FOREIGN KEY (id_paciente) REFERENCES paciente (id) ON DELETE CASCADE
);
