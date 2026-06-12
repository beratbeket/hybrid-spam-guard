# ⚡ Hybrid LLM Spam Detector 🌐

<div align="center">

  <img src="https://img.shields.io/badge/Architecture-Hybrid%20%7C%20ML%20%2B%20LLM-blueviolet?style=for-the-badge&logo=diagrams.net" alt="Architecture">
  <img src="https://img.shields.io/badge/Gemini%202.5%20Flash-Integration-blue?style=for-the-badge&logo=google-gemini&logoColor=white" alt="Gemini">
  <img src="https://img.shields.io/badge/UI%20Dashboard-Gradio-orange?style=for-the-badge&logo=gradio" alt="Gradio">
  <img src="https://img.shields.io/badge/Accuracy-%2598.2-success?style=for-the-badge" alt="Accuracy">

  <br>

  ### 🚀 "Maliyet Odaklı Yapay Zeka ve Akıllı Sınıflandırma Mimarisi"

  *Geleneksel Makine Öğrenmesinin hızı ile Büyük Dil Modellerinin (LLM) derin anlama yeteneği tek bir potada eritildi.*

</div>

---

## 🌌 Proje Vizyonu & Akıllı Optimizasyon

Canlı test ortamlarında her mesaja doğrudan LLM çağırmak **yüksek API maliyetlerine** ve **gecikme sürelerine** yol açacağından bu proje **Hibrit bir Doğrulama Mimarisi (LLM Verifier)** kullanır. Sistem, kararları ışık hızında ve sıfır maliyetle filtrelerken, sadece ihtiyaç duyduğu o dar "gri alanda" akıllıca yapay zekaya danışır.

Bu proje, bu problemi çözmek için 

---

## 📊 Hibrit Karar Akış Mimarisi

### 1. Akıllı Gri Alan Kontrolü (%43 - %62 Kararsızlık Bandı)
* Modelin spam olasılığını `%43` ile `%62` arasında bulduğu anların, modelin en çok kararsız kaldığı ve "gri alan" olarak adlandırılan bölge olduğu tespit edilmiştir.
* Sistem bu dar bantta inisiyatifi eline alır ve kararı güçlendirmek için **Gemini 2.5 Flash** modeline devreder. 

### 2. Maliyet ve Latency Yönetimi
Her gelen mesaja doğrudan LLM çağrısı yapmak finansal açıdan sürdürülemez bir yaklaşımdır. Kurulan bu hibrit yapı sayesinde:
* Gelen mesajların yaklaşık **%80-85'lik net kısmı**, lokalde sıfır maliyetle ve milisaniyeler içinde elenir.
* Sadece gerçekten şüpheli ve karmaşık olan **%15-20'lik gri alan** için bulut tabanlı bir LLM doğrulaması tetiklenir.

**Sonuç:** Sistem genelinde **%80'e varan API maliyet tasarrufu** ve minimum gecikme süresiyle, maksimum (%98+) doğruluk payına ulaşan, endüstri standartlarında akıllı bir pipeline geliştirilmiştir.
