import os
PREFIX = ".posttexts/"

text_name = input()
lines = []

# Note: You must give each image a unique line
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                lines.append(line.strip())
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        exit()
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
        exit()

def wrap_line(line):
    if (len(line) > 0 and line[0] == '<'):
        return image(line)
    if (line == ""):
        return "<br>"
    return "<p class=\"paragraph\">" + line + "</p>"

def image(line):
    url = ""
    for i in range(1, len(line)-1):
        url += line[i]
    return "<img src=\"" + url + "\">"
read_file(PREFIX + text_name)

title = lines[0]
text = "<!-- " + title + " -->\n"
title_text = "<h1 class=\"titles\">" + title + "</h1>"
text += """<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Taylor Gu</title>
        <link rel="stylesheet", href="../css/default.css">
        <link rel="stylesheet", href="../css/toolbar.css">
        <link rel="stylesheet", href="../css/default.css">
    </head>

<body>
    <div class="toolbar">
        <ul>
          <li><a href="../index.html">About me</a></li>
          <li><a href="../resume.html">Resume</a></li>
          <li><a href="../projects.html">Projects</a></li>
          <li><a href="../contact.html">Contact</a></li>
          <li><a href="../blog.html">Blog</a></li>
        </ul>
    </div>

    <div class="main">
        """ + title_text + """
        <div class="info">
"""


END = """
        </div>
    </div>
</body>
</html>"""

for i in range(1, len(lines)):
    text += "           " + wrap_line(lines[i]) + '\n'

FINAL = text + END

final_path = "posts/" + title.split()[0] + ".html"

with open(final_path, 'w') as file:
    file.write(FINAL)

print(f"Long string has been written to '{final_path}'")
