```python
# transaction_tracking.py

from web3 import Web3
from loguru import logger

# Connect to Ethereum network (replace 'infura_url' with your actual Infura URL)
infura_url = "https://mainnet.infura.io/v3/your_project_id"
web3 = Web3(Web3.HTTPProvider(infura_url))

def track_transaction(transaction_hash):
    """Function to track the status of a transaction."""
    try:
        # Get the transaction receipt using the transaction hash
        transaction_receipt = web3.eth.getTransactionReceipt(transaction_hash)
        # Check the status of the transaction
        if transaction_receipt['status']:
            return "Transaction successful"
        else:
            return "Transaction failed"
    except Exception as e:
        logger.error(f"Error in transaction tracking: {e}")
        return None
```
