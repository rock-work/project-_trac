from trac.core import *
from trac.web.chrome import INavigationContributor, ITemplateProvider
from trac.web.main import IRequestHandler
from pkg_resources import resource_filename
from trac.util import escape, Markup


class hello(Component):
	implements(IRequestHandler, ITemplateProvider)
	# IRequestHandler methods
	def match_request(self, req):
		if req.path_info == '/hello':
			return True

	def process_request(self, req):
		a=3

		return 'hello_world.html', {'ass':a}, None

	def get_templates_dirs(self):
		return [resource_filename('project_hello', 'templates')]


class Hello2(Component):
	implements(IRequestHandler)

	def match_request(self,req):
		if req.path_info=='/asd':
			return True
	def process_request(self,req):
		print req.args.get('abc')

		return 'cc.html',{},None

class submitt(Component):
	implements(IRequestHandler)

	def match_request(self,req):
		if req.path_info=='/sub':
			return True
	def process_request(self,req):

		print req.args.get('te')

		return 'cc.html',{},None
