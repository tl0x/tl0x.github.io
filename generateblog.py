# I'm not sure the correct way to set up a blog is so this is my next best thing\
# Steal idrc
import os

PREFIX = "posts/"
START = """
<!DOCTYPE html>

<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Taylor Gu</title>
        <link rel="stylesheet", href="css/default.css">
        <link rel="stylesheet", href="css/toolbar.css">
        <link rel="stylesheet", href="css/default.css">
    </head>

<body>
    <div class="toolbar">
        <ul>
          <li><a href="index.html">About me</a></li>
          <li><a href="resume.html">Resume</a></li>
          <li><a href="projects.html">Projects</a></li>
          <li><a href="contact.html">Contact</a></li>
          <li><a href="blog.html">Blog</a></li>
        </ul>
    </div>

    <div class="main">
        <h1 class="titles">Blog</h1>
        <div class="info">
            <ul>"""

END = """           </ul>
        </div>
    </div>
</body>
</html>"""


def strip_title(title):
    temp = ""
    for c in title:
        if (c != "<" and c != "-" and c != ">" and c != "\n"):
            temp += c

    lst = temp.split(" ")
    new = ""
    for i in range(len(lst)):
        if (i != 0 and lst[i] != " "):
            new += lst[i] + " "

    return new.rstrip()

posts = []
def add(folder_path):
    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' does not exist.")
        return
    
    for root, dirs, files in os.walk(folder_path):
        title = ""
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as t:
                title = t.readline()
            posts.append([file, strip_title(title)])

add(PREFIX)

for file_name, title in posts:
    START += "\n                <li><a href=\"" + PREFIX + file_name + "\"><p class=\"paragraph\">" + title + "</p></a></li>"

START += "\n"
FINAL = START + END

final_path = "blog.html" # Write to blog.html

with open(final_path, 'w') as file:
    file.write(FINAL)

print(f"Long string has been written to '{final_path}'")
