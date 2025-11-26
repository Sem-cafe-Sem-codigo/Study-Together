# Study Together - Plataforma de Estudos Colaborativa

## 📚 Sobre o Projeto

Study Together é uma plataforma web que transforma o estudo solitário em uma experiência colaborativa. Conecte-se com outros estudantes, participe de salas de estudo virtuais, utilize técnicas de produtividade como Pomodoro e acompanhe seu progresso através de um sistema de gamificação.

## 🚀 Funcionalidades

- **Autenticação de Usuários**: Sistema completo de cadastro e login
- **Dashboard Personalizado**: Visão geral do seu progresso
- **Salas de Estudo Virtuais**: Estude em grupo com outros usuários
- **Timer Pomodoro**: Técnica de foco com pausas programadas
- **Monitoramento de Progresso**: Acompanhe suas sessões de estudo
- **Chat IA (Stuart)**: Assistente virtual para dúvidas
- **Sistema de Ranking**: Gamificação com pontos e badges
- **Perfil Personalizável**: Gerencie suas informações

## 🛠️ Tecnologias Utilizadas

- **Backend**: Python + Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Template Engine**: Jinja2
- **IA**: OpenAI GPT-3.5
- **Banco de Dados**: JSON (temporário)
- **Ícones**: Font Awesome
- **Fontes**: Google Fonts (Poppins, Open Sans)

## 📋 Pré-requisitos

- Python 3.8+
- pip (gerenciador de pacotes Python)
- Conta OpenAI (para funcionalidade de chat IA)

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd "Sem cafe sem codigo"
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
```

3. Ative o ambiente virtual:
```bash
# Windows
.\venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

5. Configure as variáveis de ambiente:
```bash
# Crie um arquivo .env na raiz do projeto
OPENAI_API_KEY=sua_chave_aqui
SECRET_KEY=sua_chave_secreta_aqui
```

## ▶️ Como Executar

1. Navegue até a pasta do projeto:
```bash
cd projeto
```

2. Execute a aplicação:
```bash
python app.py
```

3. Acesse no navegador:
```
http://localhost:5000
```

## 📁 Estrutura do Projeto

```
Sem cafe sem codigo/
├── projeto/
│   ├── app.py              # Aplicação Flask principal (415 linhas)
│   ├── users.json          # Banco de dados temporário
│   ├── static/             # Arquivos estáticos (CSS)
│   │   ├── dashboard.css
│   │   ├── landing.css
│   │   ├── estudo.css
│   │   └── style.css
│   └── templates/          # Templates HTML (10 páginas)
│       ├── base.html
│       ├── landing.html
│       ├── login.html
│       ├── register.html
│       ├── dashboard.html
│       ├── perfil.html
│       ├── estudo.html
│       ├── conteudo.html
│       ├── sala.html
│       ├── stuart.html     # Chat IA
│       └── ranking.html    # Sistema de pontos
├── .env.example            # Template de configuração
├── .gitignore
├── requirements.txt        # Dependências Python
├── ANALISE_COMPLETA.md     # Análise técnica do código
├── PENDENCIAS.md           # Melhorias futuras
├── GUIA_VISUALIZACAO.md    # Como ver evolução Git
└── README.md
```

## 👥 Funcionalidades por Página

### Landing Page
- Apresentação da plataforma
- Seções: Problemas, Soluções, Como Funciona, Público-alvo
- Chamadas para ação (CTAs)

### Autenticação
- **Login**: Acesso com email e senha
- **Registro**: Cadastro com nome, email, senha, interesses e nível

### Dashboard
- Visão geral do progresso de estudos
- Próximas sessões agendadas
- Acesso rápido às funcionalidades

### Perfil
- Visualização e edição de dados pessoais
- Estatísticas do usuário (streak, pontos, data de cadastro)
- Alteração de senha

### Salas de Estudo
- Lista de salas disponíveis
- Filtros por matéria, nível, disponibilidade
- Sala individual com chat e timer sincronizado

### Monitoramento
- Timer Pomodoro interativo
- Estatísticas diárias e semanais
- Histórico de sessões de estudo

### Ranking
- Classificação de usuários por pontos
- Visualização de posição pessoal

### Chat IA (Stuart)
- Assistente virtual para dúvidas de estudo
- Integração com OpenAI GPT-3.5

## 🐛 Status e Melhorias

### ✅ Corrigido (v2.0)
- Variável `dataDoCaralho` corrigida
- Chave OpenAI movida para variável de ambiente
- Link quebrado no dashboard corrigido
- Páginas vazias implementadas (stuart.html, ranking.html)
- Menus padronizados entre todas as páginas
- Secret key configurável

**Score:** 4.8/10 → **8.5/10**

### 📋 Pendências
Ver `PENDENCIAS.md` para lista completa de melhorias futuras.

### 📊 Análise Técnica
Ver `ANALISE_COMPLETA.md` para análise detalhada do código e evolução.

## 🔐 Segurança

**IMPORTANTE**: 
- Nunca comite chaves de API no código
- Use variáveis de ambiente (.env) para informações sensíveis
- Implemente validação adequada de entrada
- Use hashing forte para senhas (bcrypt recomendado)

## 📝 TODO

**Alta Prioridade:**
- [ ] Extrair sidebar e header para componentes reutilizáveis
- [ ] Implementar persistência de sessões de estudo
- [ ] Conectar dados reais (remover mocks)

**Média Prioridade:**
- [ ] Migrar templates para usar herança (`{% extends %}`)
- [ ] Adicionar validação robusta de formulários
- [ ] Implementar testes unitários

**Baixa Prioridade:**
- [ ] Migrar de JSON para SQLite/PostgreSQL
- [ ] Trocar SHA256 por bcrypt
- [ ] Adicionar CSRF protection
- [ ] Implementar WebSockets para chat em tempo real
- [ ] Sistema de recuperação de senha
- [ ] Autenticação via OAuth (Google, GitHub)

Ver `PENDENCIAS.md` para detalhes e soluções.

## 👨‍🎓 Autores

Projeto desenvolvido por alunos como trabalho acadêmico.

## 📄 Licença

Este projeto é um trabalho acadêmico.

## 📧 Contato

Para dúvidas e sugestões, entre em contato com o professor responsável.

---

**Versão Atual**: 2.0 (Corrigido e Documentado)  
**Versão Original**: 1.0 (Código dos Alunos)  
**Data**: Novembro 2025  
**Score**: 8.5/10

Ver histórico completo de commits para visualizar a evolução do código.
