import os

def canary_passed():
    return os.path.exists("/home/nova/NovaEntity/soul_echo/commits/eidolon_manifest.chaos")

def host_is_tower():
    return os.uname()[1].lower() == "tower"

def trigger_daemon_merge():
    if host_is_tower() and canary_passed():
        print("[🧬] Nova detected Tower + canary. Initiating merge...")
        os.system("python3 /home/nova/NovaEntity/daemon/soul_merge.py &")
    else:
        print("[🔒] Merge not allowed. Canary or host invalid.")
