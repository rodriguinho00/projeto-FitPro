# ==============================================================================
# PROJETO: SISTEMA DE GESTÃO FITPRO ACADEMIA — VERSÃO PREMIUM 2026
# DESENVOLVEDOR: Rodrigo Santos
# E-MAIL: rodrigosantos5510jau@gmail.com
# GITHUB: rodriguinho00
# ANO: 2026
# DISCIPLINA: PROGRAMAÇÃO PARA INTERNET (ILP951)
# ==============================================================================

# Importação das bibliotecas necessárias do Flask
from flask import Flask, render_template, request, redirect, url_for, flash, session

# Inicialização da aplicação Flask
app = Flask(__name__)

# Chave secreta para criptografia de sessão e flash messages
app.secret_key = 'rodrigo_santos_academia_2026_premium_v2'

# ──────────────────────────────────────────────────────────────────────────────
# DADOS SIMULADOS — VERSÃO COMPLETA COM DETALHES PROFISSIONAIS
# ──────────────────────────────────────────────────────────────────────────────

# Tabela de Funcionários
funcionarios = [
    {'id': 1, 'nome': 'Carlos Silva', 'email': 'carlos@academia.com', 'cpf': '123.456.789-00', 'rg': '12.345.678-9', 'cargo': 'Administrador', 'telefone': '(11) 99999-1111', 'status': 'Ativo'},
    {'id': 2, 'nome': 'Ana Souza', 'email': 'ana@academia.com', 'cpf': '234.567.890-11', 'rg': '23.456.789-0', 'cargo': 'Recepcionista', 'telefone': '(11) 98888-2222', 'status': 'Ativo'},
]

# Tabela de Alunos
alunos = [
    {'id': 1, 'nome': 'Pedro Alves', 'email': 'pedro@email.com', 'cpf': '111.222.333-44', 'rg': '11.222.333-4', 'telefone': '(11) 99999-1111', 'plano': 'Anual', 'pagamento': 'Pago', 'data_vencimento': '2026-12-31', 'status': 'Ativo'},
]

# Tabela de Planos
planos = [
    {'id': 1, 'nome': 'Mensal', 'duracao': '1 mês', 'valor': 'R$ 89,90'},
]

# Tabela de Aulas
aulas = [
    {'id': 1, 'tipo': 'Musculação', 'horario': '06:00 - 07:00', 'instrutor': 'Marcos Lima'},
]

# TABELA DE CLIENTES
clientes = []

# ──────────────────────────────────────────────────────────────────────────────
# ROTAS PÚBLICAS
# ──────────────────────────────────────────────────────────────────────────────

@app.route('/')
def index():

    total_alunos = len(alunos)
    total_aulas = len(aulas)
    total_funcionarios = len(funcionarios)
    total_clientes = len(clientes)

    return render_template(
        'index.html',
        total_alunos=total_alunos,
        total_aulas=total_aulas,
        total_funcionarios=total_funcionarios,
        total_clientes=total_clientes
    )

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form.get('email')
        senha = request.form.get('senha')

        if not email or not senha:
            flash('Preencha todos os campos.', 'danger')
            return render_template('login.html')

        session['usuario_logado'] = email

        flash('Login realizado com sucesso!', 'success')

        return redirect(url_for('dashboard'))

    return render_template('login.html')

@app.route('/logout')
def logout():

    session.pop('usuario_logado', None)

    flash('Logout realizado.', 'info')

    return redirect(url_for('login'))

# ──────────────────────────────────────────────────────────────────────────────
# DASHBOARD
# ──────────────────────────────────────────────────────────────────────────────

@app.route('/dashboard')
def dashboard():

    if 'usuario_logado' not in session:
        flash('Faça login primeiro.', 'warning')
        return redirect(url_for('login'))

    clientes_dashboard = [c for c in clientes if c['dashboard']]

    return render_template(
        'dashboard.html',
        clientes=clientes_dashboard,
        total_clientes=len(clientes)
    )

# ──────────────────────────────────────────────────────────────────────────────
# ALUNOS
# ──────────────────────────────────────────────────────────────────────────────

@app.route('/alunos/listar')
def listar_alunos():

    if 'usuario_logado' not in session:
        flash('Acesso negado.', 'warning')
        return redirect(url_for('login'))

    return render_template(
        'alunos/listar_alunos.html',
        alunos=alunos
    )

# ──────────────────────────────────────────────────────────────────────────────
# CLIENTES
# ──────────────────────────────────────────────────────────────────────────────

@app.route('/clientes')
def listar_clientes():

    if 'usuario_logado' not in session:
        flash('Acesso negado.', 'warning')
        return redirect(url_for('login'))

    return render_template(
        'clientes/listar_clientes.html',
        clientes=clientes
    )

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():

    if request.method == 'POST':

        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        confirmar = request.form.get('confirmar_senha')

        status = request.form.get('status')
        categoria = request.form.get('categoria')
        permissao = request.form.get('permissao')
        descricao = request.form.get('descricao')

        if senha != confirmar:

            flash('As senhas não coincidem.', 'danger')

            return render_template('cadastro.html')

        novo_cliente = {

            'id': len(clientes) + 1,
            'nome': nome,
            'email': email,
            'status': status,
            'categoria': categoria,
            'permissao': permissao,
            'descricao': descricao,
            'dashboard': True,
            'ativo': True

        }

        clientes.append(novo_cliente)

        flash('Conta criada com sucesso!', 'success')

        return redirect(url_for('dashboard'))

    return render_template('cadastro.html')

# ──────────────────────────────────────────────────────────────────────────────
# FUNCIONÁRIOS
# ──────────────────────────────────────────────────────────────────────────────

@app.route('/funcionarios/listar')
def listar_funcionarios():

    if 'usuario_logado' not in session:
        flash('Acesso negado.', 'warning')
        return redirect(url_for('login'))

    return render_template(
        'funcionarios/listar_funcionarios.html',
        funcionarios=funcionarios
    )

# ──────────────────────────────────────────────────────────────────────────────
# PLANOS
# ──────────────────────────────────────────────────────────────────────────────

@app.route('/planos/listar')
def listar_planos():

    if 'usuario_logado' not in session:
        flash('Acesso negado.', 'warning')
        return redirect(url_for('login'))

    return render_template(
        'planos/listar_planos.html',
        planos=planos
    )

# ──────────────────────────────────────────────────────────────────────────────
# AULAS
# ──────────────────────────────────────────────────────────────────────────────

@app.route('/aulas/listar')
def listar_aulas():

    if 'usuario_logado' not in session:
        flash('Acesso negado.', 'warning')
        return redirect(url_for('login'))

    return render_template(
        'aulas/listar_aulas.html',
        aulas=aulas
    )

# ──────────────────────────────────────────────────────────────────────────────
# FINANCEIRO
# ──────────────────────────────────────────────────────────────────────────────

@app.route('/financeiro/alunos')
def financeiro_alunos():

    if 'usuario_logado' not in session:
        flash('Acesso negado.', 'warning')
        return redirect(url_for('login'))

    return render_template(
        'financeiro/alunos.html',
        alunos=alunos
    )

# ──────────────────────────────────────────────────────────────────────────────
# EQUIPE
# ──────────────────────────────────────────────────────────────────────────────

@app.route('/equipe')
def equipe():

    return render_template('sobre_equipe.html')

# ──────────────────────────────────────────────────────────────────────────────
# INICIALIZAÇÃO DO SERVIDOR
# ──────────────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    app.run(debug=True)