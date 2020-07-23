# FloorPlan3D Development

## Let's Get Started
- Install Python. Access the given link if you don't have Python installed in your system. https://www.python.org/downloads/
- Make sure you install pip while downloading Python
- Also, ADD TO PATH while installing Python

## Requirements
Install all the requirements of the Project using requirements.txt file
```
pip install -r requirements.txt
```

## Wall Detection
### Getting Base64 
- Take the 2D Floorplan image and convert it to Base64 from the link here. https://www.browserling.com/tools/image-to-base64
- Copy the Base64 for further use

### Using PostMan
- Open PostMan and give Post Request to the localhost http://127.0.0.1:5000/
- Click 'Body' and give your Base64 as a json as given below
```
{
"base__64":"****Your Base64 Here****"
}
```
### Points to Note
- Give the same name as 'base__64' as given above while give Post Request

## Result
Result is given as a json having all the corner co-ordinates of the wall with the detailed information
```
{"metadata": {"url": "", "dimensions": [357, 359]}, "walls": {"corners": [{"id": 2, "xy": [88, 26], "connections": [3, 18, 38, 41, 55]}]}}
```
- This json can be further used in Unity for 3D deployment.
