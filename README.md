# docker_thoipapy
use the docker to run the standalone thoipapy application
### Installing the Docker
  * follow the latest instructions to install Docker Community Edition for your operating system
     * https://docs.docker.com/install/
  * e.g. Windows : https://docs.docker.com/docker-for-windows/install/
     * currently the installation differs between Win10 pro and above, and other windows versions.
  * e.g. Linux : https://docs.docker.com/i
### Download the thoipapy docker repository
git clone https://github.com/bojigu/thoipapy_docker.git  
then open the docker machine, e.g. in windows, open the Docker Quickstart Terminal, the terminal looks like this:
![run docker1](https://github.com/bojigu/docker_thoipapy/blob/master/docs/run_docker1.png)  
cd to the directory where thoipapy docker is, e.g:
cd /Where/docker_thoipapy/folder/is  
In the docker_thoipapy folder, there are three main files named:
 * dockerfile ,a text document that contains all the commands a user could call on the command line to assemble an image, the dockerfile mainly install perl, python, freecontact, thoipapy, thoipapy dependencies in the docker environment.
 * app.py, the standalone thoipapy prediction application python script.
 * requirements.txt, the python dependencies for thoipapy.  
### Build the thoipa image
Now run the build command. This creates a Docker image, which we’re going to tag using -t so it has a name.  
docker build -t thoipa .
![run docker2](https://github.com/bojigu/docker_thoipapy/blob/master/docs/run_docker2.png) 
### Run the app
docker run thoipa
![run docker3](https://github.com/bojigu/docker_thoipapy/blob/master/docs/run_docker3.png)  
And the prediction output can also be printed on the terminal:
![run docker4](https://github.com/bojigu/docker_thoipapy/blob/master/docs/run_docker4.png)  
Now we can display all the installed containers, including the thoipa container just installed:
Docker container ls --all
![run docker5](https://github.com/bojigu/docker_thoipapy/blob/master/docs/run_docker5.png)  
### Copy files from the container
Now we are going to copy the prediction output file from the thoipa container to our host machine:  
docker cp 1204803a81c8:/app/bnip3/THOIPA_out.csv ./output/output.csv  
or, we can copy all the prediction folder over to the local host:  
docker cp 1204803a81c8:/app/bnip3/ ./output/  
Where 1204803a81c8 is the container ID.  
Now we can access the output file in our local machine.

