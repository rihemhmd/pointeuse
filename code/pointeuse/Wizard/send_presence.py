from odoo import models, fields, api

class SendPresenceWiz(models.TransientModel):
       _name = 'send.presence.wizard'
       _description = 'Send Presence'


       employees_ids = fields.Many2many('first_test.employee','send_presence_wizard_employees_rel','employee_id','my_id' , string='Employee ID', store=True, domain="[('id','in',pointeuseempl_ids)]")
       pointeuse_id = fields.Many2one('first_test.pointeuse' ,string="Pointeuse Name" )
       sennddel = fields.Boolean(string="Send Condition")
       pointeuseempl_ids = fields.Many2many('first_test.employee','send_presence_wizard_pointeuseempl_rel','employee_id','my_id', string='Pointeuse and employees', )


       def action_send(self):
              if self.sennddel == True :
                     _values=[(0,0,{
                                   'employee_id':line.employee_id.id,
                                   'my_id':line.my_id
                                   }
                            ) 
                            for line in self.employees_ids
                            ]
                     self.pointeuse_id.write({'employee_ids': _values})
          
              else : 
                     _values1 = []
                     for line in self.employees_ids:
                             _values1.append((4,line.id))
                     self.pointeuse_id.write({'employee_ids': _values1 }) 
                     
              
              
             