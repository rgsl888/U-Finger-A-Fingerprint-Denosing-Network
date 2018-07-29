# DeepDenoising

## Introduction
This repository provides codes that we use to study the mutual influence between image denoising and high-level vision tasks.

(1) We present an finger print denoising network which achieves state-of-the-art image denoising performance. 

(2) We propose a deep network solution that cascades two modules for image denoising and various high-level tasks, respectively, and demonstrate that the proposed architecture not only yields superior image denoising results preserving fine details, but also overcomes the performance degradation of different high-level vision tasks, such as image classification and semantic segmentation, due to image noise.

This code repository is built on top of [DeepLab v2](https://bitbucket.org/aquariusjay/deeplab-public-ver2).

For more details, please refer to our [paper](https://arxiv.org/abs/1706.04284).

### NOTE : But this code has particular changes for ECCV challenge and architectural changes such as dilated convolution network has been introduced compared to original papaer.

## Converting the colored images to gray
- `cd Testing`
- Use processimage.py to generate gray images

### Models
- `cd Testing`

### Training
- `cd exper`
- Run `main_train_denoise.sh` to train the denoising network seperately.
- Need to have an txt file where all the image names are listed and its location needs to updated in main_train_denoise.sh

### Testing
- `cd Testing`
- Use the dia_mean.ipynb file to generate images for testing
- The trained model and its deply file are also located in the same folder
- Use conv.ipynb to remove the noise on the edges 

## Citation
Please cite the paper in your publications if it helps your research:

    @inproceedings{liu2017when,
      author = {Liu, Ding and Wen, Bihan and Liu, Xianming and Huang, Thomas S.},
      title = {When Image Denoising Meets High-Level Vision Tasks: A Deep Learning Approach},
      year = {2017},
      journal={arXiv preprint arXiv:1706.04284}
      }
      
