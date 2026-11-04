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

template_layout = '''
My name is {{name}}

'''

from string import Template
a = Template('$name is the $job of the $company')
s = a.substitute(name='Arvind', job= 'CEO', company='KisansevaPlus')
print(s)


from jinja2 import Template
t = Template('Hello {{ something }}!')
print(t.render(something='world'))
t = Template('My favourite numbers: {% for n in range(1, 10) %}{{ n }} ' '{% endfor %}')
print(t.render())

Template = '''

'''