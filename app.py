from flask import Flask, render_template
import json
from jinja2 import Template

app = Flask(__name__)


@app.route('/')
def read_data():
    # Read the JSON data
    with open("data.json", "r") as json_file:
        data = json.load(json_file)
    
    # Open and read the template file
    with open("index.html", "r") as template_file:
        template_read = template_file.read()
    
    # Create a Jinja2 template object
    template = Template(template_read)
    
    # render_Sku_Template = template.render()
    # print(render_Sku_Template)
    render_Crate_Template = template.render(crate_list=data["crate_table"], sku_list=data["sku_table"])
    return render_Crate_Template


if __name__ == '__main__':
    app.run()