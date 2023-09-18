<a name="readme-channels"></a>
<h1>GSpot сhannels</h1>

<!-- PROJECT LOGO -->
<!-- TABLE OF CONTENTS -->

[//]: # ()
[//]: # (<details>)

[//]: # (  <summary> <b>Navigation</b></summary>)

[//]: # (  <ol>)

[//]: # (    <li>)

[//]: # (      <a href="#about-the-service">About The service</a> )

[//]: # (    </li>)

[//]: # (    <li>)

[//]: # (      <a href="#getting-started">Getting Started</a>)

[//]: # (      <ul>)

[//]: # (        <li><a href="#installation">Installation</a></li>)

[//]: # (      </ul>)

[//]: # (    </li>)

[//]: # (    <li><a href="#usage">Usage</a></li>)

[//]: # (    <li><a href="#acknowledgments">Acknowledgments</a></li>)

[//]: # (  </ol>)

[//]: # (</details>)



<!-- ABOUT THE SERVICE -->
## About The Service

Channels is a service for interacting with a client. Our service includes two microservices. The first is the broker microservice, which listens on the broker's main channel, sends mail to the client. 
The second service is a chat, which serves to receive a websocket connection from the client and interact with it.

### Built With

* Rabbitmq 3.10
* Redis 7.0
* MongoDB 7.0
* FastAPI 0.95
* Docker 20.10
* docker-compose 2.2.1
* Python 3.11 

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.


### Installation

The first thing to do is start the databus service to listen for events. To do this, you need to enter through the terminal to the directory `backend/databus` and run the command
1. ```sh
   docker-compose up --build
   ```
2. Next you need to rename the file `env.example` to `env.dev` in the channels directory
3. Next, in the chanels directory, you need to run the command
   ```sh
   docker-compose up --build
   ```
For the first launch, be sure to build the databus service. For all subsequent launches from the channels directory, you can run the command
   ```sh
   docker-compose up
   ```


[//]: # (<!-- USAGE EXAMPLES -->)

[//]: # (## Usage)

[//]: # ()
[//]: # (In order for the client to connect to this service, you need to make a websocket connection to ...)

[//]: # ()
[//]: # (<p align="right">&#40;<a href="#readme-top">back to top</a>&#41;</p>)


<!-- ERORORS -->
## Errors
If you saw in the console  
`network rabbitmq_net declared as external, but could not be found`,  you need to repeat  <a href="#installation"> the first paragraph of the instruction </a>








