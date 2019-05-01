# -*- coding: utf-8 -*-
#################################################################################
#
#   Copyright (c) 2017-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#   See LICENSE URL <https://store.webkul.com/license.html/> for full copyright and licensing details.
#################################################################################
import logging

from odoo import fields, models, api
from odoo.exceptions import Warning
_logger = logging.getLogger(__name__)
Position =[
    ('topleft', 'Top Left'),
    ('topcenter', 'Top Center'),
    ('topright', 'Top Right'),
    ('centerleft', 'Center Left'),
    ('center','Center'),
    ('centerright', 'Center Right'),
    ('bottomleft', 'Bottom Left'),
    ('bottomcenter', 'Bottom Center'),
    ('bottomright', 'Bottom Right')
]


class product_label(models.Model):
    _name = 'product.label'

    name = fields.Char('Label Name')
    position = fields.Selection(Position, 'Position of Label')
    img = fields.Binary('Image ')
    height = fields.Char('Height(in px) ')
    width = fields.Char('Width (in px)')
    margintop = fields.Char('Margin Top(in px)')
    marginright = fields.Char('Margin Right(in px)')
    marginbottom = fields.Char('Margin Bottom(in px)')
    marginleft = fields.Char('Margin Left(in px)')


class product_template(models.Model):
    _inherit = 'product.template'
    label = fields.Many2one('product.label', 'Label')
    img = fields.Binary('Image',
                        related='label.img',
                        compute='_get_image',
                        inverse='_set_image')

    @api.multi
    def PreView(self, context=None):
        return {
            'type': 'ir.actions.act_url',
            'url': "/shop/product/%s" % (self.sudo()._ids[0]),
            'target': 'new'
        }

    def chek_css(self, args):
        return args if args != False else '0'

    def label_style(self):
        return 'height:' + self.chek_css(self.label.height) + ';width:' + self.chek_css(self.label.width) + '; margin-top:' + self.chek_css(self.label.margintop) + ';margin-right:' + self.chek_css(self.label.marginright) + ';margin-bottom:' + self.chek_css(self.label.marginbottom) + ';margin-left:' + self.chek_css(self.label.marginleft)
