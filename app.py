from flask_openapi3 import OpenAPI, Info, Tag
from flask import Flask, redirect
from sqlalchemy.exc import IntegrityError
from model import Session, Apartamento
from schemas import *
from flask_cors import CORS

# Definindo informações e instância do OpenAPI
info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)  # Permite que o frontend acesse o backend

# Definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
apartamento_tag = Tag(name="Apartamento", description="Adição, visualização e remoção de apartamento à base")

# Rota Home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação."""
    return redirect('/openapi')

# Rota de Listar Apartamentos
@app.get('/apartamentos', tags=[apartamento_tag], responses={"200": ListagemApartamentosSchema, "404": ErrorSchema})
def get_apartamentos():
    """Busca todos os Apartamentos cadastrados."""
    session = Session()
    apartamentos = session.query(Apartamento).all()
    if not apartamentos:
        return {"message": "Nenhum apartamento cadastrado na base"}, 200
    else:
        return apresenta_apartamentos(apartamentos), 200

# Rota de Adicionar Apartamento
@app.post('/apartamento', tags=[apartamento_tag],
          responses={"200": ApartamentoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_apartamento(form: ApartamentoSchema):
    """Adiciona um novo Apartamento à base de dados."""
    apartamento = Apartamento(
        condominio=form.condominio,
        endereco=form.endereco,
        disposicao=form.disposicao,
        valor=form.valor
    )
    try:
        session = Session()
        session.add(apartamento)
        session.commit()
        return apresenta_apartamento(apartamento), 200
    except IntegrityError as e:
        error_msg = "Apartamento de mesmo nome já salvo na base :/"
        return {"mesage": error_msg}, 409
    except Exception as e:
        error_msg = "Não foi possível salvar novo apartamento :/"
        return {"mesage": error_msg}, 400

# Rota de Deletar Apartamento
@app.delete('/apartamento', tags=[apartamento_tag],
            responses={"200": ApartamentoDelSchema, "404": ErrorSchema})
def del_apartamento(query: ApartamentoBuscaSchema):
    """Deleta um Apartamento a partir do nome do condomínio informado."""
    apartamento_condominio = query.condominio
    session = Session()
    apartamento = session.query(Apartamento).filter(Apartamento.condominio == apartamento_condominio).delete()
    session.commit()

    if apartamento == 0:
        error_msg = "Apartamento não encontrado na base :/"
        return {"mesage": error_msg}, 404
    else:
        return {"mesage": "Apartamento removido", "id": apartamento_condominio}

# Inicia o app
if __name__ == "__main__":
    app.run(debug=True)