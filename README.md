# I am termed, and i'll be never coming back to these things.

# trial-redeemer-xag-support
Selenium XGPC trial redeemer, but instead of creating accounts, uses XAG. More info in readme.

# What's the difference?

This, instead of creating accounts itself, relies on XAG (Xbox account generator) API. More info below
# Bugs?

Known ones are, if account fetching fails because it was locked, it does not know how to try again and crashes. I dont know how to make it try again and copilot is NOT helping

# How can i use XAG and what's it?

XAG is basically a Microsoft account gen that you can generate and pull ready to redeem accounts from, so we don't have to solve captchas.

It's both free-to-use and you can also pay for credits. Join their discord server to get your API key (which you will use) and learn more about how you can earn credits.

https://discord.gg/DrvD5x4SN6 

# How to use this new script?

This is basically same as the other one, redeeming part bugs will happen again because i didn't fix them lmao, but should have less bugs because there's no account creation

Do the things you need to do like the other repo. (webhook url etc)

```
Install the requirements (requests, selenium, colorama, urllib3 etc)

Set your path to chromedriver on line 31, 33 and 34 (One should be it but i dont remember lmfao)

Put your codes in codes.txt like 1 code each line

Put your vcc's in ccs.txt in number|MM|YY|CVV format

Have the names.txt on the same folder as the script

Put your webhook on line 43
```

Under the webhook url, there's a variable to put your XAG api key in. Again, join their discord server to earn credits and get an api key.

# Downsides?

At this moment, the generated accounts are 3rd party domain, so you can **not** change the account's passwords, owner said it'll be implemented soon.

