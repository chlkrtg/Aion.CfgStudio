"""Реестр действий приложения.

Действие - это абстракция: стабильный id, человекочитаемое имя,
    область применения (scope) и клавиша по умолчанию.

Реестр НЕ знает:
  - о Qt (ни о QShortcut, ни о QKeySequence)
  - о БД (какие клавиши реально выбрал пользователь)
  - о страницах и презентерах
"""
from dataclasses import dataclass
from enum import Enum


class Scope(Enum):
    """Где действие имеет смысл.

    GLOBAL - работает на любой странице (F1, Ctrl+Q).
    Остальные - только на соответствующей странице.
    """
    GLOBAL  = "global"
    PROFILE = "profile"
    SERVER  = "server"
    MAIN    = "main"
    EDITOR  = "editor"


# ==================== Действие ====================

@dataclass(frozen=True)
class Action:
    """Описание одного действия.

    id          - стабильный ключ для БД (Shortcuts.action_id) и UI
    title       - человекочитаемое имя для редактора хоткеев
    scope       - область применения
    default_key - основная клавиша по умолчанию (fallback, не истина)
    extra_keys  - дополнительные клавиши (например, Return + Enter)
    context     - псевдоним Qt-контекста: "focused" | "with_children" | "window"
    target      - имя виджета-получателя для context="focused"
                  (bind_actions найдёт его через getattr(widget, target));
                  для context="window" игнорируется
    """
    id: str
    title: str
    scope: Scope
    default_key: str = ""
    extra_keys: tuple[str, ...] = ()
    context: str = "focused"
    target: str = ""

    def all_default_keys(self) -> tuple[str, ...]:
        """Все клавиши по умолчанию: основная + дополнительные."""
        if not self.default_key:
            return self.extra_keys
        return (self.default_key,) + self.extra_keys


# ==================== Реестр ====================

ACTIONS: dict[str, Action] = {}


def _register(*actions: Action) -> None:
    for a in actions:
        if a.id in ACTIONS:
            raise ValueError(f"Дублирующийся action_id: {a.id}")
        ACTIONS[a.id] = a


def by_scope(scope: Scope) -> list[Action]:
    """Все действия указанной области (без GLOBAL)."""
    return [a for a in ACTIONS.values() if a.scope == scope]


def for_page(scope: Scope) -> list[Action]:
    """Действия страницы + все GLOBAL. Удобно для UI редактора."""
    return [
        a for a in ACTIONS.values()
        if a.scope == scope or a.scope == Scope.GLOBAL
    ]


# ==================== Регистрация ====================

# ---------- GLOBAL ----------
# Работают на любой странице. Контекст window - не важно, где фокус.
_register(
    Action(
        id="global.video",
        title="action.global.video",
        scope=Scope.GLOBAL,
        default_key="F1",
        context="window",
    ),
)


# ---------- PROFILE ----------
_register(
    Action(
        id="profile.enter",
        title="action.profile.enter",
        scope=Scope.PROFILE,
        default_key="Return",
        extra_keys=("Enter",),
        context="focused",
        target="listProfiles",
    ),
    Action(
        id="profile.create",
        title="action.profile.create",
        scope=Scope.PROFILE,
        default_key="Ctrl+N",
        context="focused",
        target="listProfiles",
    ),
    Action(
        id="profile.rename",
        title="action.profile.rename",
        scope=Scope.PROFILE,
        default_key="F2",
        context="focused",
        target="listProfiles",
    ),
    Action(
        id="profile.delete",
        title="action.profile.delete",
        scope=Scope.PROFILE,
        default_key="Delete",
        context="focused",
        target="listProfiles",
    ),
    Action(
        id="profile.quit",
        title="action.profile.quit",
        scope=Scope.PROFILE,
        default_key="Ctrl+Q",
        context="window",
    ),
)


# ---------- SERVER ----------
_register(
    Action(
        id="server.enter",
        title="action.server.enter",
        scope=Scope.SERVER,
        default_key="Return",
        extra_keys=("Enter",),
        context="focused",
        target="listServers",
    ),
    Action(
        id="server.create",
        title="action.server.create",
        scope=Scope.SERVER,
        default_key="Ctrl+N",
        context="focused",
        target="listServers",
    ),
    Action(
        id="server.rename",
        title="action.server.rename",
        scope=Scope.SERVER,
        default_key="F2",
        context="focused",
        target="listServers",
    ),
    Action(
        id="server.delete",
        title="action.server.delete",
        scope=Scope.SERVER,
        default_key="Delete",
        context="focused",
        target="listServers",
    ),
    Action(
        id="server.quit",
        title="action.server.quit",
        scope=Scope.SERVER,
        default_key="Ctrl+Q",
        context="window",
    ),
)


# ---------- MAIN ----------
_register(
    Action(
        id="main.open",
        title="action.main.open",
        scope=Scope.MAIN,
        default_key="Ctrl+E",
        context="focused",
        target="treeConfigs",
    ),
    Action(
        id="main.create",
        title="action.main.create",
        scope=Scope.MAIN,
        default_key="Ctrl+N",
        context="focused",
        target="treeConfigs",
    ),
    Action(
        id="main.import",
        title="action.main.import",
        scope=Scope.MAIN,
        default_key="Ctrl+O",
        context="focused",
        target="treeConfigs",
    ),
    Action(
        id="main.export",
        title="action.main.export",
        scope=Scope.MAIN,
        default_key="Ctrl+S",
        context="focused",
        target="treeConfigs",
    ),
    Action(
        id="main.rename",
        title="action.main.rename",
        scope=Scope.MAIN,
        default_key="F2",
        context="focused",
        target="treeConfigs",
    ),
    Action(
        id="main.delete",
        title="action.main.delete",
        scope=Scope.MAIN,
        default_key="Delete",
        context="focused",
        target="treeConfigs",
    ),
    Action(
        id="main.save",
        title="action.main.save",
        scope=Scope.MAIN,
        default_key="",
        context="focused",
        target="treeConfigs",
    ),
    Action(
        id="main.quit",
        title="action.main.quit",
        scope=Scope.MAIN,
        default_key="Ctrl+Q",
        context="window",
    ),
    Action(
        id="main.find",
        title="action.main.find",
        scope=Scope.MAIN,
        default_key="Ctrl+F",
        context="window",
    ),
)


# ---------- EDITOR ----------
# F1 (global.video) уже покрыт в GLOBAL.
# В page_editor хоткей висел на listPrefixes -> target="listPrefixes".
# Ctrl+Q -> editor.cancel, window-контекст.
_register(
    Action(
        id="editor.cancel",
        title="action.main.cancelandquit",
        scope=Scope.EDITOR,
        default_key="Ctrl+Q",
        context="window",
    ),
)


# ---------- VIDEO (отложено, но структура есть) ----------
# Пока ничего не регистрируем: страница отключена.
# Когда вернём плеер — сюда добавятся video.play_pause, video.seek_back и т.д.