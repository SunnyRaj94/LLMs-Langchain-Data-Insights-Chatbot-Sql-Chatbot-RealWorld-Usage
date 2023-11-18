# ! pip install Faker
import os
import random

import pandas as pd
from config import MODELS_PATH, csv_folder
from faker import Faker

if os.path.exists(MODELS_PATH) == False:
    os.mkdir(MODELS_PATH)
if os.path.exists(csv_folder) == False:
    os.mkdir(csv_folder)
# this class helps to generate fake data
class Fake_Bank_Data():
    def __init__(self):
        self.fake = Faker()

    # Function to generate random dummy data for Customers
    def generate_customers_data(self, rows):
        cols = ["CustomerID", "FirstName", "LastName", "Email"]
        data = []
        for i in range(1, rows + 1):
            data.append(
                [i,
                 self.fake.first_name(),
                 self.fake.last_name(),
                 self.fake.email()
                ])
        return pd.DataFrame(data,columns=cols)

    # Function to generate random dummy data for Transactions
    def generate_transactions_data(self, rows):
        cols = ["TransactionID", "AccountID", "TransactionType", "Amount", "TransactionDate"]
        data = []
        for i in range(1001, 1001 + rows):
            data.append(
                [i,
                 random.randint(101, 200),
                 random.choice(["Deposit", "Withdrawal"]),
                 round(random.uniform(100, 2000), 2),
                 self.fake.date_between(start_date='-30d', end_date='today')
                ]
            )
        return pd.DataFrame(data,columns=cols)

    # Function to generate random dummy data for Accounts
    def generate_accounts_data(self, rows):
        cols = ["AccountID", "CustomerID", "AccountType", "Balance"]
        data = []
        for i in range(101, 101 + rows):
            data.append(
                [i,
                 random.randint(1, 100),
                 random.choice(["Checking", "Savings"]),
                 round(random.uniform(1000, 20000), 2)
                ]
            )
        return pd.DataFrame(data,columns=cols)

    def generate_data(self,
                      customers=20,
                      accounts=20,
                      transactions=20):
        return {'customers': self.generate_customers_data(customers),
                'accounts': self.generate_accounts_data(accounts),
                'transactions':self.generate_transactions_data(transactions)}


# bank_fake = Fake_Bank_Data()
# df_dict = bank_fake.generate_data(customers=50,accounts=100,transactions=200)

def make_folder_for_model_name(model_name):
    model_path = f"{MODELS_PATH}/{model_name}/"
    if os.path.isdir(model_path) is False:
       print('creating a new folder for this model')
       os.mkdir(model_path)
    else:
       print('folder is already present for model')
    return model_path


def split_text(text, max_length=512):
    chunks = []
    for i in range(0, len(text), max_length):
        chunks.append(text[i:i+max_length])
    return chunks