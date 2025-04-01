# Minha API
Este pequeno projeto faz parte do material diático da Disciplina **Desenvolvimento Full Stack Básico** 
O objetivo aqui é ilutsrar o conteúdo apresentado ao longo das três aulas da disciplina.
---
## Como executar 
Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.
> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).
```
(env)$ pip install -r requirements.txt
```
Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.
Para executar a API  basta executar:
```
(env)$ flask run --host 0.0.0.0 --port 5000
```
Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 
```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```
Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.

python -m venv myenv 
pip install virtualenv
.\env\scripts\activate
pip install flask reload
pip install pydantic
pip install flask flask_openapi3
pip install -r requirements.txt
pip uninstall jinja2
pip install jinja2
pip install --upgrade flask
novo_env\Scripts\activate0
pip install -U flask-openapi3[swagger,redoc,rapidoc,rapipdf,scalar,elements]
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.0.103:5000
Press CTRL+C to quit

Condominio Heitor dos Prazeres, Rua General Luís Mendes de Morais, S/N, Dois quartos, 420000
Condominio Vargas 1140, Av. Pres. Vargas 1140, Estúdio, 410000 
Condominio Epicentro, Av. Professor Pereira Reis, 42, Dois quartos c/suíte, 520000 
Residencial Quinta do Bispo, Rua do Bispo, 83, Dois quartos c/suíte, 490000

Agora é fazer as melhoras possíveis e preparar um Read.me de tal forma que não fique nenhuma dúvida.
Todos projetos de um assunto novo cabe algumas palavras que a banca avaliadora possa entendero básico da atividade a qual o Projeto se destina.
Projeto de Imobiliária é bem específico e investirei um tempo para nivelar a informação de algumas mudanças que eu fiz para implantar o que eu passarei a chamar de Versão Beta, pois a Versão Alfa é a que o cliente deseja.
No início eu cheguei a aprontar o Frontend para Imóveis Novos e Usados, sendo este último para clientes que comprassem o Imóvel novo da Construtora Cury.