{
    'name': 'Gestión de Impresoras 3D', # Nombre de tu aplicación
    'version': '1.0',
    'summary': 'Control de inventario de impresoras 3D',
    'author': 'Diego, Roberto, Javier, Mario', # Tu nombre
    'depends': ['base'], # Depende del núcleo de Odoo
    'data': [
        'views/impresora_graficos.xml',
        'security/ir.model.access.csv',
        'views/impresora_view.xml', # Aquí le diremos dónde está la interfaz
        'views/impresora_report.xml',
    ],
    'installable': True,
    'application': True, # Para que aparezca en el menú principal
}