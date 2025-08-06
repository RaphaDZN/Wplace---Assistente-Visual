<div align="center">
  <img src="https://raw.githubusercontent.com/MicaelliMedeiros/micaellimedeiros/master/image/computer-illustration.png" width="400">
  <h1>🎨 Assistente Visual Wplace 🎨</h1>
  <p><strong>Transforme qualquer imagem em uma obra de arte pixelada, passo a passo.</strong></p>

  <p>
    <a href="https://wplace-assistente-visual.onrender.com/">
      <img src="https://img.shields.io/badge/Acessar_Aplicação-Online-brightgreen?style=for-the-badge&logo=rocket" alt="Acessar Aplicação">
    </a>
    <a href="https://github.com/RaphaDZN/Wplace---Assistente-Visual/blob/main/LICENSE">
      <img src="https://img.shields.io/badge/Licença-MIT-blue?style=for-the-badge" alt="Licença MIT">
    </a>
  </p>
</div>

---

## 🚀 O Projeto

O **Assistente Visual Wplace** é uma aplicação web criada para resolver um grande desafio para os artistas da plataforma Wplace e similares: a dificuldade de traduzir imagens complexas para uma tela de pixels com cores limitadas.

A ideia inicial de criar um "bot" foi descartada ao constatar que as regras da comunidade não permitiam automação. Essa restrição foi o catalisador para uma solução muito mais criativa e útil: uma ferramenta que atua como um **copiloto para o artista**, não um piloto automático.

Esta aplicação processa sua imagem, otimiza as cores e gera um guia interativo com um minimapa visual, mostrando exatamente onde pintar cada pixel.

## ✨ Funcionalidades

* **Conversão Inteligente:** Envie sua imagem e a aplicação converte as cores para a paleta oficial do Wplace de forma otimizada.
* **Grades Flexíveis:** De `8x8` a `128x128`, incluindo formatos retangulares, para total liberdade criativa.
* **Minimapa Interativo:** Uma interface visual clara que mostra o progresso e destaca o próximo pixel a ser pintado.
* **Navegação Rápida:** Um buscador de passos permite pular para qualquer ponto do seu projeto, ideal para desenhos grandes e pausas longas.
* **Otimização de Fundo:** Opção para ignorar ou incluir pixels brancos, tratando-os como fundo ou como cor.
* **100% Web:** Acesse de qualquer dispositivo com um navegador, em qualquer lugar.

## 🎬 Demonstração em Ação

Confira abaixo uma demonstração da ferramenta em uso:

<p align="center">
  <em>(GIF 1: Processamento da imagem)</em><br>
  <img src="https://i.ibb.co/8gpbZk4h/2025-08-06-11-04-55.gif" alt="Demonstração do Assistente Visual Wplace - Processamento">
</p>

<br>

<p align="center">
  <em>(GIF 2: Desenho lado a lado - Usando o mesmo GIF de 1MB para teste)</em><br>
  <img src="https://i.ibb.co/8gpbZk4h/2025-08-06-11-04-55.gif" alt="Teste com o GIF mais leve">
</p>

## 🛠️ Tech Stack

| Ferramenta | Propósito |
| :--- | :--- |
| **Python** | Linguagem principal do backend |
| **Flask** | Micro-framework para criar o servidor web e as rotas |
| **Pillow (PIL)** | Manipulação e desenho das imagens em tempo real |
| **NumPy/SciPy** | Otimização matemática para a busca ultrarrápida de cores |
| **Gunicorn** | Servidor de produção para garantir estabilidade online |
| **HTML/CSS/JS**| Estrutura, estilo e interatividade do frontend |

## 💻 Rodando Localmente

```bash
# 1. Clone o repositório
git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
cd seu-repositorio

# 2. Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Execute a aplicação
python app.py
```

---
<p align="center">
  Criado por pura diversão e amor à programação e à comunidade.
</p>
