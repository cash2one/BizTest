# Imports the monkeyrunner modules used by this program
# --------------------------
# terminal command:
# monkeyrunner D:\HanLeiDOC\HanLeiDOC\Python\SeleniumTest\monkeyrunner\testmonkey.py
# --------------------------
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice


class LandingPage:
    TOUCH_TYPE = "DOWN_AND_UP"

    def __init__(self, device):
        self.device = device

    def tap_to_enter(self):
        self.device.touch(500, 700, self.TOUCH_TYPE)

# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()

# Installs the Android package. Notice that this method returns a boolean, so you can test
# to see if the installation worked.
# device.installPackage('D:/nuomi.apk')
type = "DOWN_AND_UP"
# sets a variable with the package's internal name
package = 'com.nuomi'

# sets a variable with the name of an Activity in the package
activity = 'com.baidu.bainuo.dex.InstallDexActivity'

# sets the name of the component to start
runComponent = package + '/' + activity

# Runs the component
device.startActivity(component=runComponent)

LandingPage.tap_to_enter(device)
# device.touch(500, 700, type)

# Takes a screenshot
result = device.takeSnapshot()

# Writes the screenshot to a file
result.writeToFile('C:/users/hanlei08/desktop/shot1.png','png')

