# -*- coding: utf-8 -*-
{
    'name' : "Guardar enlaces",
    'summary': "Modulo que guarda enlaces para compartir con usuarios",
    'autor': "MECA",
    "version": "16.0.1.0.0",
    'sequence': 2,
    'depends':['base','base_setup', 'web'],
    'data':[
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/link_save_view.xml',
    ],

    'assets': {
    },
    'demo':[],
    'qweb':[],
    'application':True,
    'installable':True,
    'auto_install':False,
}