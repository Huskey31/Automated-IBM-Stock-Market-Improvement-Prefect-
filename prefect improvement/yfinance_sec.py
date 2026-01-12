from prefect .blocks.system import Secret 
my_secret_block = Secret(value="########")
my_secret_block.save(name ="yfinance-password") 