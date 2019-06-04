from ota_update.main.ota_updater import OTAUpdater


def download_and_install_update_if_available():
    o = OTAUpdater('https://github.com/KaranRajPradhan/ota_update/tree/master/upy_ota_update/ota_update')
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