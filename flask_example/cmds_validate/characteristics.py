VERSION = 22

# validation limits
# 'msid' : (( quantile, absolute max value ))
# Note that the quantile needs to be in the set (1, 5, 16, 50, 84, 95, 99)
validation_limits = {'DP_PITCH': ((1, 7.0),
                                  (99, 7.0),
                                  (5, 0.5),
                                  (95, 0.5),),
                     'POINTING': ((1, .05),
                                  (99, .05),),
                     'ROLL': ((1, .05),
                              (99, .05),),
                     'TSCPOS': ((1, 2.0),
                                (99, 2.0),)}

# number of tolerated differences for string / discrete msids
# 'msid' : n differences before violation recorded
# this is scaled by the number of toggles or expected
# changes in the msid
validation_scale_count = {'OBSID': 2,
                          'HETG': 2,
                          'LETG': 2,
                          'PCAD_MODE': 2,
                          'DITHER': 3}

bad_times = [{'start': '2015:006:08:22:59.000',
              'stop': '2015:009:00:00:00.000'},
             {'start': '2015:012:00:30:00.000',
              'stop': '2015:013:05:26:54.011'},
             {'start': '2015:264:00:00:00.000',
              'stop': '2015:267:00:00:00.000'},
             {'start': '2016:063:12:00:00.000',
              'stop': '2016:065:06:00:00.000'},
             {'start': '2016:234:07:24:00.000',
              'stop': '2016:235:05:18:00.000'},
             {'start': '2016:324:12:59:32.000',
              'stop': '2016:326:06:00:00.000'},
             {'start': '2016:344:07:35:00.000',
              'stop': '2016:345:05:38:00.000'},
             {'start': '2017:066:00:00:00.000',
              'stop': '2017:067:08:00:00.000'},
             {'start': '2017:068:16:00:00.000',
              'stop': '2017:070:05:00:00.000'},
             {'start': '2017:090:18:00:00.000',
              'stop': '2017:092:04:00:00.000'},
             {'start': '2018:079:13:15:00.000',
              'stop': '2018:079:13:30:00.000'},
             {'start': '2018:283:13:54:00.000',
              'stop': '2018:286:12:30:00.000'},
             {'start': '2018:292:23:55:00.000',
              'stop': '2018:293:07:10:00.000'},
             {'start': '2019:248:16:00:00.000',
              'stop': '2019:249:03:00:00.000'},
             {'start': '2020:145:14:17:00.000',
              'stop': '2020:147:11:30:00.000'},
             {'start': '2020:213:02:00:00.000',
              'stop': '2020:213:11:00:00.000'},
             {'start': '2021:243:11:50:00.000',
              'stop': '2021:245:20:37:00.000'},
             ]