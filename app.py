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

# Tabela de Funcionários: Com CPF, RG, cargo e dados profissionais
funcionarios = [
    {'id': 1, 'nome': 'Carlos Silva', 'email': 'carlos@academia.com', 'cpf': '123.456.789-00', 'rg': '12.345.678-9', 'cargo': 'Administrador', 'telefone': '(11) 99999-1111', 'status': 'Ativo'},
    {'id': 2, 'nome': 'Ana Souza', 'email': 'ana@academia.com', 'cpf': '234.567.890-11', 'rg': '23.456.789-0', 'cargo': 'Recepcionista', 'telefone': '(11) 98888-2222', 'status': 'Ativo'},
    {'id': 3, 'nome': 'Marcos Lima', 'email': 'marcos@academia.com', 'cpf': '345.678.901-22', 'rg': '34.567.890-1', 'cargo': 'Instrutor de Musculação', 'telefone': '(11) 97777-3333', 'status': 'Ativo'},
    {'id': 4, 'nome': 'Juliana Costa', 'email': 'juliana@academia.com', 'cpf': '456.789.012-33', 'rg': '45.678.901-2', 'cargo': 'Instrutora de Yoga', 'telefone': '(11) 96666-4444', 'status': 'Inativo'},
    {'id': 5, 'nome': 'Rafael Mendes', 'email': 'rafael@academia.com', 'cpf': '567.890.123-44', 'rg': '56.789.012-3', 'cargo': 'Administrador', 'telefone': '(11) 95555-5555', 'status': 'Ativo'},
]

# Tabela de Alunos: Com CPF, RG, status de pagamento e plano contratado
alunos = [
    {'id': 1, 'nome': 'Pedro Alves', 'email': 'pedro@email.com', 'cpf': '111.222.333-44', 'rg': '11.222.333-4', 'telefone': '(11) 99999-1111', 'plano': 'Anual', 'pagamento': 'Pago', 'data_vencimento': '2026-12-31', 'status': 'Ativo'},
    {'id': 2, 'nome': 'Fernanda Rocha', 'email': 'ferna@email.com', 'cpf': '222.333.444-55', 'rg': '22.333.444-5', 'telefone': '(11) 98888-2222', 'plano': 'Trimestral', 'pagamento': 'Pago', 'data_vencimento': '2026-06-30', 'status': 'Ativo'},
    {'id': 3, 'nome': 'Lucas Martins', 'email': 'lucas@email.com', 'cpf': '333.444.555-66', 'rg': '33.444.555-6', 'telefone': '(11) 97777-3333', 'plano': 'Mensal', 'pagamento': 'Atrasado', 'data_vencimento': '2026-02-28', 'status': 'Ativo'},
    {'id': 4, 'nome': 'Camila Ferreira', 'email': 'camila@email.com', 'cpf': '444.555.666-77', 'rg': '44.555.666-7', 'telefone': '(11) 96666-4444', 'plano': 'Semestral', 'pagamento': 'Pendente', 'data_vencimento': '2026-03-31', 'status': 'Inativo'},
    {'id': 5, 'nome': 'Bruno Oliveira', 'email': 'bruno@email.com', 'cpf': '555.666.777-88', 'rg': '55.666.777-8', 'telefone': '(11) 95555-5555', 'plano': 'Mensal', 'pagamento': 'Pago', 'data_vencimento': '2026-04-15', 'status': 'Ativo'},
    {'id': 6, 'nome': 'Tatiane Nunes', 'email': 'tatiane@email.com', 'cpf': '666.777.888-99', 'rg': '66.777.888-9', 'telefone': '(11) 94444-6666', 'plano': 'Trimestral', 'pagamento': 'Pago', 'data_vencimento': '2026-05-30', 'status': 'Ativo'},
]

