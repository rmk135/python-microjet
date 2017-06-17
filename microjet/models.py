"""Models module."""

from domain_models import models
from domain_models import fields


DomainModel = models.DomainModel

BoolField = fields.Bool
IntField = fields.Int
StringField = fields.String
DateField = fields.Date
DateTimeField = fields.DateTime
ModelField = fields.Model
