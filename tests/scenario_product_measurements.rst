=============================
Product Measurements Scenario
=============================

Imports::

    >>> import datetime
    >>> from dateutil.relativedelta import relativedelta
    >>> from decimal import Decimal
    >>> from operator import attrgetter
    >>> from proteus import config, Model, Wizard, Report
    >>> from trytond.modules.company.tests.tools import create_company, \
    ...     get_company
    >>> from trytond.modules.account.tests.tools import create_fiscalyear, \
    ...     create_chart, get_accounts, create_tax
    >>> from.trytond.modules.account_invoice.tests.tools import \
    ...     set_fiscalyear_invoice_sequences, create_payment_term
    >>> today = datetime.date.today()

Create database::

    >>> config = config.set_trytond()
    >>> config.pool.test = True

Install product_measurements_default::

    >>> Module = Model.get('ir.module')
    >>> sale_module, = Module.find([('name', '=', 'product_measurements_default')])
    >>> sale_module.click('install')
    >>> Wizard('ir.module.install_upgrade').execute('upgrade')

Product Configuration::

    >>> Uom = Model.get('product.uom')
    >>> Template = Model.get('product.template')
    >>> Config = Model.get('product.configuration')
    >>> length_uom, = Uom.find([('name', '=', 'Meter')])
    >>> height_uom, = Uom.find([('name', '=', 'Meter')])
    >>> width_uom, = Uom.find([('name', '=', 'Meter')])
    >>> volume_uom, = Uom.find([('name', '=', 'Liter')])
    >>> weight_uom, = Uom.find([('name', '=', 'Kilogram')])
    >>> unit, = Uom.find([('name', '=', 'Unit')])
    >>> config = Config(1)
    >>> config.length_uom = length_uom
    >>> config.height_uom = height_uom
    >>> config.width_uom = width_uom
    >>> config.volume_uom = volume_uom
    >>> config.weight_uom = weight_uom
    >>> config.save()

Create category::

    >>> ProductCategory = Model.get('product.category')
    >>> category = ProductCategory(name='Category')
    >>> category.save()

Create product::

    >>> Template = Model.get('product.template')
    >>> template = Template()
    >>> template.name = 'product'
    >>> template.category = category
    >>> template.default_uom = unit
    >>> template.type = 'goods'
    >>> template.list_price = Decimal('10')
    >>> template.cost_price = Decimal('5')
    >>> template.cost_price_method = 'fixed'
    >>> template.save()
    >>> template.length_uom == length_uom
    True
    >>> template.height_uom == height_uom
    True
    >>> template.width_uom == width_uom
    True
    >>> template.volume_uom == volume_uom
    True
    >>> template.weight_uom == weight_uom
    True
