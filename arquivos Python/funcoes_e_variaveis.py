from datetime import *
import mysql.connector
from mysql.connector import Error

database = "AGENDAI"
pos = 0
lista_servicos = \
    [['Corte de cabelo', 'Pintura de cabelo', 'Penteado', 'Hidratação', 'Luzes', 'Mechas', 'Alizamento'],
     ['Peeling', 'Microagulhamento', 'Limpeza de Pele', 'Máscara de Ouro'],
     ['Limpeza de sobrancelha', 'Desenho de sobrancelha',
      'Pintura de sobrancelha(rena, tinta, Micropigmentação)', 'Colocação cílios fio a fio'],
     ['Pé', 'Mão', 'Pé e Mão', 'Alongamento de unhas']]
lista_funcionarias = \
    [['Jessica', 'Marlene', 'Daiana 2'], ['Ana Paula'], ['Ana Paula'],
     ['Andressa', 'Carla', 'Marlene', 'Daiana 1', 'Carol']]


def titulo(txt): # TÍTULO COM CABEÇALHO E RODAPÉ DE TAMANHO ADAPTÁVEIS
    tam = len(txt) + 2
    print('=-' * tam)
    print(f'{txt:^{tam * 2}}')
    print('=-' * tam)


def texto(txt):  # para títulos muito longos
    tam = 80
    print('=-' * 40)
    print(f'{txt:^{tam}}')
    print('=-' * 40)


def mostra_todos_servicos(escolha_segmento):
    contador = 0
    for e in lista_servicos[escolha_segmento - 1][0:]:
        contador += 1
        print(f'[ {str(contador)} ] {e}')


def mostra_profissionais(escolha_do_segmento):
    # precisa de 1 parâmetro(1 número inteiro): acessa a lista na posição certa
    contador = 0
    for e in lista_funcionarias[escolha_do_segmento - 1]:
        contador += 1
        print(f'[ {str(contador)} ] {e}')


# CONECTA E DESCONECTA AO BD:


def conectar():
    try:
        global con
        con = mysql.connector.connect(host="localhost", user="root", passwd="", database="AGENDAI")
    except Error as e:
        print(f'Erro de conexão: {e}')


def encerrar_conexao():  # Fechar o cursor antes
    try:
        if con.is_connected():
            con.close()
        # print('Conexão ao MySQL finalizada')
    except Error:
        print('Não foi possível encerrar a conexão com o MySQL')


# PROGRAMA PARTE 1:


def agendamento_cadastro_cliente():
    print('Digite seu nome completo e celular com DDD, ex.: 048999684524')
    nome_cliente = str(input('Nome completo: ')).upper().strip()
    celular_cliente = str(input('Celular(DDD): ')).strip()
    # Validação mínima para o campo celular:
    while celular_cliente in 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,x,y,w,z':
        print(f'Informe apenas números sem espaços, ex.: 048966548546')
        celular_cliente = str(input('Celular(DDD): ')).strip()
    while len(celular_cliente) != 12:
        print(f'Informe número telefônico de 12 dígitos, ex.: 048966548546')
        celular_cliente = str(input('Celular(DDD): ')).strip()
    cliente_agendamento = {'NOME': nome_cliente, 'CELULAR': celular_cliente}
    return cliente_agendamento


def agendamento_escolha_servico_e_profissional():
    titulo('Qual serviço deseja realizar?')
    print('[ 1 ] CABELO\n[ 2 ] ESTÉTICA FACIAL\n[ 3 ] SOBRANCELHA\n[ 4 ] PÉS / MÃOS')
    escolha_do_segmento = int(input('Escolha uma opção entre 1 a 4: '))
    print()
    mostra_todos_servicos(escolha_do_segmento)
    escolha_do_servico = int(input('Qual serviço você deseja realizar?: '))
    escolha_do_servico = lista_servicos[escolha_do_segmento - 1][escolha_do_servico - 1]
    mostra_profissionais(escolha_do_segmento)
    escolha_do_profissional = int(input('Qual profissional mais lhe agrada?: '))
    escolha_do_profissional = lista_funcionarias[escolha_do_segmento - 1][escolha_do_profissional - 1]
    servico_e_profissional = [escolha_do_segmento, escolha_do_servico, escolha_do_profissional]
    return servico_e_profissional


