<h1>Facial Recognition & Detection</h1>

<h3>Using livestream from webcam/integrated camera</h3>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/HamzaOuggadi/ProductManagement-synthese-microservice">
    <img src="/readmeImgs/img.png" alt="Logo">
  </a>

<h3 align="center">This Project was made using OpenCV and Python</h3>

  <p align="center">
    <br />
    <a href="https://docs.opencv.org/4.7.0/da/d60/tutorial_face_main.html"><strong>Explore the OpenCV docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/HamzaOuggadi/Facial-Recognition-Detection">View Demo <em>(Under Construction)</em></a>
    ·
    <a href="https://github.com/HamzaOuggadi/Facial-Recognition-Detection/issues">Report Bug</a>
    ·
    <a href="https://github.com/HamzaOuggadi/Facial-Recognition-Detection/issues">Request Feature</a>
  </p>
</div>


> **Note**
> This Project is still under construction and continuous improvement, nothing is final.

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#screenshots">Video Sample, Screenshots</a></li>
    <li><a href="#installation-and-usage">Installation and usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

<p>This Project was achieved using OpenCV and Python for Face Detection and Face Recognition.</p>

<p>OpenCV (Open Source Computer Vision Library) is an open source computer vision and machine learning software library.</p>


<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Built With

<ul>
<li>Python</li>
<li>OpenCV</li>
</ul>

<img align="center" src="/readmeImgs/img_1.png">


<p>With OpenCV we have a choice from multiple algorithms for Face Recognition : </p>

<ul>
    <li>Eigenfaces.</li>
    <li>Fisherfaces.</li>
    <li>Local Binary Patterns Histograms.</li>
</ul>

<p>I've used the Local Binary Patterns Histograms algorithm.</p>

<p>LBPH (Local Binary Pattern Histogram) is a Face-Recognition algorithm it is used to recognize the face of a person. It is known for its performance and how it is able to recognize the face of a person from both front face and side face.</p>

<p>It's a simple yet very efficient texture operator which labels the pixels of an image by thresholding the neighborhood of each pixel and considers the result as a binary number.</p>

<img align="center" src="/readmeImgs/LBPH.png">

<p>Note that face recognition is different of face detection :</p>

<ul>
    <li><b>Face Detection:</b> it has the objective of finding the faces (location and size) in an image and probably extract them to be used by the face recognition algorithm.</li>
    <li><b>Face Recognition:</b> with the facial images already extracted, cropped, resized and usually converted to grayscale, the face recognition algorithm is responsible for finding characteristics which best describe the image.</li>
</ul>

<p>So in order to get good recognition rates you'll need at least 8(+-1) images for each person and the Fisherfaces method doesn't really help here. The above experiment is a 10-fold cross validated result carried out with the facerec framework at: https://github.com/bytefish/facerec. This is not a publication, so I won't back these figures with a deep mathematical analysis. Please have a look into [168] for a detailed analysis of both methods, when it comes to small training datasets.</p>

<img align="center" src="/readmeImgs/DBSize.png">

<ul>
    <li>LBPH is one of the easiest face recognition algorithms.</li>
    <li>It can represent local features in the images.</li>
    <li>It is possible to get great results (mainly in a controlled environment).</li>
    <li>It is robust against monotonic gray scale transformations.</li>
    <li>It is provided by the OpenCV library (Open Source Computer Vision Library).</li>
</ul>

## Video Sample & Screenshots

<p>Video Demo :</p>

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/rZxZHQHujmg/0.jpg)](https://www.youtube.com/watch?v=rZxZHQHujmg)


<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Installation and Usage

The following packages are needed for this project to work properly : 

```python
pip install opencv-python
```

```python
pip install pillow --upgrade
```

<p>Imports :</p>

```python
import cv2
import numpy as np
import os
import pickle
from PIL import Image
```

<h3>Face Detection :</h3>

<p>For Face Detection a Cascade Classifier <em><b>(haarcascade_frontalface_alt2.xml)</b></em> was used, it can be found in the following directory :</p>

```shell
/cascades/haarcascade_frontalface_alt2.xml
```

```python
face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_alt2.xml')
```

<h3>The input for Face Detection/Recognition is from the default Camera in your Machine.</h3>
<p>Here is the code responsible for it :</p>

```python
cap = cv2.VideoCapture(0)
```

```python
faces = face_cascade.detectMultiScale(grayedFrame, scaleFactor=1.5, minNeighbors=5)
```
<h3>Training the Algorithm :</h3>

<p>To train the Algorithm several photos were used from photos found on the internet of celebrities and yours truly :</p>

```bash
├───images
│   ├───Emilia-Clarke
│   ├───Hamza-Ouggadi
│   ├───Jeff-Bezos
│   └───Peter-Dinklage
```

<p>The names of the folders were used as labels for each person while training.</p>

```python
recognizer = cv2.face.LBPHFaceRecognizer_create()
```

<p>The training creates a <em><b>.yaml</b></em> file that can be used on other inputs for recognition.</p>

```python
recognizer.train(x_train, np.array(y_labels))
recognizer.save("trainner.yaml")
```

<p>As can be seen below :</p>

```python
recognizer.read("trainner.yaml")
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contributing

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Hamza Ouggadi - hamza.ouggadi@gmail.com

Project Link: https://github.com/HamzaOuggadi/Facial-Recognition-Detection

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

<ul>
    <li>OpenCV Face Recognition Documentation - <a href="https://docs.opencv.org/4.7.0/da/d60/tutorial_face_main.html">OpenCV Docs</a></li>
    <li>OpenCV Python Installation and Usage - <a href="https://pypi.org/project/opencv-python/">OpenCV Python</a></li>
    <li>TowardsDataScience.com - Face Recognition: Understanding LBPH Algorithm - <a href="https://towardsdatascience.com/face-recognition-how-lbph-works-90ec258c3d6b">Understanding LBPH Algorithm</a></li>
</ul>


<p align="right">(<a href="#readme-top">back to top</a>)</p>
