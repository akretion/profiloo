# -*- coding: utf-8 -*-
# Copyright 2016 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{'name': 'Profile for managing variant',
 'version': '0.0.1',
 'author': 'Akretion',
 'website': 'www.akretion.com',
 'license': 'AGPL-3',
 'category': 'Generic Modules',
 'description': """
    This module will install basic module needed for a project with variant
 """,
 'depends': [
     'profile_base',
     'pricelist_per_product',
     'product_code_builder',
     'product_variant_usability',
     'product_variant_supplierinfo',
 ],
 'data': [
     'views/product_view.xml',
 ],
 'installable': True,
 'application': True,
 }



