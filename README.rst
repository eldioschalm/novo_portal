IFMT
====

Pré-requisitos do requirements.txt:

- requisito do python-ldap, executar:

$ sudo aptitude install build-essential python-dev libldap2-dev libsasl2-dev libssl-dev

- requisito para instalar PIL:

$ sudo aptitude install libjpeg libjpeg-dev libfreetype6 libfreetype6-dev zlib1g-dev

- resquisito para instalar psycopg2

$ sudo aptitude install postgresql-9.3 postgresql-server-dev-9.3
ou caso não seja ambiente de produção,
$ sudo aptitude install libpq-dev python-dev

- requisito para memcached
$ sudo aptitude install memcached libmemcached-dev python-pylibmc


- requisito para o módulo dirf (pyPdf que já está no requirements.txt) e pdftk via pacote debian
$ sudo aptitude install pdftk

Desenvolvimento do novo portal do IFMT

----
Versão 1.2.2

- Adicionado restrição no tamanho da imagem usada como destaque para notícias.

----
Versão 1.2.1

- Correção de exibição de thumbnail na lista de vídeos.

----
Versão 1.2

- Atualização para o django 1.7;

- Atualização de apps de terceiros.

----
Versão 1.1.4

- Melhorias no sistema de cache.

----
Versão 1.1.4

- Alterações no settings para melhoria de performance.

----
Versão 1.1.4

- Remoção de compressor html e minify dos arquivos css.

----
Versão 1.1.3

- Adição de compressor html e minify dos arquivos css.

----
Versão 1.1.2

- Correção na contagem de visitas das páginas de detalhe.

----
Versão 1.1.1

- Melhorias de performance das páginas iniciais.

----

Versão 1.1

- Atualização do django para versão 1.6.8

----
Versão 1.0

- Melhorias nas apps de conteúdo;

- Permissões por site para cada usuário;

- Adição do tinymce como editor wysiwyg;

- Adição da app django-reversion;

- Ajuste das cores dos templates;

----
Versão 0.2

- Adicionado guia de curso;

- Adicionado sistemas de tags;

- Refatoração em geral;

----
Versão 0.1

- Templates ajustados para uso do framework Zurb Foundation;

- Conteúdos adicionados:
    - Notícias;
    - Galeria de fotos;
    - Vídeos;
    - Eventos;

- Área de Seleção com filtros;

- Dados iniciais;

----