def funcao_marcacao_data_e_horario():
    """
    transforma a data marcação (string) para uma classe datetime no
    formato brasileiro; cria a data de hoje e a transforma pro formato
    brasileiro; substrai a data marcação pela data de hoje e transforma em
    string para poder transformar em inteiro (pegando só a informação referente
    aos dias subtraídos para que sejam iguais ou maiores do que 0.
    :return: 
    a função pra que se repita a pergunta caso tenha inputação errada.

    """"""
    print('MARCAÇÃO DE DATA E HORÁRIO - Se tiver dúvida digite a')
    print('=-' * 40)
    # enquanto não cumprir os critérios de tamanho e diferente de 'a'
    # a pergunta se repetirá
    while True:
            """
    # validação de dados para data
    while True:
        data_marcacao = str(input('Qual data (xx/xx/xx) é de seu desejo?: ')).strip().lower()
        if data_marcacao[0].lower() == 'a':
            print(f'exemplo de data: 17/05/22')
            print('=-' * 40)
            return funcao_marcacao_data_e_horario()
        try:
            delta1 = datetime.strptime(data_marcacao, "%d/%m/%y") - (
                datetime.strptime((datetime.today().strftime("%d/%m/%y")), '%d/%m/%y'))
            delta2 = str(delta1).strip().split()
            if int(delta2[0][:2]) >= 0:
                break
        except ValueError:
            print("Formato incorreto. Tente novamente.Ex.: 17/05/22")
            return funcao_marcacao_data_e_horario()
    # validação de dados para horário
    while True:
        '''transforma a variável horario_marcacao de uma string para uma classe 
        datetime no formato xx:xx:xx e transforma novamente para uma string apenas
        os 5 primeiros digitos do valor da variável hora, retornando apenas
        xx:xx.'''
        global hora2
        while True:
            horario_marcacao = str(input('Qual horário deseja marcar?: ')).strip().lower()
            if horario_marcacao[0].lower() == 'a':
                print('=-' * 40)
                print('exemplo de horário matutino: 07:00 ; 07:15\n'
                      'exemplo de horário vespertino: 15:00 ; 14:35\n'
                      'exemplo de horário noturno: 23:59 ; 00:30')
                print('=-' * 40)
                horario_marcacao = str(input('Qual horário deseja marcar?: ')).strip().lower()
            if len(horario_marcacao) == 5:
                break
            else:
                print("Formato incorreto. Tente novamente.Ex.: 08:00")
        try:
            hora = datetime.strptime(horario_marcacao, "%H:%M").time()
            hora2 = str(hora)[:5]
        except ValueError:
            print("Formato incorreto. Tente novamente.Ex.: 08:00")
            horario_marcacao = str(input('Qual horário deseja marcar?: ')).strip().lower()
        if horario_marcacao != 'a' and horario_marcacao != hora2:
            print("Formato incorreto. Tente novamente.Ex.: 08:00")
        if hora2 != 'a' and horario_marcacao != hora2:
            break
        break
    data_agendada = [data_marcacao, hora2]
    return data_agendada


titulo('Bem vindo ao sistema AGENDAÍ')
# reúne todas as informações inputadas numa única variável:
apresentacao_pedido = [agendamento_cadastro_cliente()], [agendamento_escolha_servico_e_profissional()],\
                      [funcao_marcacao_data_e_horario()]


