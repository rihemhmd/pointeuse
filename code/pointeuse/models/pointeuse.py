from odoo import models, fields, api, _

class pointeuse(models.Model):
     _name = 'first_test.pointeuse'
     _description = 'Pointeuse'

     name = fields.Char(string="Name")
     domaine = fields.Char(string="Domaine")
     année_de_conception = fields.Date(string="Year of conception")
     employee_ids = fields.One2many('first_test.employee', 'employee_soc_id',string="Employee")

     def callwiz(self):
          return {
               'type': 'ir.actions.act_window',
               'target': 'new',
               'name': _('Send Presence'),
               'view_mode': 'form',
               'res_model': 'send.presence.wizard',
               'context': {'default_pointeuseempl_ids': self.employee_ids.ids},
               }      

class Employee(models.Model):
     _name = 'first_test.employee'
     _description = 'Employee'
     _rec_name = 'employee_id'


     employee_id = fields.Many2one('hr.employee',string='Employee')
     my_id = fields.Char(string="id")
     employee_soc_id = fields.Many2one('first_test.pointeuse',string='Employee Code')
        
