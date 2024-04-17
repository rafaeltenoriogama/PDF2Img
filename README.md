## PDF para PNG Converter usando Django Web Framework

Este é um simples software desenvolvido em Python usando o Django Web Framework, que permite transformar arquivos PDF em imagens PNG.

## Funcionalidades

    Converte arquivos PDF em imagens PNG.
    Interface web simples e intuitiva.
    Possibilidade de upload de múltiplos arquivos simultaneamente.
    Facilidade de instalação e execução.

Requisitos de Instalação

    Python 3.x
    Django
    pdftoppm (para conversão de PDF para imagens)

Estrutura do Django

O Django segue uma estrutura de projeto MVC (Model-View-Controller) ou MVT (Model-View-Template). Aqui está uma visão geral da estrutura do projeto:

php

pdf_to_png_converter/
├── pdf_to_png_converter/
│   ├── settings.py       # Configurações do projeto
│   ├── urls.py           # Mapeamento de URLs
│   └── wsgi.py           # Ponto de entrada para servidores web
├── converter/            # Aplicativo principal
│   ├── migrations/       # Migrações de banco de dados
│   ├── templates/        # Templates HTML
│   ├── __init__.py
│   ├── admin.py          # Configurações do admin
│   ├── apps.py           # Configurações do aplicativo
│   ├── forms.py          # Formulários do aplicativo
│   ├── models.py         # Modelos de dados
│   ├── tests.py          # Testes do aplicativo
│   └── views.py          # Lógica de visualização
├── media/                # Local de armazenamento de arquivos de mídia
├── static/               # Arquivos estáticos (CSS, JavaScript, etc.)
└── manage.py             # Utilitário de linha de comando para administração do projeto

    pdf_to_png_converter/: Diretório principal do projeto.
    pdf_to_png_converter/: O diretório contém as configurações do projeto Django.
    converter/: O aplicativo principal do projeto.
        migrations/: Diretório que contém migrações de banco de dados.
        templates/: Diretório que contém os modelos HTML.
        views.py: Contém a lógica de visualização (controlador).
        models.py: Define os modelos de dados (Model).
        forms.py: Contém os formulários do aplicativo.
        admin.py: Configurações para a interface de administração do Django.

Como Usar

    Clone este repositório: git clone https://github.com/seu-usuario/pdf_to_png_converter.git
    Instale os requisitos: pip install -r requirements.txt
    Execute as migrações do banco de dados: python manage.py migrate
    Inicie o servidor: python manage.py runserver
    Acesse a aplicação em seu navegador: http://localhost:8000