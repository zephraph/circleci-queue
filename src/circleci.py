import requests


class CircleCI:

	jobs_api = "https://circleci.com/api/v1.1/project/:vcs/:username/:project?filter=running"


	def __init__(self,circleci_key,build_num,user_name,project_name,repo_url):
		self.user_name = user_name
		self


	def oldest_running_build_num(self):
		return 1

	def cancel_current(self):
		return
