# copyright 2016 Akretion (Alexis de Lattre <alexis.delattre@akretion.com>)
# copyright 2011 Camptocamp SA (Yannick Vaucher)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Switzerland - ISO 20022",
    "summary": "ISO 20022 base module for Switzerland",
    "version": "14.0.1.0.0",
    "category": "Finance",
    "website": "https://github.com/OCA/l10n-switzerland",
    "author": "Akretion,Camptocamp,Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "depends": ["account_banking_pain_base","l10n_ch_qriban"],
    "data": ["views/account_payment_line.xml"],
    "installable": True,
}
