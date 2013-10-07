#!/usr/bin/env python

#**********************************************************************************************************
# This is a dummy script created for fun to answer a few basic questions about the Facebook Group MozDevz *
# There is nothing fancy about it, tweak it, add questions, etc as you see fit				  *
# 													  *
# Written By: Fei Manheche										  *
# 07/10/2013 - Maputo Mozambique									  *
#**********************************************************************************************************

print "--------------------------"
print "| Bem Vindos ao MozDevz! |"
print "--------------------------"

def questions(what):
	if what == 'o que e':
		print "R: E a comunidade de Desenvolvidores Mocambicanos de Aplicacoes"
	elif what == 'o que faz':
		print "R: Junta pessoas que queirao/estajam desenvolver aplicacoes ou tenham ideais e interesses em software para ajudar Mocambique."
	elif what == 'tenho de ser programador':
		print "R: Todos sao bem vindos, nao restrito a desenvolvedores, geeks, amadores, etc. Para estares a ler, quer dizer que es bem vindo ;)"
	else:
		print "R: Ainda nao tenho a resposta :( Pergunte ao resto da comunidade ;)"

while 1:
	userAction = raw_input('Pergunte: ')
        if userAction == 'sair':
		print "Obrigado pelo interesse ;)"
                exit()
	questions(userAction)

