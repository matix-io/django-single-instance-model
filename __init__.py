from django.dispatch import receiver
from django.db.backends.signals import connection_created
from django.apps import apps
from .models import SingleInstanceModel


@receiver(connection_created)
def my_receiver(connection, **kwargs):
	with connection.cursor() as cursor:
		for key, app in apps.all_models.items():
			for k2, model in app.items():
				if issubclass(model, SingleInstanceModel):
					if not model.objects.exists():
						model.objects.create()