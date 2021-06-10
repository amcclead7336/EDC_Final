# Final Project
#### by Alex McClead

## Overview:
For this project, we were given data on Bank Telemarketing. The data can be found in data/Bank-Telemarketing.csv
After the review, we were supposed to 

    1. Process the data
    2. Create a predictive model and store it in the ML Tracking system
    3. Download Best Performing model and Deploy a model as API
    4. Containerize model and API
    5. Output container to Cloud repository
    6. Deploy Containerized model and API in Kubernetes Cluster
    
    
## Summary:

After preprocessing the data and testing multiple models I can create and deploy a model with 90% accuracy using a Random Forest model. I am also able to containerize and deploy the container to the cloud container registry. See below an image of the saved models:

![ML Model Backup](https://github.com/amcclead7336/EDC_Final/blob/master/docs/Screen%20Shot%202021-06-06%20at%202.21.54%20PM.png?raw=true)


and you can see here the file output to the cloud registry:
![Container Registry](https://github.com/amcclead7336/EDC_Final/blob/master/docs/Screen%20Shot%202021-06-06%20at%202.22.15%20PM.png?raw=true)

This is a demo of the API in use, run from a container:
![FlaskAPI in use](https://github.com/amcclead7336/EDC_Final/blob/master/docs/Screen%20Shot%202021-06-06%20at%202.16.34%20PM.png?raw=true)


# Steps:

### Process the data
The data started fairly clean. There were no NA values and much of the data was numerical. That being said there were a lot of object or categorical data values that I need to convert into numerical representations. I mapped these translations to a list and output the list to the Model_config file. This file has important information for the Flask API.

### Create a predictive model and store it in an ML Tracking system
After processing the data I test multiple models to find the best performer. I created a function that took different models, tested them, and output them to my ML API all in one go. This made tested fast and efficient.

### Download Best Performing model and Deploy a model as API
After testing the different models I downloaded the best performing model from my API and saved it to my deployments folder. I abstracted the folder names so that I could run tests with different models if some performed better than others. The Dockerfile, which is what I use to create the image for my containers is constantly updated with the top-performing model's information.

I also used a template FlaskAPI.py file to output to the API files. This file collects information from the model_config file to make sure it collects the proper pkl and class mapping information

### Containerize model and API
Once Downloaded the API is inserted I containerize the model with some docker commands. Even though this isn't specifically asked for in the assignment, I do it anyway as a way to make sure the container works without any issue. The above screenshot of the FlaskAPI consumption demonstrates this accurately.

### Output container to Cloud repository
I output the container to my registry. This simulates that any user I've given access to can download and deploy my API using Docker. 

### Deploy Containerized model and API in Kubernetes Cluster
I was not able to get the Kubernetes Cluster to work in the end however it does show that it is up and functioning. (Not sure what is wrong. I spent 3hr's trying to figure it out and I currently have no solutions for it.)


## Difficulties
On this final project, I was able to get almost everything to work with the exceptions of Standard Scaling, One hot encoding, and the Kubernetes cluster availability. Besides that everything went well. I was able to get around the one-hot encoder with the label encoder thankfully. 
