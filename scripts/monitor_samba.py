#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Projeto: Samba Enterprise Monitoring
Autora: Isis Carvalho
Descrição: Script de verificação de saúde de ambiente Samba 4
"""

import subprocess
import os
import time
import psutil
from datetime import datetime

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return "OK" if result.returncode == 0 else "FALHA"
    except:
        return "ERRO"

def check_replication():
    # Roda o showrepl para verificar a replicacao do domain controller
    try:
        result = subprocess.run("sudo samba-tool drs showrepl", shell=True, capture_output=True, text=True)
        if "failed" in result.stdout.lower() or result.returncode != 0:
            return "FALHA"
        return "OK"
    except:
        return "ERRO"

def monitorar():
    while True:
        os.system('clear')
        # Coleta de Hardware
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent
        
        print(f"--- [ Samba Enterprise Monitoring ] --- {datetime.now().strftime('%H:%M:%S')}")
        print(f"💻 HARDWARE: CPU: {cpu}% | RAM: {ram}%")
        print("-" * 45)

        # Verificacoes de Infra
        status_ad_dc = run_command("systemctl is-active samba-ad-dc")
        status_join = run_command("net ads testjoin")
        status_dns  = run_command("host -t SRV _ldap._tcp.isistech.corp")
        status_drs  = check_replication()

        print(f"✅ [DC]  AD Service:   {status_ad_dc}")
        print(f"🤝 [AD]  Trust Join:   {status_join}")
        print(f"🌐 [DNS] SRV Record:   {status_dns}")
        print(f"🔄 [DRS] Replication:  {status_drs}")
        
        print("-" * 45)
        print("Pressione Ctrl+C para encerrar.")
        time.sleep(5)

if __name__ == "__main__":
    try:
        monitorar()
    except KeyboardInterrupt:
        print("\nMonitoramento finalizado.")