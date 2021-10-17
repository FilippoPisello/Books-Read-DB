"""Read and store credentials from credentials.json"""
import json
from dataclasses import dataclass, field


@dataclass
class DbCredentials:
    """Store the credentials read from a json file"""

    file_path: str
    host: str = field(init=False)
    username: str = field(init=False)
    password: str = field(init=False)

    def __post_init__(self):
        self.host, self.username, self.password = self.read_credentials()

    def read_credentials(self) -> dict[str, str]:
        """Read the credentials from a json file and return the corresponding dict"""
        with open(self.file_path) as file:
            file = json.load(file)

        return file["host"], file["username"], file["password"]


CD = DbCredentials(file_path="userdata/db_credentials.json")
