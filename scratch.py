from magi.components.render import render_templates
from scratch.jinja.config import Config

context = Config().__dict__
render_templates('scratch/jinja/template', context, 'scratch/jinja/output')


