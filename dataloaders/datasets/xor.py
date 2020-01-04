'''
    Author: Sungguk Cha
    eMail : navinad@naver.com
    dataloader for XOR
'''

import numpy as np
import torch
from torch.utils import data
from torchvision import transforms

class ToTensor(object):
    """ Convert ndarrays in sample to Tensors. """
    def __call__(self, sample):
        emb = sample['image']
        label = sample['label']

        emb = torch.from_numpy(emb).float()

        return {'image': emb, 'label': label}

class XOR(data.Dataset):
    
    def __init__(self, split='train'):
        self.split = split
        self.dataset = [ ( np.array((0, 0)), np.array(0) ), ( np.array((0, 1)), np.array(1) ), ( np.array((1, 0)), np.array(1)), ( np.array((1, 1)), np.array(0)) ]

    def __len__(self):
        return len(self.dataset) * 100 if self.split == 'train' else len(self.dataset)

    def __getitem__(self, index):

        sample = {'image': self.dataset[index % 4][0], 'label': self.dataset[index % 4][1]}
        
        composed_transforms = transforms.Compose([
                ToTensor() ])

        return composed_transforms(sample)
