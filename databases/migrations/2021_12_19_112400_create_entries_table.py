"""CreateEntriesTable Migration."""

from masoniteorm.migrations import Migration


class CreateEntriesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("entries") as table:
            table.increments("id")
            table.string("date")
            table.string("title")
            table.string("body", length= 3000)
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("entries")
