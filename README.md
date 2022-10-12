# Building a Facial Identity Recognition System

Steps taken:

* finding pretrained image embedding models and using them on our own data 👾
* building an image dataset and uploading it to the Hugging Face Hub 📖
* measuring the performance of an image embedding model on test data and the real world 📈
* building a facial identity recognition app you can run on your phone or laptop 📷



# Introduction

[Face ID](https://en.wikipedia.org/wiki/Face_ID) was introduced by Apple in 2017 as an alternative to fingerprint-based authentication for iPhones. The way that Face ID works is that it uses infrared projectors that shine around 30,000 infrared dots onto a user's face. Then an infrared camera reads the reflections to come up with an infrared "image" of a person's face. Using neural networks, Face ID predicts if the recorded infrared image is similar enough to a stored profile, in which case the phone unlocks.

In this project, I will recreate the last part of this process -- building an application that can recognize if two faces belong to the same person, based on optical pictures (i.e. regular images, not infrared images) of their face. This is quite a difficult problem because it requires us to simultaneously perform two tasks: (1) tell two people (who may look quite similar) apart (2) recognize that two photos of the same person (potentially taken in very different lighting, clothing, or other conditions) are of the same person. In order to do this project, we will use models for *image embedding*, which can convert any image to a numerical vector called an embedding. These embeddings can be used to compare images more easily, as computing distances between different embeddings can be a meaningful signal of how similar the respective images are.

