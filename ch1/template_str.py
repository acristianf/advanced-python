from string import Template

# This is another way to format strings in python

# import Template strings and instantiate a template obj
templ = Template("This is a template string created by ${author}")

# substitute the previous keyword with the string
s = templ.substitute(author="Cristian")
print(s);

# Use dictionary to hold values for template
data = {
    "author": "Cristian"
}
s2 = templ.substitute(data);
print(s2)
