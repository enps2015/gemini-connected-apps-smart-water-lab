# Dados do projeto

- `telemetry_synthetic_5min.csv`: entrada do detector; 4.032 leituras em intervalos de cinco minutos, com 14 dias de dados simulados.
- `ground_truth_events.csv`: registro separado para avaliação offline; seis eventos, três rotulados como vazamento e três como não vazamento.
- `data_dictionary.csv`: descrição das variáveis.

Todos os dados de medição são gerados pelo script `../src/generate_synthetic_data.py`, com semente determinística `20261015`. Os arquivos não contêm medições reais de uma concessionária. Não os descreva como dados de campo, dados de cliente ou cópias do BattLeDIM.

A literatura real inspira o tipo geral de variável (vazão, pressão, nível e consumo agregado) e a cadência de cinco minutos, mas os coeficientes, amplitudes, ruído e horários dos eventos foram escolhidos para este experimento. Não existe calibração hidráulica nem identidade entre os valores sintéticos e os valores do benchmark citado.
