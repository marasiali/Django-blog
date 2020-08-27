from django import template
from django.utils.html import format_html

register = template.Library()

################# item_menu Tag #####################
@register.simple_tag(takes_context=True)
def item_menu(context, name, icon, title, link):
    output = '<li><a href="{}" class="{}"><i class="lnr {}"></i> <span>{}</span></a></li>'
    if context.get('has_submenu'):
        active_item = context.get('active_sidebar_subitem')
    else:
        active_item = context.get('active_sidebar_item')
    print(context.get('has_submenu'))
    class_active = 'active' if active_item == name else ''
    output = output.format(link, class_active, icon, title)
    return format_html(output)


################# Submenu Tag #####################
@register.tag(name='submenu')
def submenu(parser, token):
    nodelist = parser.parse(('endsubmenu',))
    parser.delete_first_token()
    tag_name, name, icon, title = token.split_contents()
    return SubmenuNode(nodelist, name[1:-1], icon[1:-1], title[1:-1])

class SubmenuNode(template.Node):
    counter_id = 0
    def __init__(self, nodelist, name, icon, title):
        self.nodelist = nodelist
        self.name = name
        self.icon = icon
        self.title = title
        self.counter_id = SubmenuNode.counter_id
        SubmenuNode.counter_id += 1
    def render(self, context):
        active_subitem = context.get('active_sidebar_item')
        content = self.nodelist.render(context)
        a_class_active = 'active' if active_subitem == self.name else 'collapsed'
        div_class_active = 'show' if active_subitem == self.name else ''
        output = f"""<li><a href="#subPage{self.counter_id}" data-toggle="collapse" class="{a_class_active}">
                        <i class="lnr {self.icon}"></i> <span>{self.title}</span> <i class="icon-submenu lnr lnr-chevron-left"></i>
                    </a>
                    <div id="subPage{self.counter_id}" class="collapse {div_class_active}">
                        <ul class="nav">
                            {content}
                        </ul>
                    </div><li>"""
        return output