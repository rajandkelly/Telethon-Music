import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 6499615882:"AAEZ562ygXIz3hnv4t3grmCsAvOj4I_UWe0")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOGcBu0LBe5ATsRWiCAg1g-0ddz3kTnP4M7PXNXRtDR9TAYd3onhOPEHfGiRuuUOwF6oR__LCkb6knL_alr704NMnCwxc8tKICbQSxCKFaWjVJ0xxfu_l_RR7lFwn9MNfFDNS3qVFsyn42SUY0IbMN4sRiSNPETPRFPQA8Sqg2EZ6W3o2PINneg-9w2wiMtQbuK_JsfGjhqZp2bNfpI9QPsMZRCr0tT0_CYYxndIRWi3crleV53XZBZBcRlj6etAiEUxBf6HafBLLcghujAyieTdKzF4Wm_TmNASHbKAUq_EvKqOwKq5-6mKe5cnbvg4BSPBSHvIUROiFy-9yiU_D5k71LrY=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
