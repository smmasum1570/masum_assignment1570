from wordcloud import WordCloud, STOPWORDS
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

stopwords = set(STOPWORDS)

mask = np.array(Image.open('masum1.png'))

data_file = pd.read_csv('text.csv')

wordcloud = WordCloud(
    stopwords=stopwords,
    width=1600,
    height=1200,
    mask=mask,
    #scale=2,
    background_color="black",
    colormap="Set3"
).generate(''.join(data_file['text']))

background_image = Image.open('fd.jpg')
background_array = np.array(background_image)

plt.figure(figsize=(10, 10))
plt.imshow(background_array, interpolation='bilinear')
plt.imshow(wordcloud, interpolation='bilinear', alpha=0.7)
plt.axis('off')
#image.save("w.png")
plt.show()
