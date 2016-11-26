from django.apps import AppConfig


class CommentFilterConfig(AppConfig):
    name = 'comment_filter'

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        import comment_filter.signals
