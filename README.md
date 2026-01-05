# Como instalar o `testdisk` no `Linux Ubuntu`




## Resumo

Guia direto para instalar o `testdisk` no Ubuntu, com verificacao pos-instalacao e comandos iniciais para uso em recuperacao de particoes e arquivos.


## _Abstract_

Quick guide to install `testdisk` on Ubuntu, with post-install checks and first-run commands for partition and file recovery.


## Descricao

### `testdisk`

O `testdisk` e uma ferramenta de terminal voltada a recuperar particoes perdidas e reparar tabelas de particao. Ele costuma vir acompanhado do `photorec`, que recupera arquivos a partir de midias danificadas ou formatadas, mesmo sem o sistema de arquivos original.


## 1. Instalar o `testdisk` no `Linux Ubuntu`

Para instalar o `testdisk`, siga os passos abaixo:

1. Abra o `Terminal Emulator`. Voce pode fazer isso pressionando: `Ctrl + Alt + T`


2. Atualize o indice de pacotes e instale o `testdisk` com o `apt`:

    2.1 Atualizar a lista de pacotes:
    ```bash
    sudo apt update
    ```

    2.2 Instalar o `testdisk`:
    ```bash
    sudo apt install testdisk -y
    ```

    2.3 (Opcional) Confirmar a versao instalada:
    ```bash
    testdisk --version
    ```


3. Para iniciar o `testdisk` com permissao administrativa, execute:

    ```bash
    sudo testdisk
    ```


## 2. Primeiros passos rapidos

    1. Escolha `Create` para gerar um arquivo de log e pressionar `Enter`.

    2. Selecione o disco correto (setas do teclado) e confirme em `Proceed`.

    3. Mantenha o tipo de tabela sugerido (`Intel/PC`, `EFI GPT`, etc.) e avance.

    4. Use `Analyse` para buscar particoes e confirme com `Write` apenas quando tiver certeza.


## 3. Boas praticas antes de recuperar

- Trabalhe, sempre que possivel, em uma copia do disco (imagem) para evitar sobrescrever dados.

- Evite escrever novos arquivos no disco afetado ate concluir a recuperacao.

- Tenha um disco externo preparado para salvar os arquivos recuperados.


## 4. Fluxo rapido com `photorec`

1. Para abrir o `photorec`, use:
    ```bash
    sudo photorec
    ```

2. Selecione o disco, escolha o tipo de sistema de arquivos e a particao.

3. Defina o destino de recuperacao em outro disco e inicie a varredura.


## Referencias

[1] OPENAI. ***Como instalar o testdisk no Linux Ubuntu***. Disponivel em: <https://chatgpt.com/c/695bf07a-a8b0-832b-9484-abd425ee520d>. ChatGPT. Acessado em: 11/12/2025.

[2] CGSECURITY. ***TestDisk & PhotoRec***. Disponivel em: <https://www.cgsecurity.org/>. Acessado em: 11/12/2025.