# Tabela de Planos: Com valores, benefícios e quantidade de alunos
planos = [
    {'id': 1, 'nome': 'Mensal', 'duracao': '1 mês', 'valor': 'R$ 89,90', 'aulas': 'Musculação, Cardio', 'alunos': 2, 'beneficios': ['Acesso ilimitado', 'Avaliação física', 'Treino personalizado']},
    {'id': 2, 'nome': 'Trimestral', 'duracao': '3 meses', 'valor': 'R$ 239,90', 'aulas': 'Musculação, Cardio, Spinning', 'alunos': 2, 'beneficios': ['Acesso ilimitado', 'Avaliação física', 'Treino personalizado', 'Acompanhamento nutricional']},
    {'id': 3, 'nome': 'Semestral', 'duracao': '6 meses', 'valor': 'R$ 419,90', 'aulas': 'Musculação, Cardio, Spinning, Yoga', 'alunos': 1, 'beneficios': ['Acesso ilimitado', 'Avaliação física', 'Treino personalizado', 'Acompanhamento nutricional', 'Sessões de pilates']},
    {'id': 4, 'nome': 'Anual', 'duracao': '12 meses', 'valor': 'R$ 719,90', 'aulas': 'Todas as modalidades', 'alunos': 1, 'beneficios': ['Acesso ilimitado', 'Avaliação física', 'Treino personalizado', 'Acompanhamento nutricional', 'Sessões de pilates', 'Consultoria de saúde']},
    {'id': 5, 'nome': 'Estudante', 'duracao': '1 mês', 'valor': 'R$ 59,90', 'aulas': 'Musculação, Cardio', 'alunos': 0, 'beneficios': ['Acesso ilimitado', 'Avaliação física']},
]

# Tabela de Aulas: Com tipos, horários, instrutores e vagas
aulas = [
    {'id': 1, 'tipo': 'Musculação', 'horario': '06:00 - 07:00', 'instrutor': 'Marcos Lima', 'vagas': 15, 'alunos_inscritos': 12, 'sala': 'Sala 1', 'descricao': 'Treino de força com foco em hipertrofia'},
    {'id': 2, 'tipo': 'Yoga', 'horario': '07:00 - 08:00', 'instrutor': 'Juliana Costa', 'vagas': 20, 'alunos_inscritos': 18, 'sala': 'Sala 2', 'descricao': 'Aula de yoga para relaxamento e flexibilidade'},
    {'id': 3, 'tipo': 'Spinning', 'horario': '17:00 - 18:00', 'instrutor': 'Marcos Lima', 'vagas': 25, 'alunos_inscritos': 22, 'sala': 'Sala 3', 'descricao': 'Aula de bicicleta estacionária com música animada'},
    {'id': 4, 'tipo': 'Muay Thai', 'horario': '18:00 - 19:00', 'instrutor': 'Carlos Silva', 'vagas': 12, 'alunos_inscritos': 10, 'sala': 'Sala 4', 'descricao': 'Aula de luta tailandesa para defesa pessoal'},
    {'id': 5, 'tipo': 'Pilates', 'horario': '19:00 - 20:00', 'instrutor': 'Juliana Costa', 'vagas': 15, 'alunos_inscritos': 14, 'sala': 'Sala 2', 'descricao': 'Aula de pilates para fortalecimento do core'},
    {'id': 6, 'tipo': 'CrossFit', 'horario': '20:00 - 21:00', 'instrutor': 'Rafael Mendes', 'vagas': 20, 'alunos_inscritos': 19, 'sala': 'Sala 1', 'descricao': 'Aula de CrossFit com exercícios funcionais'},
]

# ──────────────────────────────────────────────────────────────────────────────
# ROTAS PÚBLICAS (Acessíveis por qualquer pessoa)
# ──────────────────────────────────────────────────────────────────────────────

