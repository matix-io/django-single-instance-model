from django.dispatch import receiver
from django.db.backends.signals import connection_created
from django.db.migrations.executor import MigrationExecutor
from django.db import connections, DEFAULT_DB_ALIAS
from django.apps import apps
from .models import SingleInstanceModel


def is_database_synchronized(database):
    connection = connections[database]
    connection.prepare_database()
    executor = MigrationExecutor(connection)
    targets = executor.loader.graph.leaf_nodes()
    return False if executor.migration_plan(targets) else True


@receiver(connection_created)
def my_receiver(connection, **kwargs):
	if not is_database_synchronized(DEFAULT_DB_ALIAS):
		return
	
	with connection.cursor() as cursor:
		for key, app in apps.all_models.items():
			for k2, model in app.items():
				if issubclass(model, SingleInstanceModel):
					if not model.objects.exists():
						model.objects.create()