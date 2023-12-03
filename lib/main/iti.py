import PIL
from PIL import Image
import torch
from diffusers import StableDiffusionInstructPix2PixPipeline, EulerAncestralDiscreteScheduler

model_id = "timbrooks/instruct-pix2pix"

def ImageToImage(prompt, path, render):
    if render == 'cuda':
        pipe = StableDiffusionInstructPix2PixPipeline.from_pretrained(model_id, torch_dtype=torch.float16, safety_checker=None)
        pipe.to("cuda")
        pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(pipe.scheduler.config)
        
        image = PIL.Image.open(path)
        image = PIL.ImageOps.exif_transpose(image)
        image = image.convert("RGB")
        images = pipe(prompt, image=image, num_inference_steps=10, image_guidance_scale=1).images
    if render == 'cpu':
        pipe = StableDiffusionInstructPix2PixPipeline.from_pretrained(model_id, torch_dtype=torch.float32, safety_checker=None)
        pipe.to("cpu")
        pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(pipe.scheduler.config)
        
        image = PIL.Image.open(path)
        image = PIL.ImageOps.exif_transpose(image)
        image = image.convert("RGB")
        images = pipe(prompt, image=image, num_inference_steps=10, image_guidance_scale=1).images
    return images[0]