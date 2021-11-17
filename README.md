Proper documentation for the bot will be added here in the future.

Current features (as of version 0.0.7 November 17th 2021):

Required permissions for each command (listed after command name):
0 = administrator
1 = ban members
2 = kick members
3 = manage roles
4 = manage messages
not specified = none


- Bot join message
- Welcome message
- Reaction roles (hard coded to server specific, will be removed at some point, might look into adding a better system later)
- Deleted message log (specific to channel name)
- Help command
- Clear command 3
- Purge command 0 (deletes channel and creates a new one with the same name in the same category)
- Join voice channel command (not very useful right now)
- Leave voice channel command (not very useful right now)
- Bad word blocker (using customizable file badwords.txt)
- Kick command 2
- Ban command 1 ("soft ban", gives banned role and forces member to see a channel named banned, might implement temporary bans at some point)
- Unban command (for "soft ban")
- Permaban command 1 (uses the normal way of banning people from Discord servers)
- Role command 3 (adds role to user)
- Remove role command 3
- Emoji command (sends randomized emoji from a set list of emojis, not fully implemented yet)


Usage:

!help

!join

!leave

!clear number (example: !clear 10)

!purge

!kick @member reason

!ban @member reason

!unban @member

!pban @member reason

!role @member role

!rrole @member role

!emoji
