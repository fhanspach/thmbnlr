thmbnlr
=======

Thmbnlr is a simple Flask-based microservice for getting thumbnails for an image URL.

### Installation
To run thmbnlr you can simply use:
```
python main.py
```


### Usage
To use the thmbnlr service you have to specify load the image as in the following example:
```
http://thmbnlr.your-domain.org/?url=http://upload.wikimedia.org/wikipedia/commons/b/b2/Hausziege_04.jpg&width=400&max_size=100
```

This returns an image with a maximum width of 100 px and a maximum size of 100 kByte.

The following GET-Parameters can be used to define the resulting image:

|  Parameter 	| Description  	|Default|
|---	|---	|--- |
| **url**  	| Mandatory - The url of the original image.   	|- |
| width/height  	| The target width/height of the thumbnail image.	Typically only one is specified, since thmbnlr always keeps the original aspect ratio of the image. | original width/height|
| quality  	| The degree of compression in percent. 100 is the image without quality loss	| 100|
| size  	| The maximum size of the result image in kB	| original size |
| file_format  	| The file format of the resulting image. Should be one of the formats listed in: [http://pillow.readthedocs.org/en/3.1.x/handbook/image-file-formats.html]. Note that some formats need libraries for converting. | original size |

When an image already satisfies all given requirements, thmbnlr will redirect you to the original image.

