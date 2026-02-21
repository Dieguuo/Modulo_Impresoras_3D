from odoo import models, fields

class BobinaFilamento(models.Model):
    _name = 'impresion.bobina'
    _description = 'Bobina de Filamento'

    name = fields.Char(string='Color / Identificador', required=True)
    material = fields.Selection([
        ('pla', 'PLA'),
        ('abs', 'ABS'),
        ('petg', 'PETG'),
        ('tpu', 'TPU (Flexible)')
    ], string='Tipo de Material', default='pla', required=True)
    
    peso_inicial = fields.Integer(string='Peso (gramos)', default=1000)
    
    # Esto relaciona la bobina con una impresora existente
    impresora_id = fields.Many2one('impresion.impresora', string='Impresora Asignada')