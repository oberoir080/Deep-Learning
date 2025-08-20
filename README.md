# Deep Learning Coursework

This repository contains my submissions for the Deep Learning course assignments, including:

- **Assignment 1 (A1):** Custom PyTorch DataLoader and Dataset implementations for FashionMNIST and Speech Commands datasets.
- **Assignment 2 (A2):** AutoEncoder, Variational AutoEncoder, and Conditional Variational AutoEncoder models for image restoration on FashionMNIST.
- **Assignment 3 (A3):** Advanced SSIM-based experiments.
- **Assignment 4 (A4):** *Optional* — my attempt is kinda mid :P

> **Note:** These assignments were completed as part of the coursework for Deep Learning (CSE641) at IIIT Delhi, taught by Dr. Vinayak Abrol in the Winter 2025 semester.

## Assignment Scores & Results

### A1 (2021555_a1.ipynb)
- Custom DataLoader implementation benchmarked **faster than PyTorch's DataLoader** for both speech and image datasets.
- All required test cases passed successfully.
- Training/validation curves are included in the notebook.

**Results:**
- **MLP (Speech Commands):** Train Acc = 90.16%, Val Acc = 48.58%  
- **MLP (FashionMNIST):** Train Acc = 95.51%  
- **CNN (Speech Commands):** Train Acc = 93.79%, Val Acc = 63.22%  
- **CNN (FashionMNIST):** Train Acc = 99.21%, Val Acc = 93.07%  

---

### A2 (202155_a2.ipynb)
- Achieved the **highest SSIM score in the batch** for the AutoEncoder on FashionMNIST image restoration.
- Training/validation curves and reconstructions are included in the notebook.

**Results (SSIM):**
- **AutoEncoder (AE):** Train = 0.8247, Val = 0.7936  
- **Variational AutoEncoder (VAE):** Train = 0.7073, Val = 0.7126  
- **Conditional VAE (CVAE):** Train = 0.7029, Val = 0.7106  

---

### A3 (DLA3_SSIM.ipynb)
- Explored generations by creating a **Conditional GAN (cGAN) from scratch**.  

---

### A4 (Best 3/4 assignments)
- Attempted the optional assignment.  
- Didn’t push too hard on this one — result is kinda mid :P  

---
