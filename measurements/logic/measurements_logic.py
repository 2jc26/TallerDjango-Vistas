from datetime import datetime
import re
from variables.logic.variables_logic import get_variable
from ..models import Measurement

def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(Measur_pk):
    measurement = Measurement.objects.get(pk=Measur_pk)
    return measurement

def update_measurement(Measur_pk, new_Measur):
    measurement = get_measurement(Measur_pk)
    variableVar = get_variable(new_Measur["variablepk"])
    measurement.variable = variableVar
    measurement.value = new_Measur["value"]
    measurement.unit = new_Measur["unit"]
    measurement.place = new_Measur["place"]
    dateTime = datetime.strptime(new_Measur["dateTime"], '%Y-%m-%d %H:%M:%S')
    measurement.dateTime = dateTime
    measurement.save()
    return measurement

def create_measurement(Measur):
    variableVar = get_variable(Measur["variablepk"])
    measurement = Measurement(variable=variableVar, value=Measur["value"], unit=Measur["unit"], place=Measur["place"])
    measurement.save()
    return measurement

def delete_measurement(Measur_pk):
    measurement = get_measurement(Measur_pk)
    measurement.delete()
    return measurement
