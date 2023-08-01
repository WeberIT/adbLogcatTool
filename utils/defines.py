from PyQt5.QtGui import QColor

DEBUG = False
DEBUG_PRINT = True

# ERROR CODE
ERROR_CODE_BASE = 0
ERROR_CODE_SUCCESS = ERROR_CODE_BASE
ERROR_CODE_INVALID_PARAM = 1
ERROR_CODE_NO_DEVICE = 2
ERROR_CODE_ADB_PULL_FAILED = 3
ERROR_CODE_ADB_PULL_NOT_EXIST = 4
ERROR_CODE_ADB_PUSH_FAILED = 5
ERROR_CODE_ADB_MKDIR_FAILED = 6
ERROR_CODE_LOAD_LOG_LEVEL_SETTINGS_FAILED = 7
ERROR_CODE_EMPTY_LOG_DIR = 8
ERROR_CODE_PRODUCTION_DEVICE = 9
ERROR_CODE_REMOUNT_FAILED = 10
ERROR_CODE_DB_INSERT_FAILED = 11

ERROR_CODE_UNKNOWN = 1000

# MESSAGE TYPE
MESSAGE_TYPE_INFO = 0
MESSAGE_TYPE_WARNING = 1

MESSAGE_STR_SUCCESS = "Run successfully!"
MESSAGE_STR_SETTINGS_APPLIED = "The setting has taken effect."
MESSAGE_STR_ADB_ERROR_QUIT = "No valid adb path found. Please configure adb to the PATH environment variable first."
MESSAGE_STR_PARSER_EMPTY_INPUT = "Please enter a valid log level definition."
MESSAGE_STR_INVALID_PARAM = "Invalid input. Please check and re-enter."
MESSAGE_STR_DB_INSERT_FAILED = "Writing to the database failed."
MESSAGE_STR_SEARCH_FAILED = "No matching items were found."
MESSAGE_STR_NO_MASK = "No corresponding Mask value was found. Please try again after parsing again. \nSettings->Analysis log level settings"
MESSAGE_STR_NO_DEVICE = "No connected device found. Please connect the device first and try again."
MESSAGE_STR_ADB_PULL_FAILED = "Pull from device failed. Please check:\n 1. Whether the device is connected\n 2. The connection status of the device\n 3. Whether the device is ROOT\n 4. Whether there is a corresponding file in the device"
MESSAGE_STR_ADB_PUSH_FAILED = "Failed to push files to the device. Please check:\n 1. Whether the device is connected\n 2. Device connection status\n 3. Whether the device is ROOT\n 4. Whether there is a corresponding path in the device"
MESSAGE_STR_LOG_LEVEL_LOAD_FAILED = "Failed to import the log level settings in the device, please check:\n 1. Whether the setting file in the device is valid\n 2. Whether the parsed log level matches the log level of the device"
MESSAGE_STR_SRC_DIR_EMPTY = "Invalid path. Please check the selected path."
MESSAGE_STR_SAVE_DIR_EMPTY = "Invalid save path. Please check the save path pulled from the device."
MESSAGE_STR_MERGE_DST_EMPTY = "Invalid output path. Please check the path of log output after merging."
MESSAGE_STR_EMPTY_LOG_DIR = "Please select a directory containing androidlog.gz."
MESSAGE_STR_PRODUCTION_DEVICE = "The device is a commercial device and cannot be rooted."
MESSAGE_STR_REMOUNT_FAILED = "Remount failed."
MESSAGE_STR_NETWORK_ERROR = "Network connection failed, please try again."
MESSAGE_STR_DOWNLOAD_DONE_AND_INSTALL = "When the download is complete, close the dialog box to start the automatic installation."
MESSAGE_STR_UNKNOWN_ERROR = "unknown mistake."

WORKING_TYPE_PULL_AND_MERGE = 0
WORKING_TYPE_MERGE = 1
WORKING_TYPE_PULL_AND_SAVE = 2

WINDOWS = "windows"
MAC = "macOS"
LINUX = "linux"
SYSTEM = WINDOWS
RUNNABLE_WIN = ".exe"
RUNNABLE_MAC = ".dmg"
RUNNABLE_LINUX = ".deb"

UI_VERSION = "1.0.0.0"
MODULE_VERSION = "1.0.0.7"
DB_VERSION = 1
VERSION = "1.0.0.7"

DEVICE_INFO_ID = "deviceId"
DEVICE_INFO_NAME = "deviceName"
DEVICE_INFO_STATUS = "deviceStatus"

if not DEBUG:
    CAMX_OVERRIDE_SETTINGS_ROOT = "/vendor/etc/camera/"
    CAMX_OVERRIDE_SETTINGS = "camxoverridesettings.txt"
    ANDROID_LOGS_ROOT = "/data/log/android_logs"
else:
    CAMX_OVERRIDE_SETTINGS_ROOT = "/storage/emulated/0/test/"
    CAMX_OVERRIDE_SETTINGS = "test.txt"
    ANDROID_LOGS_ROOT = "/storage/emulated/0/test/android_logs"
CAMX_OVERRIDE_SETTINGS_PATH = CAMX_OVERRIDE_SETTINGS_ROOT + CAMX_OVERRIDE_SETTINGS

GIT_ACCOUNT = "GiddensA"
GIT_REPO = "adbLogcatTool"


TOOLS_ROOT_DIR = "adbTools"
TOOLS_DB_MANE = "adbTools.db"

LIST_SELECTED_COLOR = QColor(0, 0, 255, 100)
LIST_NORMAL_COLOR = QColor(255, 255, 255, 255)

def ErrorCodeToMessage(errorCode):
    if errorCode == ERROR_CODE_SUCCESS:
        return MESSAGE_TYPE_INFO, MESSAGE_STR_SUCCESS
    elif errorCode == ERROR_CODE_NO_DEVICE:
        return MESSAGE_TYPE_WARNING, MESSAGE_STR_NO_DEVICE
    elif errorCode == ERROR_CODE_ADB_PULL_FAILED or errorCode == ERROR_CODE_ADB_PULL_NOT_EXIST:
        return MESSAGE_TYPE_WARNING, MESSAGE_STR_ADB_PULL_FAILED
    elif errorCode == ERROR_CODE_ADB_PUSH_FAILED:
        return MESSAGE_TYPE_WARNING, MESSAGE_STR_ADB_PUSH_FAILED
    elif errorCode == ERROR_CODE_LOAD_LOG_LEVEL_SETTINGS_FAILED:
        return MESSAGE_TYPE_WARNING, MESSAGE_STR_LOG_LEVEL_LOAD_FAILED
    elif errorCode == ERROR_CODE_EMPTY_LOG_DIR:
        return MESSAGE_TYPE_WARNING, MESSAGE_STR_EMPTY_LOG_DIR
    elif errorCode == ERROR_CODE_PRODUCTION_DEVICE:
        return MESSAGE_TYPE_WARNING, MESSAGE_STR_PRODUCTION_DEVICE
    elif errorCode == ERROR_CODE_REMOUNT_FAILED:
        return MESSAGE_TYPE_WARNING, MESSAGE_STR_REMOUNT_FAILED
    else:
        return MESSAGE_TYPE_WARNING, MESSAGE_STR_UNKNOWN_ERROR
