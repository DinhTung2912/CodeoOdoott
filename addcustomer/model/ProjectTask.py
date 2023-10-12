from odoo import models, fields, api


class ProjectTask(models.Model):
    _inherit = 'project.task'

    stage_id = fields.Many2one('project.task.type', string='Trạng thái công đoạn')
