from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

BATCH_MESSAGE = BATCH = """
**Need to shorten or convert links from all of your channel's posts? I've got you covered! Just make me an admin in your channel and use the following command:**

**<code>/batch [channel id or username]</code>**

**For example: <code>/batch -100xxx</code>**

**I'll handle the rest and get those links shortened or converted in a short time! 💪**
"""

USERNAME_TEXT = """**Current username: {username}**

**To set the username that will be automatically replaced with other usernames in the post, use the following command:**

`/username your_username`

**(Note: Do not include the @ symbol in your username.)**

**To remove the current username, use the following command:**

`/username remove`

**This is a helpful way to make sure that all of your posts have a consistent username. Enjoy! 📎**"""

METHOD_MESSAGE = """
Current Method: {method}
    
Methods Available:

> `mdlink` - Change all the links of the post to your MDisk account first and then short to {shortener} link.

> `shortener` - Short all the links of the post to {shortener} link directly.

> `mdisk` - Save all the links of the post to your Mdisk account.
    
To change method, choose it from the following options:
"""

METHOD_REPLY_MARKUP = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "MDLINK", callback_data="change_method#mdlink"
            ),
            InlineKeyboardButton(
                "Shortener", callback_data="change_method#shortener"
            ),
            InlineKeyboardButton("Mdisk", callback_data="change_method#mdisk"),
        ],
        [
            InlineKeyboardButton("Back", callback_data="help_command"),
            InlineKeyboardButton("Close", callback_data="delete"),
        ],
    ]
)

START_MESSAGE = '''**Hi, {}**
**I Am Urlshortx.com, Bulk Link Converter. I Can Convert Links Directly From Your urlshortx.com Account.**
**
1. Go To 👉 https://urlshortx.com/member/tools/api

2. Then Copy API Key

3. Then long press /api command then paste your API Key (see example to understand more...)**

**/api Your API Key 
(See Example.👇)
Example:** `/api de303d5270f481aec92j8h9883da7b7f9a8812ac `

**➕ Hit 👉 /header To add your custom header on this bot.To remove `/header remove`**

**💁‍♀️ Hit 👉 /api To add your api token.**

**➕ Hit 👉 /footer To add your custom footer on this bot.To remove `/footer remove`**

**➕ Hit 👉 /batch To Need to shorten or convert links from all of your channel's posts**

**➕ Hit 👉 /image To automatically replaced with other images in the post.To Remove `/image remove`**

**If You Want Any Other Shortner Link Converter Bots ™ Contact Bot Developer** 👉 **@Arisu_0007 (For Shornter Bots)**

**Message @Arisu_0007 For More Help -**
'''

HELP_MESSAGE = """**Hi, {}**
A bot to short link support bulk link conversion. I can convert links directly from your urlshortx account.
    
1. Go To 👉 https://urlshortx.com/member/tools/api
2. Then Copy API Key
3. Then long press /api command then paste your API Key (see example to understand more...)

**/api Your API Key 
(See Example.👇)
Example:** `/api de303d5270f481aec92j8h9883da7b7f9a8812ac `

**➕ Hit** 👉 /features To know more features of this bot.
**💁‍♀️ Hit** 👉 /help To get help.
**➕ Hit** 👉 /footer Adding your custom footer to bot.

**Contact Bot Developer** 👉 **@Arisu_0007 (For Shornter Bots)**
"""

ABOUT_TEXT = '''**Hey! My name is {firstname}.**

**⚡Features⚡**

• I can **Convert any** links or posts to your **urlshortx** link / post. (Button Links Posts, Hidden links/Hyperlinks All Are Supported)

• I Can **auto** add custom **footer text** to your every post. Hit 👉 /footer To know more...

• I Can **auto** add custom **Header text** to your every post. Hit 👉 /header To know more...

• I Can **Automatically Replace** Your **Banner** Image To images in the post. Hit  👉/banner_image To Know More... 

• **No** need to share **password or email** to convert links.**

 **Contact Bot Developer** 👉 **@Arisu_0007 (For Shornter Bots)**

**Click On Custom Alias To Create Custom Link**
'''

CUSTOM_ALIAS_MESSAGE = """For Custom Alias, `[link] | [custom_alias]`, **Send in this format**

**This feature works only in private mode only**

**Ex: https://t.me/PanindiaFilmZ | PanindiaFilmZ**"""


ADMINS_MESSAGE = """
List of Admins who has access to this Bot

{admin_list}
"""

ABOUT_TEXT_REPLY_MARKUP = InlineKeyboardMarkup([

    [
        InlineKeyboardButton('Custom Alias', callback_data=f'alias_conf')
        
    ],


])

HELP_MESSAGE_REPLY_MARKUP = InlineKeyboardMarkup([

    [
        InlineKeyboardButton('More Features', callback_data=f'about_command')
        
    ],


])

START_MESSAGE_REPLY_MARKUP  = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('ɢᴇᴛ ᴀᴘɪ', url=f'https://urlshortx.com/member/tools/api')
    ]
])



BACK_REPLY_MARKUP = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Back', callback_data=f'about_command')
    ],

])

USER_ABOUT_MESSAGE = """
**- Website: [{base_site}](https://urlshortx.com/member/tools/api)**

**- Site Link {base_site} Current Linked API: {shortener_api}**

**- Replace Channel Username: @{username}**

**- Header Text: **
**{header_text}**

**- Footer Text: **
{footer_text}

**- Banner Image: {banner_image}**
"""


SHORTENER_API_MESSAGE = """**To add or update your Shortner Website API,** 
`/api [Your API Token]`
            
**Ex:** `/api de303d5270f481aec928hug883da7b7f9a8812ac `

**Get API From [{base_site}](https://urlshortx.com/member/tools/api)**

**Website:** `{base_site}`

**Current API:** `{shortener_api}`"""

HEADER_MESSAGE = """**Reply to the Header Text You Want**

**This Text will be added to the top of every message caption or text**

**For adding line break use** \n
**To Remove Header Text:** `/header remove`"""

FOOTER_MESSAGE = """**Reply to the Footer Text You Want**

**This Text will be added to the bottom of every message caption or text**

**For adding line break use** \n
**To Remove Footer Text:** `/footer remove`"""

USERNAME_TEXT = """**Hi! {}, I am Urlshortx bot, bulk link converter bot From Linked Your Urlshortx Account,**

**🌟 Type** **/channel (channel link or username)**

**example:**
/channel @PanindiaFilmZ
Or
/channel PanindiaFilmZ

**🤘 Hit** 👉 /features To Know More Features Of This Bot.

**- Message @Arisu_0007 For More Help -**"""

BANNER_IMAGE = """
**Usage:** `/image image_url` **or reply to any Image with this command**

**This image will be automatically replaced with other images in the post**

**To remove custom image,** `/image remove`

**Eg:** `/image https://telegra.ph/file/5e96340a9147026556b387a.jpg`"""


BANNED_USER_TXT = """
Usage: `/ban [User ID]`

Usage: `/unban [User ID]`

List of users that are banned:

{users}
"""
