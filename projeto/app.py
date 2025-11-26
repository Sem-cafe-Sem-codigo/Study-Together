from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import json
import os
from datetime import datetime
import hashlib
from openai import OpenAI
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'study_together_secret_key_CHANGE_IN_PRODUCTION')

# Arquivo para simular banco de dados
USERS_FILE = 'users.json'

# Configurar cliente da OpenAI (versão 1.0.0+)
openai_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route('/stuart')
def stuart():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('stuart.html')

@app.route('/chat', methods=['POST'])
def chat():
    if 'user' not in session:
        return jsonify({'error': 'Usuário não autenticado'}), 401
    
    user_message = request.json.get('message', '')
    
    if not user_message.strip():
        return jsonify({'error': 'Mensagem vazia'}), 400
    
    try:
        # Verificar se a OpenAI está configurada
        if not client:
            return jsonify({
                'reply': '👋 Olá! Sou o Stuart, seu assistente de estudos!\n\n💡 No momento estou em modo demo. Para ativar minhas respostas completas com IA, adicione no arquivo .env:\n\nOPENAI_API_KEY=sua-chave-aqui\n\n📚 Mesmo assim, posso te ajudar com:\n• Dicas de organização\n• Técnicas de estudo\n• Motivação\n• Planejamento\n\nO que você gostaria de saber?',
                'success': True
            })
        
        # Fazer chamada para a API da OpenAI (versão 1.3.0)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system", 
                    "content": "Você é o Stuart, um assistente de estudos amigável, útil e motivador. Você ajuda estudantes com dúvidas acadêmicas, explica conceitos complexos de forma simples, sugere métodos de estudo eficientes e oferece apoio emocional. Seja claro, direto, educado e use emojis ocasionalmente para tornar a conversa mais amigável. Mantenha as respostas em português brasileiro."
                },
                {
                    "role": "user", 
                    "content": user_message
                }
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        assistant_reply = response.choices[0].message.content
        
        return jsonify({
            'reply': assistant_reply,
            'success': True
        })
        
    except Exception as e:
        print(f"Erro na API da OpenAI: {str(e)}")
        
        # Respostas de fallback para erros comuns
        lower_message = user_message.lower().strip()
        
        fallback_responses = {
            "oi": "👋 Olá! Sou o Stuart, seu assistente de estudos! Como posso ajudar você hoje?",
            "ola": "😊 Olá! Estou aqui para ajudar com seus estudos. Tem alguma dúvida ou precisa de dicas?",
            "oi tudo bem": "Tudo ótimo! Pronto para ajudar você nos estudos. Em que posso ser útil?",
            "obrigado": "🤗 De nada! Fico feliz em ajudar. Se tiver mais alguma dúvida, é só perguntar!",
            "obrigada": "🤗 De nada! Fico feliz em ajudar. Se tiver mais alguma dúvida, é só perguntar!",
            "como você está": "Estou ótimo, obrigado! Pronto para ajudar você com os estudos! 📚",
            "quem é você": "Sou o Stuart! 🤖 Seu assistente de estudos pessoal. Estou aqui para tirar dúvidas, dar dicas de estudo e ajudar você a alcançar seus objetivos!",
            "help": "📚 Posso ajudar você com:\n• Explicação de conceitos\n• Dicas de estudo\n• Planejamento de rotina\n• Motivação\n• Resolução de dúvidas\n\nO que você precisa?",
            "ajuda": "📚 Claro! Posso ajudar com:\n• Explicação de matérias\n• Técnicas de estudo\n• Organização do tempo\n• Dicas de concentração\n• Apoio motivacional\n\nConte-me como posso ajudar!"
        }
        
        if lower_message in fallback_responses:
            return jsonify({
                'reply': fallback_responses[lower_message],
                'success': True
            })
        
        # Resposta genérica para outros erros
        return jsonify({
            'reply': '🔧 Opa, estou com um probleminha técnico no momento!\n\n📚 Mas posso te ajudar com:\n• Dicas de organização de estudos\n• Técnicas de memorização\n• Como montar um cronograma\n• Métodos para manter o foco\n\nO que você gostaria de saber sobre estudos?',
            'success': True
        })

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=4)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

@app.route('/')
def index():
    return redirect(url_for('landing'))

