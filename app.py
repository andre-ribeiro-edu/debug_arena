import streamlit as st

# ── Configuração da página ──────────────────────────────────────────────────
st.set_page_config(
    page_title="Debug Arena — Python",
    page_icon="🐛",
    layout="centered",
)

# ── Desafios ────────────────────────────────────────────────────────────────
CHALLENGES = [
    {
        "title": "Olá, Mundo!",
        "level": "Iniciante",
        "xp": 10,
        "desc": (
            "O clássico primeiro programa em Python. "
            "Encontre o erro de sintaxe que impede a mensagem de aparecer."
        ),
        "buggy": 'print("Olá, Mundo!"',
        "solution": 'print("Olá, Mundo!")',
        "hint": "Toda função em Python precisa ter seus parênteses fechados.",
        "check": lambda s: (
            'print' in s and ')' in s and '"Olá, Mundo!"' in s
        ),
    },
    {
        "title": "Variáveis e tipos",
        "level": "Iniciante",
        "xp": 15,
        "desc": (
            "Este código deveria calcular a soma de dois números e exibir o "
            "resultado como inteiro. Há um erro de tipo."
        ),
        "buggy": 'a = "10"\nb = 5\nresultado = a + b\nprint(resultado)',
        "solution": 'a = 10\nb = 5\nresultado = a + b\nprint(resultado)',
        "hint": "Não é possível somar uma string com um inteiro. Verifique o tipo de 'a'.",
        "check": lambda s: (
            '"10"' not in s and "'10'" not in s
            and 'a' in s and 'b' in s and 'print' in s
        ),
    },
    {
        "title": "Condicionais",
        "level": "Iniciante",
        "xp": 20,
        "desc": (
            "O programa deveria verificar se uma pessoa é maior de idade. "
            "O bloco condicional tem um problema de indentação."
        ),
        "buggy": 'idade = 20\nif idade >= 18:\nprint("Maior de idade")',
        "solution": 'idade = 20\nif idade >= 18:\n    print("Maior de idade")',
        "hint": "Em Python, o bloco dentro do 'if' deve ser indentado (4 espaços ou 1 tab).",
        "check": lambda s: 'if' in s and ('    print' in s or '\tprint' in s),
    },
    {
        "title": "Laço for",
        "level": "Básico",
        "xp": 25,
        "desc": (
            "O código deveria imprimir os números de 1 a 5, mas há um erro "
            "no range que faz ele imprimir apenas até 4."
        ),
        "buggy": 'for i in range(1, 5):\n    print(i)',
        "solution": 'for i in range(1, 6):\n    print(i)',
        "hint": "range(inicio, fim) não inclui o fim. Para ir até 5, o fim deve ser 6.",
        "check": lambda s: 'range(1, 6)' in s or 'range(1,6)' in s,
    },
    {
        "title": "Funções",
        "level": "Básico",
        "xp": 30,
        "desc": (
            "Esta função deveria calcular o dobro de um número, "
            "mas não retorna nada. Encontre o que está faltando."
        ),
        "buggy": (
            "def dobro(numero):\n"
            "    resultado = numero * 2\n\n"
            "print(dobro(5))"
        ),
        "solution": (
            "def dobro(numero):\n"
            "    resultado = numero * 2\n"
            "    return resultado\n\n"
            "print(dobro(5))"
        ),
        "hint": "A função calcula o resultado, mas esquece de devolvê-lo com 'return'.",
        "check": lambda s: 'return' in s,
    },
    {
        "title": "Listas",
        "level": "Intermediário",
        "xp": 40,
        "desc": (
            "O código tenta acessar o último elemento de uma lista de 3 itens, "
            "mas gera um IndexError."
        ),
        "buggy": 'frutas = ["maçã", "banana", "uva"]\nprint(frutas[3])',
        "solution": 'frutas = ["maçã", "banana", "uva"]\nprint(frutas[2])',
        "hint": "Índices em Python começam em 0. Uma lista com 3 elementos tem índices 0, 1 e 2.",
        "check": lambda s: 'frutas[2]' in s or 'frutas[-1]' in s,
    },
    {
        "title": "Dicionários",
        "level": "Intermediário",
        "xp": 45,
        "desc": (
            "O código deveria exibir o nome do aluno a partir de um dicionário, "
            "mas a chave usada está errada."
        ),
        "buggy": 'aluno = {"nome": "Ana", "nota": 9.5}\nprint(aluno["Nome"])',
        "solution": 'aluno = {"nome": "Ana", "nota": 9.5}\nprint(aluno["nome"])',
        "hint": "Chaves em dicionários são sensíveis a maiúsculas. 'Nome' e 'nome' são diferentes.",
        "check": lambda s: 'aluno["nome"]' in s or "aluno['nome']" in s,
    },
    {
        "title": "Laço while",
        "level": "Intermediário",
        "xp": 50,
        "desc": (
            "Este loop nunca para! Encontre o erro que impede "
            "a condição de parada de funcionar."
        ),
        "buggy": 'contador = 0\nwhile contador < 5:\n    print(contador)',
        "solution": (
            'contador = 0\nwhile contador < 5:\n'
            '    print(contador)\n    contador += 1'
        ),
        "hint": "Para o loop parar, 'contador' precisa ser incrementado a cada iteração.",
        "check": lambda s: 'contador += 1' in s or 'contador = contador + 1' in s,
    },
    {
        "title": "Tratamento de erros",
        "level": "Avançado",
        "xp": 60,
        "desc": (
            "O código deveria capturar o erro de divisão por zero, "
            "mas o bloco 'except' nunca é executado. Veja o tipo da exceção."
        ),
        "buggy": (
            "try:\n"
            "    resultado = 10 / 0\n"
            "except ValueError:\n"
            '    print("Erro de divisão por zero!")'
        ),
        "solution": (
            "try:\n"
            "    resultado = 10 / 0\n"
            "except ZeroDivisionError:\n"
            '    print("Erro de divisão por zero!")'
        ),
        "hint": "Divisão por zero lança 'ZeroDivisionError', não 'ValueError'.",
        "check": lambda s: (
            'ZeroDivisionError' in s
            or 'except Exception' in s
            or 'except:' in s
        ),
    },
    {
        "title": "Recursão — a missão final",
        "level": "Avançado",
        "xp": 80,
        "desc": (
            "A função recursiva calcula o fatorial, mas há DOIS bugs: "
            "a condição de parada está errada e a chamada recursiva também. "
            "Encontre os dois!"
        ),
        "buggy": (
            "def fatorial(n):\n"
            "    if n == 0:\n"
            "        return 0\n"
            "    return n * fatorial(n - 2)\n\n"
            "print(fatorial(5))"
        ),
        "solution": (
            "def fatorial(n):\n"
            "    if n == 0:\n"
            "        return 1\n"
            "    return n * fatorial(n - 1)\n\n"
            "print(fatorial(5))"
        ),
        "hint": (
            "1) O fatorial de 0 é 1, não 0.  "
            "2) A recursão deve subtrair 1 a cada chamada, não 2."
        ),
        "check": lambda s: (
            'return 1' in s
            and ('fatorial(n - 1)' in s or 'fatorial(n-1)' in s)
        ),
    },
]

