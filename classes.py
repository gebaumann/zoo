import os
from peewee import *
from flask import Flask, json, jsonify
from playhouse.shortcuts import model_to_dict

arq = 'many−to−many−com−lista.db'
db = SqliteDatabase (arq)

class BaseModel(Model):
    class Meta:
        database = db

class Alimento(BaseModel):
    nome = CharField()
    quantidade = CharField()
    tipo_alimentacao_do_animal = CharField() 

class Animal(BaseModel):
    especie = CharField()
    nome = CharField()
    idade = CharField()
    sexo = CharField()
    alimento = ForeignKeyField(Alimento)

class Funcionario(BaseModel):
    nome = CharField()
    cargo = CharField()
    cpf = CharField()
    turno = CharField()

class Setor(BaseModel):
    nome = CharField()
    localizacao = CharField()
    animais = ForeignKeyField(Animal)
    tipo_setor = CharField()

class Visitante(BaseModel):
    nome = CharField()
    idade = IntegerField()
    cpf = CharField()

class Ingresso(BaseModel):
    preco = FloatField()
    cod_ingresso = CharField()
    visitante = ForeignKeyField(Visitante)

class Bilheteria(BaseModel):
    localizacao = ForeignKey(Setor)
    ingresso = ForeignKeyField(Ingresso)

class Produto(BaseModel):
    tipo_produto = CharField()
    cod_indentificador = IntegerField()
    quantidade = IntegerField()

class Estoque(BaseModel):
    alimentacao = ForeignKeyField(Alimento)
    produto = ForeignKeyField(Produto)
    fornecedor = CharField()

class Zoologico(BaseModel):
    nome = CharField()
    setor = ForeignKeyField(Setor)
    funcionario = ForeignKeyField(Funcionario)


if __name__ == "__main__":
    db.connect()
    db.create_tables([Alimento, Animal, Funcionario, Setor, Visitante, Ingresso, Bilheteria, Produto, Estoque, Zoologico])

    
    alimento1 = Alimento.create(nome = "amora" , quantidade = "44 quilos" , tipo_alimentacao_do_animal = "herbívoro" )
    animal1 = Animal.create(especie = "girafa", nome = "Gigi", idade = "4 anos", sexo = "feminino", alimento = alimento1)
    funcionario1 = Funcionario.create(nome = "Joaquim Menezes", cargo = "Veterinário", cpf = "02304202302", turno = "matutino")
    setor1 = Setor.create(nome = "Savana", localizacao = "sul", animais = animal1, tipo_setor = "terrestre")
    visitante1 = Visitante.create(nome = "Juliana Paes", idade = 42, cpf = "02302502404")
    ingresso1 = Ingresso.create(preco = 14.50, cod_ingresso = "452313", visitante = visitante1)
    bilheteria1 = Bilheteria.create(localizacao = setor1, ingresso = ingresso1)
    produtos1 = Produto.create(tipo_produto = "limpeza", cod_indentificador = 4123733, quantidade = 40)
    estoque1 = Estoque.create(alimentacao = alimento1, produto = produtos1, forncedor = "mercado tudo")
    zoologico1 = Zoologico.create(nome = "AnjinhosZoo", setores = setor1, funcionario = funcionario1)
    
    json = list(map(model_to_dict, Alimento.select()))

    print(json)
