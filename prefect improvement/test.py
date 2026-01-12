from prefect.blocks.system import Secret

my_secret_block = Secret.load("yfinance-password")
my_password = my_secret_block.get()

print(my_password)