@app.route('/')
def index():
    # Calcula estatísticas dinâmicas para exibir na página inicial
    total_alunos = len(alunos)
    total_aulas = len(aulas)
    total_funcionarios = len(funcionarios)
    alunos_ativos = len([a for a in alunos if a['status'] == 'Ativo'])
    
    return render_template('index.html', 
                         total_alunos=total_alunos,
                         total_aulas=total_aulas,
                         total_funcionarios=total_funcionarios,
                         alunos_ativos=alunos_ativos)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        senha = request.form.get('senha', '').strip()
        
        if not email or not senha:
            flash('Erro: Preencha todos os campos para entrar.', 'danger')
            return render_template('login.html')
        
        session['usuario_logado'] = email
        flash('Bem-vindo ao FitPro! Login realizado com sucesso.', 'success')
        return redirect(url_for('listar_alunos'))
    
    return render_template('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome', '').strip()
        email = request.form.get('email', '').strip()
        senha = request.form.get('senha', '').strip()
        conf = request.form.get('confirmar_senha', '').strip()
        
        if not nome or not email or not senha or not conf:
            flash('Atenção: Todos os campos são obrigatórios.', 'danger')
            return render_template('cadastro.html')
        
        if senha != conf:
            flash('Erro: As senhas digitadas não coincidem.', 'danger')
            return render_template('cadastro.html')
        
        flash('Conta criada com sucesso! Agora você já pode entrar.', 'success')
        return redirect(url_for('login'))
    
    return render_template('cadastro.html')

@app.route('/logout')
def logout():
    session.pop('usuario_logado', None)
    flash('Sessão encerrada. Até logo!', 'info')
    return redirect(url_for('login'))

# ──────────────────────────────────────────────────────────────────────────────
# ROTAS PROTEGIDAS — ALUNOS
# ──────────────────────────────────────────────────────────────────────────────

@app.route('/alunos/listar')
def listar_alunos():
    if 'usuario_logado' not in session:
        flash('Acesso negado: Por favor, faça login primeiro.', 'warning')
        return redirect(url_for('login'))
    return render_template('alunos/listar_alunos.html', alunos=alunos)

# ──────────────────────────────────────────────────────────────────────────────
# ROTAS PROTEGIDAS — FUNCIONÁRIOS
# ──────────────────────────────────────────────────────────────────────────────

@app.route('/funcionarios/listar')
def listar_funcionarios():
    if 'usuario_logado' not in session:
        flash('Acesso negado.', 'warning')
        return redirect(url_for('login'))
    return render_template('funcionarios/listar_funcionarios.html', funcionarios=funcionarios)

# ──────────────────────────────────────────────────────────────────────────────
# ROTAS PROTEGIDAS — PLANOS
# ──────────────────────────────────────────────────────────────────────────────

@app.route('/planos/listar')
def listar_planos():
    if 'usuario_logado' not in session:
        flash('Acesso negado.', 'warning')
        return redirect(url_for('login'))
    return render_template('planos/listar_planos.html', planos=planos)

# ──────────────────────────────────────────────────────────────────────────────
# ROTAS PROTEGIDAS — AULAS
# ──────────────────────────────────────────────────────────────────────────────

@app.route('/aulas/listar')
def listar_aulas():
    if 'usuario_logado' not in session:
        flash('Acesso negado.', 'warning')
        return redirect(url_for('login'))
    return render_template('aulas/listar_aulas.html', aulas=aulas)

# ──────────────────────────────────────────────────────────────────────────────
# ROTAS PROTEGIDAS — FINANCEIRO
# ──────────────────────────────────────────────────────────────────────────────

@app.route('/financeiro/alunos')
def financeiro_alunos():
    if 'usuario_logado' not in session:
        flash('Acesso negado.', 'warning')
        return redirect(url_for('login'))
    return render_template('financeiro/alunos.html', alunos=alunos)

# ──────────────────────────────────────────────────────────────────────────────
# ROTA DA EQUIPE (Desenvolvedor)
# ──────────────────────────────────────────────────────────────────────────────

@app.route('/equipe')
def equipe():
    return render_template('sobre_equipe.html')

# ──────────────────────────────────────────────────────────────────────────────
# INICIALIZAÇÃO DO SERVIDOR
# ──────────────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    app.run(debug=True)
