from django import template

class AngularJS(template.Node):
  
  def __init__(self, bits):
    self.ng = bits

  def render(self, context):
    return "{{ %s }}" % " ".join(self.ng[1:])

def do_angularjs(parser, token):
  bits = token.split_contents()
  return AngularJS(bits)

register = template.Library()
register.tag('ng', do_angularjs)
