import os
import toml
import gspread
import discord
from datetime import datetime


def log(message: str):
    today = datetime.now()

    print(f"[{today.hour}:{today.minute}:{today.second}] {message}")


class StatisticsIngest(discord.Client):
    def __init__(self, **options):
        super().__init__(**options)
        self.config = toml.load("./config.toml")
        self.today = datetime.now()
        self.sheet = gspread \
            .service_account("./service-account.json") \
            .open_by_key(os.environ["GOOGLE_SHEET_ID"])
        self.worksheet = self.sheet.worksheet(str(self.today.year))

    """ Triggered when a connection to the Discord API is established. """
    async def on_ready(self):
        log(f"Connected to Discord as {self.user}")

        self.ingest_statistics()

        await self.close()

    """ Returns the member count of CodeSupport. """
    def get_member_count(self) -> int:
        guild_id = self.config["guild"]["id"]
        guild = self.get_guild(guild_id)

        return guild.member_count

    """ Returns the change in member count between today and yesterday. """
    def get_member_count_change(self) -> int:
        total_rows = self.worksheet.row_count

        yesterday = int(self.worksheet.cell(
            total_rows,
            self.config["columns"]["member_count"]
        ).value)

        return self.get_member_count() - yesterday

    """ Ingests the statistics by saving to Google Sheet. """
    def ingest_statistics(self):
        self.worksheet.add_rows(1)
        self.worksheet.append_row([
            f"{self.today.year}/{self.today.month}/{self.today.day}",
            self.get_member_count(),
            self.get_member_count_change()
        ])

        log("Successfully ingested statistics.")


app = StatisticsIngest()
app.run(os.environ['DISCORD_TOKEN'])
