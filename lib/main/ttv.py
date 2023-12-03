from config import *

def TextToVideo(prompt, num_frames, num_inference_steps):
    if torch.cuda.is_available():
        pipe = DiffusionPipeline.from_pretrained("cerspense/zeroscope_v2_576w", torch_dtype=torch.float16)
        pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
        pipe.enable_model_cpu_offload()

        video_frames = pipe(prompt, num_inference_steps=num_inference_steps, height=320, width=576, num_frames=num_frames).frames
        videos = export_to_video(video_frames)
        video_path = f'Your video is ready at {videos}'
    else:
        video_path = "Sorry Your Device Is Not Supported"
    return video_path