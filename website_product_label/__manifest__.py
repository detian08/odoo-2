# -*- coding: utf-8 -*-
#################################################################################
# Author      : Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# Copyright(c): 2015-Present Webkul Software Pvt. Ltd.
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://store.webkul.com/license.html/>
#################################################################################
{
  "name"                 :  "Website Product Labels & Stickers",
  "summary"              :  "Add product labels to differentiate products in order to attract customers attention.",
  "category"             :  "Website",
  "version"              :  "1.0",
  "author"               :  "Webkul Software Pvt. Ltd.",
  "license"              :  "Other proprietary",
  "maintainer"           :  "Prakash Kumar",
  "website"              :  "https://store.webkul.com/Odoo-Website-Product-Labels-And-Stickers.html",
  "description"          :  """http://webkul.com/blog/odoo-website-product-labels-stickers
    Website Product Labels & Stickers For Odoo
  """,
  "live_test_url"        :  "http://odoodemo.webkul.com/?module=website_product_label&version=12.0",
  "depends"              :  [
                             'product',
                             'website_sale_management',
                            ],
  "data"                 :  [
                             'security/ir.model.access.csv',
                             'view/product_label.xml',
                             'view/website_sale_template.xml',
                             'data/data.xml',
                            ],
  "images"               :  ['static/description/Banner.png'],
  "application"          :  True,
  "installable"          :  True,
  "price"                :  29,
  "currency"             :  "EUR",
  "pre_init_hook"        :  "pre_init_check",
}
