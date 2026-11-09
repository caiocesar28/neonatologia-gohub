# Alta da Neonatologia — HUB-UnB / EBSERH

Gerador ágil de papéis de alta e encaminhamentos da **Unidade Neonatal e Alojamento Conjunto do Hospital Universitário de Brasília (HUB-UnB/EBSERH)**.

Projeto inspirado e adaptado a partir do gerador de obstetrícia (`enfermaria.gohub`), integrando os modelos e padrões de impressos oficiais do HUB presentes no projeto [`papelada-HUB`](https://github.com/caiocesar28/papelada-HUB).

---

## 🎯 O que foi adaptado e implementado

### 1. Receita de Vitamina D
- **Item padrão:** Vitamina D (Colecalciferol) 200 UI/gota.
- **Posologia pré-configurada:** Pingar 2 gotas por via oral, 1 vez ao dia (400 UI/dia).
- **Formulário:** Receituário oficial do HUB (dois por folha A4 com linha de corte).
- Suporte adicional para **Sulfato Ferroso profilático** e **Receituário em branco** personalizável.

### 2. Solicitação de Exames
- **Exames com seleção rápida de um clique:**
  - `Bilirrubinas totais e frações` (para avaliação e controle de icterícia pós-alta)
  - `Ultrassonografia de quadril` (rastreamento de displasia do desenvolvimento do quadril - DDQ)
  - `Ultrassonografia transfontanela (USTF)` (avaliação neurológica de rotina em prematuros e sob risco)
- **Dois modelos integrados:**
  - **Requisição de Exames (HUB):** Modelo oficial de imagem e exames gerais (equivalente ao `exames-hub.pdf` do *papelada-HUB*).
  - **Laboratório de Patologia Clínica (CPA/HUB):** Formulário quadriculado oficial da patologia clínica com marcação de caixas (bioquímica, hematologia, etc.).

### 3. Retornos e Encaminhamentos
- **Retorno no Ambulatório de Crescimento e Desenvolvimento (C&D) do HUB:**
  - Guia de encaminhamento e Cartão de Consulta ambulatorial (duas vias com canhoto).
- **Retorno em 48 horas na Pediatria do HUB:**
  - Data calculada automaticamente (+2 dias a partir da data de alta).
  - Indicação clínica de reavaliação de icterícia neonatal, perda/ganho ponderal e padrão de amamentação.
- **Contrarreferência para UBS (Baixo Risco):**
  - Encaminhamento com orientações para a primeira consulta de puericultura na Atenção Primária.

### 4. Pedido de Parecer da Cirurgia Geral
- **Modelo oficial do HUB (folha inteira):** Equivalente ao `parecer-hub.pdf` do *papelada-HUB*.
- Preenchimento de:
  - DA CLÍNICA: `Neonatologia`
  - A CLÍNICA: `Cirurgia Geral` (com facilidade para alternar para `Cirurgia Pediátrica`)
  - Leito, prontuário, identificação do RN
  - Motivo da consulta editável (até 5 linhas)
  - Espaço com pauta oficial para resposta do médico consultante.

### 5. Orientações ao Recém-Nascido e Cuidados
- **Orientações gerais:** Pega da amamentação, higiene do coto umbilical com álcool 70%, banho de sol, sono seguro (barriga para cima).
- **Sinais de Alarme (Voltar ao PS):** Febre, hipotermia, gemência, cianose, icterícia zona 4-5 de Kramer, recusa de mamadas, vômitos em jato, secreção purulenta no umbigo.
- **Triagens e Vacinas:** Teste do Pezinho, Olhinho, Orelhinha, Coraçãozinho, Linguinha e vacinas BCG e Hepatite B.
- **Bancos de Leite Humano do DF:** Contatos e postos de coleta.

---

## 🚀 Como executar
Como o projeto é uma Single Page Application estática e autossuficiente (HTML + CSS + JS puro com logomarcas vetorizadas/base64 embutidas):

Basta abrir o arquivo [`index.html`](index.html) em qualquer navegador moderno (Chrome, Edge, Firefox, Safari). Não requer instalação de dependências ou servidor web para rodar.
