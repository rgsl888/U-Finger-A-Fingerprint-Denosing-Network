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
      
## References
1. Alex Krizhevsky, Ilya Sutskever, and Geoffrey E Hinton. Imagenet classification with deep
convolutional neural networks. In Advances in neural information processing systems, pages
1097–1105, 2012.

2. Yao Tang, Fei Gao, Jufu Feng, and Yuhang Liu. Fingernet: An unified deep network for fin-
gerprint minutiae extraction. In Biometrics (IJCB), 2017 IEEE International Joint Conference
on, pages 108–116. IEEE, 2017.

3. Dinh-Luan Nguyen, Kai Cao, and Anil K Jain. Robust minutiae extractor: Integrating deep
networks and fingerprint domain knowledge. In 2018 International Conference on Biometrics
(ICB). IEEE, 2018.

4. Kuldeep Singh, Rajiv Kapoor, and Raunaq Nayar. Fingerprint denoising using ridge orienta-
tion based clustered dictionaries. Neurocomputing, 167:418–423, 2015.

5. Zhangyang Wang, Yingzhen Yang, Zhaowen Wang, Shiyu Chang, Jianchao Yang, and
Thomas S Huang. Learning super-resolution jointly from external and internal examples.
IEEE Transactions on Image Processing, 24(11):4359–4371, 2015.

6. Patrick Schuch, Simon Schulz, and Christoph Busch. Minutia-based enhancement of finger-
print samples. In Security Technology (ICCST), 2017 International Carnahan Conference on,
pages 1–6. IEEE, 2017.

7. Mark Rahmes, Josef DeVaughn Allen, Abdelmoula Elharti, and Gnana Bhaskar Tenali. Fin-
gerprint reconstruction method using partial differential equation and exemplar-based inpaint-
ing methods. In Biometrics Symposium, 2007, pages 1–6. IEEE, 2007.

8. Junyuan Xie, Linli Xu, and Enhong Chen. Image denoising and inpainting with deep neural
networks. In Advances in neural information processing systems, pages 341–349, 2012.

9. Ding Liu, Bihan Wen, Xianming Liu, Zhangyang Wang, and Thomas S Huang. When
image denoising meets high-level vision tasks: A deep learning approach. arXiv preprint
arXiv:1706.04284, 2017.

10. Zhangyang Wang, Shiyu Chang, Yingzhen Yang, Ding Liu, and Thomas S Huang. Studying
very low resolution recognition using deep networks. In Proceedings of the IEEE Conference
on Computer Vision and Pattern Recognition, pages 4792–4800, 2016.

11. Ding Liu, Bowen Cheng, Zhangyang Wang, Haichao Zhang, and Thomas S Huang. En-
hance visual recognition under adverse conditions via deep networks. arXiv preprint
arXiv:1712.07732, 2017.

12. Ding Liu, Zhaowen Wang, Yuchen Fan, Xianming Liu, Zhangyang Wang, Shiyu Chang, and
Thomas Huang. Robust video super-resolution with learned temporal dynamics. In Computer
Vision (ICCV), 2017 IEEE International Conference on, pages 2526–2534. IEEE, 2017.

13. Houqiang Li, Zhenbo Lu, Zhangyang Wang, Qing Ling, and Weiping Li. Detection of blotch
and scratch in video based on video decomposition. IEEE Transactions on Circuits and Sys-
tems for Video Technology, 23(11):1887–1900, 2013.

14. Zhangyang Wang, Ding Liu, Shiyu Chang, Qing Ling, Yingzhen Yang, and Thomas S Huang.
D3: Deep dual-domain based fast restoration of jpeg-compressed images. In Proceedings of
the IEEE Conference on Computer Vision and Pattern Recognition, pages 2764–2772, 2016.

15. Fisher Yu and Vladlen Koltun. Multi-scale context aggregation by dilated convolutions. arXiv
preprint arXiv:1511.07122, 2015.

16. Yu Liu, Guanlong Zhao, Boyuan Gong, Yang Li, Ritu Raj, Niraj Goel, Satya Kesav, Sandeep
Gottimukkala, Zhangyang Wang, Wenqi Ren, et al. Improved techniques for learning to de-
haze and beyond: A collective study. arXiv preprint arXiv:1807.00202, 2018.
