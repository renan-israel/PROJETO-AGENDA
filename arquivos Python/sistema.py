from funcoes_e_variaveis import texto, titulo, mostra_todos_servicos, mostra_profissionais, conectar, encerrar_conexao, \
    agendamento_cadastro_cliente, agendamento_escolha_servico_e_profissional, funcao_marcacao_data_e_horario, \
    funcao_confirmacao_do_pedido_feito, adicao_de_servico, insere_clientes, insere_agendamentos, apresentacao_pedido, \
    consulta_clientes_bd, add_cliente, edita_cliente, exclui_clientes, procura_cliente_especifico, edita_agendamento, \
    exclui_agendamentos, funcao_menu_edicao_dos_clientes

global con
########################################################################################################
                                    #PARTE 1 de 2
########################################################################################################

while True:

    confirmacao_pedido = funcao_confirmacao_do_pedido_feito()

    add_servico = adicao_de_servico()
    if add_servico == 'N':
        break

titulo('TUDO CERTO. ATÉ LOGO.')

if confirmacao_pedido == 'S' and add_servico == 'N':  # INSERE DADOS NO BD:

    insere_clientes()  # INSERE DADOS NA TABELA CLIENTES:
    insere_agendamentos()  # INSERE DADOS NA TABELA AGENDAMENTOS:

########################################################################################################
                                    #PARTE 2 de 2
#########################################################################################################
# EDIÇÃO DE CLIENTES E AGENDAMENTOS: # apenas banco de dados

# MENU DE EDIÇÃO
funcao_menu_edicao_dos_clientes()
