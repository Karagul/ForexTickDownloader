import duka.app.app as duka
from duka.core.utils import TimeFrame
import datetime

symbols = ['XAUUSD']
start = datetime.date(2021, 5, 8)
end = datetime.date(2021, 5, 9)
threads = 1
timeframe = TimeFrame.TICK
folder = "."
header = True

duka(symbols, start, end, threads, timeframe, folder, header)
