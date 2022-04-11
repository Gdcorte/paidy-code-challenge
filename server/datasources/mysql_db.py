import logging
from os import environ
from typing import Any, Dict, List, Optional, Tuple

import mysql
from mysql.connector import MySQLConnection
from mysql.connector.cursor import MySQLCursor
from mysql.connector.errors import IntegrityError


class BaseMySqlDatasource:
    SCHEMA: str = ""
    conn: Optional[MySQLConnection] = None

    def get_credentials_from_env_file(self):
        """
        This method gets the credentials from an environment file. Note that a KeyError Exception will be raised if environment variables are not present on the format:
        - MYSQL_USER
        - MYSQL_PASSWORD
        - MYSQL_HOST
        - MYSQL_PORT
        """
        return {
            "user": environ["MYSQL_USER"],
            "password": environ["MYSQL_PASSWORD"],
            "host": environ["MYSQL_HOST"],
            "port": environ["MYSQL_PORT"],
        }

    def _connect(self) -> MySQLConnection:
        """
        Estabilished a new connection to the database and returns the instance to that connection.
        Credentials should follow the format: MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT
        enum: auth_method -> Specify how the user should login to the database, possible values are:
                - ENV_FILE -> use environment variables (MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD)
        """
        credentials = self.get_credentials_from_env_file()

        conn = mysql.connector.connect(**credentials)

        return conn

    def _prepare_connection(self):
        self.conn = self._connect()

    def get_cursor(self) -> MySQLCursor:
        if not self.conn:
            self._prepare_connection()

        cursor = self.conn.cursor(dictionary=True)

        return cursor

    def run_single_query(
        self,
        query: str,
        query_params: Tuple[Any],
    ) -> List[Dict[str, Any]]:
        cursor = self.get_cursor()

        try:
            cursor.execute(query, query_params)
            rows = cursor.fetchall()
            self._close_conn()

            return rows

        except IntegrityError as e:
            if (e.errno == 1062) and (e.sqlstate == "23000"):
                logging.exception(e)
                raise DuplicateKeyError()

            raise e

    def execute_single_statement(self, query: str, query_params: Tuple[Any]):
        cursor = self.get_cursor()

        try:
            cursor.execute(query, query_params)
            self.commit_statement()

        except IntegrityError as e:
            if (e.errno == 1062) and (e.sqlstate == "23000"):
                logging.exception(e)
                raise DuplicateKeyError()

            raise e

        except Exception as e:
            logging.exception(e)
            logging.error(cursor.statement)
            raise Exception("Error Executing DB Statement")

    def commit_statement(self):
        self.conn.commit()
        self._close_conn()

    def _close_conn(self):
        if self.conn:
            self.conn.close()
            self.conn = None


class DuplicateKeyError(Exception):
    code = 400
    description = "Duplicate Key Error"


class ResourceNotFound(Exception):
    code = 404
    description = "Resource has not been found"
