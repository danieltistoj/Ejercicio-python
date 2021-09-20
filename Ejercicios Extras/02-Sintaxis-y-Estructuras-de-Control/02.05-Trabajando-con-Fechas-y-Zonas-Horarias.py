#####################################################################
# Trabajando con fechas - Zonas Horarias                            #
#####################################################################

from datetime import datetime, timedelta, timezone
from pytz import timezone
import pytz

#Muestra por pantalla todas las zonas horarias disponibles
print(pytz.all_timezones)

#Muestra el mismo momento en diferentes zonas horarias
print(datetime.now(pytz.timezone('Asia/Tokyo')))
print(datetime.now(pytz.timezone('Europe/Madrid')))
print(datetime.now(pytz.timezone('US/Alaska')))
print(datetime.now(pytz.timezone('UTC')))