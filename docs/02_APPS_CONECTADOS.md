# Protocolo operacional: Apps Conectados no Gemini Web

## Objetivo do teste

Comprovar, por registros verificáveis, como **GitHub**, **Google Workspace** e **YouTube** contribuem para um fluxo de trabalho de engenharia. O modelo escolhido para a execução principal será **Gemini 4 Argon**. O app Serviços de pesquisa pode ser usado para conferir fontes públicas quando disponível na configuração do usuário.

Não contar um app como utilizado só porque está ativado em Configurações. Registrar se foi efetivamente acionado e que material trouxe.

## Pré-requisitos

1. Fazer login em https://gemini.google.com no computador e selecionar Gemini 4 Argon no seletor de modelo.
2. Confirmar em Configurações → Apps conectados que GitHub, Google Workspace, YouTube e Serviços de pesquisa aparecem habilitados. A disponibilidade exata pode variar por conta, idioma e interface.
3. Ter o repositório público `gemini-connected-apps-smart-water-lab` criado no GitHub e preenchido com os arquivos deste projeto.
4. No Google Drive, criar uma pasta `GeminiLab_SmartWater`.
5. Importar `data/telemetry_synthetic_5min.csv` para uma nova Google Sheet chamada `GeminiLab_Telemetria_Sintetica`. Manter cabeçalhos e todas as linhas. Esse arquivo contém só as medições sintéticas, não os rótulos de verdade-terreno.
6. Criar um Google Doc `EXPERIMENT_JOURNAL_SMART_WATER` dentro da mesma pasta, contendo: data/hora, modelo, versão visível, repositório e commit importado se conhecido, prompt utilizado, Apps efetivamente acionados, resultados e limitações.
7. Opcional para auditoria: criar uma segunda Google Sheet `GeminiLab_Eventos_Referencia` importando `data/ground_truth_events.csv`. Utilizá-la na fase de avaliação, não como variável de entrada para o detector.

## App 1 — GitHub: analisar o código importado

**Ação exata:** em um novo chat do Gemini Web, clicar no botão de adicionar arquivo → Mais uploads → Importar código → inserir URL do repositório ou branch → Importar. Não basta colar a URL no texto do prompt.

**Perguntas concretas a pedir ao modelo:**

- Quais arquivos definem o gerador, detector, testes e métricas?
- Quais variáveis entram de fato no detector? Algum rótulo de referência foi usado como feature?
- Os testes verificam cadência, integridade temporal e separação dos rótulos?
- Quais pressupostos simplificados poderiam tornar a métrica artificialmente otimista?
- Que caso de teste adversarial poderia revelar um falso positivo ou falso negativo?

**Entrega esperada:** inventário de arquivos por caminho, revisão da lógica, achados classificados por gravidade, recomendação de testes e trechos referenciados pelo caminho do arquivo.

**Limites importantes da conexão:** a documentação do Google informa que o Gemini consegue analisar o código importado, mas não recupera histórico de commits/PRs/metadados, não lê o repositório só porque sua URL foi colada no prompt e não escreve de volta no GitHub. O repositório importado fica como snapshot; mudanças posteriores não são sincronizadas automaticamente. A importação tem limite documentado de 5.000 arquivos e 100 MB por chat. Fonte: https://support.google.com/gemini/answer/16176929?hl=pt-BR

## App 2 — Google Workspace: consultar o dossiê controlado

**Ação prévia:** Eric cria a pasta, importa a telemetria CSV numa Google Sheet e cria o diário de execução. Esses materiais são disponibilizados por Eric, não por uma instituição externa. A origem científica das ideias do projeto está indicada em `01_FUNDAMENTACAO_CIENTIFICA.md`.

**Prompt de recuperação:**

`@Google Workspace Localize no meu Drive o documento EXPERIMENT_JOURNAL_SMART_WATER e a planilha GeminiLab_Telemetria_Sintetica dentro da pasta GeminiLab_SmartWater. Informe quais arquivos realmente localizou, o nome do arquivo, a dimensão aproximada dos dados acessíveis, os nomes das colunas e qualquer limitação de acesso. Não invente valores nem afirme ter lido a planilha se não conseguiu abri-la.`

