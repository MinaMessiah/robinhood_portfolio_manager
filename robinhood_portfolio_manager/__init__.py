################################################################################################################
# A python CLI that allows a Robinhood user to easily allocate and divide his capital on different stocks.
################################################################################################################
# Author: Mina Messiha
# Copyright: Copyright 2021, robinhood-portfolio-manager
# License: MIT License
# Version: 0.0b3
# Date: 02-25-2021
# Email: mena.sb.109@gmail.com
# URLs: pypi.org/project/robinhood-portfolio-manager &
# github.com/MinaMessiha109/robinhood_portfolio_manager
# Status: In development
################################################################################################################


import sys
import time
import argparse
from . import Robinhood


def main():
	
	kwargs = {}
	
	parser = argparse.ArgumentParser()
	parser.add_argument("-c", "--credentials", action="store", nargs=3, required=False, help="Username, password, and TOTP separated by a space", dest="creds")
	parser.add_argument("-s", "--simulation", action="store_true", required=False, help="Run simulation without placing actual orders", dest="sim")
	parser.add_argument("-g", "--generate_file", action="store", required=False, choices=["csv", "excel"], help="Generate excel/csv file", dest="generate_file")
	parser.add_argument("-n", "--get_new_investments", action="store_true", required=False, help="Get new investments", dest="get_new_investments")
	parser.add_argument("-o", "--get_current_investments", action="store_true", required=False, help="Get current investments", dest="get_current_investments")
	parser.add_argument("-p", "--sell_all_stocks", action="store_true", required=False, help="Sell all stocks", dest="sell_all_stocks")
	parser.add_argument("-r", "--rebalance", action="store_true", required=False, help="Rebalance portfolio", dest="rebalance")
	parser.add_argument("-d", "--debug", action="store_true", required=False, help="Run test function for debugging", dest="debug")
	parser.add_argument("-a", "--cancel_open_orders", action="store", choices=["all", "sell", "buy"], required=False, help="Cancel all open orders", dest="cancel_open_orders")
	
	args = parser.parse_args()

	if not any(vars(args).values()):
		parser.error("No arguments provided. Enter a valid argument or '--help' to see available arguments.")

	if args.creds:
		kwargs["username"] = args.creds[0]
		kwargs["password"] = args.creds[1]
		kwargs["totp"] = args.creds[2]

	robinhood = Robinhood.Robinhood(**kwargs)

	if args.generate_file:
		if args.generate_file == "csv":
			robinhood.generate_csv_file()
		elif args.generate_file == "excel":
			robinhood.generate_excel_file()
		else:
			parser.error("Invalid option. Choose 'csv' or 'exce'.")
		
		sys.exit()

	if args.get_new_investments:
		new_investments = robinhood.get_new_investments()
		[print(f"Will invest {percent*100:.2f}% in {instrument}") for instrument, percent in new_investments.items()]

	if args.get_current_investments:
		current_investments = robinhood.get_current_investments()

		for instrument, data in current_investments.items():
			print(f"{instrument}:")
			print(f"\tEquity:\t\t\t${data['equity']:.2f}")
			print(f"\tPercentage:\t\t{data['percentage']:.2f}%")
			print(f"\tAvailable Shares:\t{data['available_shares']:.2f}")
			print(f"\tCollateral Shares:\t{data['collateral_shares']:.2f}")

	if args.cancel_open_orders:
		robinhood.cancel_open_orders(args.cancel_open_orders, args.sim)

	if args.sell_all_stocks:
		robinhood.sell_all_stocks(args.sim)
		
		for sec in range(10, 0, -1):
			print(f"Cooling down {sec}")
			time.sleep(1)

	if args.rebalance:
		robinhood.rebalance(args.sim)
		
		for sec in range(10, 0, -1):
			print(f"Cooling down {sec}")
			time.sleep(1)

	if args.debug:
		robinhood.test()


if __name__ == '__main__':
	main()