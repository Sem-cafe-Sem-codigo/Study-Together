# 🚀 GUIA DE INSTALAÇÃO - STUDY TOGETHER

## 📋 Pré-requisitos

- **Python 3.8 ou superior** instalado
- **pip** (gerenciador de pacotes Python)
- **Chave da OpenAI** (opcional, para chat IA)

Verificar instalação:
```bash
python --version
pip --version
```

---

## 🔧 INSTALAÇÃO

### **OPÇÃO 1: Com Ambiente Virtual (Recomendado)**

#### Windows (PowerShell):
```powershell
# 1. Extrair o ZIP e entrar na pasta
cd "caminho/para/Sem cafe sem codigo"

# 2. Criar ambiente virtual
python -m venv venv

# 3. Ativar ambiente virtual
.\venv\Scripts\activate

# 4. Instalar dependências
pip install -r requirements.txt

# 5. Configurar variáveis de ambiente
copy .env.example .env
# Editar .env com suas chaves (use notepad .env)

# 6. Executar o projeto
cd projeto
python app.py
```

#### Linux/Mac:
```bash
# 1. Extrair o ZIP e entrar na pasta
cd "caminho/para/Sem cafe sem codigo"

# 2. Criar ambiente virtual
python3 -m venv venv

# 3. Ativar ambiente virtual
source venv/bin/activate

# 4. Instalar dependências
pip install -r requirements.txt

# 5. Configurar variáveis de ambiente
cp .env.example .env
# Editar .env com suas chaves (use nano .env ou vim .env)

# 6. Executar o projeto
cd projeto
python app.py
```

---

### **OPÇÃO 2: Sem Ambiente Virtual (Instalação Global)**

⚠️ **Atenção:** Instala bibliotecas diretamente no Python do sistema.

#### Windows:
```powershell
# 1. Entrar na pasta do projeto
cd "caminho/para/Sem cafe sem codigo"

# 2. Instalar dependências via requirements.txt
pip install -r requirements.txt

# 3. OU instalar manualmente uma por uma
pip install Flask==3.0.0
pip install openai==1.3.0
pip install python-dotenv==1.0.0
pip install Werkzeug==3.0.1
pip install httpx==0.24.1

# 4. Configurar .env
copy python .env.example .env
notepad .env

# 5. Executar
cd projeto
python app.py
```

#### Linux/Mac:
```bash
# 1. Entrar na pasta do projeto
cd "caminho/para/Sem cafe sem codigo"

# 2. Instalar dependências via requirements.txt
pip3 install -r requirements.txt

# 3. OU instalar manualmente uma por uma
pip3 install Flask==3.0.0
pip3 install openai==1.3.0
pip3 install python-dotenv==1.0.0
pip3 install Werkzeug==3.0.1
pip3 install httpx==0.24.1

# 4. Configurar .env
cp .env.example .env
nano .env

# 5. Executar
cd projeto
python3 app.py
```

---

## 🔑 Configurar Variáveis de Ambiente

Editar o arquivo `.env` na raiz do projeto:

```dotenv
# .env
SECRET_KEY=sua-chave-secreta-aqui-mude-em-producao
OPENAI_API_KEY=sk-proj-sua-chave-openai-aqui

FLASK_ENV=development
FLASK_DEBUG=True
USERS_FILE=users.json
```

### **Como obter chave da OpenAI:**
1. Acesse: https://platform.openai.com/api-keys
2. Crie uma conta (se não tiver)
3. Gere uma nova chave API
4. Copie e cole no arquivo `.env`

**Nota:** O projeto funciona SEM a chave OpenAI (modo demo), mas o chat IA não estará ativo.

---

## ▶️ EXECUTAR O PROJETO

```bash
# Entrar na pasta do código
cd projeto

# Executar o servidor Flask
python app.py
```

**Servidor rodando em:** http://localhost:5000

Acesse no navegador: http://127.0.0.1:5000

---

## 🛑 PARAR O SERVIDOR

Pressione: **CTRL + C**

---