TOTAL = len(CHALLENGES)
TROPHIES = ["🐛", "🔍", "⚡", "🛠️", "🧩", "🎯", "🚀", "💡", "🏅", "🏆"]

# ── Estado da sessão ────────────────────────────────────────────────────────
def init_state():
    defaults = {
        "current": 0,
        "xp": 0,
        "hints": 3,
        "solved": [],        # índices resolvidos
        "feedback": None,    # ("success"|"error"|"hint", mensagem)
        "show_next": False,
        "game_over": False,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()

# ── Helpers ─────────────────────────────────────────────────────────────────
def level_from_xp(x):
    if x < 50:   return 1
    if x < 120:  return 2
    if x < 220:  return 3
    if x < 350:  return 4
    return 5

def set_feedback(kind, msg):
    st.session_state.feedback = (kind, msg)

def advance():
    """Avança para a próxima fase não resolvida."""
    nxt = (st.session_state.current + 1) % TOTAL
    for _ in range(TOTAL):
        if nxt not in st.session_state.solved:
            st.session_state.current = nxt
            st.session_state.feedback = None
            st.session_state.show_next = False
            return
        nxt = (nxt + 1) % TOTAL
    st.session_state.game_over = True

# ── CSS extra ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
    .hud-box   { background:#f5f5f5; border-radius:10px; padding:10px 0;
                 text-align:center; }
    .hud-label { font-size:11px; color:#888; text-transform:uppercase;
                 letter-spacing:.05em; }
    .hud-value { font-size:22px; font-weight:600; }
    .code-box  { background:#1e1e1e; color:#d4d4d4; border-radius:8px;
                 padding:16px; font-family:monospace; font-size:14px;
                 line-height:1.7; white-space:pre; overflow-x:auto; }
    .dot-row   { display:flex; gap:6px; margin:8px 0; }
    .dot       { width:10px; height:10px; border-radius:50%;
                 background:#ddd; display:inline-block; }
    .dot-done  { background:#1D9E75; }
    .dot-active{ background:#534AB7; }
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# TELA DE VITÓRIA
# ══════════════════════════════════════════════════════════════════════════════
if st.session_state.game_over:
    st.balloons()
    st.markdown("## 🏆 Parabéns, debugger mestre!")
    st.success(
        "Você encontrou todos os bugs e o jogo agora está completamente funcional!\n\n"
        "Cada erro que você corrigiu foi uma vitória real — continue praticando."
    )
    st.markdown("### Troféus conquistados")
    cols = st.columns(TOTAL)
    for i, (col, trophy) in enumerate(zip(cols, TROPHIES)):
        col.markdown(
            f"<div style='text-align:center;font-size:28px'>{trophy}</div>"
            f"<div style='text-align:center;font-size:11px;color:#888'>Fase {i+1}</div>",
            unsafe_allow_html=True,
        )
    st.metric("XP total conquistado", f"{st.session_state.xp} XP")
    if st.button("🔄 Jogar novamente"):
        for k in ["current","xp","hints","solved","feedback","show_next","game_over"]:
            del st.session_state[k]
        st.rerun()
    st.stop()

# ══════════════════════════════════════════════════════════════════════════════
# HUD
# ══════════════════════════════════════════════════════════════════════════════
c = CHALLENGES[st.session_state.current]

st.markdown("## 🐛 Debug Arena — Python")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(
        f"<div class='hud-box'><div class='hud-label'>Nível</div>"
        f"<div class='hud-value'>{level_from_xp(st.session_state.xp)}</div></div>",
        unsafe_allow_html=True,
    )
with col2:
    st.markdown(
        f"<div class='hud-box'><div class='hud-label'>XP</div>"
        f"<div class='hud-value'>{st.session_state.xp}</div></div>",
        unsafe_allow_html=True,
    )
with col3:
    st.markdown(
        f"<div class='hud-box'><div class='hud-label'>Fase</div>"
        f"<div class='hud-value'>{st.session_state.current+1}/10</div></div>",
        unsafe_allow_html=True,
    )
with col4:
    st.markdown(
        f"<div class='hud-box'><div class='hud-label'>Dicas</div>"
        f"<div class='hud-value'>{st.session_state.hints}</div></div>",
        unsafe_allow_html=True,
    )

# Barra de progresso
progress = len(st.session_state.solved) / TOTAL
st.progress(progress, text=f"{len(st.session_state.solved)} de {TOTAL} fases concluídas")

# Bolinhas de progresso
dots_html = "<div class='dot-row'>"
for i in range(TOTAL):
    cls = "dot-done" if i in st.session_state.solved else ("dot-active" if i == st.session_state.current else "dot")
    dots_html += f"<span class='dot {cls}'></span>"
dots_html += "</div>"
st.markdown(dots_html, unsafe_allow_html=True)

st.divider()

# ══════════════════════════════════════════════════════════════════════════════
# DESAFIO ATUAL
# ══════════════════════════════════════════════════════════════════════════════
st.markdown(
    f"### Fase {st.session_state.current+1} — {c['title']} "
    f"&nbsp; `{c['level']}` &nbsp; `+{c['xp']} XP`"
)
st.write(c["desc"])

st.markdown("**Código com bug:**")
st.code(c["buggy"], language="python")

user_code = st.text_area(
    "Escreva o código corrigido abaixo:",
    height=160,
    placeholder="Cole aqui o código com a correção...",
    key=f"code_{st.session_state.current}",
)

# ── Botões de ação ───────────────────────────────────────────────────────────
b1, b2, b3 = st.columns([2, 2, 2])

with b1:
    if st.button("✅ Verificar", use_container_width=True, type="primary"):
        if not user_code.strip():
            set_feedback("error", "Escreva sua correção antes de verificar!")
        elif c["check"](user_code):
            if st.session_state.current not in st.session_state.solved:
                st.session_state.xp += c["xp"]
                st.session_state.solved.append(st.session_state.current)
            set_feedback("success", f"✓ Correto! Bug encontrado e corrigido. +{c['xp']} XP conquistados!")
            st.session_state.show_next = True
            if len(st.session_state.solved) == TOTAL:
                st.session_state.game_over = True
        else:
            set_feedback("error", "✗ Ainda há algo errado. Releia o código com atenção ou use uma dica!")
        st.rerun()

with b2:
    if st.button("💡 Dica", use_container_width=True):
        if st.session_state.hints <= 0:
            set_feedback("error", "Você usou todas as suas dicas!")
        else:
            st.session_state.hints -= 1
            set_feedback("hint", f"Dica: {c['hint']}")
        st.rerun()

with b3:
    if st.button("👁️ Ver solução", use_container_width=True):
        set_feedback("hint", f"Solução:\n\n```python\n{c['solution']}\n```\n\nEstude o que mudou e tente entender o porquê.")
        st.rerun()

# ── Feedback ─────────────────────────────────────────────────────────────────
if st.session_state.feedback:
    kind, msg = st.session_state.feedback
    if kind == "success":
        st.success(msg)
    elif kind == "error":
        st.error(msg)
    else:
        st.warning(msg)

# ── Próxima fase ─────────────────────────────────────────────────────────────
if st.session_state.show_next and not st.session_state.game_over:
    if st.button("Próxima fase ➡️", type="primary"):
        advance()
        st.rerun()