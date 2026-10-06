"""Презентеры — логика UI между View и сервисами.

Презентер знает о View (для обновления) и о сервисах
(для выполнения операций). View не знает ни о чём, кроме UI.
"""
from logic.presenters.base_presenter import BasePresenter
from logic.presenters.profile_presenter import ProfilePresenter
from logic.presenters.server_presenter import ServerPresenter
from logic.presenters.main_presenter import MainPresenter
from logic.presenters.editor_presenter import EditorPresenter
from logic.presenters.video_presenter import VideoPresenter

__all__ = [
    "BasePresenter",
    "ProfilePresenter",
    "ServerPresenter",
    "MainPresenter",
    "EditorPresenter",
    "VideoPresenter",
]