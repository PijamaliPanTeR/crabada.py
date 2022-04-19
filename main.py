import time
from sys import argv

from bin.looting.closeLoots import close_loots_run
from bin.looting.reinforceAttack import reinforce_attack_run
from bin.mining.closeMines import close_mines_run
from bin.mining.reinforceDefense import reinforce_defense_run
from bin.mining.sendTeamsMining import send_teams_mining_run
from src.common.config import users
from src.common.logger import logger
from src.helpers.general import secondOrNone, thirdOrNone, fourthOrNone


def mine_loop():
    while True:
        try:
            logger.info("Start of loop")
            for user in users:
                user_address = user['address']
                stars = '*' * int(17 + len(user_address) / 2)
                logger.info(f"{stars}Start{stars}*")
                logger.info(f"{'*' * 20}{user_address}{'*' * 20}")
                numberOfTeamsSentToMine = send_teams_mining_run(user_address)
                logger.info(f"Number of teams sent to mine: {numberOfTeamsSentToMine}")
                time.sleep(5)
                if is_mine_reinforce_on == 'true':
                    numberOfReinforcementsMade = reinforce_defense_run(user_address)
                    logger.info(f"Number of reinforcements made: {numberOfReinforcementsMade}")
                    time.sleep(5)
                numberOfMinesClaimed = close_mines_run(user_address)
                logger.info(f"Number of mines claimed: {numberOfMinesClaimed}")
                logger.info(f"{'*' * 20}{user_address}{'*' * 20}")
                logger.info(f"*{stars}End{stars}**")
                logger.info(f"Sleeping {5} sec ...")
                time.sleep(5)
            logger.info("End of loop")
            logger.info(f"Sleeping {loopSleepTime} sec ...")
            time.sleep(loopSleepTime)
        except Exception as e:
            logger.error(e)


def loot_loop():
    while True:
        try:
            logger.info("Start of loop")
            for user in users:
                user_address = user['address']
                stars = '*' * int(20 + len(user_address) / 2)
                logger.info(f"{stars}Start{stars}")
                logger.info(f"{'*' * 20}{user_address}{'*' * 20}")
                numberOfReinforcementsMade = reinforce_attack_run(user_address)
                logger.info(f"Number of reinforcements made: {numberOfReinforcementsMade}")
                time.sleep(5)
                numberOfLootsClaimed = close_loots_run(user_address)
                logger.info(f"Number of loots claimed: {numberOfLootsClaimed}")
                logger.info(f"{'*' * 20}{user_address}{'*' * 20}")
                logger.info(f"{stars}End{stars}")
                logger.info(f"Sleeping {5} sec ...")
                time.sleep(5)
            logger.info("End of loop")
            logger.info(f"Sleeping {loopSleepTime} sec ...")
            time.sleep(loopSleepTime)
        except Exception as e:
            logger.error(e)


if __name__ == '__main__':
    program = secondOrNone(argv)
    loopSleepTime = int(thirdOrNone(argv))
    is_mine_reinforce_on = fourthOrNone(argv)
    if program == "mine":
        mine_loop()
    if program == "loot":
        loot_loop()
