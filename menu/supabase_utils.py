#---------------------------------permet l'importation des image depuis supabase------------

import os
from supabase import create_client

# Charger la connexion Supabase depuis .env
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
SUPABASE_BUCKET = os.getenv("SUPABASE_BUCKET")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def upload_image_to_supabase(file):
    """
    Upload un fichier sur Supabase Storage et retourne l'URL publique.
    """
    path = f"{file.name}"

    response = supabase.storage.from_(SUPABASE_BUCKET).upload(path, file)

    if response.get("error"):
        raise Exception(response["error"]["message"])

    # URL publique (si bucket public)
    url = f"{SUPABASE_URL}/storage/v1/object/public/{SUPABASE_BUCKET}/{path}"
    return url
