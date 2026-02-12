#!/usr/bin/env python
# coding: utf-8

# # Como instalar o `testdisk` no `Linux Ubuntu`
# 
# 
# 

# ## Resumo
# 
# Guia direto para instalar o `testdisk` no `Linux Ubuntu`, com verificação pós-instalação e comandos iniciais para uso em recuperação de partições e arquivos.
# 

# ## _Abstract_
# 
# Quick guide to install `testdisk` on Ubuntu, with post-install checks and first-run commands for partition and file recovery.
# 

# ## Descrição
# 
# ### `testdisk`
# 
# O `testdisk` é uma ferramenta de terminal voltada a recuperar partições perdidas e reparar tabelas de partição. Ele costuma vir acompanhado do `photorec`, que recupera arquivos a partir de mídias danificadas ou formatadas, mesmo sem o sistema de arquivos original.
# 

# ## 1. Instalar o `testdisk` no `Linux Ubuntu`
# 
# Para instalar o `testdisk`, siga os passos abaixo:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando:
# 
#     ```bash
#     Ctrl + Alt + T
#     ```
# 

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando:
#     ```bash
#     sudo apt clean
#     ```
# 
#     2.2 Remover pacotes `.deb` antigos ou duplicados do `cache` local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando:
#     ```bash
#     sudo apt autoclean
#     ```
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando:
#     ```bash
#     sudo apt autoremove -y
#     ```
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`:
#     ```bash
#     sudo apt update
#     ```
# 
#     2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes:
#     ```bash
#     sudo apt --fix-broken install
#     ```
# 
#     2.6 Limpar o `cache` do gerenciador de pacotes `apt` novamente:
#     ```bash
#     sudo apt clean
#     ```
# 
#     2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:
#     ```bash
#     sudo apt list --upgradable
#     ```
# 
#     2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`:
#     ```bash
#     sudo apt full-upgrade -y
#     ```

# 3. Para instalar o `testdisk`, execute:
# 
#     ```bash
#     sudo apt install testdisk -y
#     ```
# 
# 4. Para iniciar o `testdisk` com permissão administrativa, execute:
# 
#     ```bash
#     sudo testdisk
#     ```
# 

# ## 2. Primeiros passos rápidos
# 
# 1. Escolha `Create` para gerar um arquivo de _log_ e pressionar `Enter`.
# 
# 2. Selecione o disco correto (setas do teclado) e confirme em `Proceed`.
# 
# 3. Mantenha o tipo de tabela sugerido (`Intel/PC`, `EFI GPT` etc.) e avance.
# 
# 4. Use `Analyse` para buscar partições e confirme com `Write` apenas quando tiver certeza.
# 

# ## 3. Boas práticas antes de recuperar
# 
# - Trabalhe, sempre que possível, em uma cópia do disco (imagem) para evitar sobrescrever dados.
# 
# - Evite escrever novos arquivos no disco afetado até concluir a recuperação.
# 
# - Tenha um disco externo preparado para salvar os arquivos recuperados.
# 

# ## 4. Fluxo rápido com `photorec`
# 
# 1. Para abrir o `photorec`, use:
#     ```bash
#     sudo photorec
#     ```
# 
# 2. Selecione o disco, escolha o tipo de sistema de arquivos e a partição.
# 
# 3. Defina o destino de recuperação em outro disco e inicie a varredura.
# 

# ## Referências
# 
# [1] OPENAI. ***Instalar o `testdisk` no `linux ubuntu` pelo `terminal emulator`***. Disponível em: <https://chatgpt.com/c/695bf07a-a8b0-832b-9484-abd425ee520d>. ChatGPT. Acessado em: 11/12/2025.
# 
# [2] CGSECURITY. ***TestDisk & photorec***. Disponível em: <https://www.cgsecurity.org/>. Acessado em: 11/12/2025.
# 
