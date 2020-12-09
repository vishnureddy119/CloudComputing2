Steps to set up the Cloud Environment and Run the model Training and the application prediction

1.	Create AWS EMR Clusters using the key pairs and select the instance as 4(one Master and three slaves) and select application as spark
2.	After Creating the Cluster add the SSH inbound rule to the master node for port 22
3.	Using putty Connect to the master node using the public ip address and the AWS pem file (connect as Hadoop user)
4.	 We must Install the following packages in the masters in order to run the python code (install the mentioned modules as Root user i.e. Run command: sudo su)
1.	pip install pyspark
2.	pip install numPy
5.	The Assignment contains two py files (Copied these two files using WinSCP from local to the vm)
1.	one python file (ModelCreation.py) to read the Trainingdata.csv train and save the model 
Command to run the python file: python ModelCreation.py
2.	Second python file (Application.py) to read the model and take the test data as input from the command line arguments and gives the F1 score as output
Command with args (Without docker): 
python Applciation.py TestDataset.csv

6.	 Create a docker file (DockerFile)
Command: nano DockerFile 
This file consists of all the commands which are needed to be executed while building the image
7.	Install Docker using the command sudo yum install docker -y
8.	Start the Docker service using   sudo service docker start
9.	 Build the image using the command below (which takes DockerFile as input)
              sudo docker build -t assignment2 . 
10.	Check whether the image is created or not using the command                 sudo docker images
11.	Once the image is created now tag the image to the docker hub.
    Command: sudo docker tag assignment2 vishnureddy119/assignment2
12.	Once the image is tagged now push the image to the docker hub for which we have to login in to the docker. Below are the steps to be followed
       sudo docker login
       sudo docker push vishnureddy119/assignment2    
13.	Once the image is pushed to the Docker hub now, we must pull the image from the docker hub and run it 

Commands to run the image as an instance (Container) and execute the application,
sudo docker run --name model -d assignment2
copying the testdata.csv into the container
sudo docker cp ../TestDataset.csv model:/  
get inside the container and execute the application
sudo docker exec -it model sh
now running the application to calculate the f1 score
python Application.py TestDataset.csv


GitHub link:
https://github.com/vishnureddy119/CloudComputing2
DockerHub link: 
https://hub.docker.com/repository/docker/vishnureddy119/assignment2
