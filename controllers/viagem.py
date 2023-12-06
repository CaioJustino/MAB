# IMPORTS
from flask import render_template, request, url_for, redirect, flash, Blueprint
from utils.utils import db
from utils.models import User, Passageiro, Viagem, Motorista, Pagamento, Veiculo
from flask_login import login_required, current_user
import datetime

# CONFIGS
bp_vi = Blueprint("vi", __name__, template_folder="templates")
mapbox_access_token = "pk.eyJ1IjoiY2p1c3QiLCJhIjoiY2xwNWU0bGtnMWViaTJscXZlZG5yZXpqaiJ9.ClDZFNMZlZD0tKHhAYbr-w"

# SOLICITAR VIAGEM - PASSAGEIRO
@bp_vi.route('/solicitar', methods=['GET','POST'])
@login_required
def solicitar_vi():
  if request.method == 'GET':
    if current_user.adm == 1:
      return redirect('/administrador/perfil')
    
    else:
      if (Passageiro.query.filter_by(id = current_user.id)).count() == 1:
        if (Viagem.query.filter_by(id_pass = current_user.id).filter_by(status = 1).count() == 1):
          return redirect(url_for('vi.acompanhar_vi_pass')) 

        else:
          return render_template('vi/solicitar_vi.html')
        
      elif (Motorista.query.filter_by(id = current_user.id)).count() == 1:
        return redirect('/motorista/perfil')
  
  if request.method == 'POST':
    passg = Passageiro.query.filter_by(id = current_user.id).first()
    embarque = request.form.get('embarque address-search')
    desembarque = request.form.get('desembarque address-search')
    tipo = request.form.get('tipo')
    data_hora = datetime.datetime.now()

    pag = Pagamento(passg.id, tipo, 10)
    db.session.add(pag)
    db.session.commit()
    vi = Viagem(passg.id, 0, pag.id, 0, embarque, desembarque, data_hora, False, True)    
    db.session.add(vi)
    db.session.commit()
    
    return redirect(url_for('vi.acompanhar_vi_pass', id=current_user.id, vi=vi))

# ACOMPANHAR VIAGEM - PASSAGEIRO
@bp_vi.route('/passageiro', methods=['GET'])
@login_required
def acompanhar_vi_pass():
  if current_user.adm == 1:
    return redirect('/administrador/perfil')
    
  else:
    if (Passageiro.query.filter_by(id = current_user.id)).count() == 1:
      if (Viagem.query.filter_by(id_pass = current_user.id).filter_by(status = 1)).count() == 0:
        flash('Viagem finalizada!', "success")
        return redirect('/passageiro/perfil')
      
      else:
        viagem = Viagem.query.filter_by(id_pass = current_user.id).filter_by(status = 1).first()
        pag = Pagamento.query.filter_by(id = viagem.id_pag).first()
        user_moto = User.query.filter_by(id = viagem.id_moto).first()
        ve = Veiculo.query.filter_by(id = viagem.id_ve).first()
        return render_template('vi/acompanhar_vi_pass.html', mapbox_access_token=mapbox_access_token, viagem=viagem, pag=pag, user_moto=user_moto, ve=ve)

    elif (Motorista.query.filter_by(id = current_user.id)).count() == 1:
      return redirect('/motorista/perfil')

# ATUALIZAR VIAGEM - PASSAGEIRO
@bp_vi.route('/editar', methods=['POST'])
@login_required
def update_vi():
  if current_user.adm == 1:
    return redirect('/administrador/perfil')
  
  else:
    if (Motorista.query.filter_by(id = current_user.id)).count() == 1:
      return redirect('/motorista/perfil')

    elif (Passageiro.query.filter_by(id = current_user.id)).count() == 1:
      viagem = Viagem.query.filter_by(id_pass = current_user.id).filter_by(status = 1).first()
      pag = Pagamento.query.filter_by(id = viagem.id_pag).first()
      viagem.embarque = request.form.get('embarque')
      viagem.desembarque = request.form.get('desembarque')
      pag.tipo = request.form.get('tipo')
      
      db.session.commit()
      
      return redirect(url_for('vi.acompanhar_vi_pass'))