def funcao_confirmacao_do_pedido_feito():
    while True:
        print('=-' * 40)
        confirmacao_do_pedido = str(input('CONFIRMA O PEDIDO?: [S ou N] ')).upper().strip()[0]
        if confirmacao_do_pedido in 'SN':
            if confirmacao_do_pedido == 'N':
                titulo('Ok, vamos recomeçar seu pedido.')
                del apresentacao_pedido[0][0]["NOME"]
                del apresentacao_pedido[0][0]["CELULAR"]
                # cliente.clear()
                del apresentacao_pedido[1][0][1]
                del apresentacao_pedido[1][0][2]
                # escolha_servico_e_profissional
                del apresentacao_pedido[2][0][0]
                del apresentacao_pedido[2][0][1]
                # data_e_hora_agendamento.clear()
                break

            if confirmacao_do_pedido == 'S':
                titulo(f'AGENDAMENTO REALIZADO COM SUCESSO')
                break
            break
        else:
            print('Valor informado inválido, digite S ou N')
    return confirmacao_do_pedido


def adicao_de_servico():
    """
    uma variável pergunta se deseja add mais algum serviço.
    se nao for digitado s ou n a pergunta ressurge na tela.
    :return:
    """
    adicao_de_servico = ' '
    while adicao_de_servico not in 'SN':
        adicao_de_servico = str(input('Deseja mais algum serviço?: [S ou N] ')).upper().strip()[0]
    return adicao_de_servico


def insere_clientes():
    try:
        conectar()
        dados = "'" + apresentacao_pedido[0][0]["NOME"] + "'""," + " " + "'" + apresentacao_pedido[0][0]["CELULAR"] + "'"')'
        declaracao = """insert into `clientes` (`NOME CLIENTE`, `CELULAR CLIENTE`) values ("""
        comando_sql = declaracao + dados
        cursor = con.cursor()
        cursor.execute(comando_sql)
        con.commit()
        # print('Nº total de registros inseridos na tabela clientes: ', cursor.rowcount)
    except Error as e:
        print(f'Erro ao inserir dados na tabela clientes: {e}')
    finally:
        encerrar_conexao()


def insere_agendamentos():
    try:
        conectar()
        # (default, 'corte cabelo', '20-02-22', '08:00', default, 'JÉSSICA', default, default),
        dados = 'default' + "," + " " + "'" + apresentacao_pedido[1][0][1] \
                + "'" + "," + " " + 'date_format' + '(' + "'" + apresentacao_pedido[1][0][2] + "'" \
                + ',' + ' ' + "'" + '%d/%m/%y' + "'" + ')' + "," + " " + "'" \
                + apresentacao_pedido[2][0][0] + "'" + "," + " " + 'default' + "," + " "\
                + "'" + apresentacao_pedido[2][0][1] + "'" + "," + " " + 'default' + "," + " " + 'default' + ')'
        declaracao = """insert into `agendamentos` values ("""
        comando_sql = declaracao + dados
        cursor = con.cursor()
        cursor.execute(comando_sql)
        con.commit()
        # print('Nº total de registros inseridos na tabela agendamentos: ', cursor.rowcount)
    except Error as e:
        print(f'Erro ao inserir dados na tabela agendamentos: {e}')
    finally:
        encerrar_conexao()


insere_agendamentos()
########################################################################################################

#  PARTE 2
# EDIÇÃO DE CLIENTES E AGENDAMENTOS: #(apenas banco de dados)

# LISTA DE CLIENTES CADASTRADOS:


def consulta_clientes_bd():
    try:
        conectar()
        consulta_sql = "select * from clientes order by `ID CLIENTE`"
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()  # pega todas as linhas
        print('Nº total de registros retornados: ', cursor.rowcount)
        print('\nMostrando os clientes cadastrados')
        for linha in linhas:
            print('Id:', linha[0])
            print('Nome:', linha[1])
            print('Celular:', linha[2], "\n")
    except Error as e:
        print(f'Erro ao acessar a tabela MySQL: {e}')
    finally:
        encerrar_conexao()

# CADASTRAR NOVO CLIENTE:


