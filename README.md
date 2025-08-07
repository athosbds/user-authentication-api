# 🔐 Flask Auth System

Sistema de autenticação completo com Flask, 
utilizando SQLite 
e Flask-Bcrypt para registro, login, 
dashboard protegido e logout de usuários.

## 🚀 Funcionalidades

- Registro de usuários com nome, email e senha
- Senha criptografada com Flask-Bcrypt
- Login com verificação segura de senha
- Sessões de usuário com Flask (`session`)
- Dashboard acessível apenas para usuários autenticados
- Logout que limpa a sessão
- Mensagens de erro personalizadas

---

![Imagem Ilustrativa](assets/register_view.gif)
![Imagem Ilustrativa](assets/logout.gif)

---

## Conceitos Aplicados

- `Flask`: Framework web minimalista
- `Flask-Bcrypt`: Hash seguro de senha
- `SQLite3`: Banco de dados leve e local
- `Jinja2`: Template engine do Flask
- `Session`: Gerenciamento de login do usuário

---
## Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/user-authentication-api.git
cd user-authentication-api



