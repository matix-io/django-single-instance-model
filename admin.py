from django.contrib import admin
from django.shortcuts import redirect
from django.urls import reverse


class SingleInstanceModelAdmin(admin.ModelAdmin):

	def has_add_permission(self, *args, **kwargs):
		return False

	def has_delete_permission(self, *args, **kwargs):
		return False

	def changelist_view(self, request, extra_context=None):
		current = request.build_absolute_uri()
		instance = self.model.objects.get()
		url = '{}{}/change/'.format(current, instance.id)
		return redirect(url)

	def response_post_save_change(self, request, obj):
		res = self._response_post_save(request, obj)
		current = request.build_absolute_uri()
		url = ('/'.join(current.split('/')[:-4])) + '/'
		return redirect(url)