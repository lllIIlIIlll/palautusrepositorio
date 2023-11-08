class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return '\n- '.join(dependencies) if len(dependencies) > 0 else "-"
    
    def get_authors(self, list):
        return '\n- '.join(list)

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}"
            '\n'
            f"\nAuthors:\n- {self.get_authors(self.authors)}"
            '\n'
            f"\nDependencies:\n- {self._stringify_dependencies(self.dependencies)}"
            '\n'
            f"\nDevelopment dependencies:\n- {self._stringify_dependencies(self.dev_dependencies)}"
        )
