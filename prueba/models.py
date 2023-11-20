from odoo import models, fields

class botella(models.Model):
    _name = 'samu.botella'
    _description = 'samu.botella'
    capacidad = fields.Integer()
    color = fields.Char()
    precio = fields.Float()
    vendedor = fields.Many2one(comodel_name='samu.vendedores')


class vendedores(models.Model):
    _name = 'samu.vendedores'
    _description = 'samu.vendedores'
    name = fields.Char()
    apellido = fields.Char()
    botella = fields.One2many(comodel_name='samu.botella', inverse_name='vendedor', string='Botellas Relacionadas')
