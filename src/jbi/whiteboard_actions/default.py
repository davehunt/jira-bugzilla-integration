# Default actions below
# from src.jbi import services


def init(whiteboard_tag, jira_project_key, **kwargs):
    return DefaultExecutor(
        whiteboard_tag=whiteboard_tag, jira_project_key=jira_project_key, **kwargs
    )


class DefaultExecutor:
    def __init__(self, **kwargs):
        self.whiteboard_tag = kwargs.get("whiteboard_tag")
        self.jira_project_key = kwargs.get("jira_project_key")

    def __call__(self, payload, parameters):
        # Called from BZ webhook
        # Call Jira SDK with project key etc.
        print(payload)
        print(parameters)
