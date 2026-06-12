import os
from google import genai
API_KEY = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)
def dil_kontrol(mesaj):

  
    print("✅ Yapay zekaya bağlanıldı ✅")
    prompt = f"Analyze the text below to determine if it's in english and answer only with yes or no \n\n {mesaj}"
    response = client.models.generate_content(model='gemini-2.5-flash',contents=prompt,)

    return response.text.strip().lower()

def spam_kontrol(mesaj):
    print("✅ Yapay zekaya bağlanıldı ✅")
    prompt = f"Analyze the text below to determine if its spam or not and answer only with yes or no \n\n {mesaj}"
    response = client.models.generate_content(model='gemini-2.5-flash',contents=prompt,)
    return response.text.strip().lower() 