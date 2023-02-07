<h1>Facial Recognition & Detection</h1>

<h3>Using livestream from webcam/integrated camera</h3>

[//]: # (<h3>Project Structure</h3>)

[//]: # (<img src="/screenshots/Product_Structure.png" alt="Project Structure">)


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
    <li><a href="#screenshots">Screenshots</a></li>
    <li><a href="#installation-and-usage">Installation and usage</a></li>
    <li><a href="#class-diagrams">Class Diagrams</a></li>
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

<p>Keycloak on the other hand, was deployed on a docker container and port bound to the Host Machine at port 8080.
Then I've configured it with a New Realm named <b><em>pm-realm</em></b> and a new client <b><em>pm-client</em></b></p>

```dockerfile
docker run -p 8080:8080 \
 -e KEYCLOAK_ADMIN=admin \
  -e KEYCLOAK_ADMIN_PASSWORD=admin \
   quay.io/keycloak/keycloak:20.0.3 start-dev
```

<p>The <mark><b>KEYCLOAK_ADMIN</b></mark> and <mark><b>KEYCLOAK_ADMIN_PASSWORD</b></mark> are Keycloak native parameters for the admin console, they can be changed later.</p>

<p>As per the users, 3 were made, one Admin and two Users. Admin has access to all the Data on the application, as for users, only limited access is given.
This difference of authorization can be seen on the backend, in the <em><b>CustomerController</b></em> Class as an example, as per picture below : </p>

<img src="/screenshots/CustomerController.png">

Code Snippet example of the authorization :

```java

    @PostMapping("/customers/addCustomer")
    @PreAuthorize("hasAuthority('Admin')")
    public Customer addCustomer(@RequestBody Customer customer) throws CustomerException {
        return customerService.addCustomer(customer);
    }
```

<p>Only Admins have the possibility to add a customer, as can be seen with annotation <em><b>@PreAuthorize("hasAuthority('Admin')")</b></em>.</p>

<p>On the other hand, a simple user can only check the customers list :</p>

```java
    @GetMapping("/customers")
    @PreAuthorize("hasAuthority('User')")
    public List<Customer> getCustomerList() {
        return customerService.listCustomers();
    }
```


## Class Diagrams

<h4 align="center">Customer Microservice</h4>

<img src="/screenshots/CustomerService.png" alt="">

<h4 align="center">Inventory Service</h4>

<img src="/screenshots/InventoryService.png" alt="">

<h4 align="center">Billing Service</h4>

<img src="/screenshots/bil.png" alt="">

<h4 align="center">Gateway Service</h4>

<img src="/screenshots/GatewayService.png" alt="">

<h4 align="center">Discovery Service</h4>

<img src="/screenshots/DiscoveryService.png" alt="">



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

Project Link: [https://github.com/HamzaOuggadi/ProductManagement-synthese-microservice](https://github.com/HamzaOuggadi/ProductManagement-synthese-microservice)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Pr. Mohamed Youssfi - Université Hassan II - ENSET Mohammedia](https://www.youtube.com/@mohamedYoussfi)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/HamzaOuggadi/ProductManagement-synthese-microservice.svg?style=for-the-badge
[contributors-url]: https://github.com/HamzaOuggadi/ProductManagement-synthese-microservice/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/HamzaOuggadi/ProductManagement-synthese-microservice.svg?style=for-the-badge
[forks-url]: https://github.com/HamzaOuggadi/ProductManagement-synthese-microservice/network/members
[stars-shield]: https://img.shields.io/github/stars/HamzaOuggadi/ProductManagement-synthese-microservice.svg?style=for-the-badge
[stars-url]: https://github.com/HamzaOuggadi/ProductManagement-synthese-microservice/stargazers
[issues-shield]: https://img.shields.io/github/issues/HamzaOuggadi/ProductManagement-synthese-microservice.svg?style=for-the-badge
[issues-url]: https://github.com/HamzaOuggadi/ProductManagement-synthese-microservice/issues
[license-shield]: https://img.shields.io/github/license/HamzaOuggadi/ProductManagement-synthese-microservice.svg?style=for-the-badge
[license-url]: https://github.com/HamzaOuggadi/ProductManagement-synthese-microservice/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
[Java.com]: https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=java&logoColor=white
[Java-url]: https://www.java.com
[Spring.io]: https://img.shields.io/badge/Spring-6DB33F?style=for-the-badge&logo=spring&logoColor=white
[Spring-url]: https://www.spring.io
[SpringSecurity.io]: https://img.shields.io/badge/Spring_Security-6DB33F?style=for-the-badge&logo=Spring-Security&logoColor=white
[Docker-url]: https://www.docker.com
[Docker.com]: https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white
[Keycloak-url]: https://www.keycloak.org/
[Keycloak.org]: https://www.keycloak.org/resources/images/keycloak_logo_200px.svg