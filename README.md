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

![image.](asset/images/fig1_teasers.pdf)

---
![image.](asset/images/1700796567631.png)


# 🔧 Dependencies and Installation

- Python >= 3.10 (Recommend to use [Anaconda](https://www.anaconda.com/download/#linux) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html))
- [PyTorch >= 1.13.0+cu11.7](https://pytorch.org/)


# ⏬ Download Models


# 💻 Inference



# ✏️ Paragraph-Image Dataset: ParaImage-Small
ParaImage-Small is a few thousand high-quality images are thoughtfully selected from LAION-Aesthetics, adhering to common principles in photography, then professionally annotated by skilled annotators. 
---
![image.](asset/images/1700796834574.png)

<img src="asset/images/1700797160959.png" width="400"/>  <img src="asset/images/1700797178853.png" width="400"/>



# ✏️ Paragraph-Image Prompts Eval: ParaPrompts-400
<img src="asset/images/1700797464794.jpg" width="400"/>  <img src="asset/images/1700797453021.jpg" width="400"/>



# 📖BibTeX

    
# 🤗Acknowledgements
- Thanks to [Diffusers](https://github.com/huggingface/diffusers) for the wonderful work and codebase.
