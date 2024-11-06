import pytest
import usuario as us


rs = us.cadastrar_usuarios("brunos","brunsox@gmail.com","12345678")
#vamos utilizar o comando assert para vereficar se o retorno do 
#cadastro de usuario é a mensagem "Cadastrou"
assert rs =="Cadastrou45"

#us.atualizar_usuarios(1,"Paula","paula@gmail.com","456")

# us.autenticar_usuarios