def add_cliente():
    titulo('ADICIONA CLIENTE')
    try:
        conectar()
        nome = input('Nome: ')
        celular = input('Celular: ')
        dados = "'" + nome + "'""," + " " + "'" + celular + "'"')'
        declaracao = """INSERT INTO `clientes` (`NOME CLIENTE`, `CELULAR CLIENTE`) values ("""
        sql = declaracao + dados
        inserir_clientes = sql
        cursor = con.cursor()
        cursor.execute(inserir_clientes)
        con.commit()
        print('Nº total de registros inseridos na tabela cliente: ', cursor.rowcount)
        cursor.close()
    except Error as e:
        print(f'Erro ao inserir novos dados na tabela cliente: {e}')
    finally:
        encerrar_conexao()
        print('CLIENTE ADICIONADO COM SUCESSO')

# EDITAR CLIENTE:


def edita_cliente():
    titulo('EDITA CLIENTE')
    try:
        conectar()
        print('Desejas alterar: [ 1 ] Nome  -  [ 2 ] Celular - [ 3 ] Ambos')
        opcao = int(input('Digite aqui: '))
        id = int(input('Digite o ID do cliente a ser editado: '))
        if opcao == 1:
            nome = input('Novo nome: ')
            declaracao = f"""update clientes set `NOME CLIENTE` = {"'" + nome + "'"} where `ID CLIENTE` = {id}"""
            cursor = con.cursor()
            cursor.execute(declaracao)
            con.commit()
            print('Nº total de registros alterados na tabela cliente: ', cursor.rowcount)
            if cursor.rowcount > 0:
                print('CLIENTE ALTERADO COM SUCESSO')
            cursor.close()
        if opcao == 2:
            celular = input('Novo celular: ')
            declaracao = f"""update clientes set `CELULAR CLIENTE` = {"'" + celular + "'"} where `ID CLIENTE` = {id}"""
            cursor = con.cursor()
            cursor.execute(declaracao)
            con.commit()
            print('Nº total de registros alterados na tabela cliente: ', cursor.rowcount)
            if cursor.rowcount > 0:
                print('CLIENTE ALTERADO COM SUCESSO')
            cursor.close()
        if opcao == 3:
            nome = input('Novo nome: ')
            celular = input('Novo celular: ')
            declaracao = f"""update clientes set `NOME CLIENTE` = {"'" + nome + "'"} where `ID CLIENTE` = {id}"""
            declaracao_2 = f"""update clientes set `CELULAR CLIENTE` = {"'" + celular + "'"} where `ID CLIENTE` = {id}"""
            cursor = con.cursor()
            cursor.execute(declaracao)
            cursor.execute(declaracao_2)
            con.commit()
            print('Nº total de registros alterados na tabela cliente: ', cursor.rowcount)
            if cursor.rowcount > 0:
                print('CLIENTE ALTERADO COM SUCESSO')
            cursor.close()
    except Error as e:
        print(f'Erro ao alterar registros da tabela cliente: {e}')
    finally:
        encerrar_conexao()


# EXCLUIR CLIENTE:


def exclui_clientes():
    try:
        conectar()
        titulo('EXCLUSÃO DE CLIENTE')
        id = input('Informe ID do cliente: ').strip()
        # usa o id pra buscar no BD e confirmar existência
        dados = "'" + id + "'"
        declaracao = 'select `NOME CLIENTE`, `ID CLIENTE` from clientes' \
                     ' where `ID CLIENTE` = ' + dados
        cursor = con.cursor()
        cursor.execute(declaracao)
        linhas = cursor.fetchall()  # pega todas as linhas
        if len(linhas) == 0:
            print('Cliente inexistente')
        for linha in linhas:
            if len(linhas) > 0:
                print(f'Confirme dados para exclusão do cliente:\nID: {linha[1]}\nNome: {linha[0]}')
                confirmacao = int(input('[ 1 ] CONFIRMO\n[ 2 ] NÃO CONFIRMO\nDigite aqui: '))
                if confirmacao == 1:
                    comando_sql = 'delete from clientes where `ID CLIENTE` = ' + dados + 'limit 1'
                    cursor.execute(comando_sql)
                    con.commit()
                    cursor.close()
                    print(f'Cliente - {linha[0]} - excluído com sucesso.')
                if confirmacao == 2:
                    print(f'Cliente - {linha[0]} - NÃO excluído.')
    except Error as e:
        print(f'Erro ao acessar a tabela MySQL: {e}')
    finally:
        encerrar_conexao()


