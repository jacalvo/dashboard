from ConfigParser import SafeConfigParser

class ConfigurationParser:
    def __init__(self, filename):
        self.configuration = SafeConfigParser()
        self.configuration.read(filename)

    def jenkins_credentials(self):
        credentials = dict(self.configuration.items('jenkins'))

        return (credentials['url'], credentials['user'], credentials['pass'], credentials['developer_key'])

    def public_tracker_credentials(self):
        credentials = dict(self.configuration.items('public_tracker'))

        return (credentials['url'], credentials['developer_key'])

    def github_credentials(self):
        credentials = dict(self.configuration.items('github'))

        return (credentials['client_id'], credentials['client_secret'])

    def zentyal_repo_path(self):
        zentyal = dict(self.configuration.items('zentyal'))

        return zentyal['repo_path']

    def jenkins_jobs(self):
        main_configuration = dict(self.configuration.items('main'))
        jobs = main_configuration['jobs'].split()
        jobs_ids = main_configuration['jobs_ids'].split()

        return (jobs, jobs_ids)

    def jenkins_configuration_prefix(self):
        main_configuration = dict(self.configuration.items('main'))

        return main_configuration['conf_prefix']

    def jenkins_grouped_components(self):
        groups_configuration = dict(self.configuration.items('grouping'))

        return groups_configuration['key_sections'].split()

    def refresh_rate(self):
        refresh_rate = dict(self.configuration.items('configuration'))['refresh_rate']

        return int(refresh_rate) if refresh_rate else 60

    def pullrequest_job(self):
        main_configuration = dict(self.configuration.items('main'))

        return main_configuration['pullrequest_job']

    def github_repositories(self):
        github_conf = dict(self.configuration.items('github'))
        repos = github_conf['repositories'].split()

        repositories = []
        for repo in repos:
            organization, repository = repo.split('/')
            repositories.append({'organization': organization, 'repository': repository})

        return repositories

    def github_retest(self):
        github = dict(self.configuration.items('github'))

        return (github['oauth_token'], github['retest_message'])

