# Develeped by Jaspreet Singh
# Dated on 19-09-20

import pdfplumber  # pdfplumber lib used for fetching text from PDF
# importing lib
from gtts import gTTS  # gtts lib used for converting text into mp3

raw_str = ""  # Global string required for fetching text from PDF

u_path = input("Enter the path and filename")  # Inputing PDF Location

# Opening pdf and reading text
with pdfplumber.open(u_path) as pdf:
    total_pages = pdf.pages  # getting total pages in pdf

    # iterating over all pages in pdf to read text
    for itr in range(len(total_pages)):
        first_page = pdf.pages[itr]

        # Applying exception due to some content (Images)
        # creating Object in extract_text function,
        # which is not required
        try:
            raw_str = raw_str + "" + first_page.extract_text()
        except Exception as e:
            print(e)

# Printing text which will going to converted into audio
print(f"Text we fetch from {u_path} ->" + raw_str)

# init gTTs
gtts_obj = gTTS(text=raw_str, lang="en")
# inputing audio filename
filename = input("Input filename for your audio")

# Saving audio file
while True:
    try:
        gtts_obj.save(filename + ".mp3")
        break
    except Exception as e:
        print(e)
print("Done")
