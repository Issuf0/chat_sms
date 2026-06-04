# SMS Chat Engine

Este projeto é um motor de processamento de SMS que filtra mensagens recebidas e gera respostas automáticas baseadas em comandos específicos. Ele utiliza um backend em **FastAPI** para a lógica de processamento e um frontend em **React Native** para simulação e interface.

## 🚀 Como Funciona

O sistema monitora mensagens de entrada e aplica as seguintes regras:

1.  **Filtro de Prefixo:** Somente mensagens que começam exatamente com `Chat:` são processadas.
2.  **Ação de Resposta:** Se a mensagem for válida, o sistema extrai o conteúdo após o prefixo e gera uma resposta curta, clara e em português.
3.  **Ação de Ignorar:** Se a mensagem não contiver o prefixo, ela é ignorada silenciosamente.

### Formato de Saída (JSON)

O motor sempre retorna um JSON válido:

- **Mensagem Válida:**
  ```json
  {"action":"reply","reply":"A capital de Moçambique é Maputo."}
  ```
- **Mensagem Ignorada:**
  ```json
  {"action":"ignore","reply":""}
  ```

## 🛠️ Tecnologias

- **Backend:** Python com [FastAPI](https://fastapi.tiangolo.com/)
- **Mobile:** [React Native](https://reactnative.dev/) (TypeScript)
- **Comunicação:** REST API (JSON)

## 📦 Estrutura do Projeto

```text
chat_sms/
├── backend/            # Servidor FastAPI
│   ├── main.py        # Lógica central e Endpoints
│   └── requirements.txt
├── mobile/             # Aplicativo React Native
│   └── App.tsx        # Interface de simulação
└── README.md
```

## 🚦 Como Iniciar

### 1. Backend

Certifique-se de ter o Python 3 instalado.

```bash
# Entre na pasta do backend
cd backend

# Crie e ative um ambiente virtual
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Inicie o servidor
python main.py
```
O servidor estará rodando em `http://localhost:8000`.

### 2. Mobile

Certifique-se de ter o ambiente React Native configurado.

```bash
# Entre na pasta mobile
cd mobile

# Instale as dependências
npm install

# Inicie o aplicativo (Android)
npx react-native run:android --device 

# Ou (iOS)
npx react-native run-ios
```

> **Nota:** Se estiver testando em um dispositivo físico, altere a URL do `fetch` no arquivo `App.tsx` para o endereço IP da sua máquina local.

## 📝 Exemplos de Uso

| Entrada | Saída (Ação) |
| :--- | :--- |
| `Chat: Qual é a capital de Moçambique?` | `reply` (Maputo) |
| `Chat: Quanto é 18 + 7?` | `reply` (25) |
| `Olá, tudo bem?` | `ignore` |
| `Alô, Chat: teste` | `ignore` (Não começa com o prefixo) |

---
Desenvolvido como um protótipo funcional para processamento inteligente de SMS.
