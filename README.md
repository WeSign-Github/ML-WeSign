# ML-WeSign

The dataset contains 20 classes:
- Vocal BISINDO: A, I, U, E, O
- Vocal SIBI: A, I, U, E, O
- Basic Words SIBI: saya, dia, teman, baik, bel, bangku, meja, sakit, tugas, pramuka
- The datasets is created by taking pictures for every class with different angles and positions
- The datasets is resized into 320x320 and implemented image augmentation such as color shifting (Gray, Red, Green, Blue)
- We collect our dataset manually
- The dataset gathered by our team is labeled using labelImg https://github.com/tzutalin/labelImg

About models:
- Our models using pretrained model SSD-MobileNet V2 FPNLite 320 with Tensorflow Object Detection API https://tfhub.dev/tensorflow/ssd_mobilenet_v2/fpnlite_320x320/1
- For Deployment will be used TFLite format
- Using mAP (mean Average Score) to measure model accuracy https://github.com/Cartucho/mAP 

We upgraded to collect vocal and word sibi in one training file, so we have 4 folders in our repository.
