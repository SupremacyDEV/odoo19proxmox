# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from urllib.parse import urlencode

class LinkSaveViewPbi(models.Model):
    _name= "link.save.view.pbi"

    name = fields.Char(string="Titulo", compute="_compute_title", store=True)
    title = fields.Char(string="Titulo")
    note = fields.Html(string="Notas")
    link = fields.Char(string="Enlace")
    iframe_html = fields.Html("Código del iFrame",sanitize=False, compute="_compute_iframe_html")
    company_id = fields.Many2one('res.company', 'Company', required=False, default=lambda self: self.env.company.id)
    dashboard_image = fields.Image("Imagén Dashboard", sanitize=False)

    user_ids = fields.Many2many('res.users', 'links_view_rel', 'links_view_id','user_id', string="Usuarios", copy=False, help="Coloque aca los usuarios que veran este registro")

    @api.depends('title')
    def _compute_title(self):
        for record in self:
            record.name = f"{record.title}" if record.title else ""

    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        if not self.env.user.has_group('view_links_save.group_views_links_admin'):
            args.append(('user_ids', 'in', [self.env.uid]))
        return super(LinkSaveViewPbi, self).search(args, offset=offset, limit=limit, order=order, count=count)
    
    @api.depends('link')
    def _compute_iframe_html(self):
        for record in self:
            if record.link:
                record.iframe_html = f"""<iframe src="{record.link}" width="100%" height="300px" frameborder="0" allowFullScreen="true"></iframe>"""
            else:
                record.iframe_html = False