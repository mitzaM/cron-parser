# cron-parser

### Usage

`python cron.py HH:MM < input_file`

```console
$ chmod +x cron.py
$ ./cron.py 16:10 < config
```

### Input file format
`<minute_of_day> <hour_of_day> <command_name>`

e.g.:
```console
30 1 /bin/run_me_daily
45 * /bin/run_me_hourly
* * /bin/run_me_every_minute
* 19 /bin/run_me_sixty_times
```