## 🐛 SOLUÇÃO DE PROBLEMAS

### **Erro: "python não é reconhecido"**
```bash
# Tentar:
python3 app.py
# Ou:
py app.py
```

### **Erro: "No module named 'flask'"**
```bash
# Reinstalar dependências:
pip install -r requirements.txt
```

### **Erro: "TypeError: Client.__init__() got an unexpected keyword argument 'proxies'"**
```bash
# Corrigir versão do httpx:
pip uninstall httpx -y
pip install httpx==0.24.1
```

### **Erro: "The api_key client option must be set"**
- Verifique se o arquivo `.env` existe na raiz do projeto
- Verifique se `OPENAI_API_KEY` está configurado no `.env`
- OU deixe vazio para usar modo demo (sem IA real)

### **Porta 5000 já em uso**
```bash
# Editar app.py, última linha:
app.run(debug=True, port=5001)  # Trocar porta
```

### **Erro ao ativar ambiente virtual no Windows**
```powershell
# Se der erro de política de execução:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# Depois tentar novamente:
.\venv\Scripts\activate
```

---

## 📦 DEPENDÊNCIAS (requirements.txt)

```
Flask==3.0.0          # Framework web
openai==1.3.0         # API OpenAI (chat IA)
python-dotenv==1.0.0  # Variáveis de ambiente
Werkzeug==3.0.1       # Utilitários Flask
httpx==0.24.1         # Cliente HTTP (compatibilidade)
```

---

## 📁 ESTRUTURA DO PROJETO

```
Sem cafe sem codigo/
├── .env                    # Variáveis de ambiente (criar)
├── .env.example            # Template de configuração
├── requirements.txt        # Dependências Python
├── README.md               # Documentação principal
├── INSTALACAO.md          # Este guia
├── ANALISE_COMPLETA.md    # Análise técnica
├── PENDENCIAS.md          # Melhorias futuras
└── projeto/
    ├── app.py             # Aplicação Flask (executar este)
    ├── users.json         # Banco de dados temporário
    ├── static/            # CSS
    └── templates/         # HTML
```

---

## 🎯 COMANDOS RÁPIDOS

### **Setup Completo (Windows com venv):**
```powershell
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
notepad .env
cd projeto
python app.py
```

### **Setup Completo (Linux/Mac com venv):**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
nano .env
cd projeto
python app.py
```

### **Setup Sem venv (qualquer OS):**
```bash
pip install -r requirements.txt
# Configurar .env manualmente
cd projeto
python app.py
```

---

## ✅ CHECKLIST DE INSTALAÇÃO

- [ ] Python 3.8+ instalado
- [ ] pip funcionando
- [ ] Projeto extraído do ZIP
- [ ] Ambiente virtual criado (opcional)
- [ ] Dependências instaladas (`pip install -r requirements.txt`)
- [ ] Arquivo `.env` criado e configurado
- [ ] Chave OpenAI adicionada (opcional)
- [ ] Servidor rodando (`python app.py`)
- [ ] Navegador aberto em http://localhost:5000
- [ ] Página de login/cadastro carregando

---

## 🆘 SUPORTE

**Problemas comuns:**
1. Verifique se está na pasta `projeto` ao executar `python app.py`
2. Verifique se o `.env` existe e está na raiz (não dentro de `projeto/`)
3. Verifique se todas as dependências foram instaladas
4. Tente reinstalar: `pip uninstall flask openai -y && pip install -r requirements.txt`

**Logs de erro:**
- Copie a mensagem de erro completa
- Verifique a seção "SOLUÇÃO DE PROBLEMAS" acima

---

## 🎓 PRIMEIRO ACESSO

1. Acesse: http://localhost:5000
2. Clique em **"Começar Agora"**
3. Faça seu **Cadastro**
4. Faça **Login**
5. Explore o **Dashboard**

**Usuário de teste** (se já existir no `users.json`):
- Email: `teste@email.com`
- Senha: `senha123`

---

**Versão:** 2.0  
**Data:** Novembro 2025  
**Score:** 8.5/10