# PROCURAR CLIENTE ESPECÍFICO:


def procura_cliente_especifico():
    """
    Tipos de consulta:
    select c.`ID CLIENTE`, c.`NOME CLIENTE`, a.`SERVIÇO SOLICITADO`, a.`DATA SERVIÇO`, a.`HORÁRIO SERVIÇO`, a.`NOME PROFISSIONAL`
    from clientes as c join agendamentos as a
    on c.`ID CLIENTE` =  a.`ID AGENDAMENTO`;

    select p.`NOME PROFISSIONAL`, c.`NOME CLIENTE`, a.`SERVIÇO SOLICITADO`, a.`DATA SERVIÇO`, a.`HORÁRIO SERVIÇO`
    from clientes as c join agendamentos as a
    on c.`ID CLIENTE` =  a.`ID AGENDAMENTO`
    join profissionais as p
    on p.`ID PROFISSIONAL` = c.`ID CLIENTE`;

    :return:
    """
    try:
        conectar()
        titulo('BUSCA POR CLIENTE ESPECÍFICO')
        print('[ 1 ] - Buscar pelo ID\n[ 2 ] - Buscar pelo nome')
        opcao = int(input('Digite aqui: '))
        if opcao == 1:
            id = input('Digite o ID do cliente a ser procurado: ')
            consulta_sql = 'select * from clientes where `ID CLIENTE` =' + "'" + id + "'"
            cursor = con.cursor()
            cursor.execute(consulta_sql)
            linhas = cursor.fetchall()  # pega todas as linhas
            print('Nº total de registros retornados: ', cursor.rowcount)
            print('---------------------------')
            for linha in linhas:
                print('Id:', linha[0])
                print('Nome:', linha[1])
                print('Celular:', linha[2])
            print('---------------------------')
            print()
            cursor.close()
        if opcao == 2:
            nome = input('digite o nome do cliente a ser procurado: ')
            consulta_sql = 'select * from clientes where `NOME CLIENTE` =' + "'" + nome + "'"
            cursor = con.cursor()
            cursor.execute(consulta_sql)
            linhas = cursor.fetchall()  # pega todas as linhas
            print('Nº total de registros retornados: ', cursor.rowcount)
            print('---------------------------')
            for linha in linhas:
                print('Id:', linha[0])
                print('Nome:', linha[1])
                print('Celular:', linha[2])
            print('---------------------------')
            print()
            cursor.close()
    except Error as e:
        print(f'Erro ao acessar a tabela MySQL: {e}')
    finally:
        encerrar_conexao()


# EDITAR AGENDAMENTO:


def edita_agendamento():
    titulo('EDITAR AGENDAMENTO')
    try:
        conectar()
        print('[ 1 ] - Serviço\n[ 2 ] - Profissional\n[ 3 ] - Data\n[ 4 ] - Horário')
        opcao = int(input('Digite aqui: '))
        id = int(input('Digite o ID do agendamento a ser editado: '))
        if opcao == 1:
            servico = input('Novo serviço: ')
            declaracao = f"""update agendamentos set `SERVIÇO SOLICITADO` = '{servico}'
            where `ID AGENDAMENTO` = {id}"""
            cursor = con.cursor()
            cursor.execute(declaracao)
            con.commit()
            n = cursor.rowcount
            if n > 0:
                print('AGENDAMENTO ALTERADO COM SUCESSO')
            cursor.close()
        if opcao == 2:
            profissional = input('Novo profissional: ')
            declaracao = f"""update agendamentos set `NOME PROFISSIONAL` = '{profissional}'
            where `ID AGENDAMENTO` = {id}"""
            cursor = con.cursor()
            cursor.execute(declaracao)
            con.commit()
            n = cursor.rowcount
            if n > 0:
                print('AGENDAMENTO ALTERADO COM SUCESSO')
            cursor.close()
        if opcao == 3:
            data = input('Nova data: ')
            declaracao = f"""update agendamentos set `DATA SERVIÇO` = '{data}'
            where `ID AGENDAMENTO` = '{id}'"""
            cursor = con.cursor()
            cursor.execute(declaracao)
            con.commit()
            n = cursor.rowcount
            if n > 0:
                print('AGENDAMENTO ALTERADO COM SUCESSO')
            cursor.close()
        if opcao == 4:
            horario = input('Novo horário: ')
            declaracao = f"""update agendamentos set `HORÁRIO SERVIÇO` = '{horario}'
            where `ID AGENDAMENTO` = '{id}'"""
            cursor = con.cursor()
            cursor.execute(declaracao)
            con.commit()
            n = cursor.rowcount
            if n > 0:
                print('AGENDAMENTO ALTERADO COM SUCESSO')
            cursor.close()
    except Error as e:
        print(f'Erro ao alterar registros da tabela agendamentos: {e}')
    finally:
        encerrar_conexao()


