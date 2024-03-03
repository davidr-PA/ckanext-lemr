import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class LemrPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, "templates")
        toolkit.add_public_directory(config_, "public")
        # Could not get CSS imports working using webassets - including as /public asset instead.
        # toolkit.add_resource("assets", "lemr")
