# Simple Image Web Server
This a simple REST API Image Web Server

you send an Image and response is JSON format that contain of the image's size.
### API
`localhost:8000/ GET POST`

###Request Format
send direct file with correct **content-type** e.g.

    curl -X POST -d @image.giflocalhost:8000 -H "Content-Type:image/gif"

###Response Format
    {
        "format" : ...(string),
        "width": ...(integer -> pixel),
        "heigth: ...(integer -> pixel),
        "doc": pixel
    }

####Step #1
please download or clone this project in your directory `git clone`

####Step #2
python version `3.7+`

please create a python environment by type `python -m venv venv` in your cloned project or directory

####Step #3
please active your environment `/venv/Script/activate`

    in Linux user : `source .\venv\bin\activate`

then must in your console (left side) look-like `(venv)...`

####Step #4
please install python requirements packages `pip isntall -r requirements.txt`

####Step #5
to run this web-service just type `python main.py`

###Test
first run app then `pytest test`