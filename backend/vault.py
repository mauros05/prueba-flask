import hvac
from config import VAULT_URL, VAULT_TOKEN


client = hvac.Client(url=VAULT_URL, token=VAULT_TOKEN)

def store_secrets_in_vault(path: str, data: dict):
    try:
        client.secrets.kv.v2.create_or_update_secrets(path=path, secret=data)
        print(f"Los datos se almacenaron correctamente en el path {path}")
    except Exception as e:
        print(f"Error al almacenar los secretos en Vault {e}")


def get_secrets_from_vault(path:str) -> dict:
    try:
        secret = client.secrets.kv.v2.read_secret_version(path=path)
        return secret['data']['data']
    except Exception as e:
        print (f"Error al recuperar los secrets de Vault {e}")
        return {}