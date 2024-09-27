import os
import json


APPDATA = os.getenv("APPDATA")
MINECRAFT = APPDATA + "//.minecraft"


def get_client_id() -> str:
    with open(MINECRAFT + "//clientId.txt", "r") as f:
        return f.read()


def get_command_history():
    with open(MINECRAFT + "//command_history.txt", "r") as f:
        commands = f.readlines()
    return commands


def a():
    with open(MINECRAFT + "//launcher_accounts_microsoft_store.json", "r") as f:
        data = json.loads(f.read())
    return data


def b():
    with open(MINECRAFT + "//launcher_entitlements_microsoft_store.json", "r") as f:
        data = json.loads(f.read())
    return data



def c():   # unneccesary
    with open(MINECRAFT + "//launcher_gamer_pics_microsoft_store.json", "r") as f:
        data = json.loads(f.read())
    return data


def get_launcher_log():
    with open(MINECRAFT + "//launcher_logs.txt", "r") as f:
        return f.readlines()


def d():
    with open(MINECRAFT + "//launcher_product_state_microsoft_store.json", "r") as f:
        return json.loads(f.read())

def get_launcher_profiles():
    """
    Installationen (1.20.x, ...)
    """
    with open(MINECRAFT + "//launcher_profiles.json", "r") as f:
        return json.loads(f.read())

def get_quick_play():
    """
    Last Quick Play
    """
    with open(MINECRAFT + "//launcher_quick_play.json", "r") as f:
        return json.loads(f.read())


def get_launcher_settings():
    with open(MINECRAFT + "//launcher_settings.json", "r") as f:
        return json.loads(f.read())


def get_options():
    with open(MINECRAFT + "//options.txt", "r") as f:
        return json.loads(f.read())


def get_realm_persistence():
    with open(MINECRAFT + "//realms_persistence.json", "r") as f:
        return json.loads(f.read())




