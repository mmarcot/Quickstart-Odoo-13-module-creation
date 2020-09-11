# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Event(models.Model):
    _name = 'simple_event.event'
    _description = 'a simple event'

    name = fields.Char("Event name", required=True)
    description = fields.Text()

