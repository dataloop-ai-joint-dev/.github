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

* [annotators-qualification-custom-metrics](#annotators-qualification-custom-metrics)

* [batch-management-app](#batch-management-app)

* [annotators-qualification-app](#annotators-qualification-app)

* [dataset-and-driver-creator-app](#dataset-and-driver-creator-app)

* [dynamic-tasks-app](#dynamic-tasks-app)

* [consensus-segmentation](#consensus-segmentation)

* [dockerized-server](#dockerized-server)

* [annotations-stitching](#annotations-stitching)


---

# annotators-qualification-custom-metrics
Visibility: Public
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

# annotators-qualification-app
Visibility: Private
### Description
Using the application you can manage scores of qualification task and add qualified annotators to tasks

### Install the Application
Contact your Dataloop customer success manager to get the application installed in your project

### Technology
* Python
* App panels based on HTML5 and JS
* Dataloop FaaS and Pipeline

 
[Go To Top](#solution-engineering-catalog)
---

# dataset-and-driver-creator-app
Visibility: Private
### Description
Using the application, you can create a new dataset linked to an existing driver or new driver based on a pre-defined driver template. 

### Install the Application
Contact your Dataloop customer success manager to get the application installed in your project.

### Technology
* Python
* App panels based on HTML5 and JS
* Dataloop FaaS

 
[Go To Top](#solution-engineering-catalog)
---

# dynamic-tasks-app
Visibility: Private
### Description:
An application that converts a `Task` to `Dynamic Task` 
and create pipeline nodes, for managing the task, to an existing inactive pipeline.

**Dynamic Task Explanation:**

A dynamic task, is a task that can hold items from different datasets on the same project.
The task receives items **only** from its related nodes inside the pipeline and handles the following case:
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
Please reach out to your Dataloop Customer Success manager to get the application installed in your project.

### Technology
* Python
* Dataloop FaaS and Pipeline

 
[Go To Top](#solution-engineering-catalog)
---

# dockerized-server
Visibility: Public
### Description:
A Docker with API server that receives image as an input, send it to a model for prediction, and sends the model 
results in json format.

**Notice:** Make sure to update the requested `host` and `port` in the file: `Dockerfile` inside the repository, 
before building the docker image: 
1. `EXPOSE 9000` - (line 14)
2. `CMD ["python", "app.py", "--host=0.0.0.0", "--port=9000"]` - (line 17)

### Install the Application
See the sections: `Prerequisite`, `How to Run Locally` and `How to Run Remotely` in the `README.md` file of this 
repository.

### Technology
* Python
* FastAPI
* Docker

 
[Go To Top](#solution-engineering-catalog)
---

# annotations-stitching
Visibility: Private
### Description:
This solution is a FAAS that supports 3 modes of annotations stitching from a group of segments to one main item. \
The 3 available modes are:
1. **AudiosToAudio** - Connect the annotations from the Audio segments, and upload them to the main Audio item.
   > ⚠️ **Warning:** This mode uses the annotations' description to add notes on stitching conflicts 
   (For more information about `AudiosToAudio` notes, see: [AudiosToAudio Mode Class](#Mode-Classes-Flow-Explanation)).
2. **ImagesToVideo** - Connect the annotations from the Image segments (Video frames), and upload them to the main Video item.
3. **VideosToVideo** - Connect the annotations from the Video segments, and upload them to the main Video item. 

### Install the Application
Please reach out to your Dataloop Customer Success manager to get the application installed in your project.

### Technology
* Python
* FastAPI
* Docker

 
[Go To Top](#solution-engineering-catalog)
---
