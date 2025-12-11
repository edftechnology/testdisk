# Como instalar e usar o editor `nano` no `Linux Ubuntu`




## Resumo

Guia rápido para instalar, configurar e usar o editor de texto `nano` no Ubuntu, incluindo atalhos essenciais e ajustes de ergonomia baseados na sessão do ChatGPT.


## _Abstract_

Quick guide on installing, configuring, and using the `nano` text editor on Ubuntu, with essential shortcuts and usability tweaks captured from the ChatGPT session.


## Descrição

### `nano`

O `nano` é um editor de terminal leve e pré-instalado em muitas distribuições, voltado para edição rápida de arquivos de configuração e código. Ele destaca atalhos diretamente no rodapé, suporta sintaxe, numeração de linhas e wraps automáticos, sendo uma opção acessível quando se precisa editar em servidores ou WSL sem interface gráfica.


## 1. Instalar o `nano` no `Linux Ubuntu`

Para instalar o `nano`, siga os passos abaixo:

1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`

2. Certifique-se de que seu sistema esteja limpo e atualizado.

    2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando:
    ```bash
    sudo apt clean
    ```

    2.2 Remover pacotes `.deb` antigos ou duplicados do `cache` local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando:
    ```bash
    sudo apt autoclean
    ```

    2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando:
    ```bash
    sudo apt autoremove -y
    ```

    2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`:
    ```bash
    sudo apt update
    ```

    2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes:
    ```bash
    sudo apt --fix-broken install
    ```

    2.6 Limpar o `cache` do gerenciador de pacotes `apt` novamente:
    ```bash
    sudo apt clean
    ```

    2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:
    ```bash
    sudo apt list --upgradable
    ```

    2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`:
    ```bash
    sudo apt full-upgrade -y
    ```


3. Para instalar o `nano`, execute o comando:

    ```bash
    sudo apt install nano -y
    ```

## 2. Ajustes rápidos de usabilidade

    4.1 Criar ou editar `~/.nanorc` com opções úteis:
    
    ```bash
    cat <<'EOF' >> ~/.nanorc
    set linenumbers
    set softwrap
    set tabsize 4
    set mouse
    EOF
    ```

    4.2 Reabra o `nano` para carregar as configurações. Use `nano ~/.nanorc` para ajustar as opções conforme preferências.

    4.3 Se quiser desativar o mouse ou wraps em uma sessão, inicie o editor com flags temporárias, por exemplo:
    
    ```bash
    nano -c -i arquivo.txt
    ```
    
    (`-c` exibe a posição do cursor na barra de status, `-i` mantém a indentação ao quebrar linhas).


## 3. Comandos essenciais dentro do `nano`

- `Ctrl+G`: abre a ajuda embutida com a lista completa de atalhos.

- `Ctrl+W` busca texto; `Alt+W` repete a busca.

- `Ctrl+K` recorta a linha ou seleção; `Ctrl+U` cola.

- `Ctrl+\` substitui texto; `Ctrl+^` (Ctrl+6) marca o início de uma seleção.

- `Ctrl+_` (Ctrl+Shift+-) permite ir direto para `linha,coluna`.

- `Alt+/` vai ao final do arquivo; `Alt+\` retorna ao início.

- `Ctrl+O` salva rapidamente; `Ctrl+X` sai.


## 5. Fluxos comuns

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

