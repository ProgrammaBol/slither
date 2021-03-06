'''
self-sufficiency levels

0: click on variables for __init__
1: write variables on __init__
2: writ custom_update
3: write functions of prite class
4: write sprite class completely
5: wirte yaml files directly (no more ui to add stuff) (resources pane,
metadata files tabs)
6: sprite base classes removed
'''

level_0 = {
    '__init__': {
        'deloopify': False
    }
}

level_1 = {
    '__init__': {
        'deloopify': False

    },
    'custom_update': {}
}

sprites_buffers_lists = [
    level_0,
    level_1,
]

controller_level_0 = {
    'custom_update': {
        'deloopify': True
    }
}
controller_level_1 = {
    'custom_update': {
        'deloopify': True
    }
}

controller_buffers_lists = [
    controller_level_0,
    controller_level_1
]


class SelfSufficiency(object):

    def __init__(self, resources, initial_level=0):
        self.resources = resources
        self.max_level = 1
        self.level = initial_level
        self.elements = [
            ('sprite', 'controller'),
            ('sprite', 'controller'),
        ]
        self.templates = {}
        self.update_templates_elements()
        self.buffers_lists = {}
        for template_name, template_def in self.resources.templates.items():
            template = self.resources.load_resource('templates', template_name)
            element = template_def['element']
            level = template_def['level']
            self.templates[element][level] = template
        self.buffers_lists['sprite'] = sprites_buffers_lists
        self.buffers_lists['controller'] = controller_buffers_lists

    def update_templates_elements(self):
        self.templates = {}
        for element in self.elements[self.level]:
            self.templates[element] = {}

    def increase_level(self):
        if self.level < self.max_level:
            self.level += 1

    def decrease_level(self):
        if self.level != 0:
            self.level -= 1

    def set_default_level(self, level):
        self.level = level

    def get_template(self, element, level=None):
        if level is None:
            level = self.level
        return self.templates[element][level]

    def get_buffers_list(self, element, level=None):
        if level is None:
            level = self.level
        return self.buffers_lists[element][level]

    def get_elements(self, level=None):
        if level is None:
            level = self.level
        return self.elements[level]
