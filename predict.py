import gradio as gr
import joblib
from llm_verifier import dil_kontrol,spam_kontrol

model = joblib.load('joblibs/spam_model.joblib')
vectorizer = joblib.load('joblibs/vectorizer.joblib')

def predict_spam(mesaj):
    response = dil_kontrol(mesaj)
    if response == "yes":
        vectorized = vectorizer.transform([mesaj])
        tahmin = model.predict(vectorized)[0]
        olasilik = model.predict_proba(vectorized)[0]
        spam_oran = int(olasilik[list(model.classes_).index('spam')]*100)
        ham_oran = int(olasilik[list(model.classes_).index('ham')]*100)
        sonuc = f"Prediction: {tahmin}\n"
        sonuc += f"Spam Probability: %{spam_oran}\n"
        sonuc += f"Ham (Normal) Probability: %{ham_oran}\n"
        if 43 < spam_oran < 62:
            response = spam_kontrol(mesaj)
           
            sonuc += f"LLM Cevabı: {response}"
    
    else:
        sonuc = "Language of the message must be English"    
    
    return sonuc

demo = gr.Interface(
    fn=predict_spam,
    inputs=gr.Textbox(lines=3, placeholder="Type Your Message Here ()", label="Message"),
    outputs=gr.Textbox(label="Result"),
    title="Spam Message Detection",
    description="Guesses whether a message is spam."
)

demo.launch()