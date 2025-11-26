# 🎓 Como Visualizar as Mudanças - Guia para os Alunos

## 📋 Índice
1. [Visualizando o Histórico](#visualizando-o-histórico)
2. [Comparando Versões](#comparando-versões)
3. [Comandos Úteis](#comandos-úteis)
4. [Documentos para Ler](#documentos-para-ler)

---

## 🔍 Visualizando o Histórico

### Ver lista de commits
```bash
cd "C:\Users\Getulio\Desktop\Nova pasta\Sem cafe sem codigo"
git log --oneline
```

**Resultado esperado:**
```
2348dc6 📚 DOCS: Histórico completo de evolução do projeto
471dbfd 🎨 REFACTOR: Padronização completa dos menus
403b2e8 ✨ FEAT: Implementação completa das páginas vazias
3b8c53d 🔧 FIX: Correções críticas de segurança e bugs
563862d 📦 Commit inicial - Código original dos alunos
```

### Ver histórico visual com gráfico
```bash
git log --graph --oneline --all --decorate
```

### Ver detalhes de um commit específico
```bash
# Exemplo: ver o que foi feito nas correções críticas
git show 3b8c53d
```

---

## 🔄 Comparando Versões

### Ver código ANTES das correções
```bash
# Voltar para o código original (só visualizar, não modifica)
git checkout 563862d
```

**⚠️ ATENÇÃO:** Isso coloca você em modo "detached HEAD". Para voltar ao código atual:
```bash
git checkout main
```

### Comparar dois commits
```bash
# Ver diferenças entre código original e atual
git diff 563862d 2348dc6
```

### Ver mudanças em um arquivo específico
```bash
# Exemplo: ver mudanças no app.py
git diff 563862d 2348dc6 -- projeto/app.py

# Exemplo: ver mudanças no perfil.html
git diff 563862d 2348dc6 -- projeto/templates/perfil.html
```

### Ver arquivos modificados em um commit
```bash
# Ver o que mudou no commit de correções
git diff 563862d 3b8c53d --stat
```

---

## 📊 Comandos Úteis

### Ver status atual
```bash
git status
```

### Ver branches
```bash
git branch -a
```

### Ver informações de um arquivo
```bash
# Ver histórico de mudanças de um arquivo
git log -- projeto/app.py

# Ver quem modificou cada linha (blame)
git blame projeto/app.py
```

### Buscar no histórico
```bash
# Buscar commits que mencionam "segurança"
git log --grep="segurança"

# Buscar commits que modificaram "dataDoCaralho"
git log -S "dataDoCaralho"
```

---

## 📚 Documentos para Ler

### 1. **SUMARIO_EXECUTIVO.md**
Visão geral da análise inicial:
- Problemas encontrados
- Scores por categoria
- Top 10 ações prioritárias
- Nota sugerida

### 2. **RELATORIO_NOMENCLATURA.md**
Análise detalhada de:
- Padrões de escrita (português vs inglês)
- Convenções de nomenclatura
- Variáveis problemáticas
- Recomendações

### 3. **RELATORIO_INCOERENCIAS.md**
Análise de continuidade:
- Sidebar duplicada
- Menus inconsistentes
- Páginas vazias
- Links quebrados

### 4. **RELATORIO_DUPLICACAO.md**
Código duplicado:
- ~1035 linhas duplicadas encontradas
- Oportunidades de refatoração
- Economia potencial: 80%

### 5. **HISTORICO_EVOLUCAO.md** ⭐ **LEIA ESTE PRIMEIRO!**
Resumo completo:
- O que foi feito em cada commit
- Antes vs Depois
- Métricas de melhoria
- Lições aprendidas

### 6. **README.md**
Documentação do projeto:
- Como instalar
- Como executar
- Estrutura de arquivos
- Tecnologias usadas

---

## 🎯 Exercício Prático: Explore as Mudanças

### Passo 1: Ver o código original
```bash
git checkout 563862d
# Abra projeto/templates/perfil.html
# Procure pela linha com "dataDoCaralho"
# Note o erro!
```

### Passo 2: Voltar para o código corrigido
```bash
git checkout main
# Abra projeto/templates/perfil.html novamente
# Veja que agora está "data_formatada"
```

### Passo 3: Ver a chave OpenAI exposta
```bash
git show 563862d:projeto/app.py | Select-String "openai.api_key"
# Você verá a chave exposta!

git show 2348dc6:projeto/app.py | Select-String "openai.api_key"
# Agora está usando os.getenv()
```

### Passo 4: Comparar menus
```bash
# Menu do dashboard ANTES
git show 563862d:projeto/templates/dashboard.html | Select-String "menu-item" -Context 1

# Menu do dashboard DEPOIS
git show 2348dc6:projeto/templates/dashboard.html | Select-String "menu-item" -Context 1
```

### Passo 5: Ver páginas que estavam vazias
```bash
# Stuart ANTES (vazio)
git show 563862d:projeto/templates/stuart.html
# Resultado: (nada)

# Stuart DEPOIS (325 linhas!)
git show 2348dc6:projeto/templates/stuart.html | Measure-Object -Line
```

---

## 📈 Visualização de Estatísticas

### Contar linhas adicionadas/removidas
```bash
# Por commit
git log --stat

# Total do projeto
git log --shortstat
```

### Ver contribuições
```bash
git shortlog -s -n
```

### Ver mudanças por arquivo
```bash
# Arquivos mais modificados
git log --pretty=format: --name-only | Sort-Object | Get-Unique -Count | Sort-Object Count -Descending | Select-Object -First 10
```

---

## 🚀 Como Criar Seus Próprios Commits

Quando vocês fizerem novas mudanças:

```bash
# 1. Ver o que mudou
git status

# 2. Adicionar arquivos
git add arquivo1.py arquivo2.html
# Ou adicionar tudo:
git add -A

# 3. Fazer commit
git commit -m "Descrição clara do que foi feito"

# 4. Ver histórico
git log --oneline
```

---

## 💡 Dicas de Mensagens de Commit

### ✅ Bom
```
✅ "FIX: Corrige erro 500 ao carregar perfil"
✅ "FEAT: Adiciona filtro de salas por matéria"
✅ "REFACTOR: Extrai sidebar para componente reutilizável"
✅ "DOCS: Atualiza README com instruções de deploy"
```

### ❌ Ruim
```
❌ "mudanças"
❌ "fix"
❌ "asdfasdf"
❌ "commit"
```

### 📝 Prefixos Recomendados
- `FIX:` - Correção de bug
- `FEAT:` - Nova funcionalidade
- `REFACTOR:` - Melhoria de código sem mudar funcionalidade
- `DOCS:` - Documentação
- `STYLE:` - Formatação, CSS
- `TEST:` - Adiciona ou corrige testes
- `CHORE:` - Tarefas de manutenção

---

## 🎓 Quiz de Verificação

Depois de explorar, teste seu conhecimento:

1. **Quantos commits foram feitos?**
   <details><summary>Resposta</summary>5 commits</details>

2. **Qual era o nome da variável problemática?**
   <details><summary>Resposta</summary>dataDoCaralho</details>

3. **Quantas páginas estavam vazias?**
   <details><summary>Resposta</summary>2 (stuart.html e ranking.html)</details>

4. **Qual foi a melhoria no score geral?**
   <details><summary>Resposta</summary>De 4.8 para 8.5 (+77%)</details>

5. **Onde a chave OpenAI deve ficar?**
   <details><summary>Resposta</summary>Em arquivo .env (variável de ambiente)</details>

---

## 📞 Precisa de Ajuda?

### Comandos de Resgate

Se algo der errado:

```bash
# Descartar mudanças não commitadas
git restore .

# Voltar para o commit mais recente
git checkout main

# Ver onde você está
git status
git log --oneline -1
```

### Recursos de Aprendizado

- **Git Básico:** https://git-scm.com/book/pt-br/v2
- **Git Visualizado:** https://git-school.github.io/visualizing-git/
- **Curso Interativo:** https://learngitbranching.js.org/?locale=pt_BR

---

## ✅ Checklist: Entendi Tudo?

- [ ] Sei ver o histórico de commits
- [ ] Consigo comparar versões diferentes
- [ ] Entendo o que foi feito em cada commit
- [ ] Li o HISTORICO_EVOLUCAO.md
- [ ] Li os 3 relatórios de análise
- [ ] Testei os comandos práticos
- [ ] Entendi as mensagens de commit
- [ ] Sei criar meus próprios commits

---

**Parabéns por explorar o histórico do projeto! 🎉**

Vocês agora têm uma visão completa de como o código evoluiu e podem usar esse conhecimento para melhorar suas próprias práticas de desenvolvimento.

Continue aprendendo e praticando! 💪
