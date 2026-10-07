
class ReferenceService:
    """Справки по профилям, серверам, cfg.

    Только чтение. Нужен презентерам, чтобы получить
    данные для отображения, не зная о репозиториях.
    """

    def __init__(self, profile_repo, server_repo, config_repo):
        self.profile_repo = profile_repo
        self.server_repo = server_repo
        self.config_repo = config_repo

    # профили
    def get_profile_name(self, profile_id: int) -> str | None:
        profile = self.profile_repo.get(profile_id)
        return profile["name"] if profile else None

    def count_servers(self, profile_id: int) -> int:
        return self.profile_repo.count_servers(profile_id)

    def count_configs_in_profile(self, profile_id: int) -> int:
        return self.profile_repo.count_configs(profile_id)

    # серверы
    def get_server_name(self, server_id: int) -> str | None:
        server = self.server_repo.get(server_id)
        return server["name"] if server else None

    def count_configs_in_server(self, server_id: int) -> int:
        return self.server_repo.count_configs(server_id)