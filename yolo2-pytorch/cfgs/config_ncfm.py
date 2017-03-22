import numpy as np


# trained model
h5_fname = 'yolo-ncfm.weights.h5'

# VOC
label_names = ('ALB','BET','DOL','LAG','NoF','OTHER','SHARK','YFT')
num_classes = len(label_names)

anchors = np.asarray([(1.08, 1.19), (3.42, 4.41), (6.63, 11.38), (9.42, 5.11), (16.62, 10.52)], dtype=np.float) #Need to change this according to our dataset
num_anchors = len(anchors)

