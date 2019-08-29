# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class bloqueo_mercancai(models.Model):
    _inherit = 'stock.move'

    def button_validates(self):
        for record in self:
            if record.move_line_ids:
                con = 0
                for line in record.move_line_ids:
                    if line.qty_done > line.product_uom_qty:
                        con =+ 1
                if con > 0:        
                    raise ValidationError('El producto no corresponde a la demanda inicial, favor de verificar.')
                else:     
                    return
class bloqueo_principal(models.Model):
    _inherit = 'stock.picking'

    def button_vali(self):
        for record in self:
            if record.move_ids_without_package:
                con = 0
                for line in record.move_ids_without_package:
                    if line.quantity_done > line.product_uom_qty:
                        con =+ 1
                if con > 0:        
                    raise ValidationError('El producto no corresponde a la demanda inicial, favor de verificar.')
                else:     
                    self.button_validate()