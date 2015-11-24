from trac.core import *
from trac.web.chrome import INavigationContributor, ITemplateProvider
from trac.web.main import IRequestHandler
from pkg_resources import resource_filename
from trac.util import escape, Markup

# req.args.get('te')

class index(Component):
	implements(IRequestHandler, ITemplateProvider)
	# IRequestHandler methods
	def match_request(self, req):
		if req.path_info == '/reg':
			return True

	def process_request(self, req):

		return 'register.html', {}, None

	def get_templates_dirs(self):
		return [resource_filename('register', 'templates')]


class index1(Component):
	implements(IRequestHandler, ITemplateProvider)
	# IRequestHandler methods
	def match_request(self, req):
		if req.path_info == '/reg1':
			return True

	def process_request(self, req):

		name=req.args.get('neme')
		passw=req.args.get('passworld')
		email=req.args.get('email')
		print name



		return 'ok.html', {'name':name}, None

	def get_templates_dirs(self):
		return [resource_filename('register', 'templates')]
