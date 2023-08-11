![diagram](img/diagram.png)

There are two codes in this repository, one representing the server and another for the client.

## Quick usage



It is required to have installed Flask. 

First, Download the project.

```
git clone https://github.com/estevanmendes/Flask_Simple_Application.git

cd Flask_Simple_Application
```

Secondly, let's run our app using Flask. 
It is set to be ran in the http://localhost:5000/

```
flask --app server run --debug

```

Now, to try out the API generated with flask with  a  simulated client by the created code, let's run the code client.py

```
python client.py

```


Or run everything at once. However, recall that one must run the client code in another tab, since the app will be running on the one in which the "flask --app server run --debug" was submitted. 


```

git clone https://github.com/estevanmendes/Flask_Simple_Application.git

cd Flask_Simple_Application

flask --app server run --debug

```


```
python client.py

```

### Client

The client representation was built using [unittest library](https://docs.python.org/3/library/unittest.html). 
Please pay attention to the need of changing the URL of the api

It contains many tests for all the methods of the API. 


### Server

The server uses a package called [Files](Files.py) from another Python file. 

It builds up the web app using the package file that will manage the creation, remotion, edition, and loading of the files in the server. 


## Api GuideLines

Base deafult url: http://localhost:5000

Perhaps, one may need to change it, due the FLASK app being ran in another port.


### Endpoits

    /

    methods:

        GET

        It works as a guideline for the user indicating the filehandler endpoint. 

        The stadard message returned in response's body is "Welcome to the server, in order of sending a command related to file management use the endpoint /file_handler"

    /file_handler/{fileId}

    methods:

        POST

        It created the file with the fileId path parameter. 
        A file is created holding the datetime string in which was created. The same datetime string is returned in body response.

        If the fileId already exists the response's body contains the following message: The filename already exist, please delete it before creating a new.

        GET

        It returns the data inside the fileId stored in the server. 

        If the fileId does not exists in the server it is returned the following message:The filename does not exist, please create it before.

        PUT

        It edits the file changing the datetime string that is stored inside it. The new datetieme string is returned in the response's body.

        If the fileId does not exists in the server it is returned the following message:The filename does not exist, please create it before.

        DELETE

        It deletes the fileId from the server. it returns a message indicating the fileId that was erased.  the message returned follows the pattern:{fileId} deleted

        If the fileId does not exists in the server it is returned the following message:The filename does not exist, please create it before.

### Examples

Examples might be found in the postman link: https://documenter.getpostman.com/view/19669380/2s9Xy3trti


