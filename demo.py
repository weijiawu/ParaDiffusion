import os
from PIL import Image
import time
import torch
import sys
from transformers import AutoTokenizer
from diffusers  import UNet2DConditionModel
from diffusers import AutoencoderKL
from diffusers import EulerDiscreteScheduler, DPMSolverMultistepScheduler, DDIMScheduler
from pipeline_stable_diffusion_llama import StableDiffusionLlamaPipeline
from transformers import LlamaModel, AutoTokenizer
from peft import PeftModel, PeftConfig


def get_pipe(
            text_encoder_id=None, 
            tokenizer_id=None,
            unet_id=None, 
            vae_id=None,
            scheduler_id=None,
            gpu_id=0, 
            half=True,
            peft_model_id=None):
    
    # text encoder
    text_encoder = LlamaModel.from_pretrained(text_encoder_id)
    if peft_model_id  is not None:
        print("-----load lora----")
        text_encoder = PeftModel.from_pretrained(text_encoder, peft_model_id)

    # tokenizer
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_id)
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.model_max_length = 256
    # scheduler
    scheduler = DPMSolverMultistepScheduler.from_pretrained(scheduler_id)
    # vae
    vae = AutoencoderKL.from_pretrained(vae_id)
    # unet
    unet = UNet2DConditionModel.from_pretrained(unet_id, revision=None)
    if half:
        vae = vae.half()
        unet = unet.half()
    pipe = StableDiffusionLlamaPipeline(vae=vae,
                            text_encoder=text_encoder,
                            tokenizer=tokenizer,
                            unet=unet,
                            scheduler=scheduler,
                            safety_checker=None,
                            feature_extractor=None,
                            requires_safety_checker=False)
    # 整理已完成，开始返回
    pipe.to("cuda:{}".format(gpu_id))
    pipe.enable_attention_slicing()
    return pipe

def predict():

    prompt = "A peaceful scene of a small town in winter, with snow-covered houses and trees around. The town is surrounded by mountains, and the sky is covered in clouds, creating a solemn atmosphere. In the foreground, there is a boat docked on the river, with the boat itself covered in snow. The water surface of the river is calm, reflecting the houses and trees in the distance. The roofs of the houses are covered in snow, and the windows are lit up, emitting a warm yellow light. The branches of the trees are also covered in snow, with the tips of the branches showing the blue-white color of the snow. The sky is blue, with some clouds drifting, and the sun is setting, casting a soft orange glow on the horizon. The entire scene is filled with the beauty of winter, evoking the feeling of tranquility and warmth."       
    # 384 模型
#     unet_id = "./weights/unet_384"
    # 512 模型
#     unet_id = "/mmu-vcg/lizhuang05/code/vcg_diffusers_train_lz/exps/lizhuang05/task_llama/log/task_llama_stage4_qt_resume/checkpoint-30000/unet"

    # 1024 模型
    unet_id = "./weights/unet"
    


    
    width = 1024
    height = 640
    pipeconfig = {
        "text_encoder_id": "./weights/Llama-2-7b-hf",
        "tokenizer_id": "./weights/Llama-2-7b-hf",
        "vae_id": "./weights/sdxl-vae-fp16-fix",
        "scheduler_id": "./weights/scheduler",
        "unet_id": unet_id,
#         "peft_model_id": None,
        "peft_model_id": "./weights/text_encoder_lora",
        "half": True}    
    
    pipe = get_pipe(**pipeconfig)
    generator = torch.Generator(pipe.device).manual_seed(45)
    out = pipe(prompt=prompt, 
                width=width, 
                height=height, 
                generator=generator, 
                num_inference_steps=100, 
                num_images_per_prompt=1, 
                guidance_scale=7.5).images

        
    out[0].save("./demo.jpg")

if __name__ == '__main__':
    predict()
