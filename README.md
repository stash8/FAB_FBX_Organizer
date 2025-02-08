<b> This Python script goes through the folders that FAB creates when you download a Quixel asset with multiple subfolders and combines all the FBXs into one folder. It doesn't move the textures only the FBX files. 
It should make it easier to drag and drop one group of FBX files into your program of choice. </b>


<header><h1>How to use this code:</h1></header>

<body>
<p><b>Save the code:</b> Save the code as a Python file (e.g., FAB_FBX_Organizer.py).

 <b>Windows:</b> Tkinter is usually included with the standard Python installer. If you had problems before, try reinstalling Python.

 <b>macOS:</b> Tkinter might be installed with Python, but sometimes needs to be installed separately. You can try:

brew install python-tk</p>


<b>Install Tkinter </b> (if needed): Tkinter is usually included with Python. If you get an error saying ModuleNotFoundError: No module named 'tkinter', you may need to install it separately. The installation of Tkinter depends on your operating system and Python distribution. Some common ways are:


<h2><b><strong>Quixel > Blender > Unity Work Flow</b></strong></b><h2>

An easy way to relink textures is to use Blender with the built-in node wrangler (ctr shift T) and it auto-attaches the materials. You still have to do it for each model but it’s better than manually doing it.

Import files into Unity
Save the file as a .blend
File > External Data > Pack Resources
File > External Data > Unpack Resources and choose the option to create new if needed
This puts the texture file with the .blend file
Import the .blend file into Unity and all material should be attached.
  
</body>
