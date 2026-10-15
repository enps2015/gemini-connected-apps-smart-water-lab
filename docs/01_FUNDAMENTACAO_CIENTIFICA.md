# Fundamentação científica e limites de validade

## 1. Por que pressão, vazão e amostragem de cinco minutos?

O benchmark BattLeDIM documenta uma rede virtual denominada L-Town e séries SCADA de referência. A página oficial descreve dados históricos de 2018 em intervalos de cinco minutos, com leituras de nível de reservatório, sensores de vazão, medições agregadas de consumo (AMR) e sensores de pressão. A página informa três sensores de vazão, 33 sensores de pressão, um sensor de nível e 82 AMRs em uma área da rede. O conjunto inclui ainda relatório de reparos e modelo EPANET para o cenário de benchmark.

**Como isso informa nossa simulação:** a cadência de cinco minutos e a combinação vazão + demanda agregada + pressão + nível são escolhas didáticas coerentes com o tipo de telemetria de um benchmark real. Não copiamos nem reestimamos os valores observados do BattLeDIM.

Fonte primária do benchmark: https://battledim.ucy.ac.cy/?page_id=33  
Referência do artigo do desafio: Vrachimis, S. G. et al. “Battle of the Leakage Detection and Isolation Methods.” *Journal of Water Resources Planning and Management*, 148(12), 04022068 (2022). Página do benchmark e citação: https://battledim.ucy.ac.cy/?page_id=33

## 2. Outro fundamento: dados laboratoriais sobre diferentes tipos de vazamento

Aghashahi et al. (2023) apresentam um conjunto aberto de bancada para detecção/localização de vazamentos. O estudo registra 280 medições, diferentes geometrias de vazamento, condições sem vazamento, topologias de rede e variação de demanda/ruído. Os sinais laboratoriais incluem acelerômetro, hidrofone e sensor dinâmico de pressão; as frequências de aquisição são muito maiores que as do SCADA de cinco minutos.

**Como isso informa nossa simulação:** incluímos cenários diferentes — vazamento sutil, vazamento grande de curta duração, deriva do sensor e evento não vazamento — porque um detector deve ser avaliado frente a diferentes mecanismos e confundidores. Não tentamos simular sinais acústicos de kHz em uma série agregada de cinco minutos; são escalas e modalidades de medição diferentes.

Referência: Aghashahi, M. et al. (2023). “Benchmarking dataset for leak detection and localization in water distribution systems.” *Data in Brief*, 48, 109148. DOI: https://doi.org/10.1016/j.dib.2023.109148  
Texto completo: https://pmc.ncbi.nlm.nih.gov/articles/PMC10147960/

## 3. O que foi modelado e o que não foi

O script usa padrões diários estilizados de demanda, ruído aleatório com semente fixa e relações simplificadas entre demanda e pressão. Os eventos introduzem offsets explícitos de vazão e pressão para testar as regras. Estes coeficientes e magnitudes são decisões didáticas arbitradas pelo autor do protótipo.

Não foi implementado solver hidráulico, calibração EPANET, identificação de parâmetros de uma rede real nem inferência estatística a partir de telemetria real. Portanto:

- o dataset é **informado por pesquisa**, mas não é um dataset científico empírico;
- as medições são totalmente sintéticas;
- as amplitudes e os limites do detector são hipóteses de ensino;
- a performance sintética não estima a performance operacional;
- não se deve aplicar o limiar em uma concessionária real sem desenho de dados, engenharia, calibração e validação de campo.

## 4. Por que os rótulos ficam separados da telemetria?

`telemetry_synthetic_5min.csv` não inclui `event_type`, `ground_truth_leak` ou `sensor_fault_flag`. Os rótulos estão em `ground_truth_events.csv` somente para avaliação offline. O detector deve usar sinais de entrada, nunca os rótulos de referência. `outputs/baseline_predictions.csv` pode conter um rótulo incorporado para calcular métricas localmente; esse arquivo é uma saída de avaliação e não uma entrada do detector.

## 5. Fontes oficiais sobre as Apps Conectados / Argon

- Gemini 4 Argon no Gemini app (Google, 13/10/2026): https://blog.google/innovation-and-ai/products/gemini-app/gemini-4-argon-availability/
- Gemini 4 Argon para desenvolvedores (Google, 13/10/2026): https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-4-argon/
- Importar um repositório GitHub e perguntar sobre código no Gemini Web: https://support.google.com/gemini/answer/16176929?hl=pt-BR
- Conectar o Google Workspace ao Gemini: https://support.google.com/gemini/answer/15229592?hl=pt-BR
- Criar um repositório GitHub: https://docs.github.com/pt/repositories/creating-and-managing-repositories/creating-a-new-repository
