# -*- coding: utf-8 -*-
import base64
from odoo import api, fields, models, tools

class Website(models.Model):
    _inherit = 'website'

    def _default_favicon(self):
        with tools.file_open('test_custom/static/src/img/fav.png', 'rb') as f:
            return base64.b64encode(f.read())

    favicon = fields.Binary(string="Website Favicon", help="This field holds the image used to display a favicon on the website.", default=_default_favicon)