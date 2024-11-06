import re
import mysql.connector as mysql

# Para estabelecer a conexão com o banco de dados mysql
# será necessário passar algumas configurações, tais como:
# endereço do servidor de banco de dados(host), porta de comunicação(3380)
# usuário do banco(root), senha de acesso(123@senac) e o nome do 
# banco de dados(dbusuarios)
con = mysql.connect(
    port=3380,
    user="root",
    host="127.0.0.1",
    password="123@senac",
    database="dbusuarios"
)

# vamos criar três funções, sendo:
# 1 - cadastrar_usuarios
# 2 - atualizar_usuarios
# 3 - autenticar_usuarios
def cadastrar_usuarios(nome,email,senha):
    
    # criar uma variável chamada msg para nos ajudar 
    # a retornar uma mensagem. Caso tenha cadastrado ou 
    # tenha dado algum erro
    msg = ""
    
    #Vamos validar a quantidade de caracteres e, para isso
    #iremos usar o comando len. Este comando tem a capacidade
    #de contar quantos caracteres há em uma variável
    if(len(senha) < 8):
        return "Sua senha dever ter no mínimo 8 caracteres"
    
    
    #Vamos fazer uma validação no nome de usuário para não aceitar
    #caracteres especiais. Utilizaremos a expressão regular para isso
    padrao = r"^[a-z]+$"
    # A expressão regular acima valida a entrada  de caracteres não especiais
    # e não númericos de a até z mínusculos.
    #O elemento ^ indica início da string e caractere $ indica o fim da string
    # entre colchetes estamos indicando quais caracteres serão aceitos
    #neste caso estamos definindo a-z, ou seja, serão aceitos caracteres de 
    #de a até z e o sinal de + indica as letras podem repetir em algum momento
    
       
    #Usando o comando match() analisa o padrão da expressão regular
    # e a variável nome para saber os caracteres combinam em sua configuração,
    # ou seja, se eles são minusculos, não especiais e não numéricos.
    # o comando match pode retornar que os dois elementos combinam ou 
    #retornar nenhum(None). Para descartar a possibilidade do None, utilizamos
    # a expressão "is not None"
    nome_valido = re.match(padrao,nome) is not None
    if(nome_valido==False):
        return "Nome de usuário inválido. Use apenas letras minúsculas"
    
    
    #validação dos campos nome,email e senha. 
    #verificar se há caracteres nas variáveis.
    #caso esteja vazio, não realizar o cadastro
    #comando strip: retira o excesso de espaço na variável
    if(nome.strip()=="" or email.strip()=="" or senha.strip()==""):
        msg = "Você deve preencher todos os campos"
    else:
        # definir um cursor que irá fazer a movimentação na 
        # tabela de usuário e, assim poderá ler, cadastrar,
        # atualizar e deletar dados.
        cursor = con.cursor()
        
        # Verificar se o e-mail do usuário já existe no banco de dados
        sqlConsulta = f"SELECT email FROM tbl_usuarios WHERE email='{email}' OR nome='{nome}'"
        cursor.execute(sqlConsulta)
        #Para saber se o e-mail existe ou não na tabela, estamos usando o comando
        #fetchall->fetch(buscar) all(todos), busca todos os dados que estão no 
        #select da consulta e caso tenha algum dado ele irá retorna o dado exitente
        #neste caso o email que já está cadastrado.
        #caso não tenha email cadastrado, a linha retona vazia.
        #o comando onde comparamos com o if linha[0], significa que o select tem
        #apenas um item de retorno que o email. Assim, sua posição na consulta:
        #SELECT email FROM tbl_usuarios é 0, por ser o primeiro e o único campo
        #de retorno da consulta.
        #Pegamos, então, a linha na posição zero(0) e comparamos com ""(vazio)
        #e se linha[0] for diferente(!=) de aspas aspas(""), significa que foi 
        #encontrado algo no banco e, portanto, temos um e-mail já cadastrado.
        #Isso fará com que a mensagem "E-Mail já cadastrado" seja retornada e 
        #o usuário não será cadastrado. 
        #caso contrário, ou seja, se ao fazer  compração linha[0] não retornar 
        #nada, iremos realizar o cadastro do novo usuário com seus dados, inclusive
        # email.
        
        linha = cursor.fetchall()
        
        if(linha!=[]):
            msg = "E-Mail ou Nome já cadastrado. Não é possivel cadastrar"
        else:
            # criar variavel que guarda a consulta de casdastro de usuarios
            sql=f"INSERT INTO tbl_usuarios(nome,email,senha)VALUES('{nome}','{email}','{senha}')"
            # vamos executar a consulta utilizando o comando execute com o parâmetro
            # sql(variável criada acima para o comando insert)
            cursor.execute(sql)
            # confirmar a execução da consulta com o comando commit para conexão(con)
            con.commit()
            msg = "Cadastrou"
        # fechar a movimentação do cursor com o comando close
        cursor.close()
        # fechar a conexão com o banco de dados com o comando close
        con.close()
    return msg





    
