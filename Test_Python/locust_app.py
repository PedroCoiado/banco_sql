from locust import HttpUser, task, between

class test_locust(HttpUser):
    tempo_chamada = between(1,3)
    url_chamada = "http://127.0.0.1:8000"
    
    @task
    def index_page(self):
        resposta = self.client.get("/listar")
        if(resposta.status_code == 200):
            print("Passou no teste de carregamento :",resposta.text)
        else:
            print("Não passou no teste de carregamento: ",resposta.text)
        