@app.route('/landing')
def landing():
    return render_template('landing.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        users = load_users()
        
        if email in users and users[email]['password'] == hash_password(password):
            session['user'] = {
                'email': email,
                'name': users[email]['name']
            }
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Email ou senha incorretos")
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        interests = request.form.get('interests', '')
        level = request.form.get('level', 'iniciante')
        
        if password != confirm_password:
            return render_template('register.html', error="As senhas não coincidem")
        
        users = load_users()
        
        if email in users:
            return render_template('register.html', error="Este email já está cadastrado")
        
        users[email] = {
            'name': name,
            'password': hash_password(password),
            'interests': interests,
            'level': level,
            'points': 0,
            'streak': 0,
            'created_at': datetime.now().isoformat()
        }
        
        save_users(users)
        
        session['user'] = {
            'email': email,
            'name': name
        }
        
        return redirect(url_for('dashboard'))
    
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    return render_template('dashboard.html', user=session['user'])

@app.route('/materiais', methods=['GET', 'POST'])
def materiais():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    users = load_users()
    user_email = session['user']['email']
    user_data = users.get(user_email, {})
    
    if request.method == 'POST':
        # Adicionar novo material
        title = request.form.get('title')
        material_type = request.form.get('type')
        description = request.form.get('description', '')
        url = request.form.get('url', '')
        
        # Inicializar lista de materiais se não existir
        if 'materials' not in user_data:
            user_data['materials'] = []
        
        # Criar novo material
        new_material = {
            'title': title,
            'type': material_type,
            'description': description,
            'url': url,
            'created_at': datetime.now().isoformat()
        }
        
        user_data['materials'].append(new_material)
        users[user_email] = user_data
        save_users(users)
        
        return redirect(url_for('materiais'))
    
    return render_template('materiais_novo.html', user_data=user_data)

@app.route('/perfil')
def perfil():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    users = load_users()
    user_email = session['user']['email']
    user_data = users.get(user_email, {})
    data_formatada = datetime.fromisoformat(user_data['created_at']).date()

    return render_template('perfil.html', user_data=user_data, data_formatada=data_formatada)

@app.route('/perfil/edit', methods=['GET', 'POST'])
def edit_perfil():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    users = load_users()
    user_email = session['user']['email']
    user_data = users.get(user_email, {})
    
    if request.method == 'POST':
        name = request.form['name']
        interests = request.form.get('interests', '')
        level = request.form.get('level', 'iniciante')
        
        # Atualizar dados do usuário
        users[user_email]['name'] = name
        users[user_email]['interests'] = interests
        users[user_email]['level'] = level
        
        # Atualizar sessão
        session['user']['name'] = name
        
        save_users(users)
        
        return redirect(url_for('perfil'))
    
    return render_template('edit_perfil.html', user_data=user_data)

@app.route('/perfil/change_password', methods=['POST'])
def change_password():
    if 'user' not in session:
        return jsonify({'success': False, 'message': 'Usuário não autenticado'})
    
    users = load_users()
    user_email = session['user']['email']
    
    current_password = request.form['current_password']
    new_password = request.form['new_password']
    confirm_password = request.form['confirm_password']
    
    # Verificar senha atual
    if users[user_email]['password'] != hash_password(current_password):
        return jsonify({'success': False, 'message': 'Senha atual incorreta'})
    
    # Verificar se as novas senhas coincidem
    if new_password != confirm_password:
        return jsonify({'success': False, 'message': 'As novas senhas não coincidem'})
    
    # Atualizar senha
    users[user_email]['password'] = hash_password(new_password)
    save_users(users)
    
    return jsonify({'success': True, 'message': 'Senha alterada com sucesso'})

# Novas rotas adicionadas
@app.route('/study_tracker')
def study_tracker():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    # Dados mock para exemplo
    today_stats = {
        'total_time': 125,  # minutos
        'session_count': 3,
        'average_efficiency': 4
    }
    
    recent_sessions = [
        {
            'time': 45,
            'date': 'Hoje, 14:30',
            'subject': 'Programação',
            'description': 'Funções e loops em Python',
            'efficiency': 4
        },
        {
            'time': 30,
            'date': 'Hoje, 10:15',
            'subject': 'Matemática',
            'description': 'Cálculo diferencial',
            'efficiency': 3
        },
        {
            'time': 50,
            'date': 'Ontem, 16:20',
            'subject': 'Inglês',
            'description': 'Vocabulário técnico',
            'efficiency': 5
        }
    ]
    
    return render_template('conteudo.html', 
                         today_stats=today_stats,
                         recent_sessions=recent_sessions,
                         streak=7)

@app.route('/study')
def study():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    # Dados mock para salas de estudo
    study_rooms = [
        {
            'id': 1,
            'name': 'Sala de Programação Avançada',
            'description': 'Estudo focado em algoritmos e estruturas de dados',
            'participants': 3,
            'max_participants': 6,
            'level': 'Avançado',
            'focus_timer': True,
            'current_timer': '25:00',
            'video_enabled': True,
            'tags': ['Python', 'Algoritmos', 'Estruturas de Dados']
        },
        {
            'id': 2,
            'name': 'Matemática para Vestibulares',
            'description': 'Revisão de conteúdos de matemática do ensino médio',
            'participants': 5,
            'max_participants': 8,
            'level': 'Intermediário',
            'focus_timer': True,
            'current_timer': '15:00',
            'video_enabled': False,
            'tags': ['Matemática', 'Vestibular', 'Revisão']
        },
        {
            'id': 3,
            'name': 'Inglês Conversação',
            'description': 'Prática de conversação em inglês para todos os níveis',
            'participants': 2,
            'max_participants': 4,
            'level': 'Todos os níveis',
            'focus_timer': False,
            'current_timer': '00:00',
            'video_enabled': True,
            'tags': ['Inglês', 'Conversação', 'Idiomas']
        }
    ]
    
    recent_rooms = [
        {
            'id': 1,
            'name': 'Sala de Programação Avançada',
            'last_joined': '2 horas atrás',
            'total_time': '3h 45min'
        }
    ]
    
    return render_template('estudo.html', 
                         study_rooms=study_rooms,
                         recent_rooms=recent_rooms)

@app.route('/study_room/<int:room_id>')
def study_room(room_id):
    if 'user' not in session:
        return redirect(url_for('login'))
    
    # Dados mock para a sala específica
    room_data = {
        'id': room_id,
        'name': 'Sala de Programação Avançada',
        'description': 'Estudo focado em algoritmos e estruturas de dados',
        'subject': 'Programação',
        'participants': [
            {'name': session['user']['name'], 'avatar': session['user']['name'][:2].upper()},
            {'name': 'João Silva', 'avatar': 'JS'},
            {'name': 'Maria Santos', 'avatar': 'MS'}
        ],
        'max_participants': 6,
        'timer_active': True,
        'current_timer': '25:00',
        'focus_timer': True,
        'video_enabled': True,
        'chat_messages': [
            {
                'type': 'system',
                'message': 'Maria Santos entrou na sala',
                'time': '14:25'
            },
            {
                'type': 'user',
                'user': 'João Silva',
                'message': 'Vamos focar no estudo de algoritmos hoje!',
                'time': '14:26'
            }
        ]
    }
    
    return render_template('sala.html', room=room_data)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('landing'))

