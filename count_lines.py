from string import Template

filename = 'README.md'

with open(filename) as file:
  num_lines = len(file.readlines())

  with open('line_count_template.html') as templateFile:
    template = Template(templateFile.read())
    countHtml = template.substitute(filename=filename, num_lines=num_lines)

    with open('count.html', 'w') as countFile:
      countFile.write(countHtml)

