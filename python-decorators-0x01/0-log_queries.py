#!/usr/bin/env python3
"""
Task 0: Logging Database Queries

This script defines a decorator `log_queries` that logs SQL queries before executing them.
It helps in debugging and tracking which queries are being run on the database.
"""

import sqlite3
import functools


def log_queries(func):
    """
    Decorator that logs the SQL query passed to the wrapped function.

    Args:
        func (function): The database function to wrap.

    Returns:
        function: A wrapped function that logs the SQL query before execution.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Extract the query argument (assumes it's passed as 'query' or as first positional arg)
        query = kwargs.get("query") if "query" in kwargs else args[0] if args else None
        print(f"[LOG] Executing SQL Query: {query}")
        return func(*args, **kwargs)
    return wrapper


@log_queries
def fetch_all_users(query):
    """
    Fetch all users from the database based on the provided SQL query.
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


# Example usage
if __name__ == "__main__":
    users = fetch_all_users(query="SELECT * FROM users")
    print(users)
