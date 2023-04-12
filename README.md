# ws-tp1
MEI Web Semântica Trabalho Prático 1 

## Pastas e conteúdos:
```
/Converter/ -> pasta que possui script para converter, dados originais, dados convertidos e dados atualizados
          /scv_to_nt.py -> ficheiro Python que faz a conversão do books.csv para um ficheiro em N-Triples
          /books.csv -> ficheiro original retirado do kaggle (https://www.kaggle.com/datasets/jealousleopard/goodreadsbooks)
          /books.nt -> ficheiro criado pelo script
          /new.nt -> ficheiro atualizado após queries com novas informações para os dados
```

```
/Dataset/ -> pasta com o ficheiro original retirado do kaggle 
          /books.csv -> ficheiro original retirado do kaggle (https://www.kaggle.com/datasets/jealousleopard/goodreadsbooks)
```

```
/GraphDB/ -> pasta que possui ficheiro python com todas as queries criadas para explorar, visualizar e perceber os dados
          /queries.py -> ficheiro Python com todas as queries criadas ao longo do projeto (algumas usadas na aplicação)
```

```
/books/ -> projeto Django da aplicação desenvolvida
```

## Configuração para executar a aplicação:

Criar repositório no graphDB
```
Setup > Repositories > Create new repository > GraphDB Repository
Repository ID: books

```

Importar os dados para o GraphDB
```
Import > Upload RDF files
Open /Converter/new.nt
Import
```
Executar projeto Django
```bash
python3 books/manage.py runserver
```
Executar conversor
```bash
python3 Converter/csv_to_nt.py Converter/books.csv
```

          
