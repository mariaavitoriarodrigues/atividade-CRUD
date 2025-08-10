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
    return render_template('base.html')