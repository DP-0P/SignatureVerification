There are two types of signature verification tecniques:
  -> Online
  -> Offline

* ONLINE signature verification consists of dynamic information of signing process
  such as pen trajectory, inclination and pressure. These are utilized in feature
  extraction for verification.
* In OFFLINE signature verification, signature image is captured by scanner
  or camera after writing in completed, and images are analyzed for verification.

** Due to missing of dynamic information of stokes, offline signature verification
is more difficult than online verification.

Many methods proposed for offline signature verification, most of them
concentrate on feature extraction and similarity/distance metric evaluation.

Recent works of signature verification mostly use deep neural networks, particularly,
the Convolutional Neural Network for learning features.

Deep neural networks allow automatic feature extraction by heirarchical layer computing.

CNN vs Siamese
CNN -> Writer-Dependent
Siamese -> Writer-Independent

### FILE: 1-s2.0-S0031320321001965-main

"As deep neural networks usually relies on a large number of training samples
for good generalization, in signature verification, the CNN is usually used
in writer-dependent (WD) verification where each user has many genuine and
forgery samples, or the samples of many users are pooled to train a network
(as in Siamese network) for writer-independent (WI) verification. Signature
synthesis has been considered for augmenting training data for CNN, which
applies Siamese network framework and focuses on random forgery verification."

Approach:

1. Preprocessing : is required to alleviate the influence of background,
   grayscale variation, size and location of signature on
   on the verification performance.
   STEPS MAY INCLUDE:> Tilt correction, background removal, RGB -> Grayscale, size normalisation
2. Feature Extraction : length, storke, width. Siamese Network is used on local region
   than on the whole image. LEARN FEATURES FROM LOCAL REGION and then FUSE THE SIMILARITY MEASURES OF
   MULTIPLE LOCAL regions. MSDN
   SOMETHING called SE-Blocks are used. Squeeze-and-excitation blocks are added into each
   DenseNet block to interact information of  two inputs.
3. CNN
   i.   Region based metric learning
   ii.  Signature verification decision
   iii. Comparision of CNN architectures
   iv.  Effectiveness of region fusion scheme
   v.   Comparision with previous methods

### FILE: 1-s2.0-S0925231219313098-main

NOTE: This paper has a great abstract, stating the diff b/w online/offline methods, WI / WD systems,
and shows the variation in the types of forgeries.(skilled, simple, random)

Approach:

1. Preprocess the signature image dataset.
2. Partition the samples into disjoint training, validation and test subsets.
3. Generate the explained signature pairs. We consider four different schemes
   to produce samples (these can be used separately or combined in the training
   process) using: Original GAVAB training set, augmented GAVAB training set,
   our proposed synthetic signatures and GPDSSynhetic dataset respectively.
   The signature pairs generation process is the same for all the schemes.
4. Train the model to build f of Eq. (1) using a Siamese NeuralNetwork.
5. Test the trained model.

Preprocessing :> Grayscale conversion, Increasing stroke widt (MORPHOLOGICAL EROSION), Resizing, normalisation of pixel values

### FILE: 1-s2.0-S1568494615007577-main

Uses Hough Transformation (General Radon Transform) as the feature extractor.
