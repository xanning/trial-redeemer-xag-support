
# XGP Trial Redeemer
Selenium XGPC trial redeemer, has XAG support. More info in readme.

# XAG Discontinued

![image](https://github.com/user-attachments/assets/b38588e7-6bff-4e18-8e95-809eaf62bd23)

# important

**I dont do these anymore. If i update it, it's either i just wanted to work on something on free time, or something critical is updated. If it doesn't work, open an issue (you will not get a response %80), do not DM me.**


# What's the difference with the other redeemer?
Does not have account creation.
# Bugs?
Known ones are:

If Microsoft auth gives an error (contextid didnt match cookie) etc, it just hangs.

On "Try a different way to pay" on redeeming isn't fixed.

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

If a credit card fails, it retries.

If gamertag is set already, after a 10 second timeout, it continues without trying to set gamertag

XAG stock checking and balance checking removed for testing with api ratelimits

If any bug happen because of this update please open an issue.

# Flags?

Flags are in-testing features. Current ones are:

`--autoname` Automatically sets a profile name in FurinaXGP_random5letter format. You can change this on the bottom of the code.

`--fromfile` Uses outlooks from "outlooks.txt" instead of XAG fetching.

