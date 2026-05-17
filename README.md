## Samba Enterprise Monitoring 🚀

Projeto de laboratório para monitoramento básico de um ambiente **Samba 4 Active Directory** em Linux.

## 📌 Objetivo

Este projeto tem como objetivo validar a saúde de um ambiente integrado ao Active Directory,
simulando verificações comuns de infraestrutura em servidores Linux.

## 🏗️ Ambiente do Laboratório

- **Domain Controller (DC):** Gerencia autenticação, DNS e objetos do Active Directory
- **Member Server:** Servidor Linux integrado ao domínio, utilizado como File Server
- **Script de Monitoramento:** Automação em Python desenvolvida para monitorar
o uso de CPU e RAM, além de validar o status de serviços críticos

## 🛠️ Tecnologias utilizadas

- Samba 4 (AD DC e Member Server)
- Ubuntu Server
- Python 3
- Git

## 📊 Funcionalidades do script (`monitor_samba.py`)

- [x] Verificação do status do serviço `samba-ad-dc`
- [x] Teste de vínculo com o domínio (`net ads testjoin`)
- [x] Validação de resolução DNS (registros SRV do AD)
- [x] Verificação de replicação do diretório (DRS)
- [x] Monitoramento de uso de CPU e memória RAM

---

## 🛠️ Pré-requisitos e Dependências

Antes de executar o script, é necessário instalar a biblioteca `psutil`, responsável pela coleta das métricas de hardware.

```bash
# Atualize os índices de pacotes do sistema
sudo apt update

# Instale a biblioteca psutil
sudo apt install python3-psutil -y
```

## 🚀 Execução

Como o script faz checagens de serviços do sistema e lê dados confidenciais do Samba Active Directory,
ele deve ser executado com privilégios de administrador:

```bash
sudo python3 monitor_samba.py
```