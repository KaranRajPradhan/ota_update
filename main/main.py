from ota_update.main.ota_updater import OTAUpdater
import os


def download_and_install_update_if_available():
    os.chdir('ota_update')
    o = OTAUpdater('https://github.com/KaranRajPradhan/ota_update')
    o.using_network('Jaaga Startup WiFi', 'jaagajaaga')
    o.check_for_update_to_install_during_next_reboot()
    o.download_and_install_update_if_available('Jaaga Startup WiFi', 'jaagajaaga')


def start():
    # your custom code goes here. Something like this: ...
    # from main.x import YourProject
    # project = YourProject()
    # ...
    print("In start()")


def boot():
    download_and_install_update_if_available()
    start()


boot()
