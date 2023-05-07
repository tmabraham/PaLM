import torch
from palm_rlhf_pytorch import PaLM

dependencies = ['torch']

def palm_model():
    num_tokens = 50304
    dim = 2048
    depth = 16
    dim_head = 128
    heads = 8

    model = PaLM(
        num_tokens=num_tokens, dim=dim, depth=depth, dim_head=dim_head, heads=heads
    )

    huggingface_url = 'https://huggingface.co/conceptofmind/palm-1b/resolve/main/pytorch_model.bin'
    state_dict = torch.hub.load_state_dict_from_url(huggingface_url, progress=True)
    model.load_state_dict(state_dict)

    return model