import torch
print(torch.cuda.is_available())  # Should print True

#Clear Cache of GPU
import torch

torch.cuda.empty_cache()