# EXCLUIR AGENDAMENTO:


def exclui_agendamentos():
    try:
        conectar()
        titulo('EXCLUSÃO DE AGENDAMENTOS')
        id = input('Informe ID do agendamento: ').strip()
        # usa o id pra buscar no BD e confirmar existência
        dados = "'" + id + "'"
        declaracao = 'select `ID AGENDAMENTO` from agendamentos' \
                     ' where `ID AGENDAMENTO` = ' + dados
        cursor = con.cursor()
        cursor.execute(declaracao)
        linhas = cursor.fetchall()  # pega todas as linhas
        if len(linhas) == 0:
            print('Agendamento inexistente')
        for linha in linhas:
            if len(linhas) > 0:
                print(f'Confirme dados para exclusão do agendamento:\nID: {linha[0]}')
                confirmacao = int(input('[ 1 ] CONFIRMO\n[ 2 ] NÃO CONFIRMO\nDigite aqui: '))
                if confirmacao == 1:
                    comando_sql = 'delete from agendamentos where `ID AGENDAMENTO` = ' + dados + 'limit 1'
                    cursor.execute(comando_sql)
                    con.commit()
                    cursor.close()
                    print(f'Agendamento de ID {linha[0]} excluído com sucesso.')
                if confirmacao == 2:
                    print(f'Agendamento de ID {linha[0]} NÃO excluído.')
    except Error as e:
        print(f'Erro ao excluir um agendamentoa: {e}')
    finally:
        encerrar_conexao()


# MENU DE EDIÇÃO:


def funcao_menu_edicao_dos_clientes():
    texto('MENU DE EDIÇÃO DE CLIENTES E AGENDAMENTOS')
    repete = 1
    while repete == 1:
        pos = 0
        if pos < 1:
            pos += 1
            print('[ 1 ] LISTA DE CLIENTES CADASTRADOS\n[ 2 ] CADASTRAR NOVO CLIENTE\n'
                  '[ 3 ] EDITAR CLIENTE\n[ 4 ] EXCLUIR CLIENTE\n[ 5 ] PROCURAR CLIENTE\n'
                  '[ 6 ] EDITAR AGENDAMENTO\n[ 7 ] EXCLUIR AGENDAMENTO\n'
                  '[ 8 ] SAIR DO SISTEMA ')
            opcao_menu = int(input('Digite sua escolha: '))
        else:
            continue
        if opcao_menu == 1:
            titulo('LISTA GERAL DOS CLIENTES')
            consulta_clientes_bd()
            print('=-' * 40)
        if opcao_menu == 2:
            add_cliente()
            print('=-' * 40)
        if opcao_menu == 3:
            edita_cliente()
            print('=-' * 40)
        if opcao_menu == 4:
            exclui_clientes()
            print('=-' * 40)
        if opcao_menu == 5:
            procura_cliente_especifico()
            print('=-' * 40)
        if opcao_menu == 6:
            edita_agendamento()
            print('=-' * 40)
        if opcao_menu == 7:
            exclui_agendamentos()
            print('=-' * 40)
        if opcao_menu == 8:
            print('TUDO CERTO. ATÉ LOGO')
            break
