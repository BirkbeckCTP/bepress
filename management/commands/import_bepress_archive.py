import csv
from django.core.management.base import BaseCommand

from journal import models as journal_models
from press.models import Press
from submission import models as sub_models

from plugins.bepress import utils

STRUCTURE_CHOICES = {"journal", "series", "events", "books"}


class Command(BaseCommand):
    """Imports a bepress archive into Janeway"""

    help = "Imports a bepress archive into Janeway"

    def add_arguments(self, parser):
        parser.add_argument('site_code')
        parser.add_argument(
            'archive_name',
            help='The name of the archive under files/plugins/bepress'
        )
        parser.add_argument('structure_type',
            choices=STRUCTURE_CHOICES,
            help="The Digital Commons structure type used in the archive",
        )
        parser.add_argument('--stamped', action="store_true", default=False)
        parser.add_argument(
            '--default-section',
            help="The ID of the section to use when one can't be found",
        )
        parser.add_argument(
            '--section-field',
            help="Custom field used for denoting the section name",
        )
        parser.add_argument(
            '--path',
            help=("Only import articles found under the given bepress path."
                " Usefull for importing a single volume or article.")
        )
        parser.add_argument(
            '--custom-fields', '-c',
            nargs=2, action="append",
            help=(
                "A key value pair of fields to map from bepress to Janeway"
                " e.g: -c location Location -c data_availability "
                " 'Data availability'"
            ),
        )
        parser.add_argument('--dry-run', action="store_true", default=False)

    def handle(self, *args, **options):
        if options["structure_type"] == "books":
            site = Press.objects.first()
            utils.import_archive(
                options["archive_name"], options["stamped"],
                site, options["structure_type"],
                import_path=options["path"],
            )
        else:
            custom_fields = {}
            if options.get("custom_fields"):
                custom_fields = dict(options["custom_fields"])
            site = journal_models.Journal.objects.get(code=options["site_code"])
            section = None
            if options.get("default_section"):
                section = sub_models.Section.objects.get(
                    id=options["default_section"],
                    journal=site,
                )
            utils.import_archive(
                options["archive_name"], options["stamped"], site,
                options["structure_type"], section, options["section_field"],
                import_path=options["path"],
                custom_fields=custom_fields,
            )
