from app import app
from flask import render_template, request, redirect, url_for

from app.models.consulta_model import ConsultaModel
from app.service.consulta_service import ConsultaService
from app.models.paciente_model import PacienteModel
from app.service.paciente_service import PacienteService

consulta_service = ConsultaService()
paciente_service = PacienteService()

@app.route('/')
def index():
    return redirect(url_for('listar_pacientes'))

@app.route('/pacientes')
def listar_pacientes():
    pacientes = paciente_service.get_all_pacientes()
    return render_template('pacientes/list_pacientes.html', pacientes=pacientes)

@app.route('/pacientes/novo', methods=['GET', 'POST'])
def criar_paciente():
    if request.method == 'POST':
        nome = request.form['nome']
        data_nascimento = request.form['data_nascimento']
        telefone = request.form['telefone']
        paciente_service.create_paciente(PacienteModel(
            id=None,
            nome=nome,
            data_nascimento=data_nascimento,
            telefone=telefone))
        return redirect(url_for('listar_pacientes'))
    return render_template('pacientes/form_pacientes.html')

@app.route('/pacientes/editar/<int:id>', methods=['GET', 'POST'])
def editar_paciente(id):
    paciente = paciente_service.get_paciente_by_id(id)
    if request.method == 'POST':
        paciente_service.update_paciente(
            PacienteModel(
                id,
                request.form['nome'],
                request.form['data_nascimento'],
                request.form['telefone']
            )
        )
        return redirect(url_for('listar_pacientes'))
    return render_template('pacientes/form_pacientes.html', paciente=paciente)

@app.route('/pacientes/excluir/<int:id>')
def excluir_paciente(id):
    paciente_service.delete_paciente(id)
    return redirect(url_for('listar_pacientes'))

@app.route('/consultas')
def listar_consultas():
    consultas = consulta_service.get_all_consultas()
    return render_template('consultas/list_consultas.html', consultas=consultas)

@app.route('/consultas/nova', methods=['GET', 'POST'])
def criar_consulta():
    pacientes = paciente_service.get_all_pacientes()
    if request.method == 'POST':
        id_paciente = request.form['id_paciente']
        data = request.form['data']
        especialidade = request.form['especialidade']

        consulta_service.create_consulta(ConsultaModel(
            id=None,
            id_paciente=id_paciente,
            data=data,
            especialidade=especialidade
        ))
        return redirect(url_for('listar_consultas'))
    return render_template('consultas/form_consultas.html', pacientes=pacientes)

@app.route('/consultas/editar/<int:id>', methods=['GET', 'POST'])
def editar_consulta(id):
    consulta = consulta_service.get_consulta_by_id(id)
    pacientes = paciente_service.get_all_pacientes()
    if request.method == 'POST':
        consulta_service.update_consulta(ConsultaModel(
            id=id,
            id_paciente=request.form['id_paciente'],
            data=request.form['data'],
            especialidade=request.form['especialidade']
        ))
        return redirect(url_for('listar_consultas'))
    return render_template('consultas/form_consultas.html', consulta=consulta, pacientes=pacientes)

@app.route('/consultas/excluir/<int:id>')
def excluir_consulta(id):
    consulta_service.delete_consulta(id)
    return redirect(url_for('listar_consultas'))