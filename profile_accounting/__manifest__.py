# -*- coding: utf-8 -*-
# Copyright 2017 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{'name': 'Accounting Profile',
 'version': '0.0.1',
 'author': 'Akretion',
 'website': 'www.akretion.com',
 'license': 'AGPL-3',
 'category': 'Profile Modules',
 'description': """
    This module is a generic profile for accounting.
 """,
 'depends': [
     'profile_base',

     # https://github.com/akretion/odoo-usability
     'product_usability',
     'sale_usability',
     'account_usability',
     'account_bank_statement_import_usability',

     # https://github.com/OCA/sale-workflow
     'sale_commercial_partner',  # install v11 OK on 9 Aout 2017

     # base
     'account_accountant',

     # https://github.com/OCA/account-financial-tools
     'account_partner_required',  # install v11 OK on 9 Aout 2017
     'account_fiscal_position_vat_check',  # install v11 OK on 9 Aout 2017

     # https://github.com/OCA/account-invoicing
     'account_payment_term_extension',  # install v11 OK on 9 Aout 2017
     'account_invoice_fiscal_position_update',  # install v11 OK on 9 Aout 2017

     # https://github.com/OCA/account-financial-reporting
     'account_financial_report_qweb',
     'account_move_line_payable_receivable_filter',  # install v11 OK on 9 Aout 2017

     # https://github.com/OCA/bank-statement-import
     'account_bank_statement_import_save_file',  # install v11 OK on 9 Aout 2017
     'account_bank_statement_import_ofx',  # install v11 OK on 9 Aout 2017
     'account_bank_statement_no_reconcile_guess',

     # https://github.com/OCA/bank-payment
     'account_payment_partner', # NOT OK (depends on account_payment_mode which breaks)

     # https://github.com/akretion/account-move-import
     'account_move_csv_import',

     # https://github.com/OCA/edi
     'account_invoice_import_invoice2data',
 ],
 'data': [
 ],
 'installable': True,
 'application': True,
 }
