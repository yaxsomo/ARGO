# ARGO - The autonomous drone

***
## Context 

This is a school project, we're working on a **AI-Powered drone**.

This file will be updated regularly to give the best implementation/execution possible.

Blog (FR) to see the evolution of the state of our projects : (Link to Blog/Medium)
***
## Environment installation

### Conda

***Environnment creation*** 

```bash

yaxsomo@DESKTOP-NSG7C6S:~/Workspace$ conda create -n [Environnment Name] python=[Python Version : Ex. 3.9]
yaxsomo@DESKTOP-NSG7C6S:~$ cd [Environnment Name]

```

***Environnment activation*** 

```bash

yaxsomo@DESKTOP-NSG7C6S:~/Workspace/[Environnment Name]$ conda activate [Environnment Name]
(Environnment Name) yaxsomo@DESKTOP-NSG7C6S:~/Workspace/[Environnment Name]$

```


### Original Python3 CLI

***Install venv*** : - `pip install venv`

***Environnment creation*** 

```bash

yaxsomo@DESKTOP-NSG7C6S:~/Workspace$ py -m venv [Environnment Name]
yaxsomo@DESKTOP-NSG7C6S:~$ cd [Environnment Name]

```

***Environnment activation*** - `conda activate ia-robot`

```bash

yaxsomo@DESKTOP-NSG7C6S:~/Workspace/[Environnment Name]$ Scripts\activate
([Environnment Name]) yaxsomo@DESKTOP-NSG7C6S:~Workspace/[Environnment Name]$ 


```
***

## Getting started

To clone the repo (main branch) into you Editor use the command below :

```bash

yaxsomo@DESKTOP-NSG7C6S:~$ git clone git@github.com:yaxsomo/ARGO.git

```

## Branches

We have 4 branches availables. Every one of them has a specific function :

> ***main*** : We will merge all the work done and tested to this branch

> ***test*** : We will test new functionalities on this branch

> ***hardware_motion*** : This branch will contain all the work in relation with the drone basic fly motions

> ***intelligence*** : This branch will contain all the Machine Learning/Computer Vision algo

You can also add the flag -b to get a specific branch using the form below :

```bash

yaxsomo@DESKTOP-NSG7C6S:~$ git clone -b intelligence git@github.com:yaxsomo/ARGO.git

```




- `pip3 install -r requirements.txt`


