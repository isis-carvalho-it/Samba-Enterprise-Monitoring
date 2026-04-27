## Samba Enterprise Monitoring 🚀

Projeto de laboratório para monitoramento básico de um ambiente **Samba 4 Active Directory** em Linux.

## 📌 Objetivo

Este projeto tem como objetivo validar a saúde de um ambiente integrado ao Active Directory,
simulando verificações comuns de infraestrutura em servidores Linux.

## 🏗️ Ambiente do Laboratório

- **Domain Controller (DC):** Gerencia autenticação, DNS e objetos do Active Directory
- **Member Server:** Servidor Linux integrado ao domínio, utilizado como File Server
- **Script de Monitoramento:** Automação em Python para validação de serviços críticos

## 🛠️ Tecnologias utilizadas

- Samba 4 (AD DC e Member Server)
- Ubuntu Server
- Python 3
- Git

## 📊 Funcionalidades do script (`monitor_samba.py`)

- [x] Verificação do status do serviço `smbd`
- [x] Teste de vínculo com o domínio (`net ads testjoin`)
- [x] Validação de resolução DNS (registros SRV do AD)
- [ ] Em desenvolvimento: verificação de replicação do diretório (DRS)

## 🚀 Execução

```bash
python3 monitor_samba.py