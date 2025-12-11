# Como instalar e usar o editor `nano` no `Linux Ubuntu`



## Resumo

Guia rápido para instalar, configurar e usar o editor de texto `nano` no Ubuntu, incluindo atalhos essenciais e ajustes de ergonomia baseados na sessão do ChatGPT.

## _Abstract_

Quick guide on installing, configuring, and using the `nano` text editor on Ubuntu, with essential shortcuts and usability tweaks captured from the ChatGPT session.

## Descrição

### `nano`

O `nano` é um editor de terminal leve e pré-instalado em muitas distribuições, voltado para edição rápida de arquivos de configuração e código. Ele destaca atalhos diretamente no rodapé, suporta sintaxe, numeração de linhas e wraps automáticos, sendo uma opção acessível quando se precisa editar em servidores ou WSL sem interface gráfica.

1. Instalar e validar o `nano` (passos marcados como "Deu certo!" no chat):

    1.1 Confirmar o pacote disponível nos repositórios oficiais do Ubuntu:
    ```bash
    apt policy nano
    ```

    1.2 Instalar (ou garantir a atualização) a partir dos repositórios oficiais:
    ```bash
    sudo apt update
    sudo apt install nano -y
    ```

    1.3 Conferir a versão instalada:
    ```bash
    nano --version
    ```

    1.4 Criar e editar um arquivo de teste:
    ```bash
    mkdir -p ~/tmp/nano-teste && cd ~/tmp/nano-teste
    printf 'linha 1\nlinha 2\n' > notas.txt
    nano notas.txt
    ```
    Dentro do `nano`, salve com `Ctrl+O` (Enter para confirmar o nome) e saia com `Ctrl+X`. Em seguida, valide o conteúdo:
    ```bash
    cat notas.txt
    ```

2. Ajustes rápidos de usabilidade

    2.1 Criar ou editar `~/.nanorc` com opções úteis:
    ```bash
    cat <<'EOF' >> ~/.nanorc
    set linenumbers
    set softwrap
    set tabsize 4
    set mouse
    EOF
    ```

    2.2 Reabra o `nano` para carregar as configurações. Use `nano ~/.nanorc` para ajustar as opções conforme preferências.

    2.3 Se quiser desativar o mouse ou wraps em uma sessão, inicie o editor com flags temporárias, por exemplo:
    ```bash
    nano -c -i arquivo.txt
    ```
    (`-c` exibe a posição do cursor na barra de status, `-i` mantém a indentação ao quebrar linhas).

3. Comandos essenciais dentro do `nano`

- `Ctrl+G`: abre a ajuda embutida com a lista completa de atalhos.
- `Ctrl+W` busca texto; `Alt+W` repete a busca.
- `Ctrl+K` recorta a linha ou seleção; `Ctrl+U` cola.
- `Ctrl+\` substitui texto; `Ctrl+^` (Ctrl+6) marca o início de uma seleção.
- `Ctrl+_` (Ctrl+Shift+-) permite ir direto para `linha,coluna`.
- `Alt+/` vai ao final do arquivo; `Alt+\` retorna ao início.
- `Ctrl+O` salva rapidamente; `Ctrl+X` sai.

4. Fluxos comuns

1. Editar com backup rápido antes de alterar configurações sensíveis:
    ```bash
    cp /etc/hosts /tmp/hosts.bak && sudo nano /etc/hosts
    ```

2. Abrir um arquivo ignorando configurações pessoais (útil para depurar a nanorc):
    ```bash
    nano -I arquivo.txt
    ```

3. Escrever notas longas e alinhar parágrafos usando `Ctrl+J` para justificar o texto selecionado.

## Referências

[1] OPENAI. ***Como instalar e usar o editor nano no Linux Ubuntu***. Disponível em: <https://chatgpt.com/c/69398f2b-bca8-8329-90ec-19a18d3dd429>. ChatGPT. Acessado em: 11/12/2025.
