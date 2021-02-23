# Robinhood Portfolio Manager
![PyPI - Downloads](https://img.shields.io/pypi/dm/robinhood-portfolio-manager?color=blue&logo=pypi&style=plastic) ![PyPI](https://img.shields.io/pypi/v/robinhood-portfolio-manager?color=gold&label=Version&logo=pypi&logoColor=gold&style=plastic) ![Twitter Follow](https://img.shields.io/twitter/follow/minabolis9?color=%231DA1F2&label=follow&logo=twitter&style=plastic) ![GitHub followers](https://img.shields.io/github/followers/MinaMessiha109?color=white&label=follow&logo=github&style=plastic)

## Description

A python CLI  that allows a Robinhood user to easily allocate and divide his capital on different stocks.

## Disclaimer

**This tool is intended to simplify and enhance user experience. It does not in any means convey financial advice, and the author is not responsible for any loss that might incur due to it's usage. USE AT YOUR OWN RISK.**

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install robinhood-portfolio-manager.

```bash
$ pip install robinhood-portfolio-manager
```
## Getting Started
To be able to login to Robinhood, you will need to enable multi-factor authentication and use the MFA code while logging in. Refer to [this](http://www.robin-stocks.com/en/latest/quickstart.html#with-mfa-entered-programmatically-from-time-based-one-time-password-totp) section of robin-stocks.

For convenience, you can add your username, password, and MFA code as environment variables using the following names:
>ROBINHOOD_USERNAME
>ROBINHOOD_PASSWORD
>ROBINHOOD_TOTP

If you prefer to provide the credentials at runtime, you can do so using the `-c` or `--credentials` flag:
```bash
$ ropoma --credentials <username> <password> <totp>
```
*Do not confuse the MFA code with the 6 digit authentication code. __They are different.__*

---
### First run
Before you can use the script, you will need to create a watchlist in Robinhood called **Portfolio** (*case sensitive*), that will hold all the stocks you would to have as part of your portfolio.

The first time you run the script, you will need to use the `-g [option]` or `--generate_file [option]` flag. This will generate an excel file (*recommended for better styling and viewing*) or a CSV file. To generate an excel file, run:
```bash
$ ropoma --generate_file excel
```
or:
```bash
$ ropoma --generate_file csv
```
to generate a CSV file.

**Note**: *If both excel and CSV file exist, precedency will be given to the excel file.*

After generating the excel/CSV file, you will have to configure the allocation for each stock. The generated file can be found in the `Documents` directory on Windows and in the user's `home` folder on Linux/Mac.

![Example of a generated excel file](https://raw.githubusercontent.com/MinaMessiha109/robinhood_portfolio_manager/main/screenshots/excel_file.png)

![Example of a generated CSV file](https://raw.githubusercontent.com/MinaMessiha109/robinhood_portfolio_manager/main/screenshots/csv_file.png)

## Example
Let's say I would like my portfolio to consist of 4 different stocks:
> AAPL
> AMZN
> MSFT
> TSLA

I would start by creating a watchlist on Robinhood called `Portfolio` that would hold those 4 stocks.

![Robinhood Portfolio List](https://raw.githubusercontent.com/MinaMessiha109/robinhood_portfolio_manager/main/screenshots/portfolio_list.png)

I would then run:
```bash
$ ropoma --generate_file excel
```
to generate an excel file, or:
```bash
$ ropoma --generate_file csv
```
to generate a CSV file.

The generated file can be found in the `Documents` directory on Windows and in the user's `home` folder on Linux/Mac.

I would like to allocate *10%* to **AAPL**, *20%* to **AMZN**, *30%* to **MSFT**, and finally, *40%* to **TSLA**. Therefore, I would configure my excel/CSV file as follows:

![Example of an allocated excel file](https://raw.githubusercontent.com/MinaMessiha109/robinhood_portfolio_manager/main/screenshots/excel_allocated.png)

![Example of an allocated CSV file](https://raw.githubusercontent.com/MinaMessiha109/robinhood_portfolio_manager/main/screenshots/csv_allocated.png)

Finally, I would like rebalance my portfolio to match my allocations. To do so, I would run:
```bash
$ ropoma --rebalance --simulation
```
It's good practice to run the tool using the `-s` or `--simulation` flag. This allows me to check the log file and make sure that the buy/sell orders are correct. The log file will be created in the same directory as excel/CSV file, and will be named `Robinhood.log`. 

![Example of the log file](https://raw.githubusercontent.com/MinaMessiha109/robinhood_portfolio_manager/main/screenshots/log_file.png)

If the log file looks good, I would then re-run the script without the `--simulation` flag to execute the buy/sell orders.
```bash
$ ropoma --rebalance
```
For other supported functions, check the [usage](#usage) section.

## Usage

To view all available functions:
```bash
$ ropoma -h
$ ropoma --help
```
To generate excel file:
```bash
$ ropoma -g excel
$ ropoma --generate_file excel
```
To generate csv file:
```bash
$ ropoma -g csv
$ ropoma --generate_file excel
```
To get planned investments (*per the excel/CSV file*):
```bash
$ ropoma -n
$ ropoma --get_new_investments
```
To get current investments (*stocks currently held*):
```bash
$ ropoma -o
$ ropoma -get_current_investments
```
To sell all stocks currently held:
```bash
$ ropoma -p
$ ropoma --sell_all_stocks
```
To cancel all open orders:
```bash
$ ropoma -a all
$ ropoma --cancel_open_orders all
```
To cancel all open *sell* orders:
```bash
$ ropoma -a sell
$ ropoma --cancel_open_orders sell
```
To cancel all open *buy* orders:
```bash
$ ropoma -a buy
$ ropoma --cancel_open_orders buy
```
**For developers:**
To execute the `test()` function:
```bash
$ ropoma -d
$ ropoma --debug
```
*The `test` function can be overwritten to test sub-functions of the module.*

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Donations
[![Donate](https://img.shields.io/badge/Donate-PayPal-blue.svg?logo=paypal)](https://paypal.me/Mina99)
[![Donate](https://img.shields.io/badge/Donate-Crypto-gold.svg?logo=bitcoin)](https://commerce.coinbase.com/checkout/ddc1023f-ffb1-44ae-97d0-ee9c494c9869)


## License

[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/MinaMessiha109/robinhood_portfolio_manager/blob/main/LICENSE)