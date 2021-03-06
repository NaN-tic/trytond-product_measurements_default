# This file is part product_measurements_default module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import product

def register():
    Pool.register(
        product.ProductConfiguration,
        product.Template,
        module='product_measurements_default', type_='model')
