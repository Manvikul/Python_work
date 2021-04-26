#TO INTEGRATE DOCKER USING PYTHON AND API/CGI
#CONTAINER
#COMMANDS USED
#STRING INTERPOLATION
#To lauch new os without giving the code or root password of this os/with mobile or any external device


#TO INTEGRATE DOCKER USING PYTHON AND API/CGI

Docker is atool that can install, boot and login any os in the world, just in 1sec.

Min requirement to install any os  : 
* Bootable DVD/image   (in docker known as DOCKER IMAGE)
	*we can install unlimited os from one single image.

##CONTAINER

Any os that is directy installed on top of docker is known as a CONTAINER(os==container).


##COMMANDS USED

* docker images: gives all the images(dvd) you have, downloaded.
* docker ps: 'ps' stands for process status.list existing docker containers in running state. 
* docker run -d -i -t --name <os_name> <image_name>: to launch or run any os, when d= detachable(means launches the os & put it in bg), i= inside, t= terminal.
* docker stop <os_name>: to switch off the os whose name you mentioned in cmd.
 

##STRING INTERPOLATION: Concept of treating a particular part in string as variable-

![Screenshot](img/dataflow.jpeg)

{} ->Place Holder
Using this, the place of varible will be replaced by value stored in it.
This replacement is example of String Interpolation. 


##To lauch new os without giving the code or root password of this os/with mobile or any external device

Step1-> webserver should be running
Step2-> program should be executable
Step3-> use Shebang(#!)
Step4-> don't use input() func as it is only for black screen.
	to give input from html form use getvalue()
	*NOTE: getvalue() func has capability to take input from http protocol


The project is licensed under [GNU General Public License](LICENSE) 
