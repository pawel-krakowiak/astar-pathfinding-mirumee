from datetime import date
from math import fabs

days_diff = lambda a, b: fabs((date(b[0],b[1],b[2])-date(a[0],a[1],a[2])).days)