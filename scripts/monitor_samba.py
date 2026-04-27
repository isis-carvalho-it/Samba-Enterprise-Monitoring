#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Projeto: Samba Enterprise Monitoring
Autora: Isis Carvalho
Descrição: Script de verificação de saúde de ambiente Samba 4
"""

import subprocess
import os

def run_command(command):
    """Executa um comando no terminal e retorna o resultado."""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout.strip(), result.returncode
    except Exception as e:
        return str(e), 1

def check_infra():
    print("--- [ Iniciando Monitoramento Samba Enterprise ] ---")

    # 1. Verificando o serviço Samba
    status, code = run_command("systemctl is-active smbd")
    if status == "active":
        print("✅ [OK] Serviço SMBD (File Server) está ativo.")
    else:
        print(f"❌ [ERRO] Serviço SMBD está {status}!")

    # 2. Verificando a conexão com o Domain Controller
    join_status, join_code = run_command("net ads testjoin")
    if join_code == 0:
        print("✅ [OK] Vínculo com o Domain Controller está saudável.")
    else:
        print("❌ [ERRO] Falha na confiança com o Domínio AD!")

    # 3. Verificando Resolução de DNS (SRV Records do AD)
    dns_status, dns_code = run_command("host -t SRV _ldap._tcp.isistech.corp")
    if dns_code == 0:
        print("✅ [OK] DNS do Active Directory resolvendo corretamente.")
    else:
        print("❌ [ERRO] Problema de DNS: Não foi possível localizar o AD.")

if __name__ == "__main__":
    check_infra()
