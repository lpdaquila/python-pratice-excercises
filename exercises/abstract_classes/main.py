from log import LogFileMixin, LogPrintMixin
from eletronic import Smartphone

galaxy_s = Smartphone('Galaxy S')
iphone = Smartphone('Iphone')

iphone.turn_off()
galaxy_s.turn_on()