# BUSCAR VIAGEM - MOTORISTA
@bp_vi.route('/buscar', methods=['GET'])
@login_required
def buscar_vi():
  if request.method == 'GET':
    if current_user.adm == 1:
      return redirect('/administrador/perfil')

    else:
      if (Motorista.query.filter_by(id = current_user.id)).count() == 1:
        if Viagem.query.filter_by(status = 1).filter_by(aceitacao = 0).count() == 0 and Viagem.query.filter_by(id_moto = current_user.id).filter_by(status = 1).count() == 0:
          flash('Nenhuma Viagem foi encontrada!', "danger")
          return redirect('/motorista/perfil') 
        
        elif Viagem.query.filter_by(id_moto = current_user.id).filter_by(status = 1).count() == 1:
          return redirect(url_for('vi.acompanhar_vi_moto')) 

        else:
          vi_count = Viagem.query.filter_by(status = 1).filter_by(aceitacao = 0).count()
          viagem = Viagem.query.filter_by(status = 1).filter_by(aceitacao = 0).order_by(Viagem.id.desc()).first()
          pag = Pagamento.query.filter_by(id = viagem.id_pag).first()
          return render_template('vi/buscar_vi.html', mapbox_access_token=mapbox_access_token, vi_count=vi_count, viagem=viagem, pag=pag)

      elif (Passageiro.query.filter_by(id = current_user.id)).count() == 1:
        return redirect('/passageiro/perfil')

# ACEITAR VIAGEM - MOTORISTA
@bp_vi.route('/aceitar/<int:id>', methods=['POST'])
@login_required
def aceitar_vi(id):
  if current_user.adm == 1:
    return redirect('/administrador/perfil')

  else:
    if (Passageiro.query.filter_by(id = current_user.id)).count() == 1:
      return redirect('/passageiro/perfil')
      
    elif (Motorista.query.filter_by(id = current_user.id)).count() == 1:
      viagem = Viagem.query.get(id)
      ve = Veiculo.query.filter_by(id_moto = current_user.id).first()
      viagem.id_moto = current_user.id
      viagem.id_ve = ve.id
      viagem.aceitacao = 1
      db.session.commit()
      return redirect(url_for('vi.acompanhar_vi_moto'))

# ACOMPANHAR VIAGEM - MOTORISTA
@bp_vi.route('/motorista', methods=['GET'])
@login_required
def acompanhar_vi_moto():
  if current_user.adm == 1:
      return redirect('/administrador/perfil')
    
  else:
    if (Passageiro.query.filter_by(id = current_user.id)).count() == 1:
      return redirect('/passageiro/perfil')
      
    elif (Motorista.query.filter_by(id = current_user.id)).count() == 1:
      if (Viagem.query.filter_by(id_moto = current_user.id).filter_by(status = 1)).count() == 0:
        return redirect('/motorista/perfil')
      
      else:
        viagem = Viagem.query.filter_by(id_moto = current_user.id).filter_by(status = 1).first()
        user_pass = User.query.filter_by(id = viagem.id_pass).first()
        pag = Pagamento.query.filter_by(id = viagem.id_pag).first()
        return render_template('vi/acompanhar_vi_moto.html', mapbox_access_token=mapbox_access_token, viagem=viagem, user_pass=user_pass, pag=pag)

# FINALIZAR VIAGEM - MOTORISTA
@bp_vi.route('/finalizar/<int:id>', methods=['POST'])
@login_required
def finalizar_vi(id):
  if current_user.adm == 1:
    return redirect('/administrador/perfil')

  else:
    if (Passageiro.query.filter_by(id = current_user.id)).count() == 1:
      return redirect('/passageiro/perfil')

    elif (Motorista.query.filter_by(id = current_user.id)).count() == 1:
      viagem = Viagem.query.get(id)
      viagem.status = 0
      db.session.commit()
      flash('Viagem finalizada!', "success")
      return redirect('/motorista/perfil')

# CANCELAR VIAGEM
@bp_vi.route('/cancelar', methods=['POST'])
@login_required
def cancelar_vi():
  if current_user.adm == 1:
    return redirect('/administrador/perfil')
  
  else:
    if (Passageiro.query.filter_by(id = current_user.id)).count() == 1:
      viagem = Viagem.query.filter_by(id_pass = current_user.id).filter_by(status = 1).first()
      viagem.status = 0
      viagem.aceitacao = 0
      db.session.commit()
      flash('Viagem cancelada!', "success")
      return redirect('/passageiro/perfil')
      
    elif (Motorista.query.filter_by(id = current_user.id)).count() == 1:
      viagem = Viagem.query.filter_by(id_moto = current_user.id).filter_by(status = 1).first()
      viagem.status = 0
      viagem.aceitacao = 0
      db.session.commit()
      flash('Viagem cancelada!', "success")
      return redirect('/motorista/perfil')
