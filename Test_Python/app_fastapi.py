from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector as mc
# instância do FastAPI()
app = FastAPI()
# Confiruguração do cors. O cors irá permitir
# que qualquer protocolo possa requisitar nossa 
# api, desde o tradicional http, passando por 
# https, ftp, ndp e outros.

origins = ["*"]
app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])

# Conexao com o banco de dados
db = mc.connect(
    host="127.0.0.1",
    port=3307,
    user="root",
    password="",
    database="dbusuarios"
)
# criando o endpoint para acessar a tabela usuarios
@app.get("/listar")
def listar():
    cursor = db.cursor()
    sql = "SELECT * FROM tbl_usuarios"
    cursor.execute(sql)
    rs = cursor.fetchall()
    db.commit()
    cursor.close()
    db.close()
    return rs
    
    
    
