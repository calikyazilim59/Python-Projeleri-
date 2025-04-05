import openai
import speech_recognition as sr

# OpenAI API anahtarınızı burada belirtin
openai.api_key = "YOUR_API_KEY"

# Sesli yanıtları almak için ses kaydı yapan fonksiyon
def get_audio_input():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Lütfen bir şeyler söyleyin...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Söylediklerinizi tanıyorum...")
        text = recognizer.recognize_google(audio)
        print(f"Söylediğiniz: {text}")
        return text
    except sr.UnknownValueError:
        print("Ne söylediğinizi anlayamadım.")
        return None
    except sr.RequestError:
        print("Google Speech API servisi ile bağlantı hatası.")
        return None

# ChatGPT API'yi çağırarak yanıt almak
def get_chatgpt_response(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Ya da kullandığınız modelin adı
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input},
        ]
    )
    return response['choices'][0]['message']['content']

# Ana program
def main():
    while True:
        user_input = get_audio_input()
        if user_input:
            response = get_chatgpt_response(user_input)
            print(f"ChatGPT Yanıtı: {response}")
        else:
            print("Lütfen yeniden deneyin.")
            continue

if __name__ == "__main__":
    main()
