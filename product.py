# This file is part product_measurements_default module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import Pool, PoolMeta
from trytond.pyson import Id

__all__ = ['ProductConfiguration', 'Template']


class ProductConfiguration:
    __metaclass__ = PoolMeta
    __name__ = 'product.configuration'
    length_uom = fields.Many2One('product.uom', 'Length Uom',
        domain=[('category', '=', Id('product', 'uom_cat_length'))])
    height_uom = fields.Many2One('product.uom', 'Height Uom',
        domain=[('category', '=', Id('product', 'uom_cat_length'))])
    width_uom = fields.Many2One('product.uom', 'Width Uom',
        domain=[('category', '=', Id('product', 'uom_cat_length'))])
    volume_uom = fields.Many2One('product.uom', 'Volume Uom',
        domain=[('category', '=', Id('product', 'uom_cat_volume'))])
    weight_uom = fields.Many2One('product.uom', 'Weight Uom',
        domain=[('category', '=', Id('product', 'uom_cat_weight'))])


class Template:
    __metaclass__ = PoolMeta
    __name__ = 'product.template'

    @classmethod
    def default_length_uom(cls):
        Config = Pool().get('product.configuration')
        config = Config(1)
        return config.length_uom.id if config.length_uom else None

    @classmethod
    def default_height_uom(cls):
        Config = Pool().get('product.configuration')
        config = Config(1)
        return config.height_uom.id if config.height_uom else None

    @classmethod
    def default_width_uom(cls):
        Config = Pool().get('product.configuration')
        config = Config(1)
        return config.width_uom.id if config.width_uom else None

    @classmethod
    def default_volume_uom(cls):
        Config = Pool().get('product.configuration')
        config = Config(1)
        return config.volume_uom.id if config.volume_uom else None

    @classmethod
    def default_weight_uom(cls):
        Config = Pool().get('product.configuration')
        config = Config(1)
        return config.weight_uom.id if config.weight_uom else None
