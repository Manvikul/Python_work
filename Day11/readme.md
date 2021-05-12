## 1. SE LINUX
## 2. SUDO POWER
## 3. HOW TO GIVE SUDO POWER
## 4. CONNECT PYTHON TO DOCKER
## 5. TO CREATE ACCOUNT IN LINUX USING PYTHON
## 6. COMMANDS USED



### SE Linux - Security Enhanced Linux

### 2 Things for python to connect to docker:
	*SE Linux should be disable
	*give sudo power


### NOTE: PYTHON NEEDS EXTRA POWER/PERMISSION TO RUN SOME COMMANDS OF O.S. USING HTTP OR CGI.
### NOTE: BY DEFAULT, ONLY "ROOT USER" HAS PERMISSION TO RUN EVERYTHING(every cmd).
 




### COMMANDS USED

* sentenforce 1: enable enforcing mode.
* sentenforce 0: enable permissive mode. '0' means disable. To disable SELinux, we use this cmd. 
* getenforce: command returns Enforcing when SELinux is enabled and returns Permissive when SELinux is disabled.
* useradd <user_name>: to create new account in linux.
* id <user_name>: to check that account exists.
	(NOTE: This cmd FAILS when run using PYTHON)

 


