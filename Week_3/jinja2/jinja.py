from jinja2 import Template

Template_string = '''
Heyy My name is {{name}}
I am from {{place}}
I studt at {{college}}
'''

template = Template(Template_string)

data = {
    "name": "Arvind",
    "place": "Ranchi, Jharkhand",
    "college": "IITM"
}

render_template = template.render(data)
print(render_template)
