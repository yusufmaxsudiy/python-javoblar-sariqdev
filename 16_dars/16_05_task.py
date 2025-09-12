davlatlar = {
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
govern = input("Davlat nomini kiriting:").lower()

if govern in davlatlar:
        info = davlatlar[govern]
        print(f"\n{govern.capitalize()}ning poytaxti {info['poytaxt'].title()}"
              f"\nHududi: {info['hududi']}"
              f"\nAholisi: {info['aholisi']}"
              f"\nPul birligi: {info['pul']}")
else:
        print("Bizda bu davlat haqida ma'lumot yo'q")