# Função para formatar data (adicionar ao app.py)
@app.template_filter('format_date')
def format_date_filter(date_string):
    try:
        date_obj = datetime.fromisoformat(date_string)
        return date_obj.strftime('%d/%m/%Y')
    except:
        return date_string

@app.route('/ranking')
def ranking():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    users = load_users()
    
    # Criar lista de usuários ordenada por pontos (decrescente)
    ranked_users = []
    for email, user_data in users.items():
        ranked_users.append({
            'name': user_data['name'],
            'points': user_data['points'],
            'level': user_data['level'],
            'streak': user_data['streak']
        })
    
    # Ordenar por pontos (maior para menor)
    ranked_users.sort(key=lambda x: x['points'], reverse=True)
    
    # Adicionar posições no ranking
    for i, user in enumerate(ranked_users):
        user['position'] = i + 1
    
    # Encontrar posição do usuário atual
    current_user_position = None
    current_user_email = session['user']['email']
    if current_user_email in users:
        current_user_points = users[current_user_email]['points']
        for i, user in enumerate(ranked_users):
            if user['points'] == current_user_points and user['name'] == session['user']['name']:
                current_user_position = i + 1
                break
    
    return render_template('ranking.html', 
                         ranked_users=ranked_users,
                         current_user_position=current_user_position,
                         total_users=len(ranked_users))

if __name__ == '__main__':
    app.run(debug=True)