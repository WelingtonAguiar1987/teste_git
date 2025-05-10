O que é Git e GitHub?
Git: É um sistema de controle de versão. Pense nele como um "diário mágico" do seu projeto. Ele registra todas as mudanças que você faz nos arquivos (código, textos, etc.) e permite voltar no tempo, comparar versões ou recuperar algo que você apagou por acidente.

GitHub: É uma plataforma online que armazena seus projetos versionados pelo Git. É como uma "nuvem" onde você pode guardar seu "diário" (repositório), compartilhar com outros e colaborar em equipe.

Por que usar Git e GitHub?
Organização: Você sabe exatamente o que mudou no projeto e quando.

Segurança: Não perde seu trabalho, mesmo se apagar algo por engano.

Colaboração: Permite que várias pessoas trabalhem no mesmo projeto sem conflitos.

Histórico: Você pode voltar para qualquer versão anterior do projeto.

Passo a passo para usar Git e GitHub
1. Instalar o Git
O que fazer: Baixe e instale o Git no seu computador.
Acesse git-scm.com e siga as instruções para Windows, Mac ou Linux.

Teste a instalação: Abra o terminal (Prompt de Comando no Windows ou Terminal no Mac/Linux) e digite:
bash

git --version

Se aparecer a versão do Git, está instalado!

2. Configurar o Git
Diga ao Git quem você é (isso identifica suas alterações):
bash

git config --global user.name "Seu Nome"
git config --global user.email "seu.email@exemplo.com"

3. Criar uma conta no GitHub
Acesse github.com e crie uma conta gratuita.

Após criar a conta, você pode criar um repositório (um lugar para guardar seu projeto).

4. Entendendo o básico do Git
Pense no Git como um sistema que tira "fotos" do seu projeto em diferentes momentos. Essas "fotos" são chamadas de commits. Cada commit é uma versão do seu projeto.
Repositório: É a pasta onde o Git guarda o projeto e o histórico de mudanças. Pode ser local (no seu PC) ou remoto (no GitHub).

Commit: É como salvar uma versão do seu projeto no "diário".

Branch: É como uma linha do tempo alternativa. Você pode criar uma branch para testar ideias sem mexer na versão principal (chamada main ou master).

Merge: É juntar as mudanças de uma branch com a principal.

Como começar um projeto com Git
a) Criar um repositório local
Crie uma pasta para seu projeto no computador:
bash

mkdir meu-projeto
cd meu-projeto

Inicie o Git na pasta:
bash

git init

Isso cria um repositório vazio (o "diário" começa em branco).

Crie um arquivo (exemplo: index.html) e adicione conteúdo.

Diga ao Git para "rastrear" esse arquivo:
bash

git add index.html

(Use git add . para rastrear todos os arquivos da pasta.)

Faça um commit (salve a "foto" do projeto):
bash

git commit -m "Primeiro commit: criei o index.html"

A mensagem (-m) descreve o que você fez.

b) Conectar ao GitHub
No GitHub, clique em New Repository, dê um nome (ex.: meu-projeto), escolha público ou privado e crie.

O GitHub vai mostrar comandos para conectar seu repositório local ao remoto. Exemplo:
bash

git remote add origin https://github.com/seu-usuario/meu-projeto.git
git branch -M main
git push -u origin main

git remote add origin: Liga seu repositório local ao GitHub.

git push: Envia seus commits para o GitHub.

c) Fluxo básico de trabalho
Edite seus arquivos (ex.: modifique index.html).

Adicione as mudanças:
bash

git add .

Faça um commit:
bash

git commit -m "Atualizei o index.html"

Envie para o GitHub:
bash

git push origin main

Funções principais do Git
Ver o status do projeto:
bash

git status

Mostra quais arquivos foram modificados e estão prontos para commit.

Ver o histórico de commits:
bash

git log

Lista todos os commits com suas mensagens.

Criar uma branch:
bash

git branch nova-funcionalidade
git checkout nova-funcionalidade

(Ou combine: git checkout -b nova-funcionalidade)

Juntar branches (merge):
Volte para a branch principal:
bash

git checkout main

Junte a branch:
bash

git merge nova-funcionalidade

Clonar um repositório:
Para baixar um projeto do GitHub:
bash

git clone https://github.com/usuario/projeto.git

Atualizar seu repositório local:
Se o repositório remoto mudou (ex.: alguém adicionou algo no GitHub):
bash

git pull origin main

Como colaborar no GitHub
Fork: Se quer contribuir para o projeto de outra pessoa, faça um "fork" (cópia) no GitHub, clicando no botão "Fork".

Clone o fork para seu PC:
bash

git clone https://github.com/seu-usuario/projeto.git

Crie uma branch, faça mudanças e envie ao seu fork:
bash

git push origin sua-branch

No GitHub, crie um Pull Request (PR) para sugerir suas mudanças ao dono do projeto original.

Dicas para iniciantes
Faça commits pequenos e descritivos: Em vez de um commit gigante, faça vários commits com mensagens claras (ex.: "Adicionei o menu" em vez de "Mudei coisas").

Use branches para experimentar: Isso evita bagunçar a versão principal.

Evite conflitos: Sempre faça git pull antes de começar a trabalhar, para ter a versão mais recente.

Leia mensagens de erro: O Git explica o que deu errado (ex.: "conflito de merge") e sugere soluções.

Exemplo prático
Imagine que você está criando um site:
Crie a pasta, inicialize o Git (git init) e adicione um arquivo index.html.

Faça um commit: git add . && git commit -m "Página inicial criada".

Crie um repositório no GitHub e conecte com git remote add origin.

Envie: git push origin main.

Para adicionar um CSS, crie uma branch (git checkout -b estilo), adicione style.css, faça commit e merge com a branch principal.

Envie tudo ao GitHub: git push origin main.

Resumo dos comandos mais usados
Comando

Função

git init

Inicia um repositório Git

git add <arquivo>

Adiciona arquivo(s) para o commit

git commit -m "mensagem"

Salva uma versão com uma mensagem

git push origin main

Envia mudanças para o GitHub

git pull origin main

Atualiza seu repositório local

git branch <nome>

Cria uma nova branch

git checkout <nome>

Muda para uma branch

git merge <nome>

Junta uma branch com a atual

git clone <url>

Baixa um repositório do GitHub

