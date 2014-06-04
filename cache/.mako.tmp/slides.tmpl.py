# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1401921440.24878
_enable_loop = True
_template_filename = u'/usr/lib/python2.7/site-packages/nikola/data/themes/bootstrap3/templates/slides.tmpl'
_template_uri = u'slides.tmpl'
_source_encoding = 'ascii'
_exports = [u'content']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        len = context.get('len', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        range = context.get('range', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        carousel_id = context.get('carousel_id', UNDEFINED)
        slides_content = context.get('slides_content', UNDEFINED)
        __M_writer = context.writer()
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 24
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        len = context.get('len', UNDEFINED)
        def content():
            return render_content(context)
        range = context.get('range', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        carousel_id = context.get('carousel_id', UNDEFINED)
        slides_content = context.get('slides_content', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n<div id="')
        # SOURCE LINE 2
        __M_writer(unicode(carousel_id))
        __M_writer(u'" class="carousel slide">\n    <ol class="carousel-indicators">\n')
        # SOURCE LINE 4
        for i in range(len(slides_content)):
            # SOURCE LINE 5
            if i == 0:
                # SOURCE LINE 6
                __M_writer(u'            <li data-target="#')
                __M_writer(unicode(carousel_id))
                __M_writer(u'" data-slide-to="')
                __M_writer(unicode(i))
                __M_writer(u'" class="active"></li>\n')
                # SOURCE LINE 7
            else:
                # SOURCE LINE 8
                __M_writer(u'            <li data-target="#')
                __M_writer(unicode(carousel_id))
                __M_writer(u'" data-slide-to="')
                __M_writer(unicode(i))
                __M_writer(u'"></li>\n')
        # SOURCE LINE 11
        __M_writer(u'    </ol>\n    <div class="carousel-inner">\n')
        # SOURCE LINE 13
        for i, image in enumerate(slides_content):
            # SOURCE LINE 14
            if i == 0:
                # SOURCE LINE 15
                __M_writer(u'                <div class="item active"><img src="')
                __M_writer(unicode(image))
                __M_writer(u'" alt="" style="margin: 0 auto 0 auto;"></div>\n')
                # SOURCE LINE 16
            else:
                # SOURCE LINE 17
                __M_writer(u'                <div class="item"><img src="')
                __M_writer(unicode(image))
                __M_writer(u'" alt="" style="margin: 0 auto 0 auto;"></div>\n')
        # SOURCE LINE 20
        __M_writer(u'    </div>\n    <a class="left carousel-control" href="#')
        # SOURCE LINE 21
        __M_writer(unicode(carousel_id))
        __M_writer(u'" data-slide="prev"><span class="icon-prev"></span></a>\n    <a class="right carousel-control" href="#')
        # SOURCE LINE 22
        __M_writer(unicode(carousel_id))
        __M_writer(u'" data-slide="next"><span class="icon-next"></span></a>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


