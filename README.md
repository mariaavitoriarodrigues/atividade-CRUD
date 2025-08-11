# Clínica Médica
Este projeto foi criado para realizar um CRUD das entidades envolvidas, permitindo um gerenciamento simples e funcional.


## 🗂 Entidades
É utilizado um banco de dados SQLite para gerenciar **pacientes** e **consultas**.

### 1. `paciente`
Tabela responsável por armazenar os dados dos pacientes.

| Campo           | Tipo     | Descrição                              |
|-----------------|----------|----------------------------------------|
| `id`            | INTEGER  | Identificador único do paciente (**PK**). |
| `nome`          | TEXT     | Nome completo do paciente.             |
| `data_nascimento` | DATE   | Data de nascimento do paciente.        |
| `telefone`      | TEXT     | Telefone de contato do paciente.       |

---

### 2. `consulta`
Tabela responsável por armazenar as consultas médicas.

| Campo          | Tipo     | Descrição                              |
|----------------|----------|----------------------------------------|
| `id`           | INTEGER  | Identificador único da consulta (**PK**). |
| `data`         | DATE     | Data em que a consulta será realizada. |
| `especialidade`| TEXT     | Especialidade médica da consulta.      |
| `id_paciente`  | INTEGER  | Identificador do paciente (**FK** para `paciente.id`). |

---

## Relacionamentos

- **Um paciente pode ter várias consultas** (relação **1:N**).
- A coluna `id_paciente` na tabela `consulta` é uma **chave estrangeira** que referencia `paciente.id`.
- Não é permitido excluir um paciente caso ele tenha consultas marcadas.


### Como executar o projeto:

1. Clone o repositório:
    ```bash
    git clone https://github.com/mariaavitoriarodrigues/atividade-CRUD.git
    cd atividade-CRUD
    ````
2. Crie o ambiente virtual:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```
3. Instale as dependências:
    ```bash
    pip install --upgrade pip
    pip install Flask
    ```
4. Execute o projeto:
    ```bash
    python run.py
    ```