def atualizar_usuarios(id,nome,email,senha):
    
    # criar uma variável chamada msg para nos ajudar 
    # a retornar uma mensagem. Caso tenha cadastrado ou 
    # tenha dado algum erro
    msg = ""
    
    #Vamos validar a quantidade de caracteres e, para isso
    #iremos usar o comando len. Este comando tem a capacidade
    #de contar quantos caracteres há em uma variável
    if(len(senha) < 8):
        return "Sua senha dever ter no mínimo 8 caracteres"
    
    
    #Vamos fazer uma validação no nome de usuário para não aceitar
    #caracteres especiais. Utilizaremos a expressão regular para isso
    padrao = r"^[a-z]+$"
    # A expressão regular acima valida a entrada  de caracteres não especiais
    # e não númericos de a até z mínusculos.
    #O elemento ^ indica início da string e caractere $ indica o fim da string
    # entre colchetes estamos indicando quais caracteres serão aceitos
    #neste caso estamos definindo a-z, ou seja, serão aceitos caracteres de 
    #de a até z e o sinal de + indica as letras podem repetir em algum momento
    
       
    #Usando o comando match() analisa o padrão da expressão regular
    # e a variável nome para saber os caracteres combinam em sua configuração,
    # ou seja, se eles são minusculos, não especiais e não numéricos.
    # o comando match pode retornar que os dois elementos combinam ou 
    #retornar nenhum(None). Para descartar a possibilidade do None, utilizamos
    # a expressão "is not None"
    nome_valido = re.match(padrao,nome) is not None
    if(nome_valido==False):
        return "Nome de usuário inválido. Use apenas letras minúsculas"
    
    
    #validação dos campos nome,email e senha. 
    #verificar se há caracteres nas variáveis.
    #caso esteja vazio, não realizar o cadastro
    #comando strip: retira o excesso de espaço na variável
    if(nome.strip()=="" or email.strip()=="" or senha.strip()==""):
        msg = "Você deve preencher todos os campos"
    # definir um cursor que irá fazer a movimentação na 
    # tabela de usuário e, assim poderá ler, cadastrar,
    # atualizar e deletar dados.
    cursor = con.cursor()
        
    # Verificar se o e-mail do usuário já existe no banco de dados
    sqlConsulta = f"SELECT email FROM tbl_usuarios WHERE email='{email}' OR nome='{nome}'"
    cursor.execute(sqlConsulta)
    #Para saber se o e-mail existe ou não na tabela, estamos usando o comando
    #fetchall->fetch(buscar) all(todos), busca todos os dados que estão no 
    #select da consulta e caso tenha algum dado ele irá retorna o dado exitente
    #neste caso o email que já está cadastrado.
    #caso não tenha email cadastrado, a linha retona vazia.
    #o comando onde comparamos com o if linha[0], significa que o select tem
    #apenas um item de retorno que o email. Assim, sua posição na consulta:
    #SELECT email FROM tbl_usuarios é 0, por ser o primeiro e o único campo
    #de retorno da consulta.
    #Pegamos, então, a linha na posição zero(0) e comparamos com ""(vazio)
    #e se linha[0] for diferente(!=) de aspas aspas(""), significa que foi 
    #encontrado algo no banco e, portanto, temos um e-mail já cadastrado.
    #Isso fará com que a mensagem "E-Mail já cadastrado" seja retornada e 
    #o usuário não será cadastrado. 
    #caso contrário, ou seja, se ao fazer  compração linha[0] não retornar 
    #nada, iremos realizar o cadastro do novo usuário com seus dados, inclusive
    # email.
    
    linha = cursor.fetchall()
    
    if(linha!=[]):
        msg = "E-Mail ou Nome já cadastrado. Não é possivel cadastrar"
    else:
        #criar uma variável que irá guardar a consulta de atualização
        #dos dados dos usuários
        sql=f"UPDATE tbl_usuarios SET nome='{nome}',email='{email}',senha='{senha}' WHERE id={id}"
        # executar a consulta com o comando execute
        cursor.execute(sql)
        # confirmar a execução da consulta com o comando commit
        con.commit()
        msg = "Atualizou"
    # fechar a movimentação do cursor com o comando close
    cursor.close()
    
    # fechar a conexao com o banco de dados
    con.close()
    return msg
    
def autenticar_usuarios(nome,email,senha):
    #criar um cursor para realizar a movimentação dentro da tabela
    #tbl_usuarios e, assim poderá selecionar, inserir, atualizar e
    # apagar os dados dos usuários
    cursor = con.cursor()
    # criar uma consulta que irá realizar a pesquisa no banco de dados
    # em busca do usuário e sua senha correspondente.
    # vamos usar o nome de usuario ou o email e a senha para realizar
    # o processo de autenticação
    sql = f"SELECT nome,email FROM tbl_usuarios WHERE nome='{nome}' OR email='{email}' AND senha='{senha}'"
    # executa a consulta com o comando execute
    cursor.execute(sql)
    
    # confirmar a execução da consulta
    con.commit()
    
    # o resultado obtido com o comando select deverá ser guardado em uma variável
    # o comando fetchall é utilizado para armazenar o resultado da consulta select
    # o termo fetch significa buscar e all todos. Busca e armazena todos os dados
    # do comando select. O resultado será apenas um nome e email de um usuário
    rs = cursor.fetchall()
    # fechar o cursor
    cursor.close()
    # fechar a conexao com o banco de dados
    con.close()
    
    if(rs[0]==""):
        return "Usuário ou senha incorreto"
    else:
        return True
    
    
    
    
    
    