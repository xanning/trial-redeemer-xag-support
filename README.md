# trial-redeemer-xag-support
Selenium XGPC trial redeemer, but instead of creating accounts, uses XAG. More info in readme.

# What's the difference?
This, instead of creating accounts itself, relies on XAG (Xbox account generator) API. More info below
# Bugs?
Known ones are:

if account fetching fails because it was locked, it does not know how to try again and crashes. | Fixed in dev version, on release soon

If selecting a pregenerated username on xbox gamertag set page fails, it just waits for you to click the other one

# How can i use XAG and what's it?
XAG is basically a Microsoft account gen that you can generate and pull ready to redeem accounts from, so we don't have to solve captchas.
It's both free-to-use and you can also pay for credits. Join their discord server to get your API key (which you will use) and learn more about how you can earn credits.
https://discord.gg/AFjxMDkS3K

# How to use this new script?
This is basically same as the other one, redeeming part bugs will happen again because i didn't fix them lmao, but should have less bugs because there's no account creation
Do the things you need to do like the other repo. (requirements etc):
```
Install the requirements (requests, selenium, colorama, urllib3 etc)
Set your path to chromedriver on line 27
Put your codes in codes.txt like 1 code each line
Put your vcc's in ccs.txt in number|MM|YY|CVV format
Have the names.txt on the same folder as the script
```
At line 44 there's a variable to put your XAG api key in. Again, join their discord server to earn credits and get an api key.

# Update 5

The redeemer() function is rewritten (more like pasted from someone who sent their code, thanks @bubbb_)

If a credit card fails, it retries. Here's one bug fixed for ya.

XAG stock checking and balance checking removed for testing with api ratelimits

If any bug happen because of this update please open an issue.

Is this latest version? No, i have a dev version that has few more features but i'm gatekeeping because its horribly written and unfinished

# Flags?

Flags are in-testing features. Current ones are:

`--autoname` Automatically sets a profile name in FurinaXGP_random5letter format. You can change this on the bottom of the code.

`--fromfile` Uses outlooks from "outlooks.txt" instead of XAG fetching. Indev feature.

