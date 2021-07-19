#!/usr/bin/env python
import sys
from datetime import time

class Cron:
  def __init__(self):
    self.current_time = self._get_time_from_args()

  def _get_time_from_args(self):
    try:
      h, m = sys.argv[1].split(':')
    except ValueError as exc:
      print("Please provide time argument in format HH:MM")
      return None
    return time(hour=int(h), minute=int(m))

  def _format_output(self, job_time, file_name):
    day = "today" if job_time >= self.current_time else "tomorrow"
    job_time = job_time.strftime("%H:%M")
    if job_time.startswith('0'):
      job_time = job_time[1:]
    return f'{job_time} {day} - {file_name}'

  def _parse_line(self, config_line):
    try:
      m, h, file_name = config_line.rstrip().split()
    except ValueError:
      print(f'Bad line found in config: {config_line.rstrip()}. Skipping.')
      return
    job_hour = self.current_time.hour if h == '*' else int(h)

    if m == '*':
      job_minute = self.current_time.minute
      if job_hour != self.current_time.hour:
        job_minute = 0
    else:
      job_minute = int(m)
      if h == '*' and job_minute < self.current_time.minute:
        job_hour = (job_hour + 1) % 24

    print(self._format_output(
      time(hour=job_hour, minute=job_minute),
      file_name
    ))

  def read_config(self):
     if self.current_time is None:
       return
     for line in sys.stdin:
       if line == '\n':
         break
       self._parse_line(line)

if __name__ == '__main__':
  cron = Cron()
  cron.read_config()

