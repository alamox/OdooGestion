from odoo import models, fields

class OrdenadoresRegistro(models.Model):
    _name = "ordenadores.cochesregistro"
    
    photo = fields.Binary(string='Imagen de Producto')
    nombre= fields.Text(string='Nombre PC', required=True)
    grafica = fields.Selection([
        ('2070', '2070'),
        ('2080', '2080'),
        ('3070', '3070'),
        ('4070', '4070'),
        ('4080', '4080')
    ], string='Tarjeta Gráfica')
    
    
    SSD = fields.Selection([
        ('128gb', '128gb'),
        ('256gb', '256gb'),
        ('512gb', '512gb'),
        ('1tb', '1tb'),
        ('2tb', '2tb')
    ], string='Almacenamiento SSD')
    
    RAM = fields.Selection([
        ('8gb', '8gb'),
        ('16gb', '16gb'),
        ('32gb', '32gb'),
        ('64gb', '64gb'),
        ('128gb', '128gb')  # Corregido aquí
    ], string='Memoria RAM')
    



    precio = fields.Float(string='Precio')
    ssoo = fields.Boolean(string="Sistema Operativo", default=False)
    calificaciones = fields.Text(string='Calificaciones Usuarios')
    mas_info = fields.Text(string='Más sobre el producto')
