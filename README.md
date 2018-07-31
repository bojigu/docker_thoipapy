# docker_thoipapy
use the docker to run the standalone thoipapy application
1. download and install docker for your local machine from: https://docs.docker.com/install/#supported-platforms
2. run docker machine in your local computer
3. git clone https://github.com/bojigu/thoipapy_docker.git
4. in the opened terminal from step 2, cd to the directory of thoipapy_docker
5. in the command line, run 'docker build -t predict .'
6. docker run predict
7, check the container ID by run: 'docker container ls --all'
8, export the prediction output file from container to local: 'docker cp 22b60e8ac63c:/app/bnip3/THOIPA_out.csv ./output/output.csv',
where the doc