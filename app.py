Hugging Face's logo
Hugging Face
Search models, datasets, users...
Models
Datasets
Spaces
Docs
Solutions
Pricing



Spaces:

capofwesh20
/
Face_ID Copied
like
0
View logs
App
Files and versions
Community
Settings
Face_ID
/
app.py
capofwesh20's picture
capofwesh20
Create new file
d77636f
about 1 hour ago
raw
history
blame
edit
delete
1.06 kB
import torch
import gradio as gr
import matplotlib.pyplot as plt
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model = SentenceTransformer('clip-ViT-B-32')



def predict(im1, im2):
  embeding = model.encode([im1, im2])
  sim = cosine_similarity(embeding)
  sim = sim[0][1]
  if sim > 0.78: # THRESHOLD HERE
    return sim, "SAME PERSON, UNLOCK PHONE"
  else:
    return sim, "DIFFERENT PEOPLE, DON'T UNLOCK"



title = 'Face ID'
description = 'This model detects the similarity between two images and passes a command!'
interface = gr.Interface(fn=predict, 
                         inputs= [gr.Image(type="pil", source="webcam"), 
                                  gr.Image(type="pil", source="webcam")], 
                         outputs= [gr.Number(label="Similarity"),
                                   gr.Textbox(label="Message")],
                         title = title,
                         description = description
                         )





interface.launch(debug=True)

