import ply.lex as lex

tokens = (
    'NUMERO',
    'MAIS',
    'MENOS',
    'PRODUTO',
    'DIVISAO',
    'ABRE_PARENTESES',
    'FECHA_PARENTESES',
    'LETRA',
    'IGUALDADE'
)

t_MAIS = r'\+'
t_MENOS = r'-'
t_PRODUTO = r'\*'
t_DIVISAO = r'/'
t_ABRE_PARENTESES = r'\('
t_FECHA_PARENTESES = r'\)'
t_IGUALDADE = r'\='

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_LETRA(t):
    r'[a-zA-Z]+'
    t.value = str(t.value)
    return t

t_ignore = ' \t'
verificar = lex.lex()
variavel = input('Insira o que se quer analisar: ')
verificar.input(variavel)

while True:
    teste = verificar.token()
    if not teste:
        break
    print(f'{teste.type}({teste.value})')