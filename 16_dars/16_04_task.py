davlarlar = {
    "o\'zbekiston":{'poytaxt':'toshkent',
                   'hududi':'448978 kv.km',
                   'aholisi':38000000,
                   'pul':"so'm"},
    'rossiya':{'poytaxt':'moskva',
                'hududi':'17098246 kv.km',
                'aholisi':144000000,
                'pul':"rubl"},
    'aqsh':{'poytaxt':'vashington',
            'hududi':'9631418 kv.km',
            'aholisi':327000000,
            'pul':"dollar"},
    'malayziya':{'poytaxt':'kuala-lumpur',
                 'hududi':'329750 kv.km',
                 'aholisi':25000000,
                 'pul':"rinngit"}
                 }

for davlat, info in davlarlar.items():
    print(f"\n{davlat.capitalize()}ning poytaxti {info['poytaxt'].title()}"
          f"\nHududi: {info['hududi']}"
          f"\nAholisi: {info['aholisi']}"
          f"\nPul birligi: {info['pul']}")