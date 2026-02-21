from odoo import models, fields, api

class Impresora3D(models.Model):
    _name = 'impresion.impresora'
    _description = 'Impresora 3D'

    name = fields.Char(string='Nombre de la Máquina', required=True)
    modelo = fields.Char(string='Modelo comercial')
    
    # Campo de imagen (Para foto)
    foto = fields.Image(string="Foto", max_width=1024, max_height=1024)
    
    fecha_compra = fields.Date(string='Fecha de Compra')
    num_impresiones = fields.Integer(string='Total Impresiones', default=0)
    
    # Campo calculado y guardado en DB (store=True)
    necesita_mantenimiento = fields.Boolean(
        string='¿Requiere SAT?', 
        compute='_compute_mantenimiento',
        store=True
    )

    tecnologia = fields.Selection([
        ('fdm', 'FDM (Filamento)'),
        ('sla', 'SLA (Resina)')
    ], string='Tecnología', default='fdm')
    
    estado = fields.Selection([
        ('disponible', 'Disponible'),
        ('imprimiendo', 'Imprimiendo'),
        ('averiada', 'Averiada')
    ], string='Estado', default='disponible')

    @api.depends('num_impresiones')
    def _compute_mantenimiento(self):
        for record in self:
            if record.num_impresiones and record.num_impresiones >= 1000:
                record.necesita_mantenimiento = True
            else:
                record.necesita_mantenimiento = False