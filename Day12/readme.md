## HOW FOR LOOP WORKS
	

#HOW TO GIVE SUDO POWER
#CONNECT PYTHON TO DOCKER
#TO CREATE ACCOUNT IN LINUX USING PYTHON
#COMMANDS USED



## HOW FOR LOOP WORKS

##2 Things for python to connect to docker:
	*SE Linux should be disable
	*give sudo power


##NOTE: PYTHON NEEDS EXTRA POWER/PERMISSION TO RUN SOME COMMANDS OF O.S. USING HTTP OR CGI.
##NOTE: BY DEFAULT, ONLY "ROOT USER" HAS PERMISSION TO RUN EVERYTHING(every cmd).
##NOTE: 

Step1-> webserver should be running
Step2-> program should be executable
Step3-> use Shebang(#!)
Step4-> don't use input() func as it is only for black screen.
	to give input from html form use getvalue()
	*NOTE: getvalue() func has capability to take input from http protocol


##COMMANDS USED

* sentenforce 1: enable enforcing mode.
* sentenforce 0: enable permissive mode. '0' means disable. To disable SELinux, we use this cmd. 
* getenforce: command returns Enforcing when SELinux is enabled and returns Permissive when SELinux is disabled.
* useradd <user_name>: to create new account in linux.
* id <user_name>: to check that account exists.
	(NOTE: This cmd FAILS when run using PYTHON)
* sentenforce 1: enable enforcing mode.
 

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
