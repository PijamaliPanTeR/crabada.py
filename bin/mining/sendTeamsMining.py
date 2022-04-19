#!/usr/bin/env python3
"""
Crabada script to send mining all available teams for
the given user.

Usage:
    python3 -m bin.mining.sendTeamsMining <userAddress>

Author:
    @coccoinomane (Twitter)
"""

from src.bot.mining.sendTeamsMining import sendTeamsMining
from src.helpers.general import secondOrNone
from src.models.User import User
from src.common.logger import logger
from sys import argv, exit

# userAddress = secondOrNone(argv)
#
# if not userAddress:
#     logger.error("Specify a user address")
#     exit(1)
#
# nSent = sendTeamsMining(User(userAddress))


def send_teams_mining_run(user_address) -> int:
    return sendTeamsMining(User(user_address))
