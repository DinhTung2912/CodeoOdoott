from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    project_id = fields.Many2one('project.project', string='Project')


@api.model
def create(self, vals):

    partner = super(ResPartner, self).create(vals)

    if partner.project_id:
        task = self.env['project.task'].create({
            'name': partner.name,  # Đặt tên task theo tên khách hàng
            'project_id': partner.project_id.id,
            'stage_id': partner.project_id.stage_ids and partner.project_id.stage_ids[0].id or False,

        })

    return partner
