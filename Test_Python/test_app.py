import pytest
import usuario as us

# def test_cad():
#     rs = us.cadastrar_usuarios("marcia","marcia.oliveira@terra.com.br","123456789")
#     assert rs=="Cadastrou"

def test_at():
    rs = us.atualizar_usuarios()
    assert rs == "Atualizou"