**Validação:** conferir no resultado que a planilha correta foi localizada. Pedir ao modelo para enumerar os cabeçalhos. Comparar manualmente os cabeçalhos com `data/data_dictionary.csv`. Se só localizar o arquivo ou não conseguir ler os valores, registrar essa limitação e não dizer que houve análise dos dados via Workspace.

**Entrega esperada:** confirmação de localização/acesso e uma síntese contextual do diário; a Google Sheet serve como fonte de verificação complementar para os campos e a estrutura da telemetria.

**Privacidade:** esses dados são sintéticos; ainda assim, não compartilhar documentos pessoais, e-mails, arquivos de trabalho da concessionária ou dados operacionais restritos no projeto público.

## App 3 — YouTube: pesquisa técnica qualificada

O YouTube deve fornecer contexto técnico, não funcionar como prova final. Use somente conteúdo público pertinente e registre os links que de fato forem retornados.

**Consulta em português brasileiro:**

`@YouTube Encontre aulas universitárias, seminários de pesquisa ou workshops técnicos sobre detecção e localização de vazamentos em redes de distribuição de água, usando sensores SCADA de vazão e pressão. Priorize universidades, grupos de pesquisa, instituições de saneamento e palestrantes identificados. Procure materiais sobre o benchmark BattLeDIM/L-Town ou métodos de detecção baseados em pressão e vazão. Para cada resultado, informe título, canal/instituição, data, palestrante quando identificado, método discutido e link. Exclua opinião sem referências como fundamento científico.`

**Consulta em inglês:**

`@YouTube Find university lectures, research seminars or engineering workshops on leakage detection in water distribution networks using SCADA flow and pressure time series. Prioritize research groups, universities, water utility research programs and identified speakers. Search for BattLeDIM/L-Town, EPANET-based leak detection, pressure residuals and flow balance. Return title, channel/institution, date, speaker when available, method discussed, cited paper and video URL. Do not treat a video as sufficient proof of a technical claim.`

**Seleção:** incluir no dossiê no máximo dois vídeos, selecionados por credibilidade e pertinência. Um vídeo pode ser relevante para explicar o contexto, mas os fundamentos técnicos devem ser rastreados para artigos ou documentação primária.

**Entrega esperada:** duas entradas verificáveis com links, resumo do método e questões a comparar com a fundamentação científica. Se não houver vídeo bom, registrar “não encontrado na busca executada”; não inventar títulos nem substituir por canais aleatórios.

## App 4 — Serviços de pesquisa: rastrear a fonte original

Executar a busca por documento científico/documentação citada no dossiê:

- `BattLeDIM dataset 5-minute SCADA flow pressure sensors tank level L-Town official`
- `Aghashahi 2023 Benchmarking dataset leak detection localization water distribution systems Data in Brief DOI`

**Entrega esperada:** confirmar que o benchmark tem série SCADA de cinco minutos com fluxo, pressão, nível e consumo; confirmar que o conjunto de Aghashahi tem medições de bancada com diferentes tipos de sensor e cenários. Guardar os links e não copiar conjuntos de dados de terceiros para o repositório sem necessidade/licença e sem documentar procedência.

## Ordem recomendada dos passos

1. Começar por um chat Argon novo e importar o repositório; executar a auditoria do código.
2. Na mesma conversa, pedir ao Workspace a recuperação da planilha e do diário; guardar uma captura que mostre o resultado real.
3. Acionar YouTube para as consultas estabelecidas e escolher até dois vídeos reais. Verificar os URLs manualmente.
4. Usar Serviços de pesquisa para confrontar as afirmações técnicas com as fontes primárias.
5. Pedir a entrega estruturada com o prompt principal em `03_PROMPT_GEMINI_ARGON.md`.
6. Salvar a resposta de Argon manualmente no repositório; executar os testes locais; anotar quais sugestões foram aceitas, rejeitadas e por quê.
7. Preencher `04_RELATORIO_EXPERIENCIA_TEMPLATE.md` com dados reais da execução.

## Evidências mínimas a capturar

- Tela do seletor com Gemini 4 Argon selecionado (não divulgar dados da conta).
- Processo de importação do repositório e indicação do repositório anexado ao chat.
- Resposta que cite caminhos reais do código.
- Resposta mostrando acesso ou falha de acesso ao Google Workspace.
- Resultados reais da busca do YouTube, incluindo títulos e links.
- Resultado dos testes locais executados no terminal e o relatório final depois de preenchido.
