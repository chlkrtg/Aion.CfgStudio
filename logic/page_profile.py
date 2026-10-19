"""Страница выбора профиля.

Вся логика - в ProfilePresenter.
"""
from PyQt6.QtCore import Qt, QTimer

from logic.widgets.base_page import BasePage
from logic.widgets.context_menu import build_context_menu
from logic.widgets.shortcuts import bind_actions
from logic.widgets.shortcut_labels import with_hotkey
from logic.core.constants import MAX_PROFILE_NAME_LEN, MAX_DESCRIPTION_LEN
from logic.presenters import ProfilePresenter
from ui.profile_select import Ui_ProfileSelectDialog
from logic.core.i18n import t, t as _t


class PageProfile(BasePage, Ui_ProfileSelectDialog):

    # константы доступны презентеру через view.MAX_*self.lblTitle.setStyleSheet(
    #     "font-size: 16pt; font-weight: 700; color: #d4a95a; "
    #     "background: transparent;"
    # )
    MAX_PROFILE_NAME_LEN = MAX_PROFILE_NAME_LEN
    MAX_DESCRIPTION_LEN = MAX_DESCRIPTION_LEN

    def __init__(self, parent, service, reference):
        super().__init__(parent)
        self.setupUi(self)

        # =========== презентер ===========
        self.presenter = ProfilePresenter(self, service, reference)

        # =========== UI ===========
        self.listProfiles.setContextMenuPolicy(
            Qt.ContextMenuPolicy.CustomContextMenu
        )
        self.listProfiles.customContextMenuRequested.connect(
            self._show_context_menu
        )

        self.editDescription.setReadOnly(False)
        self.editDescription.setPlaceholderText(
            f"Сохраняется автоматически (до {MAX_DESCRIPTION_LEN} символов)..."
        )

        self._save_timer = QTimer(self)
        self._save_timer.setSingleShot(True)
        self._save_timer.setInterval(1000)
        self._save_timer.timeout.connect(self.presenter.save_description)
        self.editDescription.textChanged.connect(
            lambda: self._save_timer.start()
        )

        self._connect_signals()

        # хоткеи (см. rebind_shortcuts)
        self._shortcut_handles: dict[str, list] = {}
        self.rebind_shortcuts()
        self.retranslate()

        self.lblTitle.setStyleSheet(
            "font-size: 16pt; font-weight: 700; color: #d4a95a; "
            "background: transparent;"
        )

    # ============== сигналы ==============

    def _connect_signals(self):
        self.btnNew.clicked.connect(self.presenter.create)
        self.btnRename.clicked.connect(self.presenter.rename)
        self.btnDelete.clicked.connect(self.presenter.delete)
        self.btnEnter.clicked.connect(self.presenter.enter)

        self.listProfiles.currentItemChanged.connect(
            self.presenter.on_profile_selected
        )
        self.listProfiles.itemDoubleClicked.connect(
            lambda _: self.presenter.enter()
        )
        self.btnCancel.clicked.connect(
            lambda: self.window().close()
        )
        self.btnVideoHelp.clicked.connect(
            lambda: self.window().go_video()
        )

    def _bindings(self) -> dict:
        """Действия страницы — action_id → slot."""
        return {
            "global.video":   lambda: self.window().go_video(),
            "profile.enter":  self.presenter.enter,
            "profile.create": self.presenter.create,
            "profile.rename": self.presenter.rename,
            "profile.delete": self.presenter.delete,
            "profile.quit":   lambda: self.window().close(),
        }

    def rebind_shortcuts(self):
        """Перевешивает хоткеи с актуальными override'ами."""
        for handles in self._shortcut_handles.values():
            for sc in handles:
                sc.setEnabled(False)
                sc.deleteLater()
        self._shortcut_handles.clear()

        self._shortcut_handles = bind_actions(
            self,
            self._bindings(),
            keys=self.window().shortcut_service.keys_for_scope("profile"),
        )

    def retranslate(self):
        """Обновляет тексты страницы при смене языка / хоткеев."""
        svc = self.window().shortcut_service

        # заголовок окна
        self.setWindowTitle(t("profile.window_title"))

        # статичные label'ы
        self.lblTitle.setText(t("profile.lbl_title"))
        self.lblProfilesTitle.setText(t("profile.lbl_profiles"))
        self.lblDetailsTitle.setText(t("profile.lbl_details"))

        # кнопки с хоткеями
        self.btnNew.setText(
            with_hotkey(t("profile.btn_new"), svc, "profile.create")
        )
        self.btnRename.setText(
            with_hotkey(t("profile.btn_rename"), svc, "profile.rename")
        )
        self.btnDelete.setText(
            with_hotkey(t("profile.btn_delete"), svc, "profile.delete")
        )
        self.btnEnter.setText(
            with_hotkey(t("profile.btn_enter"), svc, "profile.enter")
        )
        self.btnVideoHelp.setText(
            with_hotkey(t("profile.btn_video"), svc, "global.video")
        )
        self.btnCancel.setText(
            with_hotkey(t("profile.btn_cancel"), svc, "profile.quit")
        )
        self.editDescription.setPlaceholderText(
            t("profile.desc_placeholder").format(n=MAX_DESCRIPTION_LEN)
        )
        self.presenter.on_profile_selected(
            self.listProfiles.currentItem(), None
        )

        # обновить плейсхолдер (если список пуст)
        if self.listProfiles.count() == 0 or (
                self.listProfiles.count() == 1
                and self.listProfiles.item(0).data(
            Qt.ItemDataRole.UserRole) is None
        ):
            self.listProfiles.clear()
            from logic.widgets.empty_state import add_empty_item
            self.listProfiles.blockSignals(True)
            add_empty_item(self.listProfiles, _t("empty.profiles"))
            self.listProfiles.setCurrentItem(None)
            self.listProfiles.blockSignals(False)

    # ============== жизненный цикл ==============

    def on_enter(self):
        self.presenter.on_enter()

    def on_leave(self) -> bool:
        if self._save_timer.isActive():
            self._save_timer.stop()
        self.presenter.on_leave()

        return True

    # ============== UI-хелперы (зовёт презентер) ==============

    def fill_details(self, profile, stats):
        """Заполняет правую панель данными профиля."""
        self.editDescription.blockSignals(True)
        self.editDescription.setPlainText(profile["description"] or "")
        self.editDescription.blockSignals(False)

        self.lblName.setText(
            t("profile.lbl_selected").format(name=profile["name"])
        )
        self.lblStats.setText(
            t("profile.stats").format(
                s=stats["servers"], c=stats["configs"]
            )
        )

        first_letter = (profile["name"] or "?")[0].upper()
        self.lblAvatar.setText(first_letter)
        self.lblAvatar.setStyleSheet(
            "font-size: 60px; color: #d4a95a; font-weight: bold;"
        )

    def clear_details(self):
        """Очищает правую панель."""
        self.lblName.setText(t("profile.lbl_none"))
        self.editDescription.blockSignals(True)
        self.editDescription.clear()
        self.editDescription.blockSignals(False)
        self.lblStats.setText(t("profile.stats").format(s=0, c=0))
        self.lblAvatar.clear()

    def set_controls_enabled(self, enabled: bool):
        """Включает/выключает контролы, требующие выбранного профиля."""
        super().set_controls_enabled(
            enabled,
            self.btnRename,
            self.btnDelete,
            self.btnEnter,
            self.editDescription,
        )

    # ============== контекстное меню ==============

    def _show_context_menu(self, pos):
        item = self.listProfiles.itemAt(pos)
        if item is None:
            return

        if item.data(Qt.ItemDataRole.UserRole) is None:
            return

        self.listProfiles.setCurrentItem(item)
        svc = self.window().shortcut_service

        menu = build_context_menu(self, [
            (with_hotkey(t("ctx.enter"), svc, "profile.enter"),
             self.presenter.enter),
            None,
            (t("ctx.duplicate"), self.presenter.duplicate),
            None,
            (with_hotkey(t("ctx.rename"), svc, "profile.rename"),
             self.presenter.rename),
            None,
            (with_hotkey(t("ctx.delete"), svc, "profile.delete"),
             self.presenter.delete),
        ])
        menu.exec(self.listProfiles.mapToGlobal(pos))

    def build_menus(self) -> dict:
        win = self.window()
        m = win.page_main
        return {
            t("menu.settings"): [
                win.actionShortcuts,
                None,
                win.actionLangRu,
                win.actionLangEn,
            ],
            t("menu.help"): [
                m.actionVideoHelp,
                m.actionAbout,
            ],
        }