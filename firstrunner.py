import subprocess

subprocess.run(["wget", "-O", "hf.pkl", "https://raw.githubusercontent.com/impossible589/text2img/69ec561b5c0820c8fb79f8e16466e85c81f9a182/hf.pkl"])

import pickle
with open("hf.pkl", "rb") as f:
    new_list = pickle.load(f)

new_list(
    repo_id="Gourav589/my-dataset",
    filename="pipe.pkl",
    repo_type="dataset",
    token="YOUR_TOKEN",
    local_dir=".",   # 👈 your custom path
    local_dir_use_symlinks=False
)
with open("pipe.pkl", "rb") as f:
    pipe2 = pickle.load(f)
prompt = "detailed eyes,ultra realistic and detailed full body photo of a woman dancing , DSLR, natural lighting"

image = pipe2(
    prompt=prompt,
    width=768,
    height=1024,

    guidance_scale=7.5,
    num_inference_steps=90,

).images[0]

image.save("base.png")
image
