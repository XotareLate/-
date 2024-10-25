import speech_recognition as sr
from pydub import AudioSegment

def convert_audio_to_wav(audio_path):
    audio = AudioSegment.from_file(audio_path)
    wav_path = 'converted_audio.wav'
    audio.export(wav_path, format='wav')
    return wav_path

def transcribe_audio(audio_path):
    # Конвертируем аудио в формат .wav, если необходимо
    wav_path = convert_audio_to_wav(audio_path)
    
    # Создаем распознаватель
    recognizer = sr.Recognizer()

wav_path = convert_audio_to_wav(audio_path)

recognizer = sr.Recognizer()

with sr.AudioFile(wav_path) as source:
    print("Listening...")
    audio_data = recognizer.record(source)
    print("Transforming...")

    try:
        text = recognizer.recognize_google(audio_data, language='ru-RU')
        print("Transforming text:", text)
    except sr.UnknownValueError:
            print("Couldn't transform")
    except sr.RequestError as e:
            print(f"Error Google Web Speech API: {e}")
            
    audio_file_path = "путь до вашего файла mp3"
    transcribe_audio(audio_file_path)