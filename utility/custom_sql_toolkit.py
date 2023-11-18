"""Toolkit for interacting with an SQL database."""
import sqlite3
from typing import List

import pandas as pd
from langchain.agents import AgentExecutor, create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents.agent_toolkits.base import BaseToolkit
from langchain.agents.agent_types import AgentType
from langchain.pydantic_v1 import Field
from langchain.schema.language_model import BaseLanguageModel
from langchain.sql_database import SQLDatabase
from langchain.tools import BaseTool
from langchain.tools.sql_database.tool import (
    InfoSQLDatabaseTool,
    ListSQLDatabaseTool,
    QuerySQLCheckerTool,
    QuerySQLDataBaseTool,
)
from smart_open import open
from tabulate import tabulate


def create_sqlite_db_from_csv(db_name, table_name="employee_data", data_df=None, csv_url=None):
    # Connect to the SQLite database (it will be created if it doesn't exist)
    conn = sqlite3.connect(db_name)

    if data_df is None and csv_url is not None:
        # Load CSV file into a Pandas dataframe directly from the URL
        with open(csv_url, "r") as f:
            data_df = pd.read_csv(f)
    data_df.fillna('', inplace=True)
    # Write the dataframe to the SQLite database
    data_df.to_sql(table_name, conn, if_exists="replace", index=False)

    # Commit and close connection
    conn.commit()
    conn.close()
    print(f"Database {db_name} with table {table_name} created successfully!")


def create_agent(
    db_uri,
    toolkit=None,
    verbose=True,
    temperature=0.5,
    llm=None,
    handle_parsing_errors=True
):
    db = SQLDatabase.from_uri(db_uri)
    if toolkit is None:
        toolkit = SQLDatabaseToolkit(db=db,
                                     llm=llm,
                                     sample_rows_in_table_info=1)

    return create_sql_agent(
        llm=llm,
        toolkit=toolkit,
        verbose=verbose,
        temperature=temperature,
        handle_parsing_errors=handle_parsing_errors
    )


class MySQLDatabaseToolkit(BaseToolkit):
    """Toolkit for interacting with SQL databases."""

    db: SQLDatabase = Field(exclude=True)
    llm: BaseLanguageModel = Field(exclude=True)

    @property
    def dialect(self) -> str:
        """Return string representation of SQL dialect to use."""
        return self.db.dialect

    class Config:
        """Configuration for this pydantic object."""

        arbitrary_types_allowed = True

    def get_tools(self) -> List[BaseTool]:
        """Get the tools in the toolkit."""
        list_sql_database_tool = ListSQLDatabaseTool(db=self.db)
        info_sql_database_tool_description = (
            "Input to this tool is a comma-separated list of tables, output is the "
            "schema and sample rows for those tables. "
            "Be sure that the tables actually exist by calling "
            f"{list_sql_database_tool.name} first! "
            "Example Input: 'table1, table2, table3'"
        )
        info_sql_database_tool = InfoSQLDatabaseTool(
            db=self.db, description=info_sql_database_tool_description
        )
        query_sql_database_tool_description = (
            "Input to this tool is a detailed and correct SQL query, output is a "
            "result from the database. If the query is not correct, an error message "
            "will be returned. If an error is returned, rewrite the query, check the "
            "query, and try again. If you encounter an issue with Unknown column "
            f"'xxxx' in 'field list', using {info_sql_database_tool.name} "
            "to query the correct table fields."
        )
        query_sql_database_tool = QuerySQLDataBaseTool(
            db=self.db, description=query_sql_database_tool_description
        )
        query_sql_checker_tool_description = (
            "Use this tool to double check if your query is correct before executing "
            "it. Always use this tool before executing a query with "
            f"{query_sql_database_tool.name}!"
        )
        query_sql_checker_tool = QuerySQLCheckerTool(
            db=self.db, llm=self.llm, description=query_sql_checker_tool_description
        )
        return [
            query_sql_database_tool,
            # info_sql_database_tool,
            # list_sql_database_tool,
            query_sql_checker_tool,
        ]

# Create SQLite databases from CSV datasets
# create_sqlite_db_from_csv(
#     data_df=sample_all_brands_dfm_data,
#     db_name="synthetic-sqlite.db",
#     table_name="sample_all_brands_dfm")

# db_uri = "sqlite:////content/synthetic-sqlite.db"
# handle_parsing_errors = "return final answer as string"
# db = SQLDatabase.from_uri(db_uri, sample_rows_in_table_info=1)
# toolkit = MySQLDatabaseToolkit(db=db, llm=cpp_llm)

# custom_agent = create_sql_agent(
#         llm=cpp_llm,
#         toolkit=toolkit,
#         verbose=True,
#         handle_parsing_errors=handle_parsing_errors
#     )