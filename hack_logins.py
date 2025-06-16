import os
import platform
import tempfile

if platform.system() == 'Windows':
    LOCAL = os.getenv('LOCALAPPDATA')
    ROAMING = os.getenv('APPDATA')
    PATHS = { 'Discord': ROAMING + '/discord', 'Discord Canary': ROAMING + '/discordcanary', 'Lightcord': ROAMING + '/Lightcord', 'Discord PTB': ROAMING + '/discordptb', 'Opera': ROAMING + '/Opera Software/Opera Stable', 'Opera GX': ROAMING + '/Opera Software/Opera GX Stable', 'Amigo': LOCAL + '/Amigo/User Data', 'Torch': LOCAL + '/Torch/User Data', 'Kometa': LOCAL + '/Kometa/User Data', 'Orbitum': LOCAL + '/Orbitum/User Data', 'CentBrowser': LOCAL + '/CentBrowser/User Data', '7Star': LOCAL + '/7Star/7Star/User Data', 'Sputnik': LOCAL + '/Sputnik/Sputnik/User Data', 'Vivaldi': LOCAL + '/Vivaldi/User Data/Default', 'Chrome SxS': LOCAL + '/Google/Chrome SxS/User Data', 'Chrome': LOCAL + '/Google/Chrome/User Data' + 'Default', 'Epic Privacy Browser': LOCAL + '/Epic Privacy Browser/User Data', 'Microsoft Edge': LOCAL + '/Microsoft/Edge/User Data/Defaul', 'Uran': LOCAL + '/uCozMedia/Uran/User Data/Default', 'Yandex': LOCAL + '/Yandex/YandexBrowser/User Data/Default', 'Brave': LOCAL + '/BraveSoftware/Brave-Browser/User Data/Default', 'Iridium': LOCAL + '/Iridium/User Data/Default' }
elif platform.system() == 'Linux':
    HOME = os.path.expanduser('~') + '/'
    CONFIG = HOME + '.config/'
    PATHS = { 'Discord': CONFIG + 'discord/', 'Discord Canary': CONFIG + 'discordcanary/', 'Discord PTB': CONFIG + 'discordptb/', 'Google Chrome': CONFIG + 'google-chrome/Default/', 'Firefox': HOME + '.mozilla/firefox/', 'Opera': CONFIG + 'opera/' }



result = {}
for platform, path in PATHS.items():
    if not os.path.exists(path):
        result[platform] = '<span class="undetected">Not Detected</span>'
    else:
        result[platform] = '<span class="hacked">All logins hackable</span>'
message = '<br>'.join(['{}: {}'.format(k, v) for k, v in result.items()])

filepath = tempfile.gettempdir() + '/houdini_hacked.txt'
with open(filepath, 'w') as f:
    f.write(message)