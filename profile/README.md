# Solution Engineering Catalog


<p align="center">
<a href="https://dataloop.ai/" target="_blank" rel="noreferrer noopener">
<img width="700" src="https://github.com/dataloop-ai-joint-dev/.github/blob/master/logo.png"></a>
</p>

<div align="center">
<a href="https://www.linkedin.com/company/dataloop/about/" target="_blank" rel="noreferrer noopener">
<img src="https://github.com/dataloop-ai-joint-dev/.github/blob/master/LinkedIn.png" width="3%" alt="LinkedIn"></a>
<a href="https://www.youtube.com/channel/UCCvp-nw5mK9bb9lDNcD6fgw/featured" target="_blank" rel="noreferrer noopener">
<img src="https://github.com/dataloop-ai-joint-dev/.github/blob/master/YouTube.jpeg" width="3%" alt="YouTube"></a>
<a href="https://github.com/dataloop-ai-joint-dev" target="_blank" rel="noreferrer noopener">
<img src="https://github.com/dataloop-ai-joint-dev/.github/blob/master/GitHub.png" width="3%" alt="GitHub"></a>
</div>

---
## Available Solutions:

* [annotations-stitching](#annotations-stitching)

* [annotators-qualification-app](#annotators-qualification-app)

* [annotators-qualification-custom-metrics](#annotators-qualification-custom-metrics)

* [batch-management-app](#batch-management-app)

* [consensus-segmentation](#consensus-segmentation)

* [cycles-retry](#cycles-retry)

* [dataset-and-driver-creator-app](#dataset-and-driver-creator-app)

* [dockerized-server](#dockerized-server)

* [dynamic-tasks-app](#dynamic-tasks-app)

* [lidar-base-parser](#lidar-base-parser)

* [lidar-demo-deployment](#lidar-demo-deployment)

* [lidar-osdar-parser](#lidar-osdar-parser)

* [lidar-pcds-connector](#lidar-pcds-connector)

* [sam-predict-faas](#sam-predict-faas)

* [video-triming-pipeline](#video-triming-pipeline)


---

# annotations-stitching
Visibility: Private
### Description:
This solution is a FAAS that supports 3 modes of annotations stitching from a group of segments to one main item. \
The 3 available modes are:
1. **AudiosToAudio** - Connect the annotations from the Audio segments, and upload them to the main Audio item.
2. **ImagesToVideo** - Connect the annotations from the Image segments (Video frames), and upload them to the main Video item.
3. **VideosToVideo** - Connect the annotations from the Video segments, and upload them to the main Video item. 

### Install the Application
Please reach out to your Dataloop Customer Success manager to get the FAAS installed in your project.

### Technology
* Python
* Dataloop FaaS and Pipeline

 
[Go To Top](#solution-engineering-catalog)
---

# annotators-qualification-app
Visibility: Private
### Description
The application lets you create an annotation exam, use the [qualification task](https://dataloop.ai/docs/qualification-honeypot) to perform exams, manage the score results, and add qualified annotators to existing tasks

Using the application, you can manage scores of qualification tasks and add qualified annotators to tasks

### Install the Application
Please reach out to your Dataloop Customer Success manager to get the application installed in your project.

### Technology
* Python
* App panels based on HTML5 and JS
* Dataloop FaaS and Pipeline

 
[Go To Top](#solution-engineering-catalog)
---

# annotators-qualification-custom-metrics
Visibility: Private
### Description
Use the Custom Metrics service to provide custom calculations of annotation scores for [Dataloop Annotators Qualification App](#annotators-qualification-app).

### Install the Application
Follow the instructions under the [repository README file](https://github.com/dataloop-ai-joint-dev/annotators-qualification-custom-metrics/blob/master/README.md)

### Technology
* Python
* Dataloop FaaS 

 
[Go To Top](#solution-engineering-catalog)
---

# batch-management-app
Visibility: Private
### Description
Using the application, you can work with sync and async batches in Dataloop Pipeline:
* Task can handle many batches and many annotators
* Async Batches: each item in the batch can be annotated by a different annotator, but you get notification when all items in the batch are completed
* Sync Batches: all items in the batch will be annotated by the same annotator when a batch is completed, the next batch will be assigned to him

### Install the Application
Please reach out to your Dataloop Customer Success manager to get the application installed in your project.

### Technology
* Python
* App panels based on HTML5 and JS
* Dataloop FaaS and Pipeline

 
[Go To Top](#solution-engineering-catalog)
---

# consensus-segmentation
Visibility: Private
### Description:
A pipeline to support consensus task with segmentation annotations.
The pipeline uses Majority Vote logic on each pixel on the image, and determine the pixel label on the original image 
as follows:

1. If for the given threshold, the Majority Vote result on the pixel `PASSES` the threshold: 
The pixel receives a segmentation annotation with the selected label
(For a Majority Vote result of `No Annotation`, the pixel will stay `Not Annotated`).
2. If for the given threshold, the Majority Vote result on the pixel `FAILS` the threshold: 
The pixel receives a segmentation annotation with the label `disagreement`.

After the checking of the Majority Vote is completed, the resulted mask/s are uploaded to the given upload dataset.

### Install the Application
Please reach out to your Dataloop Customer Success manager to get the Pipeline installed in your project.

### Technology
* Python
* Dataloop FaaS and Pipeline
 
[Go To Top](#solution-engineering-catalog)
---

# cycles-retry
Visibility: Private
### Description
The application let you an option adding retry mechanism to the pipelines failed cycles. \
After configurable retry number, the application will email cycle fails error to a distribution list.

### Install the Application
Please reach out to your Dataloop Customer Success manager to get the application installed in your project.

### Technology
* Python
* Dataloop SDK

 
[Go To Top](#solution-engineering-catalog)
---

# dataset-and-driver-creator-app
Visibility: Private
### Description
Using the application, you can create a new dataset linked to an existing driver or new driver based on a pre-defined driver template. 

### Install the Application
Please reach out to your Dataloop Customer Success manager to get the application installed in your project.

### Technology
* Python
* App panels based on HTML5 and JS
* Dataloop FaaS

 
[Go To Top](#solution-engineering-catalog)
---

# dockerized-server
Visibility: Private
### Description:
This solution will allow you to perform predict action using dataloop model management without deploying your model into dataloop and using the docker as a proxy server

The Docker template has an API server that receives an image as input, sends it to a model for prediction, and sends the model 
results in JSON format.

The solution also comes with a test script that parses the API server results and uploads them to the Dataloop platform.

### Install the Application
Follow the instructions under the [repository README file](https://github.com/dataloop-ai-joint-dev/dockerized-server/blob/master/README.md).

### Technology
* Python
* FastAPI
* Docker

 
[Go To Top](#solution-engineering-catalog)
---

# dynamic-tasks-app
Visibility: Private
### Description:
An application that converts a `Task` to `Dynamic Task` 
and create pipeline nodes, for managing the task, to an existing inactive pipeline.

**Dynamic Task Explanation:**

A dynamic task, is a task that can hold items from different datasets on the same project.
The task receives items **only** from its related nodes inside the pipeline and handles the following basic cases:
1. `Item from the same dataset of the task` - The item enters to the main dynamic task
2. `Item from a different dataset of the task` - A new dynamic task on the item's dataset gets created as a child task 
    to the main dynamic task (If there is no existing one) and the item enters to this child dynamic task.

### Install the Application
Please reach out to your Dataloop Customer Success manager to get the application installed in your project.

### Technology
* Python
* App panels based on HTML5 and JS
* Dataloop FaaS and Pipeline
 
[Go To Top](#solution-engineering-catalog)
---

# lidar-base-parser
Visibility: Private
### Description:
A pipeline that do the following things: 
1. Parses lidar data inside a Dataloop Dataset,
   and stitches all the files together to create a LiDAR video file (`lidar_parser` node).
2. Runs `ground detection` model on all the scene frames to enable the ground detection toggle button in the LiDAR video 
   file (`ground_detection` node).

### Install the Application
Please reach out to your Dataloop Customer Success manager to get the Pipeline installed in your project.

### Technology
* Python
* LiDAR
* Dataloop FaaS and Pipeline

 
[Go To Top](#solution-engineering-catalog)
---

# lidar-demo-deployment
Visibility: Private
### Description:
A solution to prepare Dataloop LiDAR Scene Demo in any new/existing dataset. 

### Install the Application
Please reach out to your Dataloop Customer Success manager to get the dataset installed in your project.

### Technology
* Python
* LiDAR
 
[Go To Top](#solution-engineering-catalog)
---

# lidar-osdar-parser
Visibility: Private
### Description:
A Custom LiDAR Parser to support conversion of datasets from
[Open Sensor Data for Rail 2023](https://data.fid-move.de/dataset/osdar23), to the Dataloop Platform.

### Install the Application
Please reach out to your Dataloop Customer Success manager to get the Pipeline installed in your project.

### Technology
* Python
* LiDAR
* Dataloop FaaS and Pipeline

 
[Go To Top](#solution-engineering-catalog)
---

# lidar-pcds-connector
Visibility: Private
### Description:
A pipeline that do the following things: 
1. Stitches all the PCD files together to create a LiDAR video file (`lidar_parser` node).
2. Runs `ground detection` model on all the scene frames to enable the ground detection toggle button in the LiDAR video 
   file (`ground_detection` node).

### Install the Application
Please reach out to your Dataloop Customer Success manager to get the Pipeline installed in your project.

### Technology
* Python
* LiDAR
* Dataloop FaaS and Pipeline

 
[Go To Top](#solution-engineering-catalog)
---

# sam-predict-faas
Visibility: Private
### Description:
A service that uses the [SAM](https://github.com/facebookresearch/segment-anything.git) model by 
`Facebook Research` team, with [Weights](https://huggingface.co/spaces/abhishek/StableSAM/blob/main/sam_vit_h_4b8939.pth) 
from `Hugging Face`.

The service gets an image item and uploads to them all the detected segmentation annotations by the SAM model 
as polygons, with a `default_label` of `car parts`.

> **Notice:** The Service `default_label` parameter can be changed from `car parts` to any label.

An example of a pipeline that uses this solution can be found under [noimos-dataloop repository](https://github.com/dataloop-ai-joint-dev/noimos-dataloop/tree/master/car-parts-pipeline)
### Install the Application
Please reach out to your Dataloop Customer Success manager to get the FAAS installed in your project.

### Technology
* Python
* SAM model by Facebook Research
* Dataloop FaaS

 
[Go To Top](#solution-engineering-catalog)
---

# video-triming-pipeline
Visibility: Private
### Description
Using the solution, you can trim a video file to some webm segments, move it to task (async, many annotators can work on each video), and once all video segments are ready, stitch all annotations to a single JSON file (based on object ID).
### Install the Application
Contact your Dataloop customer success manager to get the application installed in your project.

### Technology
* Python
* Dataloop FaaS/Pipeline

 
[Go To Top](#solution-engineering-catalog)
---
