# Como publicar este projeto no GitHub (passo a passo)

## Escolha de repositório

Nome sugerido: `gemini-connected-apps-smart-water-lab`  
Conta detectada pela conexão GitHub: `enps2015`  
Visibilidade recomendada: **Public**, pois o objetivo é permitir reprodução pela comunidade. O repositório contém apenas dados sintéticos, código e documentação. Antes de publicar, confirme que não foram adicionados materiais privados.

Já existe um projeto relacionado na sua conta: `https://github.com/enps2015/smart-hydrometer-data-simulation`. Este novo repositório tem escopo mais estreito: auditoria do detector por vazão/pressão e experimento com Apps Conectados do Gemini, evitando duplicar a coleção maior de hidrômetros.

## 1. Criar o repositório vazio

1. Abra https://github.com/new e entre na conta `enps2015`.
2. Repository name: `gemini-connected-apps-smart-water-lab`.
3. Description: `Reproducible educational experiment using Gemini Connected Apps and Gemini 4 Argon to audit a synthetic smart-water anomaly detector.`
4. Selecione **Public**.
5. **Não** marque Add a README, Add .gitignore ou Choose a license, porque este pacote já inclui esses arquivos.
6. Clique em Create repository.

A criação do repositório pela interface web é necessária porque a conexão GitHub disponível nesta sessão permite consultar repositórios e criar/atualizar arquivos dentro de um repositório existente, mas não expõe uma ação de criação de repositório.

## 2. Descompactar o pacote e fazer o primeiro push

Descompacte o ZIP de modo que a pasta `gemini-connected-apps-smart-water-lab` contenha `README.md`, `LICENSE`, `data/`, `src/`, `tests/` e `docs/` diretamente.

No terminal Linux, entre na pasta do projeto e execute:

```bash
git init -b main
git add .
git status --short
git commit -m "chore: initial Smart Water Anomaly Lab prototype"
git remote add origin https://github.com/enps2015/gemini-connected-apps-smart-water-lab.git
git push -u origin main
```

Antes de `git commit`, confira `git status --short` para verificar que não está incluindo arquivos pessoais ou grandes arquivos acidentais. Se o Git pedir identificação, configure `git config --global user.name` e `git config --global user.email` com os dados que deseja associar aos commits.

## 3. Conferir no GitHub

- O README aparece na página inicial.
- Os arquivos `data/telemetry_synthetic_5min.csv` e `data/ground_truth_events.csv` estão presentes.
- A pasta `src/` contém o gerador e o baseline.
- A pasta `.github/workflows/` contém `python-tests.yml`.
- O workflow de testes executa depois do primeiro push.
- O repositório permanece abaixo de 100 MB para a importação pelo Gemini Web.

## 4. Importar para o Gemini

No Gemini Web em computador: **Adicionar arquivo → Mais uploads → Importar código**, informe o URL do repositório ou da branch, clique em Importar e só depois cole o prompt de `docs/03_PROMPT_GEMINI_ARGON.md`. A conexão importa um snapshot. Se alterar o código depois, importe novamente para uma nova revisão.
