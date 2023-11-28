# ParaDiffusion
### <div align="center"> Paragraph-to-Image Generation with Information-Enriched Diffusion Model <div> 

<div align="center">
  <a href="aaa"><img src="https://img.shields.io/static/v1?label=Project%20Page&message=Github&color=blue&logo=github-pages"></a> &ensp;
  <a href="aa"><img src="https://img.shields.io/static/v1?label=Paper&message=Arxiv&color=red&logo=arxiv"></a> &ensp;
</div>

## :notes: **Updates**

- [ ] Nov. 15, 2023. Release the inference code in **three months**.
- [x] Nov. 15, 2023. Rep initialization.


---

## 🐱 Abstract
<font color="red">ParaDiffusion</font> an information-enriched diffusion model for paragraph-to-image generation task, which delves into the transference of the extensive semantic comprehension capabilities of large language models to the task of image generation. At its core is using a large language model (e.g., Llama V2) to encode long-form text, followed by fine-tuning with LORA to align the text-image feature spaces in the generation task. A high-quality paragraph-image pair dataset, namely ParaImage is proposed to facilitate the training of long-text semantic alignment.

---

![image.](asset/images/WX20231124-120031@2x.png)

---
![image.](asset/images/WX20231124-120233@2x.png)


## 🔧 Dependencies and Installation

- Python >= 3.10 (Recommend to use [Anaconda](https://www.anaconda.com/download/#linux) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html))
- [PyTorch >= 1.13.0+cu11.7](https://pytorch.org/)


## ⏬ Download Models


## 💻 Inference



## ✏️ Paragraph-Image Dataset: ParaImage-Small
 
---
![image.](asset/images/WX20231124-120329@2x.png)

The proposed ParaImage dataset mainly includes two parts:

(a) ParaImage-Big: High-quality images with generative captions (ParaImage-Big) are primarily employed for the paragraph-image alignment learning in Stage 2.

(b) ParaImage-Small: Aesthetic images with manual long-term description (ParaImage- Small) are primarily used for quality-tuning in Stage 3.



<img src="asset/images/1700797160959.jpeg" width="400"/>  <img src="asset/images/1700797178853.jpeg" width="400"/>


**ParaImage-Small** is a few thousand high-quality images are thoughtfully selected from LAION-Aesthetics, adhering to common principles in photography, then professionally annotated by skilled annotators.


The ParaImage-Small can be download from [Google Drive](https://drive.google.com/file/d/12x0uS0KgD4_NqzJ1A7hLjGkPIwD1Ozud/view?usp=drive_link)




## ✏️ New Prompts Eval: ParaPrompts-400

The current test prompts focus on short text-to-image generation, ignoring the evaluation for paragraph-to-image generation, we introduced a new evaluation set of prompts called ParaPrompts, including 400 long-text descriptions.

The previous prompts testing was mostly concentrated on text alignments within the range of 0-25 words, while our prompts extend to long-text alignments of 100 words or more.


<img src="asset/images/1700797464794.jpg" width="400"/>  <img src="asset/images/1700797453021.jpg" width="400"/>



## 📖BibTeX

    
## 🤗Acknowledgements
- Thanks to [Diffusers](https://github.com/huggingface/diffusers) for the wonderful work and codebase.
