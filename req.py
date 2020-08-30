import requests
import json

class ListaDeRepositorios():

    def __init__(self,usuario):

        self._usuario= usuario

    def requisicao_api(self):
        
        resposta = requests.get(f'https://api.github.com/users/{self._usuario}/repos')
        if resposta.status_code == 200:
            return resposta.json()
        else:
            return resposta.status_code
    def imprime_repositorios(self):
        
        dados_api = self.requisicao_api()
        
        if type(dados_api) is not int:
            for i in range(len(dados_api)):
                context = {
                        "nome": dados_api[i]['name'],
                        "linguagem": dados_api[i]['language'],
                        "url_clone": dados_api[i]['clone_url'],
                        "visualizações": dados_api[i]['watchers']
                    }
                print(context)
                
        else:
            print(dados_api)
repositorios = ListaDeRepositorios('mateusrodc')
repositorios.imprime_repositorios()
        



