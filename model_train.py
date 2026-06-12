import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
import joblib

df = pd.read_csv(
    'https://raw.githubusercontent.com/mohitgupta-omg/Kaggle-SMS-Spam-Collection-Dataset-/master/spam.csv',
    encoding='latin-1'
)[['v1','v2']]
df.columns = ['etiket', 'mesaj']

print(df['etiket'].value_counts())

x = df['mesaj']
y = df['etiket']   

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42)

vectorizer = CountVectorizer(stop_words='english')
x_train_vectorized = vectorizer.fit_transform(x_train)
x_test_vectorized  = vectorizer.transform(x_test)

model = MultinomialNB()
model.fit(x_train_vectorized, y_train)

tahmin = model.predict(x_test_vectorized)
print(classification_report(y_test, tahmin))
accuracy_orani = accuracy_score(y_test,tahmin)
print(f"Modelin doğruluk oranı: %{(accuracy_orani*100):.2f}")

joblib.dump(model,      'joblibs/spam_model.joblib')
joblib.dump(vectorizer, 'joblibs/vectorizer.joblib')
print("Kaydedildi.")