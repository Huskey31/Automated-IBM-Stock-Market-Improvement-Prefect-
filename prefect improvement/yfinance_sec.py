"""
This script is for DEMONSTRATION PURPOSES ONLY.

It shows how a Prefect Secret block was created locally.
The value below is a placeholder and NOT a real password.
"""
from prefect .blocks.system import Secret 
my_secret_block = Secret(value="########")

my_secret_block.save(name ="yfinance-password") 
