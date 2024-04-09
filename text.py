# import whisper
# import ssl

# ssl._create_default_https_context = ssl._create_unverified_context

# model = whisper.load_model("small")

# # load audio and pad/trim it to fit 30 seconds
# audio = whisper.load_audio("files/test.mp3")
# # audio = whisper.pad_or_trim(audio)

# result = model.transcribe("/content/file.mp3", language="Turkish")

# # make log-Mel spectrogram and move to the same device as the model
# mel = whisper.log_mel_spectrogram(audio).to(model.device)

# # detect the spoken language
# _, probs = model.detect_language(mel)
# print(f"Detected language: {max(probs, key=probs.get)}")

# # decode the audio
# options = whisper.DecodingOptions()
# result = whisper.decode(model, mel, options)

# # print the recognized text
# print(result.text)



import whisper
import os
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# input audio file name
audio_file = "/content/file.mp3"

# load the model and transcribe the audio
model = whisper.load_model("large-v2")
result = model.transcribe('files/test.mp3')

print(result)

# # extract the text and language information
# text = result["text"]
# language = result["language"]

# # create the output text file name based on the input mp3 file name
# text_file = os.path.splitext(audio_file)[0] + ".txt"

# # write the text and language information to the output text file
# with open(text_file, "w") as f:
#     f.write(f"Text:\n\n{text}\n\nLanguage: {language}")

# # print the text and language information to the console
# print("Text:\n\n", text)
# print("Language: ", language)

