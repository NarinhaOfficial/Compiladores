import ply.lex as lex

tokens = ('PALAVRA',)

def t_PALAVRA(t):
	r'(a|b)*bab'
	return t
def t_error(t):
	print(f'Caracter errado! {t.value[0]}')
	t.lexer.skip(1)

t_ignore = ' \t\n'
verificar = lex.lex()
variavel = input('Insira o que se quer analisar: ')
verificar.input(variavel)


while True:
	teste = verificar.token()
	if not teste:
		break
	print(teste)
#data = "abab aabab bb"
