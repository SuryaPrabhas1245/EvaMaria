class Script(object):
    START_TXT = """𝙷𝙴𝙻𝙾 {},
𝙼𝚈 𝙽𝙰MfG 𝙸𝚂 <a href=https://t.me/{}>{}</a>, 𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂, 𝙹𝚄𝚂্ট 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄ָר 𝙶𝚁𝙾𝚄𝓅 𝙰𝙽𝙳 𝙴𝙽𝙹ഒ𝓎 """
    HELP_TXT = """𝙷𝙴Յ {}
𝙷𝙴ָר𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻ꦥ 𝙵ഒ 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽ଡ𝚂."""
    ABOUT_TXT = """✯ 𝙼𝚈 𝙽𝙰MfG: {}
✯ 𝙲𝚁𝙴𝙰𝚃𝙾𝑅: <a href=https://t.me/SuryaPrabhas>Surya Prabhas</a>
✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝐘: 𝙿𝚈𝚁𝙾𝚁𝙰𝙼
✯ 𝙻𝙰𝙽𝙶𝚄𝙰ꦒ𝙴: 𝙿𝚈𝚃𝙷𝙾ᚾ 𝟹
✯ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: 𝙼𝙾𝙽𝙾 𝙳𝙱
✯ 𝙱𝙾 𝚂𝙴𝚁𝚅𝙴𝑅: 𝙷𝙴𝚁𝙾𝙺𝚄
✯ 𝙱𝚄𝙸𝓁डी 𝚂𝚃𝙰𝚃𝚄𝚂: v1.0.1 [ 𝙱𝙴𝚃𝙰 ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- Movie Search Bot is a open source project. 
- Source - https://github.com/suryaprabhas1245/EvaMaria  
<b>DEV:</b>
- <a href=https://t.me/SuryaPrabhas>Surya Prabhas</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>
- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message
<b>NOTE:</b>
1. Movie Search Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.
<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>
- Movie Search Bot Supports both url and alert inline buttons.
<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format
<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/MovieFindingRoBot)</code>
<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>
<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>
- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.
<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM
<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>
<b>NOTE:</b>
these are the extra features of Eva Maria
<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>
<b>NOTE:</b>
This module only works for my admins
<b>Commands and Usage:</b>
• /
