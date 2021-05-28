<h1 align="center">Welcome to Binance Spot Order Notifier via Telegram👋</h1>
<h2>Binance order notification when order created, cancelled or filled etc.. With this repo you will receive telegram notification for your binance spot order status.</h2>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/PiyushDixit96/binance-spot-order-notification/blob/main/LICENSE" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
  <a href="https://twitter.com/PiyushDixit_" target="_blank">
    <img alt="Twitter: PiyushDixit_" src="https://img.shields.io/twitter/follow/PiyushDixit_.svg?style=social" />
  </a>
</p>

> This repo sends TELEGRAM ALERTS for BINANCE ORDER STATUS like CREATED, PARTIALLY FILLED, FILLED, CANCELLED, PENDING CANCEL, REJECTED, EXPIRED etc.

<h2>Deploy to Heroku</h2>

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/PiyushDixit96/binance-spot-order-notification)


```diff
- when new commit/update happens, you need to create new heroku app using Deploy to heroku button,
- So that you can use the new feature.
```
------------
<h2>Setup before Deploy to Heroku</h2>

<h4>SETUP TELEGRAM BOT</h4>

1. Create account on Telegram (skip if you have)
2. Create Telegram Bot Goto [Bot help](https://core.telegram.org/bots#3-how-do-i-create-a-bot) follow steps at the END Copy **TOKEN**
3. Open created Bot and click **START**
4. Goto [@getuseridbot](https://t.me/getuseridbot) and click **START** and copy **NUMERIC VALUE** this is your **CHAT ID**

<h4>SETUP BINANCE ACCOUNT</h4>

1. [Signup](https://www.binance.com/en/register?ref=35219097) for Binance (skip if you have)
2. Enable Two-factor Authentication (skip if you're done already)
3. Go API Center, [Create New](https://www.binance.com/en/my/settings/api-management?ref=35219097) Api Key and follow steps and at the END, SET API restrictions to  **ENABLE READING ** only
4. **Copy API Key and Secret Key** save and Notepad for later use

<h4>DEPLOY TO HEROKU</h4>

1. Create account on Heroku (skip if you have)
2. Login to Heroku (if you are not)
3. Click [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/PiyushDixit96/binance-spot-order-notification)
5. Give any name in "App name" field
6. Fill required fields in "Config Vars"
7. Click "Deploy app"
8. When you see , "Your app was successfully deployed." then you need the start the app if your app did not started automatically.
9. Now Enjoy
------------
> <h3>Give a ⭐️ if this project helped you!</h3>
------------
### Run Locally
- Download and install python
- Download Repo and open Repo root folder.
- Create .env in root folder and copy , paste below code
 ```sh
BINANCE_API_KEY="your binance api key"
BINANCE_SECRET_KEY="your binance api secret"
TELEGRAM_TOKEN="your telegram token"
TELEGRAM_CHAT_ID="your telegram chat id"
```
- Edit required fields in .env file and save
- Open terminal on current folder 
- Run this command to install `python spot.py`

## Author

👤 **Piyush Dixit**

* Twitter: [@PiyushDixit\_](https://twitter.com/PiyushDixit_)
* Github: [@PiyushDixit96](https://github.com/PiyushDixit96)
* Telegram: [@Killer_PD](https://t.me/Killer_PD)

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2021 [@PiyushDixit96](https://github.com/PiyushDixit96).<br />
This project is [MIT](https://github.com/PiyushDixit96/binance-spot-order-notification/blob/main/LICENSE) licensed.
***
