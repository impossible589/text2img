import pickle
from huggingface_hub import hf_hub_download


# Save
with open("hf.pkl", "wb") as f:
   pickle.dump(hf_hub_download, f)
