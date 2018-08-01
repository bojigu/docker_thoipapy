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

2. run docker machine in your local computer
3. git clone https://github.com/bojigu/thoipapy_docker.git
4. in the opened terminal from step 2, cd to the directory of thoipapy_docker
5. in the command line, run 'docker build -t predict .'
6. docker run predict
7, check the container ID by run: 'docker container ls --all'
8, export the prediction output file from container to local: 'docker cp 22b60e8ac63c:/app/bnip3/THOIPA_out.csv ./output/output.csv',
where the doc
