# GeoBeats - Sistema de Gestão Musical

Aplicação web desenvolvida em Python com Django para gerenciamento de músicas, álbuns e playlists. O sistema oferece uma interface web moderna e uma API RESTful completa, permitindo operações de CRUD com autenticação de usuários e isolamento de dados.

---

## Objetivo

Fornecer uma aplicação completa para gestão de biblioteca musical, permitindo que cada utilizador cadastre, organize e gerencie suas músicas, álbuns e playlists de forma segura e estruturada.

---

## Funcionalidades

* Autenticação de usuários (registro, login e logout)
* Gerenciamento completo de músicas
* Gerenciamento completo de álbuns
* Gerenciamento completo de playlists
* Relacionamento entre playlists e músicas (Many-to-Many)
* Interface web responsiva com tema escuro
* API RESTful com suporte a operações CRUD
* Isolamento de dados por usuário

---

## Tecnologias utilizadas

* Python
* Django
* Django Rest Framework (DRF)
* SQLite
* HTML5
* CSS3
* Bootstrap 5
* JSON

---

## Estrutura do projeto

```bash
geobeats/
│
├── setup/              # Configurações do projeto (settings, urls)
├── music/              # App principal
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── static/             # Arquivos estáticos (CSS, imagens)
├── templates/          # Templates HTML
├── manage.py           # Gerenciador do Django
└── requirements.txt    # Dependências
```

---

## Instalação e execução

### 1. Clonar o repositório

```bash
git clone https://github.com/geovanelvs/geobeats.git
cd geobeats
```

---

### 2. Criar ambiente virtual

```bash
python -m venv venv
```

---

### 3. Ativar ambiente virtual

**Windows**
```bash
venv\Scripts\activate
```

**Linux/Mac**
```bash
source venv/bin/activate
```

---

### 4. Instalar dependências

```bash
pip install -r requirements.txt
```

ou

```bash
pip install django djangorestframework
```

---

### 5. Aplicar migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 6. Criar usuário administrador

```bash
python manage.py createsuperuser
```

---

### 7. Executar a aplicação

```bash
python manage.py runserver
```

---

## Acesso

Servidor local:

```
http://127.0.0.1:8000/
```

---

## Endpoints da API

### 1. Listar músicas

* Método: GET  
* Rota: `/api/musicas/`  
* Status: 200 OK  

```bash
curl http://127.0.0.1:8000/api/musicas/
```

---

### 2. Buscar música por ID

* Método: GET  
* Rota: `/api/musicas/{id}`  
* Status: 200 OK / 404 Not Found  

```bash
curl http://127.0.0.1:8000/api/musicas/1
```

---

### 3. Criar música

* Método: POST  
* Rota: `/api/musicas/`  
* Status: 201 Created  

#### Corpo da requisição:

```json
{
  "titulo": "Nome da Música",
  "artista": "Artista",
  "album": "Álbum",
  "genero": "Gênero"
}
```

---

### 4. Atualizar música

* Método: PUT / PATCH  
* Rota: `/api/musicas/{id}`  
* Status: 200 OK / 404 Not Found  

---

### 5. Remover música

* Método: DELETE  
* Rota: `/api/musicas/{id}`  
* Status: 204 No Content / 404 Not Found  

---

## Modelo de dados

### Música

| Campo   | Tipo  | Descrição           |
|--------|------|---------------------|
| id     | INT  | Identificador único |
| titulo | TEXT | Nome da música      |
| artista| TEXT | Nome do artista     |
| genero | TEXT | Gênero musical      |

---

### Álbum

| Campo | Tipo  | Descrição           |
|------|------|---------------------|
| id   | INT  | Identificador único |
| nome | TEXT | Nome do álbum       |

---

### Playlist

| Campo | Tipo  | Descrição           |
|------|------|---------------------|
| id   | INT  | Identificador único |
| nome | TEXT | Nome da playlist    |

---

## Boas práticas aplicadas

* Arquitetura baseada em Django (MVT)
* Uso de Django Rest Framework
* Separação de responsabilidades (models, views, serializers)
* Retorno de dados em JSON
* Uso correto de códigos HTTP
* Isolamento de dados por usuário
* Interface responsiva

---

## Observações

* O banco SQLite é utilizado para desenvolvimento
* Recomenda-se não versionar o arquivo `db.sqlite3`
* Pode ser facilmente adaptado para PostgreSQL em produção

---

## Autor

Geovane Alves
