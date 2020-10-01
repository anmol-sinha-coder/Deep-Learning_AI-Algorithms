# Transfer Learning using TensorFlow and Keras

Used Resnet OR Inception v3. ResNet solves the vanishing gradient problem by using Identity shortcut connection or skip connections that skip one or more layers. 
When we have a relatively small dataset, a super-effective technique is to use Transfer Learning where we use a pre-trained model. This model has been trained on an extremely large dataset, and we would be able to transfer weights which were learned through hundreds of hours of training on multiple high powered GPUs.

Many such models are open-sourced such as VGG-19 and Inception-v3. They were trained on millions of images with extremely high computing power which can be very expensive to achieve from scratch.
