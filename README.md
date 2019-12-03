# Advent of Code bot with Slack integration

## How to use: ##
* Copy the bot.py file
* Update the bot.py file with own session token and Slack webhooks.

Session token can be obtained by fetching the private leaderboards JSON data
`https://adventofcode.com/2019/leaderboard/private/view/[teamID].json` 
and opening the Cookie tab from the browser's Inspect tool

Set up the cron job to run bot.py file
* ```*/15 * * * * bot.py``` to run one query every 15 minutes (recommended minimum interval)
