-- Aion.CfgStudio — переводы описаний команд и префиксов
-- Автогенерация: scripts/generate_seed.py

-- ==================== PrefixTranslations ====================
INSERT OR IGNORE INTO PrefixTranslations (prefix_id, lang, name, description) SELECT id, 'ru', 'Общий игровой параметр', 'Общий игровой параметр' FROM Prefixes WHERE code='g_';
INSERT OR IGNORE INTO PrefixTranslations (prefix_id, lang, name, description) SELECT id, 'en', 'General gameplay', 'General gameplay setting' FROM Prefixes WHERE code='g_';
INSERT OR IGNORE INTO PrefixTranslations (prefix_id, lang, name, description) SELECT id, 'ru', 'Параметр рендеринга', 'Параметр рендеринга' FROM Prefixes WHERE code='r_';
INSERT OR IGNORE INTO PrefixTranslations (prefix_id, lang, name, description) SELECT id, 'en', 'Render / graphics', 'Render setting' FROM Prefixes WHERE code='r_';
INSERT OR IGNORE INTO PrefixTranslations (prefix_id, lang, name, description) SELECT id, 'ru', 'Параметр движка / мира', 'Параметр движка / мира' FROM Prefixes WHERE code='e_';
INSERT OR IGNORE INTO PrefixTranslations (prefix_id, lang, name, description) SELECT id, 'en', 'Engine / world', 'Engine / world setting' FROM Prefixes WHERE code='e_';
INSERT OR IGNORE INTO PrefixTranslations (prefix_id, lang, name, description) SELECT id, 'ru', 'Параметр физики', 'Параметр физики' FROM Prefixes WHERE code='p_';
INSERT OR IGNORE INTO PrefixTranslations (prefix_id, lang, name, description) SELECT id, 'en', 'Physics', 'Physics setting' FROM Prefixes WHERE code='p_';
INSERT OR IGNORE INTO PrefixTranslations (prefix_id, lang, name, description) SELECT id, 'ru', 'Параметр сущностей', 'Параметр сущностей' FROM Prefixes WHERE code='es_';
INSERT OR IGNORE INTO PrefixTranslations (prefix_id, lang, name, description) SELECT id, 'en', 'Entity system', 'Entity system setting' FROM Prefixes WHERE code='es_';
INSERT OR IGNORE INTO PrefixTranslations (prefix_id, lang, name, description) SELECT id, 'ru', 'Параметр персонажа / анимации', 'Параметр персонажа / анимации' FROM Prefixes WHERE code='ca_';
INSERT OR IGNORE INTO PrefixTranslations (prefix_id, lang, name, description) SELECT id, 'en', 'Character / animation', 'Character / animation setting' FROM Prefixes WHERE code='ca_';
INSERT OR IGNORE INTO PrefixTranslations (prefix_id, lang, name, description) SELECT id, 'ru', 'Параметр консоли', 'Параметр консоли' FROM Prefixes WHERE code='con_';
INSERT OR IGNORE INTO PrefixTranslations (prefix_id, lang, name, description) SELECT id, 'en', 'Console', 'Console setting' FROM Prefixes WHERE code='con_';
INSERT OR IGNORE INTO PrefixTranslations (prefix_id, lang, name, description) SELECT id, 'ru', 'Отладочная визуализация', 'Отладочная визуализация' FROM Prefixes WHERE code='CV_';
INSERT OR IGNORE INTO PrefixTranslations (prefix_id, lang, name, description) SELECT id, 'en', 'Debug visualization', 'Debug visualization setting' FROM Prefixes WHERE code='CV_';
INSERT OR IGNORE INTO PrefixTranslations (prefix_id, lang, name, description) SELECT id, 'ru', 'Параметр DirectX 9', 'Параметр DirectX 9' FROM Prefixes WHERE code='d3d9_';
INSERT OR IGNORE INTO PrefixTranslations (prefix_id, lang, name, description) SELECT id, 'en', 'DirectX 9', 'DirectX 9 setting' FROM Prefixes WHERE code='d3d9_';
INSERT OR IGNORE INTO PrefixTranslations (prefix_id, lang, name, description) SELECT id, 'ru', 'Параметр звука', 'Параметр звука' FROM Prefixes WHERE code='s_';
INSERT OR IGNORE INTO PrefixTranslations (prefix_id, lang, name, description) SELECT id, 'en', 'Sound', 'Sound setting' FROM Prefixes WHERE code='s_';
INSERT OR IGNORE INTO PrefixTranslations (prefix_id, lang, name, description) SELECT id, 'ru', 'Системный параметр', 'Системный параметр' FROM Prefixes WHERE code='sys_';
INSERT OR IGNORE INTO PrefixTranslations (prefix_id, lang, name, description) SELECT id, 'en', 'System', 'System setting' FROM Prefixes WHERE code='sys_';
INSERT OR IGNORE INTO PrefixTranslations (prefix_id, lang, name, description) SELECT id, 'ru', 'Параметр ввода', 'Параметр ввода' FROM Prefixes WHERE code='i_';
INSERT OR IGNORE INTO PrefixTranslations (prefix_id, lang, name, description) SELECT id, 'en', 'Input', 'Input setting' FROM Prefixes WHERE code='i_';
INSERT OR IGNORE INTO PrefixTranslations (prefix_id, lang, name, description) SELECT id, 'ru', 'Параметр логирования', 'Параметр логирования' FROM Prefixes WHERE code='log_';
INSERT OR IGNORE INTO PrefixTranslations (prefix_id, lang, name, description) SELECT id, 'en', 'Logging', 'Logging setting' FROM Prefixes WHERE code='log_';
INSERT OR IGNORE INTO PrefixTranslations (prefix_id, lang, name, description) SELECT id, 'ru', 'Параметр видео / катсцен', 'Параметр видео / катсцен' FROM Prefixes WHERE code='mov_';
INSERT OR IGNORE INTO PrefixTranslations (prefix_id, lang, name, description) SELECT id, 'en', 'Movies', 'Movies setting' FROM Prefixes WHERE code='mov_';
INSERT OR IGNORE INTO PrefixTranslations (prefix_id, lang, name, description) SELECT id, 'ru', 'Параметр профилирования', 'Параметр профилирования' FROM Prefixes WHERE code='profile';
INSERT OR IGNORE INTO PrefixTranslations (prefix_id, lang, name, description) SELECT id, 'en', 'Profiling', 'Profiling setting' FROM Prefixes WHERE code='profile';
INSERT OR IGNORE INTO PrefixTranslations (prefix_id, lang, name, description) SELECT id, 'ru', 'Параметр памяти', 'Параметр памяти' FROM Prefixes WHERE code='Mem';
INSERT OR IGNORE INTO PrefixTranslations (prefix_id, lang, name, description) SELECT id, 'en', 'Memory', 'Memory setting' FROM Prefixes WHERE code='Mem';
INSERT OR IGNORE INTO PrefixTranslations (prefix_id, lang, name, description) SELECT id, 'ru', 'Прочий параметр', 'Прочий параметр' FROM Prefixes WHERE code='misc';
INSERT OR IGNORE INTO PrefixTranslations (prefix_id, lang, name, description) SELECT id, 'en', 'Miscellaneous', 'Miscellaneous setting' FROM Prefixes WHERE code='misc';

-- ==================== CommandTranslations ====================
INSERT OR IGNORE INTO CommandTranslations (command_id, lang, description)
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_2dDamage'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_2dDamageCri'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_2dDamageCriT2'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_2dDamageMargin'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_2dDamageOffset'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_2dDamageR'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_2dDamageSize'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_2dDamageSize2'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_2dDamageT1'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_2dDamageT2'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_2dDamageT3'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_2dDamageT4'
UNION ALL
SELECT id, 'ru', 'Камера в бою' FROM Commands WHERE key_name='g_battleCamActive'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_battleCamRadius'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_battleCamSmallR'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_battleCamWeight'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_battleCamWeightNear'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_cam_key_rot'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_cam_p_max'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_cam_p_min'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_cam_rot_ratio'
UNION ALL
SELECT id, 'ru', 'Чит-режим камеры' FROM Commands WHERE key_name='g_camera_cheat'
UNION ALL
SELECT id, 'ru', 'Максимальная дистанция камеры' FROM Commands WHERE key_name='g_camMax'
UNION ALL
SELECT id, 'ru', 'Средняя дистанция камеры' FROM Commands WHERE key_name='g_camMid'
UNION ALL
SELECT id, 'ru', 'Минимальная дистанция камеры' FROM Commands WHERE key_name='g_camMin'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_camOffsetZ'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_camStep'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_captureIME'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_cfg_version'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_cfg_video_BACKGROUND'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_cfg_video_ENTITY_DIST'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_cfg_video_ENV_TEX'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_cfg_video_FSAA'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_cfg_video_GENERAL'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_cfg_video_GLARE'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_cfg_video_GLOW'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_cfg_video_MODEL_CACHE'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_cfg_video_screen_res'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_cfg_video_SHADER'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_cfg_video_SHADOW'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_cfg_video_SKILLFX'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_cfg_video_TERRAIN_DIST'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_cfg_video_TEXTURE'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_cfg_video_WATER'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_cfg_video_WEATHER'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_chainSkillChangeCooltimeDelay'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_chainSkillIndicateDelay'
UNION ALL
SELECT id, 'ru', 'Управление персонажем' FROM Commands WHERE key_name='g_char_manager'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_charCustomColor'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_CharRotateSpeed';
INSERT OR IGNORE INTO CommandTranslations (command_id, lang, description)
SELECT id, 'ru', 'Логирование чата' FROM Commands WHERE key_name='g_chatlog'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_CheckDeadServer'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_damage_blend'
UNION ALL
SELECT id, 'ru', 'Камера при смерти' FROM Commands WHERE key_name='g_deathCamActive'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_deathCamDist'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_deathCamSpeedFO'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_deathCamSpeedP'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_deathCamSpeedZ'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_desolveEnd'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_desolveStart'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_disperse_loading'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_EffectPriorityDistance'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_fall_height'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_falx'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_faly'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_falz'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_fatx'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_faty'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_fatz'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_favx'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_favy'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_favz'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_fheight'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_fireCamOffset'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_fireCamSpeed'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_gameFlags'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_gameReplay'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_gameReplayControl'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_gameReplayName'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_gameReplaySpeed'
UNION ALL
SELECT id, 'ru', 'Использовать GameGuard' FROM Commands WHERE key_name='g_ggAuth'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_headCamDegree'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_headCamDist'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_headCamStiff'
UNION ALL
SELECT id, 'ru', 'Скрыть модель персонажа' FROM Commands WHERE key_name='g_hide'
UNION ALL
SELECT id, 'ru', 'Скрыть интерфейс' FROM Commands WHERE key_name='g_hide_ui'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_hit_freeze'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_hit_freeze_time'
UNION ALL
SELECT id, 'ru', 'Тряска камеры при попадании' FROM Commands WHERE key_name='g_hitCamActive'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_hitCamShake'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_hitCamShakeReduce'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_hitFxMonsterSize'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_IDDreScoreAlarm'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_idle002_time'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_IDLF1ScoreAlarm'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_IgnoreUICoolTime'
UNION ALL
SELECT id, 'ru', 'Максимальный FOV' FROM Commands WHERE key_name='g_maxFov'
UNION ALL
SELECT id, 'ru', 'Максимальный FPS (0 — без лимита)' FROM Commands WHERE key_name='g_maxfps'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_midFov'
UNION ALL
SELECT id, 'ru', 'Минимальный угол обзора' FROM Commands WHERE key_name='g_minFov';
INSERT OR IGNORE INTO CommandTranslations (command_id, lang, description)
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_MP_fixed_timestep'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_observe'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_pathfinding'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_Render'
UNION ALL
SELECT id, 'ru', 'Сохранять пресеты настроек' FROM Commands WHERE key_name='g_save_preset'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_scaled_attack'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_scaled_attack_limit'
UNION ALL
SELECT id, 'ru', 'Всегда показывать выбор сервера' FROM Commands WHERE key_name='g_select_server'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_send_level_version'
UNION ALL
SELECT id, 'ru', 'Показывать дыхание' FROM Commands WHERE key_name='g_show_breath'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_show_create_btn'
UNION ALL
SELECT id, 'ru', 'Показывать оглушение' FROM Commands WHERE key_name='g_show_stunned'
UNION ALL
SELECT id, 'ru', 'Показывать сообщения урона' FROM Commands WHERE key_name='g_showDamageMsg'
UNION ALL
SELECT id, 'ru', 'Показывать счётчик FPS' FROM Commands WHERE key_name='g_showFps'
UNION ALL
SELECT id, 'ru', 'Показывать отладку макросов' FROM Commands WHERE key_name='g_showMacroMsg'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_showPanningCursor'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_targetMarkerType'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_targetSound'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_tempPseudoFullscreen'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_test'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_testFxcSpawn'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_testIntersect'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_testPut'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_testRecvWorld'
UNION ALL
SELECT id, 'ru', 'Авто-телепорт (чит)' FROM Commands WHERE key_name='g_testTeleport'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_ThirdPersonRange'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_thrust_time'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_ui_filter'
UNION ALL
SELECT id, 'ru', 'Шрифт интерфейса' FROM Commands WHERE key_name='g_ui_font'
UNION ALL
SELECT id, 'ru', 'Масштаб интерфейса' FROM Commands WHERE key_name='g_ui_scale'
UNION ALL
SELECT id, 'ru', 'Пользовательский множитель масштаба UI' FROM Commands WHERE key_name='g_ui_scale_factor'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_ui_stillview'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_ui_tile'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_uiContour'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_UIForTuning'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_uiFX'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_var1'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_var2'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_var3'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_var4'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_verbose'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_verbose_animation'
UNION ALL
SELECT id, 'ru', 'Тряска камеры при ходьбе' FROM Commands WHERE key_name='g_walkCamActive'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_walkCamAmp'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_walkCamFreq'
UNION ALL
SELECT id, 'ru', 'Масштаб оружия' FROM Commands WHERE key_name='g_weapon_scale'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_windBox'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_draw_3dView'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_draw_radar'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_spf';
INSERT OR IGNORE INTO CommandTranslations (command_id, lang, description)
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_country_code'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_create_info'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_fmode'
UNION ALL
SELECT id, 'ru', 'Чит-код полёта' FROM Commands WHERE key_name='g_freefly'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_fjump'
UNION ALL
SELECT id, 'ru', 'Полноэкранный режим' FROM Commands WHERE key_name='g_fullscreen'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_NoWarFog'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_glide'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_fly_height'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_auto_disconnect'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_rotate_speed'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_rotate_speed_mouse'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_tutorialReset'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_player_nameid'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_player_armor'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_player_armor_color'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_player_face'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_player_hair'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_player_skin_color'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_player_hair_color'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_player_body_scales'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_player_speed'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_player_pos'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_player_camera_shake'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_player_fx'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_smooth_move'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_blade_fx'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_blade_time'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_blade_tex'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_clear_attack_count'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_client_var'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_program_damage'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_blend1'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_blend2'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_mxID'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_player_scale'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_player_listener_pos'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_player_listener_height'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_sound_min_dist'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_sound_max_dist'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_blend_time'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_blendout_time'
UNION ALL
SELECT id, 'ru', 'Автоприближение камеры' FROM Commands WHERE key_name='g_autoZoom'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_autoZoomDegree'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_autoZoomSpeed'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_npcCamPosRatio'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_npcCamPosDist'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_npcCamAngleZ'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_npcCamAngleX'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_npcCamRange';
INSERT OR IGNORE INTO CommandTranslations (command_id, lang, description)
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_npcCamSpeedP'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_npcCamZ'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_npcCamFov'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_transCamStiffness'
UNION ALL
SELECT id, 'ru', 'Открывать сайт Aion при выходе' FROM Commands WHERE key_name='g_open_aion_web'
UNION ALL
SELECT id, 'ru', 'Игровые эффекты' FROM Commands WHERE key_name='g_enableGameEffect'
UNION ALL
SELECT id, 'ru', 'Голосовые реплики скиллов' FROM Commands WHERE key_name='g_enableSkillVoice'
UNION ALL
SELECT id, 'ru', 'Показывать сообщения урона' FROM Commands WHERE key_name='g_showDamageMsg'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_ammoHeightRatio'
UNION ALL
SELECT id, 'ru', 'Кровь и расчленение' FROM Commands WHERE key_name='g_gore'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_testPutUser'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_testRecvWorld'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_clbone'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_useRotateAnimation'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_charCustomColor'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_BlendSpine'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_2dDamageR'
UNION ALL
SELECT id, 'ru', 'Общий игровой параметр' FROM Commands WHERE key_name='g_AutoWalkType'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_AccurateParticles'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_Beams'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_BumpSelfShadow'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_Char_AmbientColor_Amount'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_Char_SunColor_Amount'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_Character_Debug'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_Character_LOD_Bias'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_Character_NoAnim'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_Character_NoDeform'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_Character_NoPhys'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_Character_Shadow_Volume'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_checkSunVis'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_DebugLights'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_DebugScreenEffects'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_DecalTextures'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_depth_buffer'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_DepthBits'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_DetailDefault'
UNION ALL
SELECT id, 'ru', 'Дистанция детальных текстур' FROM Commands WHERE key_name='r_DetailDistance'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_DetailNumLayers'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_DetailScale'
UNION ALL
SELECT id, 'ru', 'Детальные текстуры' FROM Commands WHERE key_name='r_DetailTextures'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_DisableSfx'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_DisplayInfo'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_EfMultiTex'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_EMBM'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_FadeAmount'
UNION ALL
SELECT id, 'ru', 'Полноэкранное сглаживание (FSAA)' FROM Commands WHERE key_name='r_FSAA'
UNION ALL
SELECT id, 'ru', 'Качество сглаживания' FROM Commands WHERE key_name='r_FSAA_quality'
UNION ALL
SELECT id, 'ru', 'Количество сэмплов сглаживания' FROM Commands WHERE key_name='r_FSAA_samples'
UNION ALL
SELECT id, 'ru', 'Гамма-коррекция' FROM Commands WHERE key_name='r_Gamma'
UNION ALL
SELECT id, 'ru', 'Геометрический инстансинг' FROM Commands WHERE key_name='r_GeomInstancing';
INSERT OR IGNORE INTO CommandTranslations (command_id, lang, description)
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_GetScreenShot'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_HDRBrightOffset'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_HDRBrightThreshold'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_HDRDebug'
UNION ALL
SELECT id, 'ru', 'Псевдо-HDR' FROM Commands WHERE key_name='r_HDRFake'
UNION ALL
SELECT id, 'ru', 'Уровень HDR' FROM Commands WHERE key_name='r_HDRLevel'
UNION ALL
SELECT id, 'ru', 'HDR-рендеринг' FROM Commands WHERE key_name='r_HDRRendering'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_HeatHaze'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_HeatMapMips'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_HeatMapSave'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_HeatSize'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_HeatType'
UNION ALL
SELECT id, 'ru', 'Высота окна/экрана' FROM Commands WHERE key_name='r_Height'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_HWLights'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_LightSourcesAsHeatSources'
UNION ALL
SELECT id, 'ru', 'Разворачивать окно на весь экран' FROM Commands WHERE key_name='r_MaximizeWindow'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_MaxTexLodBias'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_MeasureOverdraw'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_NightMapSave'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_NightSize'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_NightType'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_OceanHeightScale'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_OceanLodDist'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_OceanMaxSplashes'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_OceanRendType'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_OceanSectorSize'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_OceanSplashScale'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_OceanTexUpdate'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_OffsetBump'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_OffsetBumpForce'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_RainMapSize'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_RB_Merge'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_ReloadShaders'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_RenderMode'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_ReplaceCubemap'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_ResetScreenFx'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_RestoreLeft'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_RestoreTop'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_Scissor'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_ScopeLens_fx'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_ScreenRefract'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_SelfRefract'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_SelfShadow'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_ShaderDefault'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_ShaderDetailObjectsBending'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_ShaderInfo'
UNION ALL
SELECT id, 'ru', 'Модель шейдеров (2.0, 3.0)' FROM Commands WHERE key_name='r_ShaderModel'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_ShadersPrecache'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_ShadersSave'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_ShaderTerrainDOT3';
INSERT OR IGNORE INTO CommandTranslations (command_id, lang, description)
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_ShaderTerrainSpecular'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_shadow_maps_debug'
UNION ALL
SELECT id, 'ru', 'Размытие теней' FROM Commands WHERE key_name='r_ShadowBlur'
UNION ALL
SELECT id, 'ru', 'Тип теней' FROM Commands WHERE key_name='r_ShadowType'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_Shininess'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_ShowLight'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_ShowLines'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_ShowNormals'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_ShowOnlyShader'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_ShowTangents'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_ShowTexTimeGraph'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_ShowTimeGraph'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_ShowVideoMemoryStats'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_SM2XPATH'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_SM30PATH'
UNION ALL
SELECT id, 'ru', 'Использование SSE-инструкций' FROM Commands WHERE key_name='r_SSE'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_SubSurfaceType'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_SunStyleCoronas'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_SupportCompressedTextures'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_SupportPalettedTextures'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_TexBindMode'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_TexBumpQuality'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_TexBumpResolution'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_TexForceSquare'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_TexGrayOverage'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_TexHWDXTCompression'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_TexHWMipsGeneration'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_TexLMResolution'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_TexLoadMipmapForce'
UNION ALL
SELECT id, 'ru', 'Максимальный размер текстур' FROM Commands WHERE key_name='r_TexMaxSize'
UNION ALL
SELECT id, 'ru', 'Минимальный размер текстур' FROM Commands WHERE key_name='r_TexMinSize'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_TexNormalMapCompressed'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_TexNormalMapType'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_TexProcedures'
UNION ALL
SELECT id, 'ru', 'Качество текстур' FROM Commands WHERE key_name='r_TexQuality'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_TexQuantizeDither'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_TexResolution'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_TexSimpleMips'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_TexSkyQuality'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_TexSkyResolution'
UNION ALL
SELECT id, 'ru', 'Уровень анизотропной фильтрации (1–16)' FROM Commands WHERE key_name='r_Texture_Anisotropic_Level'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_TexturesBaseMip'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_TexturesPixelSize'
UNION ALL
SELECT id, 'ru', 'Потоковая загрузка текстур' FROM Commands WHERE key_name='r_TexturesStreaming'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_TexturesStreamingOnlyVideo'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_TexturesStreamingSync'
UNION ALL
SELECT id, 'ru', 'Размер пула текстур' FROM Commands WHERE key_name='r_TexturesStreamPoolSize'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_texUnloadDelay'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_Vegetation_Debug'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_Vegetation_IgnoreVertColors';
INSERT OR IGNORE INTO CommandTranslations (command_id, lang, description)
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_Vegetation_PerpixelLight'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_VegetationSpritesAlphaBlend'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_VegetationSpritesNoBend'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_VPFog'
UNION ALL
SELECT id, 'ru', 'Вертикальная синхронизация' FROM Commands WHERE key_name='r_VSync'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_Water_Distance_Far'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_WaterBeachRefractions'
UNION ALL
SELECT id, 'ru', 'Отражения в воде' FROM Commands WHERE key_name='r_WaterReflections'
UNION ALL
SELECT id, 'ru', 'Максимальная дистанция отражений' FROM Commands WHERE key_name='r_WaterReflections_MaxViewDist'
UNION ALL
SELECT id, 'ru', 'Преломления в воде' FROM Commands WHERE key_name='r_WaterRefractions'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_WaterUpdateDeltaAngle'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_WaterUpdateDistance'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_WaterUpdateFactor'
UNION ALL
SELECT id, 'ru', 'Параметр рендеринга' FROM Commands WHERE key_name='r_WaveScale'
UNION ALL
SELECT id, 'ru', 'Ширина окна/экрана' FROM Commands WHERE key_name='r_Width'
UNION ALL
SELECT id, 'ru', 'Высота окна (оконный режим)' FROM Commands WHERE key_name='r_WindowHeight'
UNION ALL
SELECT id, 'ru', 'Ширина окна (оконный режим)' FROM Commands WHERE key_name='r_WindowWidth'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_active_shadow_maps_receving'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_bboxes'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_beach'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_bflyes'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_capture_file_format'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_capture_folder'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_capture_frames'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_cbuffer'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_ccgf_load'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_ccgf_make_if_not_found'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_cgf_cache'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_cgf_load_lods'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_check_number_of_physicalized_polygons'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_debug_lights'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_debug_rndenv'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_debug_shaders'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_debug_shaders_offset'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_decals'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_decals_life_time_scale'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_decals_neighbor_max_life_time'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_decals_offset'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_decals_test'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_deformable_terrain'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_detail_objects'
UNION ALL
SELECT id, 'ru', 'Детальные текстуры' FROM Commands WHERE key_name='e_detail_texture'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_detail_texture_min_fov'
UNION ALL
SELECT id, 'ru', 'Качество детальных текстур' FROM Commands WHERE key_name='e_detail_texture_quality'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_disable_fx_preprocess'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_disable_fx_process'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_disable_watercubemap'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_display_musiczone_info'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_editor_time_ratio'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_game_slopeview';
INSERT OR IGNORE INTO CommandTranslations (command_id, lang, description)
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_gametime_control_manual'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_geomorph_enable'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_geomorph_enable_test'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_geomorph_renderer'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_hires_screenshoot'
UNION ALL
SELECT id, 'ru', 'Карты освещения' FROM Commands WHERE key_name='e_light_maps'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_light_maps_exportVersion'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_light_maps_occlusion'
UNION ALL
SELECT id, 'ru', 'Качество карт освещения' FROM Commands WHERE key_name='e_light_maps_quality'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_materials'
UNION ALL
SELECT id, 'ru', 'Максимум источников света' FROM Commands WHERE key_name='e_max_entity_lights'
UNION ALL
SELECT id, 'ru', 'Максимальный размер карты теней' FROM Commands WHERE key_name='e_max_shadow_map_size'
UNION ALL
SELECT id, 'ru', 'Максимальная дальность прорисовки' FROM Commands WHERE key_name='e_maxdistance_enable'
UNION ALL
SELECT id, 'ru', 'Дальность прорисовки сущностей' FROM Commands WHERE key_name='e_maxdistance_entities'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_maxdistance_ratio_entities'
UNION ALL
SELECT id, 'ru', 'Дальность прорисовки ландшафта' FROM Commands WHERE key_name='e_maxdistance_terrain'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_new_object_xml'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_obj_load_dist_ratio'
UNION ALL
SELECT id, 'ru', 'Соотношение LOD объектов' FROM Commands WHERE key_name='e_obj_lod_ratio'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_obj_min_view_dist'
UNION ALL
SELECT id, 'ru', 'Дистанция видимости объектов' FROM Commands WHERE key_name='e_obj_view_dist_ratio'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_objects'
UNION ALL
SELECT id, 'ru', 'Дистанция отрисовки объектов' FROM Commands WHERE key_name='e_objects_draw_range'
UNION ALL
SELECT id, 'ru', 'Затухание объектов на расстоянии' FROM Commands WHERE key_name='e_objects_fade_on_distance'
UNION ALL
SELECT id, 'ru', 'Окклюзионные объёмы' FROM Commands WHERE key_name='e_occlusion_volumes'
UNION ALL
SELECT id, 'ru', 'Частицы (вкл/выкл)' FROM Commands WHERE key_name='e_particles'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_particles_cull'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_particles_debug'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_particles_debug_spawntest'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_particles_debug_string'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_particles_debug_type'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_Particles_Draw_Area'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_Particles_Draw_Box'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_Particles_Draw_Range'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_particles_freeze'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_particles_fullfx'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_particles_info'
UNION ALL
SELECT id, 'ru', 'LOD частиц' FROM Commands WHERE key_name='e_particles_lod'
UNION ALL
SELECT id, 'ru', 'Максимальное количество частиц' FROM Commands WHERE key_name='e_particles_max_count'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_particles_receive_shadows'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_particles_showemitter_name'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_particles_showonly'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_particles_spawn_distance_ratio'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_particles_system_only'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_particles_use_partice_table'
UNION ALL
SELECT id, 'ru', 'Количество дождя' FROM Commands WHERE key_name='e_rain_amount'
UNION ALL
SELECT id, 'ru', 'Частицы дождя' FROM Commands WHERE key_name='e_rain_particle'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_register_in_sectors'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_scissor_debug'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_sequence_debug_playtime';
INSERT OR IGNORE INTO CommandTranslations (command_id, lang, description)
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_sequence_debug_spawntime'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_sequence_debug_string'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_sequence_info'
UNION ALL
SELECT id, 'ru', 'Карты теней' FROM Commands WHERE key_name='e_shadow_maps'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_shadow_maps_color_ratio'
UNION ALL
SELECT id, 'ru', 'Отладка карт теней' FROM Commands WHERE key_name='e_shadow_maps_debug'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_shadow_maps_fade_from_light_bit'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_shadow_maps_from_static_objects'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_shadow_maps_frustums'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_shadow_maps_max_casters_per_object'
UNION ALL
SELECT id, 'ru', 'Получение теней объектами' FROM Commands WHERE key_name='e_shadow_maps_receiving'
UNION ALL
SELECT id, 'ru', 'Самозатенение объектов' FROM Commands WHERE key_name='e_shadow_maps_self_shadowing'
UNION ALL
SELECT id, 'ru', 'Соотношение размера карт теней' FROM Commands WHERE key_name='e_shadow_maps_size_ratio'
UNION ALL
SELECT id, 'ru', 'Дистанция видимости теней' FROM Commands WHERE key_name='e_shadow_maps_view_dist_ratio'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_shadow_spots'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_simple_shadow_maps'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_SupportLightmaps'
UNION ALL
SELECT id, 'ru', 'Ландшафт (вкл/выкл)' FROM Commands WHERE key_name='e_terrain'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_terrain_debug'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_terrain_draw_this_sector_adjacency'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_terrain_draw_this_sector_only'
UNION ALL
SELECT id, 'ru', 'LOD ландшафта' FROM Commands WHERE key_name='e_terrain_lod_ratio'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_terrain_log'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_terrain_merge_far_sectors'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_terrain_occlusion_culling'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_terrain_occlusion_culling_precision'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_terrain_sector_grid'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_terrain_shadow_index'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_terrain_single_pass'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_terrain_single_pass_vol_fog'
UNION ALL
SELECT id, 'ru', 'Зеркальность ландшафта' FROM Commands WHERE key_name='e_terrain_specular'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_terrain_texture_bind'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_terrain_texture_mip_offset'
UNION ALL
SELECT id, 'ru', 'Mipmap ландшафта' FROM Commands WHERE key_name='e_terrain_texture_mipmaps'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_terrain_texture_pool'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_TerrainSectorsInfo'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_time_env_enable'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_time_profiling'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_time_smoothing'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_timedemo_frames'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_timedemo_milliseconds'
UNION ALL
SELECT id, 'ru', 'Растительность' FROM Commands WHERE key_name='e_vegetation'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_vegetation_3donly'
UNION ALL
SELECT id, 'ru', 'Изгиб растительности от ветра' FROM Commands WHERE key_name='e_vegetation_bending'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_vegetation_debug'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_vegetation_min_size'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_vegetation_plants1_distance'
UNION ALL
SELECT id, 'ru', 'Спрайты растительности' FROM Commands WHERE key_name='e_vegetation_sprites'
UNION ALL
SELECT id, 'ru', 'Дистанция спрайтов растительности' FROM Commands WHERE key_name='e_vegetation_sprites_distance_ratio'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_vegetation_sprites_min_distance';
INSERT OR IGNORE INTO CommandTranslations (command_id, lang, description)
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_vegetation_sprites_slow_switch'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_vegetation_sprites_texres'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_vegetation_update_shadow_every_frame'
UNION ALL
SELECT id, 'ru', 'Океан' FROM Commands WHERE key_name='e_water_ocean'
UNION ALL
SELECT id, 'ru', 'Отражение солнца на воде' FROM Commands WHERE key_name='e_water_ocean_sun_reflection'
UNION ALL
SELECT id, 'ru', 'Тесселяция океана' FROM Commands WHERE key_name='e_water_ocean_tesselation'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_water_render_cull_terrain'
UNION ALL
SELECT id, 'ru', 'Дистанция отрисовки воды' FROM Commands WHERE key_name='e_water_render_distance'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_water_volumes'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_weather_change_immediate'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_weather_change_speed'
UNION ALL
SELECT id, 'ru', 'Параметр движка / мира' FROM Commands WHERE key_name='e_weather_cutscene'
UNION ALL
SELECT id, 'ru', 'Погодные эффекты' FROM Commands WHERE key_name='e_weather_enable'
UNION ALL
SELECT id, 'ru', 'FX-эффекты погоды' FROM Commands WHERE key_name='e_weather_fx_enable'
UNION ALL
SELECT id, 'ru', 'Широкоэкранный режим' FROM Commands WHERE key_name='e_widescreen'
UNION ALL
SELECT id, 'ru', 'Параметр физики' FROM Commands WHERE key_name='p_accuracy_LCPCG'
UNION ALL
SELECT id, 'ru', 'Параметр физики' FROM Commands WHERE key_name='p_accuracy_LCPCG_no_improvement'
UNION ALL
SELECT id, 'ru', 'Параметр физики' FROM Commands WHERE key_name='p_accuracy_MC'
UNION ALL
SELECT id, 'ru', 'Параметр физики' FROM Commands WHERE key_name='p_characterik'
UNION ALL
SELECT id, 'ru', 'Параметр физики' FROM Commands WHERE key_name='p_characterik_arm'
UNION ALL
SELECT id, 'ru', 'Параметр физики' FROM Commands WHERE key_name='p_damping_group_size'
UNION ALL
SELECT id, 'ru', 'Время жизни декалей (следов)' FROM Commands WHERE key_name='p_decalLifetime'
UNION ALL
SELECT id, 'ru', 'Фиксированный шаг физики' FROM Commands WHERE key_name='p_fixed_timestep'
UNION ALL
SELECT id, 'ru', 'Параметр физики' FROM Commands WHERE key_name='p_GEB_max_cells'
UNION ALL
SELECT id, 'ru', 'Камера от головы' FROM Commands WHERE key_name='p_head_camera'
UNION ALL
SELECT id, 'ru', 'Параметр физики' FROM Commands WHERE key_name='p_limit_simple_solver_energy'
UNION ALL
SELECT id, 'ru', 'Параметр физики' FROM Commands WHERE key_name='p_list_active_objects'
UNION ALL
SELECT id, 'ru', 'Параметр физики' FROM Commands WHERE key_name='p_max_contact_gap'
UNION ALL
SELECT id, 'ru', 'Параметр физики' FROM Commands WHERE key_name='p_max_contact_gap_player'
UNION ALL
SELECT id, 'ru', 'Параметр физики' FROM Commands WHERE key_name='p_max_contact_gap_simple'
UNION ALL
SELECT id, 'ru', 'Максимум контактов' FROM Commands WHERE key_name='p_max_contacts'
UNION ALL
SELECT id, 'ru', 'Параметр физики' FROM Commands WHERE key_name='p_max_LCPCG_fruitless_iters'
UNION ALL
SELECT id, 'ru', 'Параметр физики' FROM Commands WHERE key_name='p_max_LCPCG_iters'
UNION ALL
SELECT id, 'ru', 'Параметр физики' FROM Commands WHERE key_name='p_max_LCPCG_microiters'
UNION ALL
SELECT id, 'ru', 'Параметр физики' FROM Commands WHERE key_name='p_max_LCPCG_microiters_final'
UNION ALL
SELECT id, 'ru', 'Параметр физики' FROM Commands WHERE key_name='p_max_LCPCG_subiters'
UNION ALL
SELECT id, 'ru', 'Параметр физики' FROM Commands WHERE key_name='p_max_LCPCG_subiters_final'
UNION ALL
SELECT id, 'ru', 'Параметр физики' FROM Commands WHERE key_name='p_max_MC_iters'
UNION ALL
SELECT id, 'ru', 'Параметр физики' FROM Commands WHERE key_name='p_max_plane_contacts'
UNION ALL
SELECT id, 'ru', 'Параметр физики' FROM Commands WHERE key_name='p_max_plane_contacts_distress'
UNION ALL
SELECT id, 'ru', 'Максимальная скорость игрока' FROM Commands WHERE key_name='p_max_player_velocity'
UNION ALL
SELECT id, 'ru', 'Параметр физики' FROM Commands WHERE key_name='p_max_substeps'
UNION ALL
SELECT id, 'ru', 'Параметр физики' FROM Commands WHERE key_name='p_max_unproj_vel'
UNION ALL
SELECT id, 'ru', 'Параметр физики' FROM Commands WHERE key_name='p_max_velocity'
UNION ALL
SELECT id, 'ru', 'Параметр физики' FROM Commands WHERE key_name='p_max_world_step'
UNION ALL
SELECT id, 'ru', 'Параметр физики' FROM Commands WHERE key_name='p_min_LCPCG_improvement'
UNION ALL
SELECT id, 'ru', 'Параметр физики' FROM Commands WHERE key_name='p_min_separation_speed'
UNION ALL
SELECT id, 'ru', 'Параметр физики' FROM Commands WHERE key_name='p_penalty_scale'
UNION ALL
SELECT id, 'ru', 'Параметр физики' FROM Commands WHERE key_name='p_single_step_mode'
UNION ALL
SELECT id, 'ru', 'Параметр физики' FROM Commands WHERE key_name='p_time_granularity';
INSERT OR IGNORE INTO CommandTranslations (command_id, lang, description)
SELECT id, 'ru', 'Параметр физики' FROM Commands WHERE key_name='p_waterbob_mindepth'
UNION ALL
SELECT id, 'ru', 'Покачивание камеры в воде (pitch)' FROM Commands WHERE key_name='p_waterbob_pitch'
UNION ALL
SELECT id, 'ru', 'Параметр физики' FROM Commands WHERE key_name='p_waterbob_pitchspeed'
UNION ALL
SELECT id, 'ru', 'Покачивание камеры в воде (roll)' FROM Commands WHERE key_name='p_waterbob_roll'
UNION ALL
SELECT id, 'ru', 'Параметр физики' FROM Commands WHERE key_name='p_waterbob_rollspeed'
UNION ALL
SELECT id, 'ru', 'Параметр сущностей' FROM Commands WHERE key_name='es_bboxes'
UNION ALL
SELECT id, 'ru', 'Параметр сущностей' FROM Commands WHERE key_name='es_CamHeight'
UNION ALL
SELECT id, 'ru', 'Параметр сущностей' FROM Commands WHERE key_name='es_CamHeightNear'
UNION ALL
SELECT id, 'ru', 'Параметр сущностей' FROM Commands WHERE key_name='es_CamRestoreStiff'
UNION ALL
SELECT id, 'ru', 'Параметр сущностей' FROM Commands WHERE key_name='es_charArmIK_Range'
UNION ALL
SELECT id, 'ru', 'Параметр сущностей' FROM Commands WHERE key_name='es_charIK_Range'
UNION ALL
SELECT id, 'ru', 'Параметр сущностей' FROM Commands WHERE key_name='es_CharZOffsetSpeed'
UNION ALL
SELECT id, 'ru', 'Параметр сущностей' FROM Commands WHERE key_name='es_DebugTimer'
UNION ALL
SELECT id, 'ru', 'Параметр сущностей' FROM Commands WHERE key_name='es_DisplayInfo'
UNION ALL
SELECT id, 'ru', 'Параметр сущностей' FROM Commands WHERE key_name='es_EnableCloth'
UNION ALL
SELECT id, 'ru', 'Параметр сущностей' FROM Commands WHERE key_name='es_FxSystemRVRLevel'
UNION ALL
SELECT id, 'ru', 'Параметр сущностей' FROM Commands WHERE key_name='es_helpers'
UNION ALL
SELECT id, 'ru', 'Параметр сущностей' FROM Commands WHERE key_name='es_HitCharacters'
UNION ALL
SELECT id, 'ru', 'Параметр сущностей' FROM Commands WHERE key_name='es_HitDeadBodies'
UNION ALL
SELECT id, 'ru', 'Параметр сущностей' FROM Commands WHERE key_name='es_ImpulseScale'
UNION ALL
SELECT id, 'ru', 'Параметр сущностей' FROM Commands WHERE key_name='es_LODShaderDistance'
UNION ALL
SELECT id, 'ru', 'Параметр сущностей' FROM Commands WHERE key_name='es_LODShaderStep'
UNION ALL
SELECT id, 'ru', 'Параметр сущностей' FROM Commands WHERE key_name='es_MaxImpulseAdjMass'
UNION ALL
SELECT id, 'ru', 'Параметр сущностей' FROM Commands WHERE key_name='es_MinImpulseVel'
UNION ALL
SELECT id, 'ru', 'Параметр сущностей' FROM Commands WHERE key_name='es_OnDemandPhysics'
UNION ALL
SELECT id, 'ru', 'Параметр сущностей' FROM Commands WHERE key_name='es_PiercingCamera'
UNION ALL
SELECT id, 'ru', 'Параметр сущностей' FROM Commands WHERE key_name='es_SplashThreshold'
UNION ALL
SELECT id, 'ru', 'Параметр сущностей' FROM Commands WHERE key_name='es_SplashTimeout'
UNION ALL
SELECT id, 'ru', 'Параметр сущностей' FROM Commands WHERE key_name='es_UpdateAI'
UNION ALL
SELECT id, 'ru', 'Параметр сущностей' FROM Commands WHERE key_name='es_UpdateBonePositions'
UNION ALL
SELECT id, 'ru', 'Параметр сущностей' FROM Commands WHERE key_name='es_UpdateCamera'
UNION ALL
SELECT id, 'ru', 'Параметр сущностей' FROM Commands WHERE key_name='es_UpdateCollision'
UNION ALL
SELECT id, 'ru', 'Параметр сущностей' FROM Commands WHERE key_name='es_UpdateCollisionScript'
UNION ALL
SELECT id, 'ru', 'Параметр сущностей' FROM Commands WHERE key_name='es_UpdateContainer'
UNION ALL
SELECT id, 'ru', 'Параметр сущностей' FROM Commands WHERE key_name='es_UpdateCoocooEgg'
UNION ALL
SELECT id, 'ru', 'Параметр сущностей' FROM Commands WHERE key_name='es_UpdateEntities'
UNION ALL
SELECT id, 'ru', 'Параметр сущностей' FROM Commands WHERE key_name='es_UpdateInvisibleCharacter'
UNION ALL
SELECT id, 'ru', 'Параметр сущностей' FROM Commands WHERE key_name='es_UpdatePhysics'
UNION ALL
SELECT id, 'ru', 'Параметр сущностей' FROM Commands WHERE key_name='es_UpdateScript'
UNION ALL
SELECT id, 'ru', 'Параметр сущностей' FROM Commands WHERE key_name='es_UpdateTimer'
UNION ALL
SELECT id, 'ru', 'Параметр сущностей' FROM Commands WHERE key_name='es_VisCheckForUpdate'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_ac_cos'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_ac_hcos'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_ac_hsin'
UNION ALL
SELECT id, 'ru', 'Интенсивность ambient-света на персонаже' FROM Commands WHERE key_name='ca_ambient_light_intensity'
UNION ALL
SELECT id, 'ru', 'Дальность ambient-света' FROM Commands WHERE key_name='ca_ambient_light_range'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_AnimationDeferredLoad'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_AnimationUnloadCheckPerFrame'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_AnimationUnloadDelay'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_AnimationUnloadMaxPerFrame';
INSERT OR IGNORE INTO CommandTranslations (command_id, lang, description)
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_AnimDisplacementThreshold'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_AnimDistanceThreshold'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_AnimIFrame'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_AnimWarningLevel'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_BoneAnimUFM'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_BoundZOffset'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_cb_iteration'
UNION ALL
SELECT id, 'ru', 'Режим ткани (плащи, робы)' FROM Commands WHERE key_name='ca_ClothMode'
UNION ALL
SELECT id, 'ru', 'Кастомный цвет волос' FROM Commands WHERE key_name='ca_CustomColorHair'
UNION ALL
SELECT id, 'ru', 'Кастомный цвет кожи' FROM Commands WHERE key_name='ca_CustomColorSkin'
UNION ALL
SELECT id, 'ru', 'Время анимации смерти' FROM Commands WHERE key_name='ca_DeathBlendTime'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_Debug'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_DebugHeatSources'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_DebugInfo'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_DebugShaders'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_DecalAntiflickerHack'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_DecalSizeMultiplier'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_DefaultDecalTexture'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_DisableAnimEvents'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_DisablePlusRotationMask'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_DisplayInfo'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_drag'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_DrawAnims'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_DrawBBox'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_DrawBBoxSub'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_DrawBones'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_DrawDecalOutline'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_DrawLHelpers'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_edge_max'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_edge_min'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_EnableAnimationLog'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_EnableCCG'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_EnableCharacterShadowVolume'
UNION ALL
SELECT id, 'ru', 'Кубическое смешивание (улучшает качество графики)' FROM Commands WHERE key_name='ca_EnableCubicBlending'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_EnableDecals'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_EnableLightUpdate'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_EnableTangentSkinning'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_EnableVertexColors'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_fixed_time'
UNION ALL
SELECT id, 'ru', 'Анимация волос' FROM Commands WHERE key_name='ca_HairAnim'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_HairAnimBackPlaneOffset'
UNION ALL
SELECT id, 'ru', 'Демпфирование волос (1)' FROM Commands WHERE key_name='ca_HairAnimDamping1'
UNION ALL
SELECT id, 'ru', 'Демпфирование волос (2)' FROM Commands WHERE key_name='ca_HairAnimDamping2'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_HairAnimDistance'
UNION ALL
SELECT id, 'ru', 'Гравитация волос (1)' FROM Commands WHERE key_name='ca_HairAnimGravity1'
UNION ALL
SELECT id, 'ru', 'Гравитация волос (2)' FROM Commands WHERE key_name='ca_HairAnimGravity2'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_HairAnimLimitAngle'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_HairAnimMassInc'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_HairAnimRelaxationIterCount'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_horz_edge';
INSERT OR IGNORE INTO CommandTranslations (command_id, lang, description)
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_Iteration'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_KeepMaxCacheSize'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_KeepMaxCacheSize2'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_KeepMaxCacheSize3'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_KeepModels'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_KeepOrthoUniform'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_LimitShadowLOD'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_LodBias'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_LogAnimation'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_MatPlusDebug'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_MatPlusDebug2'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_MaxMorphDist'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_MinVertexWeightLOD0'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_MinVertexWeightLOD1'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_MinVertexWeightLOD2'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_MorphNormals'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_NoAnim'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_NoDeform'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_NoDraw'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_NoDrawBound'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_NoDrawShadowVolumes'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_NoMatPlus'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_NoMatPlus2'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_NoMorph'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_NoMtlSorting'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_NoPhys'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_NormalizeBases'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_NoTransScale'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_OverrideLayer'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_PerforatingDecals'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_PrebuildShadowConnectivity'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_Profile'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_RainPower'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_RestartBehaviour'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_RuntimeScale'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_SafeReskin'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_ShadowBufferLimit'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_ShadowDoubleBuffer'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_ShadowVolumeExtent'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_SkinBasedBBoxMask'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_SkipBoneAnim'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_SSEEnable'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_SSEEnable1'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_SSEEnable2'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_StopDeformingAfter'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_StripifyGeometry'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_TangentBasisCalcPeriod'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_TestMirror'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_TestSkinningRepeats'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_TickVersion';
INSERT OR IGNORE INTO CommandTranslations (command_id, lang, description)
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_UpdateSpeed'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_UpdateSpeed0'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_UpdateSpeed1'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_UpdateSpeed2'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_UpdateSpeed3'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_UpdateSpeed4'
UNION ALL
SELECT id, 'ru', 'Использовать кастомный цвет' FROM Commands WHERE key_name='ca_UseCustomColor'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_UseLowestLOD'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_VertsPerTangSubskin'
UNION ALL
SELECT id, 'ru', 'Параметр персонажа / анимации' FROM Commands WHERE key_name='ca_ZDeleteConstructionData'
UNION ALL
SELECT id, 'ru', 'Автодополнение команд в консоли' FROM Commands WHERE key_name='con_auto_complete'
UNION ALL
SELECT id, 'ru', 'Отключить внутриигровую консоль (PauseBreak)' FROM Commands WHERE key_name='con_disable_console'
UNION ALL
SELECT id, 'ru', 'Показывать последние сообщения консоли' FROM Commands WHERE key_name='con_display_last_messages'
UNION ALL
SELECT id, 'ru', 'Размер буфера строк консоли' FROM Commands WHERE key_name='con_line_buffer_size'
UNION ALL
SELECT id, 'ru', 'Отладочная визуализация' FROM Commands WHERE key_name='CV_ind_DrawBorderEdges'
UNION ALL
SELECT id, 'ru', 'Отладочная визуализация' FROM Commands WHERE key_name='CV_ind_ReverseShadowVolumes'
UNION ALL
SELECT id, 'ru', 'Отладочная визуализация' FROM Commands WHERE key_name='CV_ind_VisualizeShadowVolumes'
UNION ALL
SELECT id, 'ru', 'Разрешить программный рендеринг' FROM Commands WHERE key_name='d3d9_AllowSoftware'
UNION ALL
SELECT id, 'ru', 'Параметр DirectX 9' FROM Commands WHERE key_name='d3d9_ClipPlanes'
UNION ALL
SELECT id, 'ru', 'Сжатые текстуры D3D9' FROM Commands WHERE key_name='d3d9_CompressedTextures'
UNION ALL
SELECT id, 'ru', 'Параметр DirectX 9' FROM Commands WHERE key_name='d3d9_DecalOffset'
UNION ALL
SELECT id, 'ru', 'Параметр DirectX 9' FROM Commands WHERE key_name='d3d9_Device'
UNION ALL
SELECT id, 'ru', 'Принудительно программный рендеринг' FROM Commands WHERE key_name='d3d9_ForceSoftware'
UNION ALL
SELECT id, 'ru', 'Параметр DirectX 9' FROM Commands WHERE key_name='d3d9_MipProcedures'
UNION ALL
SELECT id, 'ru', 'Параметр DirectX 9' FROM Commands WHERE key_name='d3d9_NoDepthMaps'
UNION ALL
SELECT id, 'ru', 'Параметр DirectX 9' FROM Commands WHERE key_name='d3d9_NodeviceId'
UNION ALL
SELECT id, 'ru', 'Параметр DirectX 9' FROM Commands WHERE key_name='d3d9_NormalMapScale'
UNION ALL
SELECT id, 'ru', 'Параметр DirectX 9' FROM Commands WHERE key_name='d3d9_NV30_PS20'
UNION ALL
SELECT id, 'ru', 'Параметр DirectX 9' FROM Commands WHERE key_name='d3d9_NVPerfHUD'
UNION ALL
SELECT id, 'ru', 'Запросы окклюзии' FROM Commands WHERE key_name='d3d9_Occlusion_Query'
UNION ALL
SELECT id, 'ru', 'Палитровые текстуры' FROM Commands WHERE key_name='d3d9_PalettedTextures'
UNION ALL
SELECT id, 'ru', 'Размер pipeline-буфера' FROM Commands WHERE key_name='d3d9_pip_buff_size'
UNION ALL
SELECT id, 'ru', 'Параметр DirectX 9' FROM Commands WHERE key_name='d3d9_rb_Tris'
UNION ALL
SELECT id, 'ru', 'Параметр DirectX 9' FROM Commands WHERE key_name='d3d9_rb_Verts'
UNION ALL
SELECT id, 'ru', 'Параметр DirectX 9' FROM Commands WHERE key_name='d3d9_ResetDeviceAfterLoading'
UNION ALL
SELECT id, 'ru', 'Параметр DirectX 9' FROM Commands WHERE key_name='d3d9_SaveDepthmaps'
UNION ALL
SELECT id, 'ru', 'Квадратные текстуры' FROM Commands WHERE key_name='d3d9_SquareTextures'
UNION ALL
SELECT id, 'ru', 'Параметр DirectX 9' FROM Commands WHERE key_name='d3d9_TexMipFilter'
UNION ALL
SELECT id, 'ru', 'Анизотропная фильтрация D3D9' FROM Commands WHERE key_name='d3d9_Texture_Filter_Anisotropic'
UNION ALL
SELECT id, 'ru', 'Параметр DirectX 9' FROM Commands WHERE key_name='d3d9_TextureBits'
UNION ALL
SELECT id, 'ru', 'Трилинейная фильтрация' FROM Commands WHERE key_name='d3d9_TextureFilter'
UNION ALL
SELECT id, 'ru', 'Тройная буферизация (даёт прирост производительности)' FROM Commands WHERE key_name='d3d9_TripleBuffering'
UNION ALL
SELECT id, 'ru', 'Использовать bump-карты' FROM Commands WHERE key_name='d3d9_UseBumpmap'
UNION ALL
SELECT id, 'ru', 'Пулы вершинных буферов' FROM Commands WHERE key_name='d3d9_VBPools'
UNION ALL
SELECT id, 'ru', 'Размер пула вершинных буферов' FROM Commands WHERE key_name='d3d9_VBPoolSize'
UNION ALL
SELECT id, 'ru', 'Параметр звука' FROM Commands WHERE key_name='s_CapsCheck'
UNION ALL
SELECT id, 'ru', 'Параметр звука' FROM Commands WHERE key_name='s_DebugMusic'
UNION ALL
SELECT id, 'ru', 'Параметр звука' FROM Commands WHERE key_name='s_DebugSound'
UNION ALL
SELECT id, 'ru', 'Параметр звука' FROM Commands WHERE key_name='s_DebugSoundBuffer'
UNION ALL
SELECT id, 'ru', 'Параметр звука' FROM Commands WHERE key_name='s_FixedSoundPriority';
INSERT OR IGNORE INTO CommandTranslations (command_id, lang, description)
SELECT id, 'ru', 'Параметр звука' FROM Commands WHERE key_name='s_KeepSound'
UNION ALL
SELECT id, 'ru', 'Общая громкость' FROM Commands WHERE key_name='s_MasterVolume'
UNION ALL
SELECT id, 'ru', 'Максимум активных источников звука' FROM Commands WHERE key_name='s_MaxActiveSoundSpots'
UNION ALL
SELECT id, 'ru', 'Максимум аппаратных каналов' FROM Commands WHERE key_name='s_MaxHWChannels'
UNION ALL
SELECT id, 'ru', 'Максимальная дистанция звука' FROM Commands WHERE key_name='s_MaxSoundDist'
UNION ALL
SELECT id, 'ru', 'Минимум аппаратных каналов' FROM Commands WHERE key_name='s_MinHWChannels'
UNION ALL
SELECT id, 'ru', 'Параметр звука' FROM Commands WHERE key_name='s_MinRepeatSoundTimeout'
UNION ALL
SELECT id, 'ru', 'Частота дискретизации' FROM Commands WHERE key_name='s_SampleRate'
UNION ALL
SELECT id, 'ru', 'Параметр звука' FROM Commands WHERE key_name='s_SFXMute_COMMENT_GOSSIP'
UNION ALL
SELECT id, 'ru', 'Параметр звука' FROM Commands WHERE key_name='s_SFXMute_COMMENT_NPC'
UNION ALL
SELECT id, 'ru', 'Параметр звука' FROM Commands WHERE key_name='s_SFXMute_COMMENT_QUEST'
UNION ALL
SELECT id, 'ru', 'Параметр звука' FROM Commands WHERE key_name='s_SFXMute_COMMENT_SYSTEM'
UNION ALL
SELECT id, 'ru', 'Параметр звука' FROM Commands WHERE key_name='s_SFXMute_COMMENT_WEATHER'
UNION ALL
SELECT id, 'ru', 'Параметр звука' FROM Commands WHERE key_name='s_SFXMute_ENV'
UNION ALL
SELECT id, 'ru', 'Отключить звуки эффектов' FROM Commands WHERE key_name='s_SFXMute_FX'
UNION ALL
SELECT id, 'ru', 'Отключить весь звук' FROM Commands WHERE key_name='s_SFXMute_MASTER'
UNION ALL
SELECT id, 'ru', 'Отключить звуки интерфейса' FROM Commands WHERE key_name='s_SFXMute_UI'
UNION ALL
SELECT id, 'ru', 'Параметр звука' FROM Commands WHERE key_name='s_SFXVolume_COMMENT_GOSSIP'
UNION ALL
SELECT id, 'ru', 'Параметр звука' FROM Commands WHERE key_name='s_SFXVolume_COMMENT_NPC'
UNION ALL
SELECT id, 'ru', 'Параметр звука' FROM Commands WHERE key_name='s_SFXVolume_COMMENT_QUEST'
UNION ALL
SELECT id, 'ru', 'Параметр звука' FROM Commands WHERE key_name='s_SFXVolume_COMMENT_SYSTEM'
UNION ALL
SELECT id, 'ru', 'Громкость окружения' FROM Commands WHERE key_name='s_SFXVolume_ENV'
UNION ALL
SELECT id, 'ru', 'Громкость эффектов' FROM Commands WHERE key_name='s_SFXVolume_FX'
UNION ALL
SELECT id, 'ru', 'Громкость интерфейса' FROM Commands WHERE key_name='s_SFXVolume_UI'
UNION ALL
SELECT id, 'ru', 'Громкость погоды' FROM Commands WHERE key_name='s_SFXVolume_WEATHER'
UNION ALL
SELECT id, 'ru', 'Параметр звука' FROM Commands WHERE key_name='s_VisAreasPropagation'
UNION ALL
SELECT id, 'ru', 'Системный параметр' FROM Commands WHERE key_name='sys_AdaptiveCharLOD'
UNION ALL
SELECT id, 'ru', 'Системный параметр' FROM Commands WHERE key_name='sys_AdaptiveCharLOD_FF'
UNION ALL
SELECT id, 'ru', 'Привязка потоков к ядрам CPU' FROM Commands WHERE key_name='sys_affinity'
UNION ALL
SELECT id, 'ru', 'Первый запуск (флаг)' FROM Commands WHERE key_name='sys_firstlaunch'
UNION ALL
SELECT id, 'ru', 'Фиксированный FPS' FROM Commands WHERE key_name='sys_fixedframe'
UNION ALL
SELECT id, 'ru', 'Системный параметр' FROM Commands WHERE key_name='sys_fixedframe_target'
UNION ALL
SELECT id, 'ru', 'Системный параметр' FROM Commands WHERE key_name='sys_noupdate'
UNION ALL
SELECT id, 'ru', 'Системный параметр' FROM Commands WHERE key_name='sys_PakLogMissingFiles'
UNION ALL
SELECT id, 'ru', 'Системный параметр' FROM Commands WHERE key_name='sys_PakPriority'
UNION ALL
SELECT id, 'ru', 'Системный параметр' FROM Commands WHERE key_name='sys_PakReadSlice'
UNION ALL
SELECT id, 'ru', 'Системный параметр' FROM Commands WHERE key_name='sys_script_debugger'
UNION ALL
SELECT id, 'ru', 'Пропускать на слабых системах' FROM Commands WHERE key_name='sys_skiponlowspec'
UNION ALL
SELECT id, 'ru', 'Уровень системных требований (1–4)' FROM Commands WHERE key_name='sys_spec'
UNION ALL
SELECT id, 'ru', 'Информация о суперсэмплинге' FROM Commands WHERE key_name='sys_SSInfo'
UNION ALL
SELECT id, 'ru', 'Бюджет времени стриминга (мкс)' FROM Commands WHERE key_name='sys_StreamCallbackTimeBudget'
UNION ALL
SELECT id, 'ru', 'Маска сжатия стриминга' FROM Commands WHERE key_name='sys_StreamCompressionMask'
UNION ALL
SELECT id, 'ru', 'Системные предупреждения' FROM Commands WHERE key_name='sys_warnings'
UNION ALL
SELECT id, 'ru', 'Параметр ввода' FROM Commands WHERE key_name='i_direct_input'
UNION ALL
SELECT id, 'ru', 'Уровень логов в файле' FROM Commands WHERE key_name='log_FileVerbosity'
UNION ALL
SELECT id, 'ru', 'Добавлять время в лог' FROM Commands WHERE key_name='log_IncludeTime'
UNION ALL
SELECT id, 'ru', 'Фильтр строк лога' FROM Commands WHERE key_name='log_linefilter'
UNION ALL
SELECT id, 'ru', 'Уровень детализации логов' FROM Commands WHERE key_name='log_Verbosity'
UNION ALL
SELECT id, 'ru', 'Отключить катсцены' FROM Commands WHERE key_name='mov_NoCutscenes'
UNION ALL
SELECT id, 'ru', 'Соотношение шрифта в видео' FROM Commands WHERE key_name='movie_fontRatio';
INSERT OR IGNORE INTO CommandTranslations (command_id, lang, description)
SELECT id, 'ru', 'Профилирование (вкл/выкл)' FROM Commands WHERE key_name='profile'
UNION ALL
SELECT id, 'ru', 'Параметр профилирования' FROM Commands WHERE key_name='profile_filter'
UNION ALL
SELECT id, 'ru', 'График профилирования' FROM Commands WHERE key_name='profile_graph'
UNION ALL
SELECT id, 'ru', 'Параметр профилирования' FROM Commands WHERE key_name='profile_graphScale'
UNION ALL
SELECT id, 'ru', 'Профиль сети' FROM Commands WHERE key_name='profile_network'
UNION ALL
SELECT id, 'ru', 'Параметр профилирования' FROM Commands WHERE key_name='profile_pagefaults'
UNION ALL
SELECT id, 'ru', 'Пиковые значения' FROM Commands WHERE key_name='profile_peak'
UNION ALL
SELECT id, 'ru', 'Информация о памяти' FROM Commands WHERE key_name='MemInfo'
UNION ALL
SELECT id, 'ru', 'Статистика памяти' FROM Commands WHERE key_name='MemStats'
UNION ALL
SELECT id, 'ru', 'Параметр памяти' FROM Commands WHERE key_name='MemStatsMaxDepth'
UNION ALL
SELECT id, 'ru', 'Порог статистики памяти' FROM Commands WHERE key_name='MemStatsThreshold'
UNION ALL
SELECT id, 'ru', 'Выход при завершении' FROM Commands WHERE key_name='ExitOnQuit'
UNION ALL
SELECT id, 'ru', 'Фиксированный шаг времени' FROM Commands WHERE key_name='fixed_time_step'
UNION ALL
SELECT id, 'ru', 'Прочий параметр' FROM Commands WHERE key_name='f_FTKerning'
UNION ALL
SELECT id, 'ru', 'VoIP в Blaze (голосовой чат)' FROM Commands WHERE key_name='net_blaze_voip_enable'
UNION ALL
SELECT id, 'ru', 'VoIP push-to-talk (кнопка разговора)' FROM Commands WHERE key_name='net_blaze_voip_enable_ptt'
UNION ALL
SELECT id, 'ru', 'Громкость воспроизведения VoIP' FROM Commands WHERE key_name='net_blaze_voip_playback_volume'
UNION ALL
SELECT id, 'ru', 'Бюджет видеопамяти (МБ)' FROM Commands WHERE key_name='sys_budget_videomem'
UNION ALL
SELECT id, 'ru', 'Бюджет системной памяти (МБ)' FROM Commands WHERE key_name='sys_budget_sysmem'
UNION ALL
SELECT id, 'ru', 'Максимальное количество потоков CPU' FROM Commands WHERE key_name='sys_MaxThreads'
UNION ALL
SELECT id, 'ru', 'Отключить диалог краша' FROM Commands WHERE key_name='sys_DisableCrashDialog'
UNION ALL
SELECT id, 'ru', 'Включить asserts' FROM Commands WHERE key_name='sys_EnableAsserts'
UNION ALL
SELECT id, 'ru', 'Отключить предупреждения' FROM Commands WHERE key_name='sys_WarningDisable'
UNION ALL
SELECT id, 'ru', '64-битный кеш' FROM Commands WHERE key_name='sys_64bitCache'
UNION ALL
SELECT id, 'ru', 'Отключить консоль' FROM Commands WHERE key_name='sys_DeactivateConsole'
UNION ALL
SELECT id, 'ru', 'Включить asserts' FROM Commands WHERE key_name='sys_EnableAsserts'
UNION ALL
SELECT id, 'ru', 'Фиксированный кадр' FROM Commands WHERE key_name='sys_FixedFrame'
UNION ALL
SELECT id, 'ru', 'Включить job-систему' FROM Commands WHERE key_name='sys_job_system_enable'
UNION ALL
SELECT id, 'ru', 'Пак для слабых ПК' FROM Commands WHERE key_name='sys_LowSpecPak'
UNION ALL
SELECT id, 'ru', 'Ядро CPU для главного потока' FROM Commands WHERE key_name='sys_main_CPU'
UNION ALL
SELECT id, 'ru', 'Максимальный FPS (системный)' FROM Commands WHERE key_name='sys_maxFPS'
UNION ALL
SELECT id, 'ru', 'Максимальный FPS' FROM Commands WHERE key_name='sys_MaxFps'
UNION ALL
SELECT id, 'ru', 'Ядро для физики' FROM Commands WHERE key_name='sys_physics_CPU'
UNION ALL
SELECT id, 'ru', 'GPU для физики' FROM Commands WHERE key_name='sys_physics_GPU'
UNION ALL
SELECT id, 'ru', 'Предзагрузка ресурсов' FROM Commands WHERE key_name='sys_preload'
UNION ALL
SELECT id, 'ru', 'Уровень качества окружения' FROM Commands WHERE key_name='sys_spec_Environment'
UNION ALL
SELECT id, 'ru', 'Уровень игровых эффектов' FROM Commands WHERE key_name='sys_spec_GameEffects'
UNION ALL
SELECT id, 'ru', 'Уровень освещения' FROM Commands WHERE key_name='sys_spec_light'
UNION ALL
SELECT id, 'ru', 'Уровень детализации объектов' FROM Commands WHERE key_name='sys_spec_ObjectDetail'
UNION ALL
SELECT id, 'ru', 'Уровень частиц' FROM Commands WHERE key_name='sys_spec_Particles'
UNION ALL
SELECT id, 'ru', 'Уровень физики' FROM Commands WHERE key_name='sys_spec_Physics'
UNION ALL
SELECT id, 'ru', 'Уровень постобработки' FROM Commands WHERE key_name='sys_spec_PostProcessing'
UNION ALL
SELECT id, 'ru', 'Общий уровень качества' FROM Commands WHERE key_name='sys_spec_Quality'
UNION ALL
SELECT id, 'ru', 'Уровень шейдинга' FROM Commands WHERE key_name='sys_spec_Shading'
UNION ALL
SELECT id, 'ru', 'Уровень теней' FROM Commands WHERE key_name='sys_spec_Shadows'
UNION ALL
SELECT id, 'ru', 'Уровень звука' FROM Commands WHERE key_name='sys_spec_Sound'
UNION ALL
SELECT id, 'ru', 'Уровень текстур' FROM Commands WHERE key_name='sys_spec_Texture'
UNION ALL
SELECT id, 'ru', 'Разрешение текстур' FROM Commands WHERE key_name='sys_spec_TextureResolution'
UNION ALL
SELECT id, 'ru', 'Объёмные эффекты' FROM Commands WHERE key_name='sys_spec_VolumetricEffects'
UNION ALL
SELECT id, 'ru', 'Отключить предупреждения' FROM Commands WHERE key_name='sys_WarningDisable';
INSERT OR IGNORE INTO CommandTranslations (command_id, lang, description)
SELECT id, 'ru', 'Windows Error Reporting' FROM Commands WHERE key_name='sys_WER'
UNION ALL
SELECT id, 'ru', 'Игнорировать предупреждения в логе' FROM Commands WHERE key_name='log_IgnoreWarnings'
UNION ALL
SELECT id, 'ru', 'Полностью отключить лог' FROM Commands WHERE key_name='log_Silence'
UNION ALL
SELECT id, 'ru', 'Принудительно использовать Pixel Shader 1.1' FROM Commands WHERE key_name='d3d9_PSforce11'
UNION ALL
SELECT id, 'ru', 'Вершинные шейдеры 3.0' FROM Commands WHERE key_name='d3d9_VS30'
UNION ALL
SELECT id, 'ru', 'Принудительно использовать Vertex Shader 1.1' FROM Commands WHERE key_name='d3d9_VSforce11'
UNION ALL
SELECT id, 'ru', 'Разрешить программный рендеринг' FROM Commands WHERE key_name='d3d9_AllowSoftware'
UNION ALL
SELECT id, 'ru', 'Размер pipeline-буфера' FROM Commands WHERE key_name='d3d9_pip_buff_size'
UNION ALL
SELECT id, 'ru', 'Размер пула вершинных буферов' FROM Commands WHERE key_name='d3d9_VBPoolSize'
UNION ALL
SELECT id, 'ru', 'Тип батчинга' FROM Commands WHERE key_name='r_BatchType'
UNION ALL
SELECT id, 'ru', 'Батчинг' FROM Commands WHERE key_name='r_Batching'
UNION ALL
SELECT id, 'ru', 'Батчинг материалов' FROM Commands WHERE key_name='r_MaterialsBatching'
UNION ALL
SELECT id, 'ru', 'Тени для NVIDIA 3D Vision' FROM Commands WHERE key_name='r_3dvision_bubbleshadow'
UNION ALL
SELECT id, 'ru', 'Адаптивные тени Aion' FROM Commands WHERE key_name='r_aionshadow_adaptive'
UNION ALL
SELECT id, 'ru', 'Размытие теней Aion' FROM Commands WHERE key_name='r_aionshadow_blur'
UNION ALL
SELECT id, 'ru', 'Размер объектов для теней Aion' FROM Commands WHERE key_name='r_aionshadow_obj_size'
UNION ALL
SELECT id, 'ru', 'Высота текстуры теней Aion' FROM Commands WHERE key_name='r_aionshadow_tex_height'
UNION ALL
SELECT id, 'ru', 'Режим антиалиасинга' FROM Commands WHERE key_name='r_AntialiasingMode'
UNION ALL
SELECT id, 'ru', 'Яркость' FROM Commands WHERE key_name='r_Brightness'
UNION ALL
SELECT id, 'ru', 'LOD-смещение персонажа' FROM Commands WHERE key_name='r_CharacterLODBias'
UNION ALL
SELECT id, 'ru', 'Хроматическая аберрация' FROM Commands WHERE key_name='r_ChromaticAberration'
UNION ALL
SELECT id, 'ru', 'Битность цвета' FROM Commands WHERE key_name='r_ColorBits'
UNION ALL
SELECT id, 'ru', 'Цветокоррекция' FROM Commands WHERE key_name='r_ColorGrading'
UNION ALL
SELECT id, 'ru', 'Ambient-освещение в deferred shading' FROM Commands WHERE key_name='r_DeferredShadingAmbientLights'
UNION ALL
SELECT id, 'ru', 'Глубина резкости' FROM Commands WHERE key_name='r_DepthOfField'
UNION ALL
SELECT id, 'ru', 'Детализация' FROM Commands WHERE key_name='r_Detail'
UNION ALL
SELECT id, 'ru', 'FOV для ближней отрисовки' FROM Commands WHERE key_name='r_DrawNearFOV'
UNION ALL
SELECT id, 'ru', 'Z-диапазон ближней отрисовки' FROM Commands WHERE key_name='r_DrawNearZRange'
UNION ALL
SELECT id, 'ru', 'Максимальный размер атласа облаков' FROM Commands WHERE key_name='r_DynTexAtlasCloudsMaxSize'
UNION ALL
SELECT id, 'ru', 'Максимальный размер атласа спрайтов' FROM Commands WHERE key_name='r_DynTexAtlasSpritesMaxSize'
UNION ALL
SELECT id, 'ru', 'Максимальный размер динамических текстур' FROM Commands WHERE key_name='r_DynTexMaxSize'
UNION ALL
SELECT id, 'ru', 'Улучшение изображения' FROM Commands WHERE key_name='r_EnhanceImage'
UNION ALL
SELECT id, 'ru', 'Разрешение cubemap окружения' FROM Commands WHERE key_name='r_EnvCMResolution'
UNION ALL
SELECT id, 'ru', 'Интервал обновления cubemap' FROM Commands WHERE key_name='r_EnvCMupdateInterval'
UNION ALL
SELECT id, 'ru', 'Размер light cubemap окружения' FROM Commands WHERE key_name='r_EnvLightCMSize'
UNION ALL
SELECT id, 'ru', 'Разрешение текстур окружения' FROM Commands WHERE key_name='r_EnvTexResolution'
UNION ALL
SELECT id, 'ru', 'Интервал обновления текстур окружения' FROM Commands WHERE key_name='r_EnvTexUpdateInterval'
UNION ALL
SELECT id, 'ru', 'Тесселяция бликов' FROM Commands WHERE key_name='r_FlaresTessellationRatio'
UNION ALL
SELECT id, 'ru', 'Тени от тумана' FROM Commands WHERE key_name='r_FogShadows'
UNION ALL
SELECT id, 'ru', 'Приоритет полноэкранного режима' FROM Commands WHERE key_name='r_FullscreenPreemption'
UNION ALL
SELECT id, 'ru', 'Высота fullscreen' FROM Commands WHERE key_name='r_FullScreenHeight'
UNION ALL
SELECT id, 'ru', 'Ширина fullscreen' FROM Commands WHERE key_name='r_FullScreenWidth'
UNION ALL
SELECT id, 'ru', 'Соотношение HDR-свечения' FROM Commands WHERE key_name='r_HDRBloomRatio'
UNION ALL
SELECT id, 'ru', 'Уровень яркости HDR' FROM Commands WHERE key_name='r_HDRBrightLevel'
UNION ALL
SELECT id, 'ru', 'Зернистость HDR' FROM Commands WHERE key_name='r_HDRGrainAmount'
UNION ALL
SELECT id, 'ru', 'Смещение LOD' FROM Commands WHERE key_name='r_LodBias'
UNION ALL
SELECT id, 'ru', 'Предзагрузка мешей' FROM Commands WHERE key_name='r_MeshPrecache'
UNION ALL
SELECT id, 'ru', 'Размытие в движении' FROM Commands WHERE key_name='r_MotionBlur'
UNION ALL
SELECT id, 'ru', 'Рендер глубины MRT' FROM Commands WHERE key_name='r_mrt_depthrender'
UNION ALL
SELECT id, 'ru', 'Определение MRT при инициализации' FROM Commands WHERE key_name='r_mrt_initdetect';
INSERT OR IGNORE INTO CommandTranslations (command_id, lang, description)
SELECT id, 'ru', 'Мультисэмплинг MSAA' FROM Commands WHERE key_name='r_MSAA'
UNION ALL
SELECT id, 'ru', 'Поддержка нескольких GPU' FROM Commands WHERE key_name='r_MultiGPU'
UNION ALL
SELECT id, 'ru', 'Полу-разрешение частиц' FROM Commands WHERE key_name='r_ParticlesHalfRes'
UNION ALL
SELECT id, 'ru', 'Режим блендинга half-res частиц' FROM Commands WHERE key_name='r_ParticlesHalfResBlendMode'
UNION ALL
SELECT id, 'ru', 'Motion blur для частиц' FROM Commands WHERE key_name='r_ParticlesMotionBlur'
UNION ALL
SELECT id, 'ru', 'Тесселяция частиц' FROM Commands WHERE key_name='r_ParticlesTessellation'
UNION ALL
SELECT id, 'ru', 'Постобработка антиалиасинга' FROM Commands WHERE key_name='r_PostAA'
UNION ALL
SELECT id, 'ru', 'Фильтр краёв пост-AA' FROM Commands WHERE key_name='r_PostAAEdgeFilter'
UNION ALL
SELECT id, 'ru', 'Постпроцессинг эффектов' FROM Commands WHERE key_name='r_PostProcessEffects'
UNION ALL
SELECT id, 'ru', 'Постпроцессинг игровых FX' FROM Commands WHERE key_name='r_PostProcessEffectsGameFx'
UNION ALL
SELECT id, 'ru', 'Фильтры постобработки' FROM Commands WHERE key_name='r_PostProcessFilters'
UNION ALL
SELECT id, 'ru', 'Постпроцессинг GameFX' FROM Commands WHERE key_name='r_PostProcessGameFx'
UNION ALL
SELECT id, 'ru', 'Процедурные блики' FROM Commands WHERE key_name='r_ProcFlares'
UNION ALL
SELECT id, 'ru', 'Псевдо-полноэкранный режим' FROM Commands WHERE key_name='r_PseudoFullscreen'
UNION ALL
SELECT id, 'ru', 'Качество bump-mapping' FROM Commands WHERE key_name='r_Quality_BumpMapping'
UNION ALL
SELECT id, 'ru', 'Дождь' FROM Commands WHERE key_name='r_rain'
UNION ALL
SELECT id, 'ru', 'Резкость' FROM Commands WHERE key_name='r_Sharpening'
UNION ALL
SELECT id, 'ru', 'Джиттеринг теней' FROM Commands WHERE key_name='r_ShadowJittering'
UNION ALL
SELECT id, 'ru', 'SSAO (ambient occlusion)' FROM Commands WHERE key_name='r_ssao'
UNION ALL
SELECT id, 'ru', 'SSDO' FROM Commands WHERE key_name='r_ssdo'
UNION ALL
SELECT id, 'ru', 'Screen-space reflections' FROM Commands WHERE key_name='r_SSReflections'
UNION ALL
SELECT id, 'ru', 'Битность stencil-буфера' FROM Commands WHERE key_name='r_StencilBits'
UNION ALL
SELECT id, 'ru', 'Солнечные лучи (god rays)' FROM Commands WHERE key_name='r_sunshafts'
UNION ALL
SELECT id, 'ru', 'Синхронизация вершинного буфера' FROM Commands WHERE key_name='r_SyncVBuf'
UNION ALL
SELECT id, 'ru', 'Максимум анизотропной фильтрации' FROM Commands WHERE key_name='r_TexMaxAnisotropy'
UNION ALL
SELECT id, 'ru', 'Потоковая загрузка текстур' FROM Commands WHERE key_name='r_TextureStreaming'
UNION ALL
SELECT id, 'ru', 'Пропускать mip-уровни при стриминге' FROM Commands WHERE key_name='r_TexturesStreamingSkipMips'
UNION ALL
SELECT id, 'ru', 'Прогрев текстур' FROM Commands WHERE key_name='r_TexturesWarmup'
UNION ALL
SELECT id, 'ru', 'Шейдинг UI' FROM Commands WHERE key_name='r_ui_shading'
UNION ALL
SELECT id, 'ru', 'Форсировать half-res частиц' FROM Commands WHERE key_name='r_UseParticlesHalfResForce'
UNION ALL
SELECT id, 'ru', 'Объединение частиц' FROM Commands WHERE key_name='r_UseParticlesMerging'
UNION ALL
SELECT id, 'ru', 'Рефракция частиц' FROM Commands WHERE key_name='r_UseParticlesRefraction'
UNION ALL
SELECT id, 'ru', 'Мягкие частицы' FROM Commands WHERE key_name='r_UseSoftParticles'
UNION ALL
SELECT id, 'ru', 'Разрешение спрайтов растительности' FROM Commands WHERE key_name='r_VegetationSpritesTexRes'
UNION ALL
SELECT id, 'ru', 'Объёмный туман' FROM Commands WHERE key_name='r_VolumetricFog'
UNION ALL
SELECT id, 'ru', 'Каустика воды' FROM Commands WHERE key_name='r_WaterCaustics'
UNION ALL
SELECT id, 'ru', 'God rays на воде' FROM Commands WHERE key_name='r_WaterGodRays'
UNION ALL
SELECT id, 'ru', 'Дистанция объединения зон' FROM Commands WHERE key_name='e_area_merging_distance'
UNION ALL
SELECT id, 'ru', 'Автопредзагрузка CGF' FROM Commands WHERE key_name='e_AutoPrecacheCgf'
UNION ALL
SELECT id, 'ru', 'Минимальный LOD персонажа' FROM Commands WHERE key_name='e_CharLodMin'
UNION ALL
SELECT id, 'ru', 'Активация отсечения растительности' FROM Commands WHERE key_name='e_CullVegActivation'
UNION ALL
SELECT id, 'ru', 'Разрешить игровые декали' FROM Commands WHERE key_name='e_DecalsAllowGameDecals'
UNION ALL
SELECT id, 'ru', 'Масштаб времени жизни декалей' FROM Commands WHERE key_name='e_DecalsLifeTimeScale'
UNION ALL
SELECT id, 'ru', 'Растворение объектов' FROM Commands WHERE key_name='e_Dissolve'
UNION ALL
SELECT id, 'ru', 'Динамические источники света' FROM Commands WHERE key_name='e_DynamicLights'
UNION ALL
SELECT id, 'ru', 'Качество эффектов' FROM Commands WHERE key_name='e_effect_quality'
UNION ALL
SELECT id, 'ru', 'Дистанция видимости сущностей' FROM Commands WHERE key_name='e_ent_view_dist_ratio'
UNION ALL
SELECT id, 'ru', 'Туман' FROM Commands WHERE key_name='e_fog'
UNION ALL
SELECT id, 'ru', 'Global Illumination' FROM Commands WHERE key_name='e_GI'
UNION ALL
SELECT id, 'ru', 'Кеш GSM-теней' FROM Commands WHERE key_name='e_GsmCache';
INSERT OR IGNORE INTO CommandTranslations (command_id, lang, description)
SELECT id, 'ru', 'Количество LOD GSM' FROM Commands WHERE key_name='e_GsmLodsNum'
UNION ALL
SELECT id, 'ru', 'HW-отсечение объектов' FROM Commands WHERE key_name='e_HwOcclusionCullingObjects'
UNION ALL
SELECT id, 'ru', 'HW-отсечение частиц' FROM Commands WHERE key_name='e_HwOcclusionCullingparticles'
UNION ALL
SELECT id, 'ru', 'HW-отсечение растительности' FROM Commands WHERE key_name='e_HwOcclusionCullingVegetation'
UNION ALL
SELECT id, 'ru', 'HW-отсечение воды' FROM Commands WHERE key_name='e_HwOcclusionCullingWater'
UNION ALL
SELECT id, 'ru', 'HW-отсечение воды (старое)' FROM Commands WHERE key_name='e_hw_occlusion_culling_water'
UNION ALL
SELECT id, 'ru', 'Включить видео-джукбокс' FROM Commands WHERE key_name='e_jukebox_movie_enable'
UNION ALL
SELECT id, 'ru', 'Уровень' FROM Commands WHERE key_name='e_level'
UNION ALL
SELECT id, 'ru', 'Максимальный размер LOD-компонента' FROM Commands WHERE key_name='e_LodCompMaxSize'
UNION ALL
SELECT id, 'ru', 'Минимальный LOD' FROM Commands WHERE key_name='e_LodMin'
UNION ALL
SELECT id, 'ru', 'Мин. треугольников для LOD' FROM Commands WHERE key_name='e_LodMinTtris'
UNION ALL
SELECT id, 'ru', 'Форсировать использование LOD' FROM Commands WHERE key_name='e_LodsForceUse'
UNION ALL
SELECT id, 'ru', 'Макс. дистанция интерполяции вида' FROM Commands WHERE key_name='e_MaxViewDistSpecLerp'
UNION ALL
SELECT id, 'ru', 'Не рисовать тень ландшафта' FROM Commands WHERE key_name='e_nodraw_terrain_shadow'
UNION ALL
SELECT id, 'ru', 'Дистанция occlusion culling' FROM Commands WHERE key_name='e_OcclusionCullingViewDistRatio'
UNION ALL
SELECT id, 'ru', 'Оптимизация рендер-объектов' FROM Commands WHERE key_name='e_optimized_render_object'
UNION ALL
SELECT id, 'ru', 'Качество объектов' FROM Commands WHERE key_name='e_ObjQuality'
UNION ALL
SELECT id, 'ru', 'Diffuse cubemap для частиц' FROM Commands WHERE key_name='e_ParticlesDiffCM'
UNION ALL
SELECT id, 'ru', 'Форсировать мягкие частицы' FROM Commands WHERE key_name='e_ParticlesForceSoftParticles'
UNION ALL
SELECT id, 'ru', 'Global Illumination для частиц' FROM Commands WHERE key_name='e_ParticlesGI'
UNION ALL
SELECT id, 'ru', 'Макс. размер частиц на экране' FROM Commands WHERE key_name='e_ParticlesMaxDrawScreen'
UNION ALL
SELECT id, 'ru', 'Макс. заполнение экрана частицами' FROM Commands WHERE key_name='e_ParticlesMaxScreenFill'
UNION ALL
SELECT id, 'ru', 'Мин. размер частиц в пикселях' FROM Commands WHERE key_name='e_ParticlesMinDrawPixels'
UNION ALL
SELECT id, 'ru', 'Коллизии частиц с объектами' FROM Commands WHERE key_name='e_ParticlesObjectCollisions'
UNION ALL
SELECT id, 'ru', 'Предзагрузка частиц' FROM Commands WHERE key_name='e_ParticlesPreload'
UNION ALL
SELECT id, 'ru', 'Качество частиц' FROM Commands WHERE key_name='e_ParticlesQuality'
UNION ALL
SELECT id, 'ru', 'Тени от частиц' FROM Commands WHERE key_name='e_ParticlesShadows'
UNION ALL
SELECT id, 'ru', 'Поток для частиц' FROM Commands WHERE key_name='e_ParticlesThread'
UNION ALL
SELECT id, 'ru', 'Уровень предзагрузки' FROM Commands WHERE key_name='e_precache_level'
UNION ALL
SELECT id, 'ru', 'Уровень предзагрузки' FROM Commands WHERE key_name='e_PrecacheLevel'
UNION ALL
SELECT id, 'ru', 'Предзагрузка материалов' FROM Commands WHERE key_name='e_PreloadMaterials'
UNION ALL
SELECT id, 'ru', 'Подготовка деформируемых объектов при загрузке' FROM Commands WHERE key_name='e_PrepareDeformableObjectsAtLoadTime'
UNION ALL
SELECT id, 'ru', 'Процедурная растительность' FROM Commands WHERE key_name='e_proc_vegetation'
UNION ALL
SELECT id, 'ru', 'Рекурсия' FROM Commands WHERE key_name='e_Recursion'
UNION ALL
SELECT id, 'ru', 'Рекурсивное occlusion culling' FROM Commands WHERE key_name='e_recursion_occlusion_culling'
UNION ALL
SELECT id, 'ru', 'Рендер' FROM Commands WHERE key_name='e_Render'
UNION ALL
SELECT id, 'ru', 'Тени' FROM Commands WHERE key_name='e_shadows'
UNION ALL
SELECT id, 'ru', 'Пропустить отсечение ландшафта' FROM Commands WHERE key_name='e_skip_terrain_culling'
UNION ALL
SELECT id, 'ru', 'Небесный куб' FROM Commands WHERE key_name='e_SkyBox'
UNION ALL
SELECT id, 'ru', 'Качество неба' FROM Commands WHERE key_name='e_SkyQuality'
UNION ALL
SELECT id, 'ru', 'Тип неба' FROM Commands WHERE key_name='e_SkyType'
UNION ALL
SELECT id, 'ru', 'Буфер задач рендера статических объектов' FROM Commands WHERE key_name='e_StatObjBufferRenderTasks'
UNION ALL
SELECT id, 'ru', 'Предзагрузка статических объектов' FROM Commands WHERE key_name='e_StatObjPreload'
UNION ALL
SELECT id, 'ru', 'Стриминг CGF' FROM Commands WHERE key_name='e_streamCgf'
UNION ALL
SELECT id, 'ru', 'Солнце' FROM Commands WHERE key_name='e_sun'
UNION ALL
SELECT id, 'ru', 'Ambient Occlusion ландшафта' FROM Commands WHERE key_name='e_TerrainAo'
UNION ALL
SELECT id, 'ru', 'LOD ландшафта' FROM Commands WHERE key_name='e_TerrainLodRatio'
UNION ALL
SELECT id, 'ru', 'Макс. дистанция occlusion culling ландшафта' FROM Commands WHERE key_name='e_TerrainOcclusionCullingMaxDist'
UNION ALL
SELECT id, 'ru', 'LOD текстур ландшафта' FROM Commands WHERE key_name='e_TerrainTextureLodRatio'
UNION ALL
SELECT id, 'ru', 'Смещение LOD текстур ландшафта' FROM Commands WHERE key_name='e_TerrainTextureLodRatioBias';
INSERT OR IGNORE INTO CommandTranslations (command_id, lang, description)
SELECT id, 'ru', 'Использовать запасной шейдер' FROM Commands WHERE key_name='e_use_backup_shader'
UNION ALL
SELECT id, 'ru', 'Тень ландшафта от источника света' FROM Commands WHERE key_name='e_use_terrain_shadow_light'
UNION ALL
SELECT id, 'ru', 'Изгиб растительности' FROM Commands WHERE key_name='e_VegetationBending'
UNION ALL
SELECT id, 'ru', 'Минимальный размер растительности' FROM Commands WHERE key_name='e_VegetationMinSize'
UNION ALL
SELECT id, 'ru', 'Static instancing растительности' FROM Commands WHERE key_name='e_vegetation_static_instancing'
UNION ALL
SELECT id, 'ru', 'Спрайты растительности' FROM Commands WHERE key_name='e_VegetationSprites'
UNION ALL
SELECT id, 'ru', 'Батчинг спрайтов растительности' FROM Commands WHERE key_name='e_VegetationSpritesBatching'
UNION ALL
SELECT id, 'ru', 'Мин. дистанция кастомных спрайтов' FROM Commands WHERE key_name='e_VegetationSpritesDistanceCustomRatioMin'
UNION ALL
SELECT id, 'ru', 'Мин. дистанция спрайтов' FROM Commands WHERE key_name='e_VegetationSpritesDistanceatioMin'
UNION ALL
SELECT id, 'ru', 'Цвет растительности от ландшафта' FROM Commands WHERE key_name='e_VegetationUseTerrainColor'
UNION ALL
SELECT id, 'ru', 'Дистанция видимости' FROM Commands WHERE key_name='e_ViewDistRatio'
UNION ALL
SELECT id, 'ru', 'Кастомная дистанция видимости' FROM Commands WHERE key_name='e_ViewDistRatioCustom'
UNION ALL
SELECT id, 'ru', 'Дистанция деталей' FROM Commands WHERE key_name='e_ViewDistRatioDetail'
UNION ALL
SELECT id, 'ru', 'Дистанция видимости источников света' FROM Commands WHERE key_name='e_ViewDistRatioLights'
UNION ALL
SELECT id, 'ru', 'Дистанция видимости растительности' FROM Commands WHERE key_name='e_ViewDistRatioVegetation'
UNION ALL
SELECT id, 'ru', 'Дистанция видимости' FROM Commands WHERE key_name='e_view_dist_ratio'
UNION ALL
SELECT id, 'ru', 'Дистанция деталей' FROM Commands WHERE key_name='e_view_dist_ratio_detail'
UNION ALL
SELECT id, 'ru', 'Дистанция растительности' FROM Commands WHERE key_name='e_view_dist_ratio_vegetation'
UNION ALL
SELECT id, 'ru', 'Дистанция видимости растительности' FROM Commands WHERE key_name='e_view_dist_vegetation'
UNION ALL
SELECT id, 'ru', 'Мягкие частицы на воде' FROM Commands WHERE key_name='e_water_ocean_soft_particles'
UNION ALL
SELECT id, 'ru', 'Ветер' FROM Commands WHERE key_name='e_wind'
UNION ALL
SELECT id, 'ru', 'Океан' FROM Commands WHERE key_name='e_waterocean'
UNION ALL
SELECT id, 'ru', 'Ограничение ошибок анимации' FROM Commands WHERE key_name='ac_animErrorClamp'
UNION ALL
SELECT id, 'ru', 'Ограничение времени анимации' FROM Commands WHERE key_name='ac_clampTimeAnimation'
UNION ALL
SELECT id, 'ru', 'Ограничение времени сущности' FROM Commands WHERE key_name='ac_clampTimeEntity'
UNION ALL
SELECT id, 'ru', 'Отключить fancy-переходы' FROM Commands WHERE key_name='ac_disableFancyTransitions'
UNION ALL
SELECT id, 'ru', 'Минимальный LOD персонажа' FROM Commands WHERE key_name='ca_CharLodMin'
UNION ALL
SELECT id, 'ru', 'Дефрагментация памяти' FROM Commands WHERE key_name='ca_MemoryDefragEnabled'
UNION ALL
SELECT id, 'ru', 'Предзагрузка наборов анимаций' FROM Commands WHERE key_name='ca_PrecacheAnimationSets'
UNION ALL
SELECT id, 'ru', 'Общие вершины' FROM Commands WHERE key_name='ca_ShareVertex'
UNION ALL
SELECT id, 'ru', 'Кеш анимаций' FROM Commands WHERE key_name='ca_UseAnimationsCache'
UNION ALL
SELECT id, 'ru', 'Лицевая анимация' FROM Commands WHERE key_name='ca_UseFacialAnimation'
UNION ALL
SELECT id, 'ru', 'Физика персонажа' FROM Commands WHERE key_name='ca_UsePhysics'
UNION ALL
SELECT id, 'ru', 'Отключить поток анимации' FROM Commands WHERE key_name='ca_disable_thread'
UNION ALL
SELECT id, 'ru', 'Форсировать LOD' FROM Commands WHERE key_name='ca_lod_force'
UNION ALL
SELECT id, 'ru', 'Соотношение LOD' FROM Commands WHERE key_name='ca_lod_ratio'
UNION ALL
SELECT id, 'ru', 'Поток для анимации' FROM Commands WHERE key_name='ca_thread'
UNION ALL
SELECT id, 'ru', 'Ambient fire (огонь в мире)' FROM Commands WHERE key_name='ai_AmbientFireEnable'
UNION ALL
SELECT id, 'ru', 'Квота ambient fire' FROM Commands WHERE key_name='ai_AmbientFireQuota'
UNION ALL
SELECT id, 'ru', 'Интервал обновления ambient fire' FROM Commands WHERE key_name='ai_AmbientFireUpdateInterval'
UNION ALL
SELECT id, 'ru', 'Отладка ambient fire' FROM Commands WHERE key_name='ai_DebugDrawAmbientFire'
UNION ALL
SELECT id, 'ru', 'DirectInput-клавиши' FROM Commands WHERE key_name='i_dinputkeys'
UNION ALL
SELECT id, 'ru', 'Объём тумана у фонаря' FROM Commands WHERE key_name='i_flashlight_has_fog_volume'
UNION ALL
SELECT id, 'ru', 'Ускорение мыши' FROM Commands WHERE key_name='i_mouse_accel'
UNION ALL
SELECT id, 'ru', 'Инерция мыши' FROM Commands WHERE key_name='i_mouse_inertia'
UNION ALL
SELECT id, 'ru', 'Сглаживание мыши' FROM Commands WHERE key_name='i_mouse_smooth'
UNION ALL
SELECT id, 'ru', 'Предзагрузка ввода' FROM Commands WHERE key_name='i_precache'
UNION ALL
SELECT id, 'ru', 'Потоковый ввод' FROM Commands WHERE key_name='iThreaded'
UNION ALL
SELECT id, 'ru', 'Эффекты частиц' FROM Commands WHERE key_name='i_particleeffects'
UNION ALL
SELECT id, 'ru', 'Отклонять эффекты' FROM Commands WHERE key_name='i_rejecteffects';
INSERT OR IGNORE INTO CommandTranslations (command_id, lang, description)
SELECT id, 'ru', 'Ледяные эффекты' FROM Commands WHERE key_name='i_iceeffects'
UNION ALL
SELECT id, 'ru', 'Дальность света' FROM Commands WHERE key_name='p_lightrange'
UNION ALL
SELECT id, 'ru', 'Общий шейдер' FROM Commands WHERE key_name='q_ShaderGeneral'
UNION ALL
SELECT id, 'ru', 'Шейдер постобработки' FROM Commands WHERE key_name='q_ShaderPostProcess'
UNION ALL
SELECT id, 'ru', 'Шейдер ландшафта' FROM Commands WHERE key_name='q_ShaderTerrain'
UNION ALL
SELECT id, 'ru', 'Шейдер растительности' FROM Commands WHERE key_name='q_ShaderVegetation'
UNION ALL
SELECT id, 'ru', 'Ограниченная консоль' FROM Commands WHERE key_name='con_restricted'
UNION ALL
SELECT id, 'ru', 'Размер heap Aion' FROM Commands WHERE key_name='g_aionHeapSize'
UNION ALL
SELECT id, 'ru', 'Уровень FX' FROM Commands WHERE key_name='g_fxLevel'
UNION ALL
SELECT id, 'ru', 'Физика частиц на GPU' FROM Commands WHERE key_name='g_gpu_particle_physics'
UNION ALL
SELECT id, 'ru', 'Состояние загрузки слота' FROM Commands WHERE key_name='g_loadSlotState'
UNION ALL
SELECT id, 'ru', 'Отключить звук питомца' FROM Commands WHERE key_name='g_muteMyPet'
UNION ALL
SELECT id, 'ru', 'Громкость OBS' FROM Commands WHERE key_name='g_OBS_volume'
UNION ALL
SELECT id, 'ru', 'Открыть особый список серверов' FROM Commands WHERE key_name='g_openSpecialServerList'
UNION ALL
SELECT id, 'ru', 'Профиль игрока' FROM Commands WHERE key_name='g_playerprofile'
UNION ALL
SELECT id, 'ru', 'Радиальное размытие' FROM Commands WHERE key_name='g_radialBlur'
UNION ALL
SELECT id, 'ru', 'Возможность переподключения' FROM Commands WHERE key_name='g_reconnectable'
UNION ALL
SELECT id, 'ru', 'Путь скриншотов' FROM Commands WHERE key_name='g_screenshot_preset_path'
UNION ALL
SELECT id, 'ru', 'Сообщения действий UI' FROM Commands WHERE key_name='g_showUIActionMsg'
UNION ALL
SELECT id, 'ru', 'Задержка UI телепорта' FROM Commands WHERE key_name='g_teleportUIDelay'
UNION ALL
SELECT id, 'ru', 'ID интерполяции UI' FROM Commands WHERE key_name='g_ui_interpolation_id'
UNION ALL
SELECT id, 'ru', 'Тип интерполяции UI' FROM Commands WHERE key_name='g_ui_interpolation_type'
UNION ALL
SELECT id, 'ru', 'Тень UI' FROM Commands WHERE key_name='g_ui_shadow'
UNION ALL
SELECT id, 'ru', 'Опции осады' FROM Commands WHERE key_name='g_ui_siegewarfare_option'
UNION ALL
SELECT id, 'ru', 'Тип tile UI' FROM Commands WHERE key_name='g_ui_tile_type'
UNION ALL
SELECT id, 'ru', 'Анимации переходов' FROM Commands WHERE key_name='g_useTransitionAnimation'
UNION ALL
SELECT id, 'ru', 'Свечение (GLOW)' FROM Commands WHERE key_name='g_video_GLOW'
UNION ALL
SELECT id, 'ru', 'Физика частиц на GPU' FROM Commands WHERE key_name='gpu_particle_physics'
UNION ALL
SELECT id, 'ru', 'Отладка HUD' FROM Commands WHERE key_name='hud_debug'
UNION ALL
SELECT id, 'ru', 'HUD на паузе при старте' FROM Commands WHERE key_name='hud_startpaused'
UNION ALL
SELECT id, 'ru', 'Порог приоритета' FROM Commands WHERE key_name='PriorityThreshold'
UNION ALL
SELECT id, 'ru', 'MRT-профиль: фон' FROM Commands WHERE key_name='g_cfg_video_MRT_BACKGROUND'
UNION ALL
SELECT id, 'ru', 'MRT-профиль: bump-маппинг' FROM Commands WHERE key_name='g_cfg_video_MRT_BUMP'
UNION ALL
SELECT id, 'ru', 'MRT-профиль: камера' FROM Commands WHERE key_name='g_cfg_video_MRT_CAMERA'
UNION ALL
SELECT id, 'ru', 'MRT-профиль: глубина резкости' FROM Commands WHERE key_name='g_cfg_video_MRT_DOF'
UNION ALL
SELECT id, 'ru', 'MRT-профиль: эффекты' FROM Commands WHERE key_name='g_cfg_video_MRT_EFFECT'
UNION ALL
SELECT id, 'ru', 'MRT-профиль: дистанция сущностей' FROM Commands WHERE key_name='g_cfg_video_MRT_ENTITY_DIST'
UNION ALL
SELECT id, 'ru', 'MRT-профиль: текстуры окружения' FROM Commands WHERE key_name='g_cfg_video_MRT_ENV_TEX'
UNION ALL
SELECT id, 'ru', 'MRT-профиль: сглаживание' FROM Commands WHERE key_name='g_cfg_video_MRT_FSAA'
UNION ALL
SELECT id, 'ru', 'MRT-профиль: общий' FROM Commands WHERE key_name='g_cfg_video_MRT_GENERAL'
UNION ALL
SELECT id, 'ru', 'MRT-профиль: блики' FROM Commands WHERE key_name='g_cfg_video_MRT_GLARE'
UNION ALL
SELECT id, 'ru', 'MRT-профиль: свечение' FROM Commands WHERE key_name='g_cfg_video_MRT_GLOW'
UNION ALL
SELECT id, 'ru', 'MRT-профиль: минимальный' FROM Commands WHERE key_name='g_cfg_video_MRT_LOWEST'
UNION ALL
SELECT id, 'ru', 'MRT-профиль: кеш моделей' FROM Commands WHERE key_name='g_cfg_video_MRT_MODEL_CACHE'
UNION ALL
SELECT id, 'ru', 'MRT-профиль: шейдеры' FROM Commands WHERE key_name='g_cfg_video_MRT_SHADER'
UNION ALL
SELECT id, 'ru', 'MRT-профиль: тени' FROM Commands WHERE key_name='g_cfg_video_MRT_SHADOW'
UNION ALL
SELECT id, 'ru', 'MRT-профиль: эффекты скиллов' FROM Commands WHERE key_name='g_cfg_video_MRT_SKILLFX'
UNION ALL
SELECT id, 'ru', 'MRT-профиль: солнечные лучи' FROM Commands WHERE key_name='g_cfg_video_MRT_SUNSHAFT'
UNION ALL
SELECT id, 'ru', 'MRT-профиль: дистанция ландшафта' FROM Commands WHERE key_name='g_cfg_video_MRT_TERRAIN_DIST'
UNION ALL
SELECT id, 'ru', 'MRT-профиль: текстуры' FROM Commands WHERE key_name='g_cfg_video_MRT_TEXTURE';
INSERT OR IGNORE INTO CommandTranslations (command_id, lang, description)
SELECT id, 'ru', 'MRT-профиль: вода' FROM Commands WHERE key_name='g_cfg_video_MRT_WATER'
UNION ALL
SELECT id, 'ru', 'MRT-профиль: погодные слои' FROM Commands WHERE key_name='g_cfg_video_MRT_WEATHERLAYER'
UNION ALL
SELECT id, 'ru', 'Уровень видео-эффектов' FROM Commands WHERE key_name='g_cfg_video_EFFECT'
UNION ALL
SELECT id, 'ru', 'Режим энергосбережения (отключает звук при низком заряде)' FROM Commands WHERE key_name='s_BatterySave_Enable'
UNION ALL
SELECT id, 'ru', 'Частота дискретизации звука (Гц)' FROM Commands WHERE key_name='s_FormatSampleRate'
UNION ALL
SELECT id, 'ru', 'HRTF (объёмный звук в наушниках)' FROM Commands WHERE key_name='s_HRTFEnable'
UNION ALL
SELECT id, 'ru', 'Игнорировать статус игры для музыки' FROM Commands WHERE key_name='s_MusicIgnoreGameStatus'
UNION ALL
SELECT id, 'ru', 'Отключить музыку' FROM Commands WHERE key_name='s_MusicMute'
UNION ALL
SELECT id, 'ru', 'Играть музыку один раз' FROM Commands WHERE key_name='s_MusicPlayOnce'
UNION ALL
SELECT id, 'ru', 'Громкость музыки' FROM Commands WHERE key_name='s_MusicVolume'
UNION ALL
SELECT id, 'ru', 'Пинг NPC-звуков' FROM Commands WHERE key_name='s_NCPing_Enable'
UNION ALL
SELECT id, 'ru', 'Порог приоритета звука' FROM Commands WHERE key_name='s_PriorityThreshold'
UNION ALL
SELECT id, 'ru', 'Уровень шейдинга звука (устаревшее)' FROM Commands WHERE key_name='s_spec_Shading'
UNION ALL
SELECT id, 'ru', 'Отключить музыку (дубль)' FROM Commands WHERE key_name='ss_MusicMute';
INSERT OR IGNORE INTO CommandTranslations (command_id, lang, description)
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_2dDamage'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_2dDamageCri'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_2dDamageCriT2'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_2dDamageMargin'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_2dDamageOffset'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_2dDamageR'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_2dDamageSize'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_2dDamageSize2'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_2dDamageT1'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_2dDamageT2'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_2dDamageT3'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_2dDamageT4'
UNION ALL
SELECT id, 'en', 'Battle camera' FROM Commands WHERE key_name='g_battleCamActive'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_battleCamRadius'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_battleCamSmallR'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_battleCamWeight'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_battleCamWeightNear'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_cam_key_rot'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_cam_p_max'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_cam_p_min'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_cam_rot_ratio'
UNION ALL
SELECT id, 'en', 'Camera cheat mode' FROM Commands WHERE key_name='g_camera_cheat'
UNION ALL
SELECT id, 'en', 'Maximum camera distance' FROM Commands WHERE key_name='g_camMax'
UNION ALL
SELECT id, 'en', 'Mid camera distance' FROM Commands WHERE key_name='g_camMid'
UNION ALL
SELECT id, 'en', 'Minimum camera distance' FROM Commands WHERE key_name='g_camMin'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_camOffsetZ'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_camStep'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_captureIME'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_cfg_version'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_cfg_video_BACKGROUND'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_cfg_video_ENTITY_DIST'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_cfg_video_ENV_TEX'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_cfg_video_FSAA'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_cfg_video_GENERAL'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_cfg_video_GLARE'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_cfg_video_GLOW'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_cfg_video_MODEL_CACHE'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_cfg_video_screen_res'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_cfg_video_SHADER'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_cfg_video_SHADOW'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_cfg_video_SKILLFX'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_cfg_video_TERRAIN_DIST'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_cfg_video_TEXTURE'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_cfg_video_WATER'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_cfg_video_WEATHER'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_chainSkillChangeCooltimeDelay'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_chainSkillIndicateDelay'
UNION ALL
SELECT id, 'en', 'Character manager' FROM Commands WHERE key_name='g_char_manager'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_charCustomColor'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_CharRotateSpeed';
INSERT OR IGNORE INTO CommandTranslations (command_id, lang, description)
SELECT id, 'en', 'Chat logging' FROM Commands WHERE key_name='g_chatlog'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_CheckDeadServer'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_damage_blend'
UNION ALL
SELECT id, 'en', 'Death camera' FROM Commands WHERE key_name='g_deathCamActive'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_deathCamDist'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_deathCamSpeedFO'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_deathCamSpeedP'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_deathCamSpeedZ'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_desolveEnd'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_desolveStart'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_disperse_loading'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_EffectPriorityDistance'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_fall_height'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_falx'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_faly'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_falz'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_fatx'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_faty'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_fatz'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_favx'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_favy'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_favz'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_fheight'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_fireCamOffset'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_fireCamSpeed'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_gameFlags'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_gameReplay'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_gameReplayControl'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_gameReplayName'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_gameReplaySpeed'
UNION ALL
SELECT id, 'en', 'Use GameGuard' FROM Commands WHERE key_name='g_ggAuth'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_headCamDegree'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_headCamDist'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_headCamStiff'
UNION ALL
SELECT id, 'en', 'Hide character model' FROM Commands WHERE key_name='g_hide'
UNION ALL
SELECT id, 'en', 'Hide UI' FROM Commands WHERE key_name='g_hide_ui'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_hit_freeze'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_hit_freeze_time'
UNION ALL
SELECT id, 'en', 'Camera shake on hit' FROM Commands WHERE key_name='g_hitCamActive'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_hitCamShake'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_hitCamShakeReduce'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_hitFxMonsterSize'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_IDDreScoreAlarm'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_idle002_time'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_IDLF1ScoreAlarm'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_IgnoreUICoolTime'
UNION ALL
SELECT id, 'en', 'Maximum FOV' FROM Commands WHERE key_name='g_maxFov'
UNION ALL
SELECT id, 'en', 'Maximum FPS (0 = unlimited)' FROM Commands WHERE key_name='g_maxfps'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_midFov'
UNION ALL
SELECT id, 'en', 'Minimum field of view' FROM Commands WHERE key_name='g_minFov';
INSERT OR IGNORE INTO CommandTranslations (command_id, lang, description)
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_MP_fixed_timestep'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_observe'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_pathfinding'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_Render'
UNION ALL
SELECT id, 'en', 'Save settings presets' FROM Commands WHERE key_name='g_save_preset'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_scaled_attack'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_scaled_attack_limit'
UNION ALL
SELECT id, 'en', 'Always show server select' FROM Commands WHERE key_name='g_select_server'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_send_level_version'
UNION ALL
SELECT id, 'en', 'Show breath' FROM Commands WHERE key_name='g_show_breath'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_show_create_btn'
UNION ALL
SELECT id, 'en', 'Show stun state' FROM Commands WHERE key_name='g_show_stunned'
UNION ALL
SELECT id, 'en', 'Show damage messages' FROM Commands WHERE key_name='g_showDamageMsg'
UNION ALL
SELECT id, 'en', 'Show FPS counter' FROM Commands WHERE key_name='g_showFps'
UNION ALL
SELECT id, 'en', 'Show macro debug' FROM Commands WHERE key_name='g_showMacroMsg'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_showPanningCursor'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_targetMarkerType'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_targetSound'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_tempPseudoFullscreen'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_test'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_testFxcSpawn'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_testIntersect'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_testPut'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_testRecvWorld'
UNION ALL
SELECT id, 'en', 'Auto-teleport (cheat)' FROM Commands WHERE key_name='g_testTeleport'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_ThirdPersonRange'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_thrust_time'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_ui_filter'
UNION ALL
SELECT id, 'en', 'UI font' FROM Commands WHERE key_name='g_ui_font'
UNION ALL
SELECT id, 'en', 'UI scale' FROM Commands WHERE key_name='g_ui_scale'
UNION ALL
SELECT id, 'en', 'Custom UI scale multiplier' FROM Commands WHERE key_name='g_ui_scale_factor'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_ui_stillview'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_ui_tile'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_uiContour'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_UIForTuning'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_uiFX'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_var1'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_var2'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_var3'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_var4'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_verbose'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_verbose_animation'
UNION ALL
SELECT id, 'en', 'Camera shake while walking' FROM Commands WHERE key_name='g_walkCamActive'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_walkCamAmp'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_walkCamFreq'
UNION ALL
SELECT id, 'en', 'Weapon scale' FROM Commands WHERE key_name='g_weapon_scale'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_windBox'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_draw_3dView'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_draw_radar'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_spf';
INSERT OR IGNORE INTO CommandTranslations (command_id, lang, description)
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_country_code'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_create_info'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_fmode'
UNION ALL
SELECT id, 'en', 'Fly cheat' FROM Commands WHERE key_name='g_freefly'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_fjump'
UNION ALL
SELECT id, 'en', 'Fullscreen mode' FROM Commands WHERE key_name='g_fullscreen'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_NoWarFog'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_glide'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_fly_height'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_auto_disconnect'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_rotate_speed'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_rotate_speed_mouse'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_tutorialReset'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_player_nameid'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_player_armor'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_player_armor_color'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_player_face'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_player_hair'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_player_skin_color'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_player_hair_color'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_player_body_scales'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_player_speed'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_player_pos'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_player_camera_shake'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_player_fx'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_smooth_move'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_blade_fx'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_blade_time'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_blade_tex'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_clear_attack_count'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_client_var'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_program_damage'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_blend1'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_blend2'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_mxID'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_player_scale'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_player_listener_pos'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_player_listener_height'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_sound_min_dist'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_sound_max_dist'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_blend_time'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_blendout_time'
UNION ALL
SELECT id, 'en', 'Auto camera zoom' FROM Commands WHERE key_name='g_autoZoom'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_autoZoomDegree'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_autoZoomSpeed'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_npcCamPosRatio'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_npcCamPosDist'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_npcCamAngleZ'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_npcCamAngleX'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_npcCamRange';
INSERT OR IGNORE INTO CommandTranslations (command_id, lang, description)
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_npcCamSpeedP'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_npcCamZ'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_npcCamFov'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_transCamStiffness'
UNION ALL
SELECT id, 'en', 'Open Aion website on exit' FROM Commands WHERE key_name='g_open_aion_web'
UNION ALL
SELECT id, 'en', 'Game effects' FROM Commands WHERE key_name='g_enableGameEffect'
UNION ALL
SELECT id, 'en', 'Skill voice lines' FROM Commands WHERE key_name='g_enableSkillVoice'
UNION ALL
SELECT id, 'en', 'Show damage messages' FROM Commands WHERE key_name='g_showDamageMsg'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_ammoHeightRatio'
UNION ALL
SELECT id, 'en', 'Blood and gore' FROM Commands WHERE key_name='g_gore'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_testPutUser'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_testRecvWorld'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_clbone'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_useRotateAnimation'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_charCustomColor'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_BlendSpine'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_2dDamageR'
UNION ALL
SELECT id, 'en', 'General gameplay setting' FROM Commands WHERE key_name='g_AutoWalkType'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_AccurateParticles'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_Beams'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_BumpSelfShadow'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_Char_AmbientColor_Amount'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_Char_SunColor_Amount'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_Character_Debug'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_Character_LOD_Bias'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_Character_NoAnim'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_Character_NoDeform'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_Character_NoPhys'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_Character_Shadow_Volume'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_checkSunVis'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_DebugLights'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_DebugScreenEffects'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_DecalTextures'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_depth_buffer'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_DepthBits'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_DetailDefault'
UNION ALL
SELECT id, 'en', 'Detail texture distance' FROM Commands WHERE key_name='r_DetailDistance'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_DetailNumLayers'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_DetailScale'
UNION ALL
SELECT id, 'en', 'Detail textures' FROM Commands WHERE key_name='r_DetailTextures'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_DisableSfx'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_DisplayInfo'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_EfMultiTex'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_EMBM'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_FadeAmount'
UNION ALL
SELECT id, 'en', 'Fullscreen anti-aliasing (FSAA)' FROM Commands WHERE key_name='r_FSAA'
UNION ALL
SELECT id, 'en', 'Anti-aliasing quality' FROM Commands WHERE key_name='r_FSAA_quality'
UNION ALL
SELECT id, 'en', 'Anti-aliasing sample count' FROM Commands WHERE key_name='r_FSAA_samples'
UNION ALL
SELECT id, 'en', 'Gamma correction' FROM Commands WHERE key_name='r_Gamma'
UNION ALL
SELECT id, 'en', 'Geometry instancing' FROM Commands WHERE key_name='r_GeomInstancing';
INSERT OR IGNORE INTO CommandTranslations (command_id, lang, description)
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_GetScreenShot'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_HDRBrightOffset'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_HDRBrightThreshold'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_HDRDebug'
UNION ALL
SELECT id, 'en', 'Fake HDR' FROM Commands WHERE key_name='r_HDRFake'
UNION ALL
SELECT id, 'en', 'HDR level' FROM Commands WHERE key_name='r_HDRLevel'
UNION ALL
SELECT id, 'en', 'HDR rendering' FROM Commands WHERE key_name='r_HDRRendering'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_HeatHaze'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_HeatMapMips'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_HeatMapSave'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_HeatSize'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_HeatType'
UNION ALL
SELECT id, 'en', 'Screen / window height' FROM Commands WHERE key_name='r_Height'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_HWLights'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_LightSourcesAsHeatSources'
UNION ALL
SELECT id, 'en', 'Maximize window on launch' FROM Commands WHERE key_name='r_MaximizeWindow'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_MaxTexLodBias'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_MeasureOverdraw'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_NightMapSave'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_NightSize'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_NightType'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_OceanHeightScale'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_OceanLodDist'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_OceanMaxSplashes'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_OceanRendType'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_OceanSectorSize'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_OceanSplashScale'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_OceanTexUpdate'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_OffsetBump'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_OffsetBumpForce'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_RainMapSize'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_RB_Merge'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_ReloadShaders'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_RenderMode'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_ReplaceCubemap'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_ResetScreenFx'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_RestoreLeft'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_RestoreTop'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_Scissor'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_ScopeLens_fx'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_ScreenRefract'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_SelfRefract'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_SelfShadow'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_ShaderDefault'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_ShaderDetailObjectsBending'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_ShaderInfo'
UNION ALL
SELECT id, 'en', 'Shader model (2.0, 3.0)' FROM Commands WHERE key_name='r_ShaderModel'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_ShadersPrecache'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_ShadersSave'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_ShaderTerrainDOT3';
INSERT OR IGNORE INTO CommandTranslations (command_id, lang, description)
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_ShaderTerrainSpecular'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_shadow_maps_debug'
UNION ALL
SELECT id, 'en', 'Shadow blur' FROM Commands WHERE key_name='r_ShadowBlur'
UNION ALL
SELECT id, 'en', 'Shadow type' FROM Commands WHERE key_name='r_ShadowType'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_Shininess'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_ShowLight'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_ShowLines'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_ShowNormals'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_ShowOnlyShader'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_ShowTangents'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_ShowTexTimeGraph'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_ShowTimeGraph'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_ShowVideoMemoryStats'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_SM2XPATH'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_SM30PATH'
UNION ALL
SELECT id, 'en', 'SSE instructions' FROM Commands WHERE key_name='r_SSE'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_SubSurfaceType'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_SunStyleCoronas'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_SupportCompressedTextures'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_SupportPalettedTextures'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_TexBindMode'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_TexBumpQuality'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_TexBumpResolution'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_TexForceSquare'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_TexGrayOverage'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_TexHWDXTCompression'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_TexHWMipsGeneration'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_TexLMResolution'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_TexLoadMipmapForce'
UNION ALL
SELECT id, 'en', 'Maximum texture size' FROM Commands WHERE key_name='r_TexMaxSize'
UNION ALL
SELECT id, 'en', 'Minimum texture size' FROM Commands WHERE key_name='r_TexMinSize'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_TexNormalMapCompressed'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_TexNormalMapType'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_TexProcedures'
UNION ALL
SELECT id, 'en', 'Texture quality' FROM Commands WHERE key_name='r_TexQuality'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_TexQuantizeDither'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_TexResolution'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_TexSimpleMips'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_TexSkyQuality'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_TexSkyResolution'
UNION ALL
SELECT id, 'en', 'Anisotropic filtering level (1–16)' FROM Commands WHERE key_name='r_Texture_Anisotropic_Level'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_TexturesBaseMip'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_TexturesPixelSize'
UNION ALL
SELECT id, 'en', 'Texture streaming' FROM Commands WHERE key_name='r_TexturesStreaming'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_TexturesStreamingOnlyVideo'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_TexturesStreamingSync'
UNION ALL
SELECT id, 'en', 'Texture stream pool size' FROM Commands WHERE key_name='r_TexturesStreamPoolSize'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_texUnloadDelay'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_Vegetation_Debug'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_Vegetation_IgnoreVertColors';
INSERT OR IGNORE INTO CommandTranslations (command_id, lang, description)
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_Vegetation_PerpixelLight'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_VegetationSpritesAlphaBlend'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_VegetationSpritesNoBend'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_VPFog'
UNION ALL
SELECT id, 'en', 'Vertical sync' FROM Commands WHERE key_name='r_VSync'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_Water_Distance_Far'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_WaterBeachRefractions'
UNION ALL
SELECT id, 'en', 'Water reflections' FROM Commands WHERE key_name='r_WaterReflections'
UNION ALL
SELECT id, 'en', 'Max reflection view distance' FROM Commands WHERE key_name='r_WaterReflections_MaxViewDist'
UNION ALL
SELECT id, 'en', 'Water refractions' FROM Commands WHERE key_name='r_WaterRefractions'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_WaterUpdateDeltaAngle'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_WaterUpdateDistance'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_WaterUpdateFactor'
UNION ALL
SELECT id, 'en', 'Render setting' FROM Commands WHERE key_name='r_WaveScale'
UNION ALL
SELECT id, 'en', 'Screen / window width' FROM Commands WHERE key_name='r_Width'
UNION ALL
SELECT id, 'en', 'Window height (windowed)' FROM Commands WHERE key_name='r_WindowHeight'
UNION ALL
SELECT id, 'en', 'Window width (windowed)' FROM Commands WHERE key_name='r_WindowWidth'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_active_shadow_maps_receving'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_bboxes'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_beach'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_bflyes'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_capture_file_format'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_capture_folder'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_capture_frames'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_cbuffer'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_ccgf_load'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_ccgf_make_if_not_found'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_cgf_cache'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_cgf_load_lods'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_check_number_of_physicalized_polygons'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_debug_lights'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_debug_rndenv'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_debug_shaders'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_debug_shaders_offset'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_decals'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_decals_life_time_scale'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_decals_neighbor_max_life_time'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_decals_offset'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_decals_test'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_deformable_terrain'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_detail_objects'
UNION ALL
SELECT id, 'en', 'Detail textures' FROM Commands WHERE key_name='e_detail_texture'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_detail_texture_min_fov'
UNION ALL
SELECT id, 'en', 'Detail texture quality' FROM Commands WHERE key_name='e_detail_texture_quality'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_disable_fx_preprocess'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_disable_fx_process'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_disable_watercubemap'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_display_musiczone_info'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_editor_time_ratio'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_game_slopeview';
INSERT OR IGNORE INTO CommandTranslations (command_id, lang, description)
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_gametime_control_manual'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_geomorph_enable'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_geomorph_enable_test'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_geomorph_renderer'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_hires_screenshoot'
UNION ALL
SELECT id, 'en', 'Lightmaps' FROM Commands WHERE key_name='e_light_maps'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_light_maps_exportVersion'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_light_maps_occlusion'
UNION ALL
SELECT id, 'en', 'Lightmap quality' FROM Commands WHERE key_name='e_light_maps_quality'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_materials'
UNION ALL
SELECT id, 'en', 'Maximum entity lights' FROM Commands WHERE key_name='e_max_entity_lights'
UNION ALL
SELECT id, 'en', 'Maximum shadow map size' FROM Commands WHERE key_name='e_max_shadow_map_size'
UNION ALL
SELECT id, 'en', 'Maximum draw distance' FROM Commands WHERE key_name='e_maxdistance_enable'
UNION ALL
SELECT id, 'en', 'Entity draw distance' FROM Commands WHERE key_name='e_maxdistance_entities'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_maxdistance_ratio_entities'
UNION ALL
SELECT id, 'en', 'Terrain draw distance' FROM Commands WHERE key_name='e_maxdistance_terrain'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_new_object_xml'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_obj_load_dist_ratio'
UNION ALL
SELECT id, 'en', 'Object LOD ratio' FROM Commands WHERE key_name='e_obj_lod_ratio'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_obj_min_view_dist'
UNION ALL
SELECT id, 'en', 'Object view distance' FROM Commands WHERE key_name='e_obj_view_dist_ratio'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_objects'
UNION ALL
SELECT id, 'en', 'Object draw distance' FROM Commands WHERE key_name='e_objects_draw_range'
UNION ALL
SELECT id, 'en', 'Object fade on distance' FROM Commands WHERE key_name='e_objects_fade_on_distance'
UNION ALL
SELECT id, 'en', 'Occlusion volumes' FROM Commands WHERE key_name='e_occlusion_volumes'
UNION ALL
SELECT id, 'en', 'Particles (on/off)' FROM Commands WHERE key_name='e_particles'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_particles_cull'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_particles_debug'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_particles_debug_spawntest'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_particles_debug_string'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_particles_debug_type'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_Particles_Draw_Area'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_Particles_Draw_Box'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_Particles_Draw_Range'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_particles_freeze'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_particles_fullfx'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_particles_info'
UNION ALL
SELECT id, 'en', 'Particle LOD' FROM Commands WHERE key_name='e_particles_lod'
UNION ALL
SELECT id, 'en', 'Maximum particle count' FROM Commands WHERE key_name='e_particles_max_count'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_particles_receive_shadows'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_particles_showemitter_name'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_particles_showonly'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_particles_spawn_distance_ratio'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_particles_system_only'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_particles_use_partice_table'
UNION ALL
SELECT id, 'en', 'Rain amount' FROM Commands WHERE key_name='e_rain_amount'
UNION ALL
SELECT id, 'en', 'Rain particles' FROM Commands WHERE key_name='e_rain_particle'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_register_in_sectors'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_scissor_debug'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_sequence_debug_playtime';
INSERT OR IGNORE INTO CommandTranslations (command_id, lang, description)
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_sequence_debug_spawntime'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_sequence_debug_string'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_sequence_info'
UNION ALL
SELECT id, 'en', 'Shadow maps' FROM Commands WHERE key_name='e_shadow_maps'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_shadow_maps_color_ratio'
UNION ALL
SELECT id, 'en', 'Shadow map debug' FROM Commands WHERE key_name='e_shadow_maps_debug'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_shadow_maps_fade_from_light_bit'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_shadow_maps_from_static_objects'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_shadow_maps_frustums'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_shadow_maps_max_casters_per_object'
UNION ALL
SELECT id, 'en', 'Objects receiving shadows' FROM Commands WHERE key_name='e_shadow_maps_receiving'
UNION ALL
SELECT id, 'en', 'Self-shadowing' FROM Commands WHERE key_name='e_shadow_maps_self_shadowing'
UNION ALL
SELECT id, 'en', 'Shadow map size ratio' FROM Commands WHERE key_name='e_shadow_maps_size_ratio'
UNION ALL
SELECT id, 'en', 'Shadow view distance' FROM Commands WHERE key_name='e_shadow_maps_view_dist_ratio'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_shadow_spots'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_simple_shadow_maps'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_SupportLightmaps'
UNION ALL
SELECT id, 'en', 'Terrain (on/off)' FROM Commands WHERE key_name='e_terrain'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_terrain_debug'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_terrain_draw_this_sector_adjacency'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_terrain_draw_this_sector_only'
UNION ALL
SELECT id, 'en', 'Terrain LOD' FROM Commands WHERE key_name='e_terrain_lod_ratio'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_terrain_log'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_terrain_merge_far_sectors'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_terrain_occlusion_culling'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_terrain_occlusion_culling_precision'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_terrain_sector_grid'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_terrain_shadow_index'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_terrain_single_pass'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_terrain_single_pass_vol_fog'
UNION ALL
SELECT id, 'en', 'Terrain specular' FROM Commands WHERE key_name='e_terrain_specular'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_terrain_texture_bind'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_terrain_texture_mip_offset'
UNION ALL
SELECT id, 'en', 'Terrain mipmaps' FROM Commands WHERE key_name='e_terrain_texture_mipmaps'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_terrain_texture_pool'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_TerrainSectorsInfo'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_time_env_enable'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_time_profiling'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_time_smoothing'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_timedemo_frames'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_timedemo_milliseconds'
UNION ALL
SELECT id, 'en', 'Vegetation' FROM Commands WHERE key_name='e_vegetation'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_vegetation_3donly'
UNION ALL
SELECT id, 'en', 'Vegetation wind bending' FROM Commands WHERE key_name='e_vegetation_bending'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_vegetation_debug'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_vegetation_min_size'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_vegetation_plants1_distance'
UNION ALL
SELECT id, 'en', 'Vegetation sprites' FROM Commands WHERE key_name='e_vegetation_sprites'
UNION ALL
SELECT id, 'en', 'Vegetation sprite distance' FROM Commands WHERE key_name='e_vegetation_sprites_distance_ratio'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_vegetation_sprites_min_distance';
INSERT OR IGNORE INTO CommandTranslations (command_id, lang, description)
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_vegetation_sprites_slow_switch'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_vegetation_sprites_texres'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_vegetation_update_shadow_every_frame'
UNION ALL
SELECT id, 'en', 'Ocean' FROM Commands WHERE key_name='e_water_ocean'
UNION ALL
SELECT id, 'en', 'Sun reflection on water' FROM Commands WHERE key_name='e_water_ocean_sun_reflection'
UNION ALL
SELECT id, 'en', 'Ocean tessellation' FROM Commands WHERE key_name='e_water_ocean_tesselation'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_water_render_cull_terrain'
UNION ALL
SELECT id, 'en', 'Water draw distance' FROM Commands WHERE key_name='e_water_render_distance'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_water_volumes'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_weather_change_immediate'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_weather_change_speed'
UNION ALL
SELECT id, 'en', 'Engine / world setting' FROM Commands WHERE key_name='e_weather_cutscene'
UNION ALL
SELECT id, 'en', 'Weather effects' FROM Commands WHERE key_name='e_weather_enable'
UNION ALL
SELECT id, 'en', 'Weather FX' FROM Commands WHERE key_name='e_weather_fx_enable'
UNION ALL
SELECT id, 'en', 'Widescreen mode' FROM Commands WHERE key_name='e_widescreen'
UNION ALL
SELECT id, 'en', 'Physics setting' FROM Commands WHERE key_name='p_accuracy_LCPCG'
UNION ALL
SELECT id, 'en', 'Physics setting' FROM Commands WHERE key_name='p_accuracy_LCPCG_no_improvement'
UNION ALL
SELECT id, 'en', 'Physics setting' FROM Commands WHERE key_name='p_accuracy_MC'
UNION ALL
SELECT id, 'en', 'Physics setting' FROM Commands WHERE key_name='p_characterik'
UNION ALL
SELECT id, 'en', 'Physics setting' FROM Commands WHERE key_name='p_characterik_arm'
UNION ALL
SELECT id, 'en', 'Physics setting' FROM Commands WHERE key_name='p_damping_group_size'
UNION ALL
SELECT id, 'en', 'Decal lifetime' FROM Commands WHERE key_name='p_decalLifetime'
UNION ALL
SELECT id, 'en', 'Fixed physics timestep' FROM Commands WHERE key_name='p_fixed_timestep'
UNION ALL
SELECT id, 'en', 'Physics setting' FROM Commands WHERE key_name='p_GEB_max_cells'
UNION ALL
SELECT id, 'en', 'Head camera' FROM Commands WHERE key_name='p_head_camera'
UNION ALL
SELECT id, 'en', 'Physics setting' FROM Commands WHERE key_name='p_limit_simple_solver_energy'
UNION ALL
SELECT id, 'en', 'Physics setting' FROM Commands WHERE key_name='p_list_active_objects'
UNION ALL
SELECT id, 'en', 'Physics setting' FROM Commands WHERE key_name='p_max_contact_gap'
UNION ALL
SELECT id, 'en', 'Physics setting' FROM Commands WHERE key_name='p_max_contact_gap_player'
UNION ALL
SELECT id, 'en', 'Physics setting' FROM Commands WHERE key_name='p_max_contact_gap_simple'
UNION ALL
SELECT id, 'en', 'Max contacts' FROM Commands WHERE key_name='p_max_contacts'
UNION ALL
SELECT id, 'en', 'Physics setting' FROM Commands WHERE key_name='p_max_LCPCG_fruitless_iters'
UNION ALL
SELECT id, 'en', 'Physics setting' FROM Commands WHERE key_name='p_max_LCPCG_iters'
UNION ALL
SELECT id, 'en', 'Physics setting' FROM Commands WHERE key_name='p_max_LCPCG_microiters'
UNION ALL
SELECT id, 'en', 'Physics setting' FROM Commands WHERE key_name='p_max_LCPCG_microiters_final'
UNION ALL
SELECT id, 'en', 'Physics setting' FROM Commands WHERE key_name='p_max_LCPCG_subiters'
UNION ALL
SELECT id, 'en', 'Physics setting' FROM Commands WHERE key_name='p_max_LCPCG_subiters_final'
UNION ALL
SELECT id, 'en', 'Physics setting' FROM Commands WHERE key_name='p_max_MC_iters'
UNION ALL
SELECT id, 'en', 'Physics setting' FROM Commands WHERE key_name='p_max_plane_contacts'
UNION ALL
SELECT id, 'en', 'Physics setting' FROM Commands WHERE key_name='p_max_plane_contacts_distress'
UNION ALL
SELECT id, 'en', 'Max player velocity' FROM Commands WHERE key_name='p_max_player_velocity'
UNION ALL
SELECT id, 'en', 'Physics setting' FROM Commands WHERE key_name='p_max_substeps'
UNION ALL
SELECT id, 'en', 'Physics setting' FROM Commands WHERE key_name='p_max_unproj_vel'
UNION ALL
SELECT id, 'en', 'Physics setting' FROM Commands WHERE key_name='p_max_velocity'
UNION ALL
SELECT id, 'en', 'Physics setting' FROM Commands WHERE key_name='p_max_world_step'
UNION ALL
SELECT id, 'en', 'Physics setting' FROM Commands WHERE key_name='p_min_LCPCG_improvement'
UNION ALL
SELECT id, 'en', 'Physics setting' FROM Commands WHERE key_name='p_min_separation_speed'
UNION ALL
SELECT id, 'en', 'Physics setting' FROM Commands WHERE key_name='p_penalty_scale'
UNION ALL
SELECT id, 'en', 'Physics setting' FROM Commands WHERE key_name='p_single_step_mode'
UNION ALL
SELECT id, 'en', 'Physics setting' FROM Commands WHERE key_name='p_time_granularity';
INSERT OR IGNORE INTO CommandTranslations (command_id, lang, description)
SELECT id, 'en', 'Physics setting' FROM Commands WHERE key_name='p_waterbob_mindepth'
UNION ALL
SELECT id, 'en', 'Water camera bob (pitch)' FROM Commands WHERE key_name='p_waterbob_pitch'
UNION ALL
SELECT id, 'en', 'Physics setting' FROM Commands WHERE key_name='p_waterbob_pitchspeed'
UNION ALL
SELECT id, 'en', 'Water camera bob (roll)' FROM Commands WHERE key_name='p_waterbob_roll'
UNION ALL
SELECT id, 'en', 'Physics setting' FROM Commands WHERE key_name='p_waterbob_rollspeed'
UNION ALL
SELECT id, 'en', 'Entity system setting' FROM Commands WHERE key_name='es_bboxes'
UNION ALL
SELECT id, 'en', 'Entity system setting' FROM Commands WHERE key_name='es_CamHeight'
UNION ALL
SELECT id, 'en', 'Entity system setting' FROM Commands WHERE key_name='es_CamHeightNear'
UNION ALL
SELECT id, 'en', 'Entity system setting' FROM Commands WHERE key_name='es_CamRestoreStiff'
UNION ALL
SELECT id, 'en', 'Entity system setting' FROM Commands WHERE key_name='es_charArmIK_Range'
UNION ALL
SELECT id, 'en', 'Entity system setting' FROM Commands WHERE key_name='es_charIK_Range'
UNION ALL
SELECT id, 'en', 'Entity system setting' FROM Commands WHERE key_name='es_CharZOffsetSpeed'
UNION ALL
SELECT id, 'en', 'Entity system setting' FROM Commands WHERE key_name='es_DebugTimer'
UNION ALL
SELECT id, 'en', 'Entity system setting' FROM Commands WHERE key_name='es_DisplayInfo'
UNION ALL
SELECT id, 'en', 'Entity system setting' FROM Commands WHERE key_name='es_EnableCloth'
UNION ALL
SELECT id, 'en', 'Entity system setting' FROM Commands WHERE key_name='es_FxSystemRVRLevel'
UNION ALL
SELECT id, 'en', 'Entity system setting' FROM Commands WHERE key_name='es_helpers'
UNION ALL
SELECT id, 'en', 'Entity system setting' FROM Commands WHERE key_name='es_HitCharacters'
UNION ALL
SELECT id, 'en', 'Entity system setting' FROM Commands WHERE key_name='es_HitDeadBodies'
UNION ALL
SELECT id, 'en', 'Entity system setting' FROM Commands WHERE key_name='es_ImpulseScale'
UNION ALL
SELECT id, 'en', 'Entity system setting' FROM Commands WHERE key_name='es_LODShaderDistance'
UNION ALL
SELECT id, 'en', 'Entity system setting' FROM Commands WHERE key_name='es_LODShaderStep'
UNION ALL
SELECT id, 'en', 'Entity system setting' FROM Commands WHERE key_name='es_MaxImpulseAdjMass'
UNION ALL
SELECT id, 'en', 'Entity system setting' FROM Commands WHERE key_name='es_MinImpulseVel'
UNION ALL
SELECT id, 'en', 'Entity system setting' FROM Commands WHERE key_name='es_OnDemandPhysics'
UNION ALL
SELECT id, 'en', 'Entity system setting' FROM Commands WHERE key_name='es_PiercingCamera'
UNION ALL
SELECT id, 'en', 'Entity system setting' FROM Commands WHERE key_name='es_SplashThreshold'
UNION ALL
SELECT id, 'en', 'Entity system setting' FROM Commands WHERE key_name='es_SplashTimeout'
UNION ALL
SELECT id, 'en', 'Entity system setting' FROM Commands WHERE key_name='es_UpdateAI'
UNION ALL
SELECT id, 'en', 'Entity system setting' FROM Commands WHERE key_name='es_UpdateBonePositions'
UNION ALL
SELECT id, 'en', 'Entity system setting' FROM Commands WHERE key_name='es_UpdateCamera'
UNION ALL
SELECT id, 'en', 'Entity system setting' FROM Commands WHERE key_name='es_UpdateCollision'
UNION ALL
SELECT id, 'en', 'Entity system setting' FROM Commands WHERE key_name='es_UpdateCollisionScript'
UNION ALL
SELECT id, 'en', 'Entity system setting' FROM Commands WHERE key_name='es_UpdateContainer'
UNION ALL
SELECT id, 'en', 'Entity system setting' FROM Commands WHERE key_name='es_UpdateCoocooEgg'
UNION ALL
SELECT id, 'en', 'Entity system setting' FROM Commands WHERE key_name='es_UpdateEntities'
UNION ALL
SELECT id, 'en', 'Entity system setting' FROM Commands WHERE key_name='es_UpdateInvisibleCharacter'
UNION ALL
SELECT id, 'en', 'Entity system setting' FROM Commands WHERE key_name='es_UpdatePhysics'
UNION ALL
SELECT id, 'en', 'Entity system setting' FROM Commands WHERE key_name='es_UpdateScript'
UNION ALL
SELECT id, 'en', 'Entity system setting' FROM Commands WHERE key_name='es_UpdateTimer'
UNION ALL
SELECT id, 'en', 'Entity system setting' FROM Commands WHERE key_name='es_VisCheckForUpdate'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_ac_cos'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_ac_hcos'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_ac_hsin'
UNION ALL
SELECT id, 'en', 'Character ambient light intensity' FROM Commands WHERE key_name='ca_ambient_light_intensity'
UNION ALL
SELECT id, 'en', 'Character ambient light range' FROM Commands WHERE key_name='ca_ambient_light_range'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_AnimationDeferredLoad'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_AnimationUnloadCheckPerFrame'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_AnimationUnloadDelay'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_AnimationUnloadMaxPerFrame';
INSERT OR IGNORE INTO CommandTranslations (command_id, lang, description)
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_AnimDisplacementThreshold'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_AnimDistanceThreshold'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_AnimIFrame'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_AnimWarningLevel'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_BoneAnimUFM'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_BoundZOffset'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_cb_iteration'
UNION ALL
SELECT id, 'en', 'Cloth mode (capes, robes)' FROM Commands WHERE key_name='ca_ClothMode'
UNION ALL
SELECT id, 'en', 'Custom hair color' FROM Commands WHERE key_name='ca_CustomColorHair'
UNION ALL
SELECT id, 'en', 'Custom skin color' FROM Commands WHERE key_name='ca_CustomColorSkin'
UNION ALL
SELECT id, 'en', 'Death animation time' FROM Commands WHERE key_name='ca_DeathBlendTime'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_Debug'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_DebugHeatSources'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_DebugInfo'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_DebugShaders'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_DecalAntiflickerHack'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_DecalSizeMultiplier'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_DefaultDecalTexture'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_DisableAnimEvents'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_DisablePlusRotationMask'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_DisplayInfo'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_drag'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_DrawAnims'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_DrawBBox'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_DrawBBoxSub'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_DrawBones'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_DrawDecalOutline'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_DrawLHelpers'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_edge_max'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_edge_min'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_EnableAnimationLog'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_EnableCCG'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_EnableCharacterShadowVolume'
UNION ALL
SELECT id, 'en', 'Cubic blending (better graphics quality)' FROM Commands WHERE key_name='ca_EnableCubicBlending'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_EnableDecals'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_EnableLightUpdate'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_EnableTangentSkinning'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_EnableVertexColors'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_fixed_time'
UNION ALL
SELECT id, 'en', 'Hair animation' FROM Commands WHERE key_name='ca_HairAnim'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_HairAnimBackPlaneOffset'
UNION ALL
SELECT id, 'en', 'Hair damping (1)' FROM Commands WHERE key_name='ca_HairAnimDamping1'
UNION ALL
SELECT id, 'en', 'Hair damping (2)' FROM Commands WHERE key_name='ca_HairAnimDamping2'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_HairAnimDistance'
UNION ALL
SELECT id, 'en', 'Hair gravity (1)' FROM Commands WHERE key_name='ca_HairAnimGravity1'
UNION ALL
SELECT id, 'en', 'Hair gravity (2)' FROM Commands WHERE key_name='ca_HairAnimGravity2'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_HairAnimLimitAngle'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_HairAnimMassInc'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_HairAnimRelaxationIterCount'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_horz_edge';
INSERT OR IGNORE INTO CommandTranslations (command_id, lang, description)
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_Iteration'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_KeepMaxCacheSize'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_KeepMaxCacheSize2'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_KeepMaxCacheSize3'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_KeepModels'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_KeepOrthoUniform'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_LimitShadowLOD'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_LodBias'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_LogAnimation'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_MatPlusDebug'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_MatPlusDebug2'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_MaxMorphDist'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_MinVertexWeightLOD0'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_MinVertexWeightLOD1'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_MinVertexWeightLOD2'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_MorphNormals'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_NoAnim'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_NoDeform'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_NoDraw'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_NoDrawBound'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_NoDrawShadowVolumes'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_NoMatPlus'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_NoMatPlus2'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_NoMorph'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_NoMtlSorting'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_NoPhys'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_NormalizeBases'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_NoTransScale'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_OverrideLayer'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_PerforatingDecals'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_PrebuildShadowConnectivity'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_Profile'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_RainPower'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_RestartBehaviour'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_RuntimeScale'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_SafeReskin'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_ShadowBufferLimit'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_ShadowDoubleBuffer'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_ShadowVolumeExtent'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_SkinBasedBBoxMask'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_SkipBoneAnim'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_SSEEnable'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_SSEEnable1'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_SSEEnable2'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_StopDeformingAfter'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_StripifyGeometry'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_TangentBasisCalcPeriod'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_TestMirror'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_TestSkinningRepeats'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_TickVersion';
INSERT OR IGNORE INTO CommandTranslations (command_id, lang, description)
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_UpdateSpeed'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_UpdateSpeed0'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_UpdateSpeed1'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_UpdateSpeed2'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_UpdateSpeed3'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_UpdateSpeed4'
UNION ALL
SELECT id, 'en', 'Use custom color' FROM Commands WHERE key_name='ca_UseCustomColor'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_UseLowestLOD'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_VertsPerTangSubskin'
UNION ALL
SELECT id, 'en', 'Character / animation setting' FROM Commands WHERE key_name='ca_ZDeleteConstructionData'
UNION ALL
SELECT id, 'en', 'Console command autocomplete' FROM Commands WHERE key_name='con_auto_complete'
UNION ALL
SELECT id, 'en', 'Disable in-game console (PauseBreak)' FROM Commands WHERE key_name='con_disable_console'
UNION ALL
SELECT id, 'en', 'Show last console messages' FROM Commands WHERE key_name='con_display_last_messages'
UNION ALL
SELECT id, 'en', 'Console line buffer size' FROM Commands WHERE key_name='con_line_buffer_size'
UNION ALL
SELECT id, 'en', 'Debug visualization setting' FROM Commands WHERE key_name='CV_ind_DrawBorderEdges'
UNION ALL
SELECT id, 'en', 'Debug visualization setting' FROM Commands WHERE key_name='CV_ind_ReverseShadowVolumes'
UNION ALL
SELECT id, 'en', 'Debug visualization setting' FROM Commands WHERE key_name='CV_ind_VisualizeShadowVolumes'
UNION ALL
SELECT id, 'en', 'Allow software rendering' FROM Commands WHERE key_name='d3d9_AllowSoftware'
UNION ALL
SELECT id, 'en', 'DirectX 9 setting' FROM Commands WHERE key_name='d3d9_ClipPlanes'
UNION ALL
SELECT id, 'en', 'D3D9 compressed textures' FROM Commands WHERE key_name='d3d9_CompressedTextures'
UNION ALL
SELECT id, 'en', 'DirectX 9 setting' FROM Commands WHERE key_name='d3d9_DecalOffset'
UNION ALL
SELECT id, 'en', 'DirectX 9 setting' FROM Commands WHERE key_name='d3d9_Device'
UNION ALL
SELECT id, 'en', 'Force software rendering' FROM Commands WHERE key_name='d3d9_ForceSoftware'
UNION ALL
SELECT id, 'en', 'DirectX 9 setting' FROM Commands WHERE key_name='d3d9_MipProcedures'
UNION ALL
SELECT id, 'en', 'DirectX 9 setting' FROM Commands WHERE key_name='d3d9_NoDepthMaps'
UNION ALL
SELECT id, 'en', 'DirectX 9 setting' FROM Commands WHERE key_name='d3d9_NodeviceId'
UNION ALL
SELECT id, 'en', 'DirectX 9 setting' FROM Commands WHERE key_name='d3d9_NormalMapScale'
UNION ALL
SELECT id, 'en', 'DirectX 9 setting' FROM Commands WHERE key_name='d3d9_NV30_PS20'
UNION ALL
SELECT id, 'en', 'DirectX 9 setting' FROM Commands WHERE key_name='d3d9_NVPerfHUD'
UNION ALL
SELECT id, 'en', 'Occlusion queries' FROM Commands WHERE key_name='d3d9_Occlusion_Query'
UNION ALL
SELECT id, 'en', 'Paletted textures' FROM Commands WHERE key_name='d3d9_PalettedTextures'
UNION ALL
SELECT id, 'en', 'Pipeline buffer size' FROM Commands WHERE key_name='d3d9_pip_buff_size'
UNION ALL
SELECT id, 'en', 'DirectX 9 setting' FROM Commands WHERE key_name='d3d9_rb_Tris'
UNION ALL
SELECT id, 'en', 'DirectX 9 setting' FROM Commands WHERE key_name='d3d9_rb_Verts'
UNION ALL
SELECT id, 'en', 'DirectX 9 setting' FROM Commands WHERE key_name='d3d9_ResetDeviceAfterLoading'
UNION ALL
SELECT id, 'en', 'DirectX 9 setting' FROM Commands WHERE key_name='d3d9_SaveDepthmaps'
UNION ALL
SELECT id, 'en', 'Square textures' FROM Commands WHERE key_name='d3d9_SquareTextures'
UNION ALL
SELECT id, 'en', 'DirectX 9 setting' FROM Commands WHERE key_name='d3d9_TexMipFilter'
UNION ALL
SELECT id, 'en', 'D3D9 anisotropic filtering' FROM Commands WHERE key_name='d3d9_Texture_Filter_Anisotropic'
UNION ALL
SELECT id, 'en', 'DirectX 9 setting' FROM Commands WHERE key_name='d3d9_TextureBits'
UNION ALL
SELECT id, 'en', 'Trilinear filtering' FROM Commands WHERE key_name='d3d9_TextureFilter'
UNION ALL
SELECT id, 'en', 'Triple buffering (performance boost)' FROM Commands WHERE key_name='d3d9_TripleBuffering'
UNION ALL
SELECT id, 'en', 'Use bump maps' FROM Commands WHERE key_name='d3d9_UseBumpmap'
UNION ALL
SELECT id, 'en', 'Vertex buffer pools' FROM Commands WHERE key_name='d3d9_VBPools'
UNION ALL
SELECT id, 'en', 'Vertex buffer pool size' FROM Commands WHERE key_name='d3d9_VBPoolSize'
UNION ALL
SELECT id, 'en', 'Sound setting' FROM Commands WHERE key_name='s_CapsCheck'
UNION ALL
SELECT id, 'en', 'Sound setting' FROM Commands WHERE key_name='s_DebugMusic'
UNION ALL
SELECT id, 'en', 'Sound setting' FROM Commands WHERE key_name='s_DebugSound'
UNION ALL
SELECT id, 'en', 'Sound setting' FROM Commands WHERE key_name='s_DebugSoundBuffer'
UNION ALL
SELECT id, 'en', 'Sound setting' FROM Commands WHERE key_name='s_FixedSoundPriority';
INSERT OR IGNORE INTO CommandTranslations (command_id, lang, description)
SELECT id, 'en', 'Sound setting' FROM Commands WHERE key_name='s_KeepSound'
UNION ALL
SELECT id, 'en', 'Master volume' FROM Commands WHERE key_name='s_MasterVolume'
UNION ALL
SELECT id, 'en', 'Max active sound sources' FROM Commands WHERE key_name='s_MaxActiveSoundSpots'
UNION ALL
SELECT id, 'en', 'Max hardware channels' FROM Commands WHERE key_name='s_MaxHWChannels'
UNION ALL
SELECT id, 'en', 'Maximum sound distance' FROM Commands WHERE key_name='s_MaxSoundDist'
UNION ALL
SELECT id, 'en', 'Min hardware channels' FROM Commands WHERE key_name='s_MinHWChannels'
UNION ALL
SELECT id, 'en', 'Sound setting' FROM Commands WHERE key_name='s_MinRepeatSoundTimeout'
UNION ALL
SELECT id, 'en', 'Sample rate' FROM Commands WHERE key_name='s_SampleRate'
UNION ALL
SELECT id, 'en', 'Sound setting' FROM Commands WHERE key_name='s_SFXMute_COMMENT_GOSSIP'
UNION ALL
SELECT id, 'en', 'Sound setting' FROM Commands WHERE key_name='s_SFXMute_COMMENT_NPC'
UNION ALL
SELECT id, 'en', 'Sound setting' FROM Commands WHERE key_name='s_SFXMute_COMMENT_QUEST'
UNION ALL
SELECT id, 'en', 'Sound setting' FROM Commands WHERE key_name='s_SFXMute_COMMENT_SYSTEM'
UNION ALL
SELECT id, 'en', 'Sound setting' FROM Commands WHERE key_name='s_SFXMute_COMMENT_WEATHER'
UNION ALL
SELECT id, 'en', 'Sound setting' FROM Commands WHERE key_name='s_SFXMute_ENV'
UNION ALL
SELECT id, 'en', 'Mute effect sounds' FROM Commands WHERE key_name='s_SFXMute_FX'
UNION ALL
SELECT id, 'en', 'Mute all sound' FROM Commands WHERE key_name='s_SFXMute_MASTER'
UNION ALL
SELECT id, 'en', 'Mute UI sounds' FROM Commands WHERE key_name='s_SFXMute_UI'
UNION ALL
SELECT id, 'en', 'Sound setting' FROM Commands WHERE key_name='s_SFXVolume_COMMENT_GOSSIP'
UNION ALL
SELECT id, 'en', 'Sound setting' FROM Commands WHERE key_name='s_SFXVolume_COMMENT_NPC'
UNION ALL
SELECT id, 'en', 'Sound setting' FROM Commands WHERE key_name='s_SFXVolume_COMMENT_QUEST'
UNION ALL
SELECT id, 'en', 'Sound setting' FROM Commands WHERE key_name='s_SFXVolume_COMMENT_SYSTEM'
UNION ALL
SELECT id, 'en', 'Environment volume' FROM Commands WHERE key_name='s_SFXVolume_ENV'
UNION ALL
SELECT id, 'en', 'Effects volume' FROM Commands WHERE key_name='s_SFXVolume_FX'
UNION ALL
SELECT id, 'en', 'UI volume' FROM Commands WHERE key_name='s_SFXVolume_UI'
UNION ALL
SELECT id, 'en', 'Weather volume' FROM Commands WHERE key_name='s_SFXVolume_WEATHER'
UNION ALL
SELECT id, 'en', 'Sound setting' FROM Commands WHERE key_name='s_VisAreasPropagation'
UNION ALL
SELECT id, 'en', 'System setting' FROM Commands WHERE key_name='sys_AdaptiveCharLOD'
UNION ALL
SELECT id, 'en', 'System setting' FROM Commands WHERE key_name='sys_AdaptiveCharLOD_FF'
UNION ALL
SELECT id, 'en', 'CPU thread affinity' FROM Commands WHERE key_name='sys_affinity'
UNION ALL
SELECT id, 'en', 'First launch (flag)' FROM Commands WHERE key_name='sys_firstlaunch'
UNION ALL
SELECT id, 'en', 'Fixed framerate' FROM Commands WHERE key_name='sys_fixedframe'
UNION ALL
SELECT id, 'en', 'System setting' FROM Commands WHERE key_name='sys_fixedframe_target'
UNION ALL
SELECT id, 'en', 'System setting' FROM Commands WHERE key_name='sys_noupdate'
UNION ALL
SELECT id, 'en', 'System setting' FROM Commands WHERE key_name='sys_PakLogMissingFiles'
UNION ALL
SELECT id, 'en', 'System setting' FROM Commands WHERE key_name='sys_PakPriority'
UNION ALL
SELECT id, 'en', 'System setting' FROM Commands WHERE key_name='sys_PakReadSlice'
UNION ALL
SELECT id, 'en', 'System setting' FROM Commands WHERE key_name='sys_script_debugger'
UNION ALL
SELECT id, 'en', 'Skip on low-spec systems' FROM Commands WHERE key_name='sys_skiponlowspec'
UNION ALL
SELECT id, 'en', 'System spec level (1–4)' FROM Commands WHERE key_name='sys_spec'
UNION ALL
SELECT id, 'en', 'Supersampling info' FROM Commands WHERE key_name='sys_SSInfo'
UNION ALL
SELECT id, 'en', 'Streaming time budget (µs)' FROM Commands WHERE key_name='sys_StreamCallbackTimeBudget'
UNION ALL
SELECT id, 'en', 'Streaming compression mask' FROM Commands WHERE key_name='sys_StreamCompressionMask'
UNION ALL
SELECT id, 'en', 'System warnings' FROM Commands WHERE key_name='sys_warnings'
UNION ALL
SELECT id, 'en', 'Input setting' FROM Commands WHERE key_name='i_direct_input'
UNION ALL
SELECT id, 'en', 'File log verbosity' FROM Commands WHERE key_name='log_FileVerbosity'
UNION ALL
SELECT id, 'en', 'Include time in log' FROM Commands WHERE key_name='log_IncludeTime'
UNION ALL
SELECT id, 'en', 'Log line filter' FROM Commands WHERE key_name='log_linefilter'
UNION ALL
SELECT id, 'en', 'Log verbosity level' FROM Commands WHERE key_name='log_Verbosity'
UNION ALL
SELECT id, 'en', 'Disable cutscenes' FROM Commands WHERE key_name='mov_NoCutscenes'
UNION ALL
SELECT id, 'en', 'Movie font ratio' FROM Commands WHERE key_name='movie_fontRatio';
INSERT OR IGNORE INTO CommandTranslations (command_id, lang, description)
SELECT id, 'en', 'Profiling (on/off)' FROM Commands WHERE key_name='profile'
UNION ALL
SELECT id, 'en', 'Profiling setting' FROM Commands WHERE key_name='profile_filter'
UNION ALL
SELECT id, 'en', 'Profiling graph' FROM Commands WHERE key_name='profile_graph'
UNION ALL
SELECT id, 'en', 'Profiling setting' FROM Commands WHERE key_name='profile_graphScale'
UNION ALL
SELECT id, 'en', 'Network profile' FROM Commands WHERE key_name='profile_network'
UNION ALL
SELECT id, 'en', 'Profiling setting' FROM Commands WHERE key_name='profile_pagefaults'
UNION ALL
SELECT id, 'en', 'Peak values' FROM Commands WHERE key_name='profile_peak'
UNION ALL
SELECT id, 'en', 'Memory info' FROM Commands WHERE key_name='MemInfo'
UNION ALL
SELECT id, 'en', 'Memory stats' FROM Commands WHERE key_name='MemStats'
UNION ALL
SELECT id, 'en', 'Memory setting' FROM Commands WHERE key_name='MemStatsMaxDepth'
UNION ALL
SELECT id, 'en', 'Memory stats threshold' FROM Commands WHERE key_name='MemStatsThreshold'
UNION ALL
SELECT id, 'en', 'Exit on quit' FROM Commands WHERE key_name='ExitOnQuit'
UNION ALL
SELECT id, 'en', 'Fixed time step' FROM Commands WHERE key_name='fixed_time_step'
UNION ALL
SELECT id, 'en', 'Miscellaneous setting' FROM Commands WHERE key_name='f_FTKerning'
UNION ALL
SELECT id, 'en', 'Blaze VoIP (voice chat)' FROM Commands WHERE key_name='net_blaze_voip_enable'
UNION ALL
SELECT id, 'en', 'VoIP push-to-talk' FROM Commands WHERE key_name='net_blaze_voip_enable_ptt'
UNION ALL
SELECT id, 'en', 'VoIP playback volume' FROM Commands WHERE key_name='net_blaze_voip_playback_volume'
UNION ALL
SELECT id, 'en', 'Video memory budget (MB)' FROM Commands WHERE key_name='sys_budget_videomem'
UNION ALL
SELECT id, 'en', 'System memory budget (MB)' FROM Commands WHERE key_name='sys_budget_sysmem'
UNION ALL
SELECT id, 'en', 'Max CPU threads' FROM Commands WHERE key_name='sys_MaxThreads'
UNION ALL
SELECT id, 'en', 'Disable crash dialog' FROM Commands WHERE key_name='sys_DisableCrashDialog'
UNION ALL
SELECT id, 'en', 'Enable asserts' FROM Commands WHERE key_name='sys_EnableAsserts'
UNION ALL
SELECT id, 'en', 'Disable warnings' FROM Commands WHERE key_name='sys_WarningDisable'
UNION ALL
SELECT id, 'en', '64-bit cache' FROM Commands WHERE key_name='sys_64bitCache'
UNION ALL
SELECT id, 'en', 'Deactivate console' FROM Commands WHERE key_name='sys_DeactivateConsole'
UNION ALL
SELECT id, 'en', 'Enable asserts' FROM Commands WHERE key_name='sys_EnableAsserts'
UNION ALL
SELECT id, 'en', 'Fixed frame' FROM Commands WHERE key_name='sys_FixedFrame'
UNION ALL
SELECT id, 'en', 'Enable job system' FROM Commands WHERE key_name='sys_job_system_enable'
UNION ALL
SELECT id, 'en', 'Low-spec pak' FROM Commands WHERE key_name='sys_LowSpecPak'
UNION ALL
SELECT id, 'en', 'Main thread CPU core' FROM Commands WHERE key_name='sys_main_CPU'
UNION ALL
SELECT id, 'en', 'Maximum FPS (system)' FROM Commands WHERE key_name='sys_maxFPS'
UNION ALL
SELECT id, 'en', 'Maximum FPS' FROM Commands WHERE key_name='sys_MaxFps'
UNION ALL
SELECT id, 'en', 'Physics CPU core' FROM Commands WHERE key_name='sys_physics_CPU'
UNION ALL
SELECT id, 'en', 'Physics GPU' FROM Commands WHERE key_name='sys_physics_GPU'
UNION ALL
SELECT id, 'en', 'Resource preload' FROM Commands WHERE key_name='sys_preload'
UNION ALL
SELECT id, 'en', 'Environment quality level' FROM Commands WHERE key_name='sys_spec_Environment'
UNION ALL
SELECT id, 'en', 'Game effects quality level' FROM Commands WHERE key_name='sys_spec_GameEffects'
UNION ALL
SELECT id, 'en', 'Lighting quality level' FROM Commands WHERE key_name='sys_spec_light'
UNION ALL
SELECT id, 'en', 'Object detail level' FROM Commands WHERE key_name='sys_spec_ObjectDetail'
UNION ALL
SELECT id, 'en', 'Particle quality level' FROM Commands WHERE key_name='sys_spec_Particles'
UNION ALL
SELECT id, 'en', 'Physics quality level' FROM Commands WHERE key_name='sys_spec_Physics'
UNION ALL
SELECT id, 'en', 'Post-processing quality level' FROM Commands WHERE key_name='sys_spec_PostProcessing'
UNION ALL
SELECT id, 'en', 'Overall quality level' FROM Commands WHERE key_name='sys_spec_Quality'
UNION ALL
SELECT id, 'en', 'Shading quality level' FROM Commands WHERE key_name='sys_spec_Shading'
UNION ALL
SELECT id, 'en', 'Shadow quality level' FROM Commands WHERE key_name='sys_spec_Shadows'
UNION ALL
SELECT id, 'en', 'Sound quality level' FROM Commands WHERE key_name='sys_spec_Sound'
UNION ALL
SELECT id, 'en', 'Texture quality level' FROM Commands WHERE key_name='sys_spec_Texture'
UNION ALL
SELECT id, 'en', 'Texture resolution' FROM Commands WHERE key_name='sys_spec_TextureResolution'
UNION ALL
SELECT id, 'en', 'Volumetric effects level' FROM Commands WHERE key_name='sys_spec_VolumetricEffects'
UNION ALL
SELECT id, 'en', 'Disable warnings' FROM Commands WHERE key_name='sys_WarningDisable';
INSERT OR IGNORE INTO CommandTranslations (command_id, lang, description)
SELECT id, 'en', 'Windows Error Reporting' FROM Commands WHERE key_name='sys_WER'
UNION ALL
SELECT id, 'en', 'Ignore log warnings' FROM Commands WHERE key_name='log_IgnoreWarnings'
UNION ALL
SELECT id, 'en', 'Disable logging completely' FROM Commands WHERE key_name='log_Silence'
UNION ALL
SELECT id, 'en', 'Force Pixel Shader 1.1' FROM Commands WHERE key_name='d3d9_PSforce11'
UNION ALL
SELECT id, 'en', 'Vertex shaders 3.0' FROM Commands WHERE key_name='d3d9_VS30'
UNION ALL
SELECT id, 'en', 'Force Vertex Shader 1.1' FROM Commands WHERE key_name='d3d9_VSforce11'
UNION ALL
SELECT id, 'en', 'Allow software rendering' FROM Commands WHERE key_name='d3d9_AllowSoftware'
UNION ALL
SELECT id, 'en', 'Pipeline buffer size' FROM Commands WHERE key_name='d3d9_pip_buff_size'
UNION ALL
SELECT id, 'en', 'Vertex buffer pool size' FROM Commands WHERE key_name='d3d9_VBPoolSize'
UNION ALL
SELECT id, 'en', 'Batching type' FROM Commands WHERE key_name='r_BatchType'
UNION ALL
SELECT id, 'en', 'Batching' FROM Commands WHERE key_name='r_Batching'
UNION ALL
SELECT id, 'en', 'Material batching' FROM Commands WHERE key_name='r_MaterialsBatching'
UNION ALL
SELECT id, 'en', 'NVIDIA 3D Vision shadows' FROM Commands WHERE key_name='r_3dvision_bubbleshadow'
UNION ALL
SELECT id, 'en', 'Adaptive Aion shadows' FROM Commands WHERE key_name='r_aionshadow_adaptive'
UNION ALL
SELECT id, 'en', 'Aion shadow blur' FROM Commands WHERE key_name='r_aionshadow_blur'
UNION ALL
SELECT id, 'en', 'Aion shadow object size' FROM Commands WHERE key_name='r_aionshadow_obj_size'
UNION ALL
SELECT id, 'en', 'Aion shadow texture height' FROM Commands WHERE key_name='r_aionshadow_tex_height'
UNION ALL
SELECT id, 'en', 'Anti-aliasing mode' FROM Commands WHERE key_name='r_AntialiasingMode'
UNION ALL
SELECT id, 'en', 'Brightness' FROM Commands WHERE key_name='r_Brightness'
UNION ALL
SELECT id, 'en', 'Character LOD bias' FROM Commands WHERE key_name='r_CharacterLODBias'
UNION ALL
SELECT id, 'en', 'Chromatic aberration' FROM Commands WHERE key_name='r_ChromaticAberration'
UNION ALL
SELECT id, 'en', 'Color bit depth' FROM Commands WHERE key_name='r_ColorBits'
UNION ALL
SELECT id, 'en', 'Color grading' FROM Commands WHERE key_name='r_ColorGrading'
UNION ALL
SELECT id, 'en', 'Deferred shading ambient lights' FROM Commands WHERE key_name='r_DeferredShadingAmbientLights'
UNION ALL
SELECT id, 'en', 'Depth of field' FROM Commands WHERE key_name='r_DepthOfField'
UNION ALL
SELECT id, 'en', 'Detail level' FROM Commands WHERE key_name='r_Detail'
UNION ALL
SELECT id, 'en', 'Near draw FOV' FROM Commands WHERE key_name='r_DrawNearFOV'
UNION ALL
SELECT id, 'en', 'Near draw Z range' FROM Commands WHERE key_name='r_DrawNearZRange'
UNION ALL
SELECT id, 'en', 'Dynamic cloud atlas max size' FROM Commands WHERE key_name='r_DynTexAtlasCloudsMaxSize'
UNION ALL
SELECT id, 'en', 'Dynamic sprite atlas max size' FROM Commands WHERE key_name='r_DynTexAtlasSpritesMaxSize'
UNION ALL
SELECT id, 'en', 'Dynamic texture max size' FROM Commands WHERE key_name='r_DynTexMaxSize'
UNION ALL
SELECT id, 'en', 'Image enhancement' FROM Commands WHERE key_name='r_EnhanceImage'
UNION ALL
SELECT id, 'en', 'Environment cubemap resolution' FROM Commands WHERE key_name='r_EnvCMResolution'
UNION ALL
SELECT id, 'en', 'Cubemap update interval' FROM Commands WHERE key_name='r_EnvCMupdateInterval'
UNION ALL
SELECT id, 'en', 'Environment light cubemap size' FROM Commands WHERE key_name='r_EnvLightCMSize'
UNION ALL
SELECT id, 'en', 'Environment texture resolution' FROM Commands WHERE key_name='r_EnvTexResolution'
UNION ALL
SELECT id, 'en', 'Environment texture update interval' FROM Commands WHERE key_name='r_EnvTexUpdateInterval'
UNION ALL
SELECT id, 'en', 'Flare tessellation ratio' FROM Commands WHERE key_name='r_FlaresTessellationRatio'
UNION ALL
SELECT id, 'en', 'Fog shadows' FROM Commands WHERE key_name='r_FogShadows'
UNION ALL
SELECT id, 'en', 'Fullscreen preemption priority' FROM Commands WHERE key_name='r_FullscreenPreemption'
UNION ALL
SELECT id, 'en', 'Fullscreen height' FROM Commands WHERE key_name='r_FullScreenHeight'
UNION ALL
SELECT id, 'en', 'Fullscreen width' FROM Commands WHERE key_name='r_FullScreenWidth'
UNION ALL
SELECT id, 'en', 'HDR bloom ratio' FROM Commands WHERE key_name='r_HDRBloomRatio'
UNION ALL
SELECT id, 'en', 'HDR brightness level' FROM Commands WHERE key_name='r_HDRBrightLevel'
UNION ALL
SELECT id, 'en', 'HDR grain amount' FROM Commands WHERE key_name='r_HDRGrainAmount'
UNION ALL
SELECT id, 'en', 'LOD bias' FROM Commands WHERE key_name='r_LodBias'
UNION ALL
SELECT id, 'en', 'Mesh precache' FROM Commands WHERE key_name='r_MeshPrecache'
UNION ALL
SELECT id, 'en', 'Motion blur' FROM Commands WHERE key_name='r_MotionBlur'
UNION ALL
SELECT id, 'en', 'MRT depth render' FROM Commands WHERE key_name='r_mrt_depthrender'
UNION ALL
SELECT id, 'en', 'MRT init detection' FROM Commands WHERE key_name='r_mrt_initdetect';
INSERT OR IGNORE INTO CommandTranslations (command_id, lang, description)
SELECT id, 'en', 'MSAA multisampling' FROM Commands WHERE key_name='r_MSAA'
UNION ALL
SELECT id, 'en', 'Multi-GPU support' FROM Commands WHERE key_name='r_MultiGPU'
UNION ALL
SELECT id, 'en', 'Half-resolution particles' FROM Commands WHERE key_name='r_ParticlesHalfRes'
UNION ALL
SELECT id, 'en', 'Half-res particle blend mode' FROM Commands WHERE key_name='r_ParticlesHalfResBlendMode'
UNION ALL
SELECT id, 'en', 'Particle motion blur' FROM Commands WHERE key_name='r_ParticlesMotionBlur'
UNION ALL
SELECT id, 'en', 'Particle tessellation' FROM Commands WHERE key_name='r_ParticlesTessellation'
UNION ALL
SELECT id, 'en', 'Post-process anti-aliasing' FROM Commands WHERE key_name='r_PostAA'
UNION ALL
SELECT id, 'en', 'Post-AA edge filter' FROM Commands WHERE key_name='r_PostAAEdgeFilter'
UNION ALL
SELECT id, 'en', 'Post-process effects' FROM Commands WHERE key_name='r_PostProcessEffects'
UNION ALL
SELECT id, 'en', 'Post-process game FX' FROM Commands WHERE key_name='r_PostProcessEffectsGameFx'
UNION ALL
SELECT id, 'en', 'Post-process filters' FROM Commands WHERE key_name='r_PostProcessFilters'
UNION ALL
SELECT id, 'en', 'Post-process GameFX' FROM Commands WHERE key_name='r_PostProcessGameFx'
UNION ALL
SELECT id, 'en', 'Procedural flares' FROM Commands WHERE key_name='r_ProcFlares'
UNION ALL
SELECT id, 'en', 'Pseudo-fullscreen mode' FROM Commands WHERE key_name='r_PseudoFullscreen'
UNION ALL
SELECT id, 'en', 'Bump mapping quality' FROM Commands WHERE key_name='r_Quality_BumpMapping'
UNION ALL
SELECT id, 'en', 'Rain' FROM Commands WHERE key_name='r_rain'
UNION ALL
SELECT id, 'en', 'Sharpening' FROM Commands WHERE key_name='r_Sharpening'
UNION ALL
SELECT id, 'en', 'Shadow jittering' FROM Commands WHERE key_name='r_ShadowJittering'
UNION ALL
SELECT id, 'en', 'SSAO (ambient occlusion)' FROM Commands WHERE key_name='r_ssao'
UNION ALL
SELECT id, 'en', 'SSDO' FROM Commands WHERE key_name='r_ssdo'
UNION ALL
SELECT id, 'en', 'Screen-space reflections' FROM Commands WHERE key_name='r_SSReflections'
UNION ALL
SELECT id, 'en', 'Stencil buffer bit depth' FROM Commands WHERE key_name='r_StencilBits'
UNION ALL
SELECT id, 'en', 'Sun shafts (god rays)' FROM Commands WHERE key_name='r_sunshafts'
UNION ALL
SELECT id, 'en', 'Vertex buffer sync' FROM Commands WHERE key_name='r_SyncVBuf'
UNION ALL
SELECT id, 'en', 'Max anisotropic filtering' FROM Commands WHERE key_name='r_TexMaxAnisotropy'
UNION ALL
SELECT id, 'en', 'Texture streaming' FROM Commands WHERE key_name='r_TextureStreaming'
UNION ALL
SELECT id, 'en', 'Skip mips on streaming' FROM Commands WHERE key_name='r_TexturesStreamingSkipMips'
UNION ALL
SELECT id, 'en', 'Texture warmup' FROM Commands WHERE key_name='r_TexturesWarmup'
UNION ALL
SELECT id, 'en', 'UI shading' FROM Commands WHERE key_name='r_ui_shading'
UNION ALL
SELECT id, 'en', 'Force half-res particles' FROM Commands WHERE key_name='r_UseParticlesHalfResForce'
UNION ALL
SELECT id, 'en', 'Particle merging' FROM Commands WHERE key_name='r_UseParticlesMerging'
UNION ALL
SELECT id, 'en', 'Particle refraction' FROM Commands WHERE key_name='r_UseParticlesRefraction'
UNION ALL
SELECT id, 'en', 'Soft particles' FROM Commands WHERE key_name='r_UseSoftParticles'
UNION ALL
SELECT id, 'en', 'Vegetation sprite resolution' FROM Commands WHERE key_name='r_VegetationSpritesTexRes'
UNION ALL
SELECT id, 'en', 'Volumetric fog' FROM Commands WHERE key_name='r_VolumetricFog'
UNION ALL
SELECT id, 'en', 'Water caustics' FROM Commands WHERE key_name='r_WaterCaustics'
UNION ALL
SELECT id, 'en', 'Water god rays' FROM Commands WHERE key_name='r_WaterGodRays'
UNION ALL
SELECT id, 'en', 'Area merging distance' FROM Commands WHERE key_name='e_area_merging_distance'
UNION ALL
SELECT id, 'en', 'Auto-precache CGF' FROM Commands WHERE key_name='e_AutoPrecacheCgf'
UNION ALL
SELECT id, 'en', 'Minimum character LOD' FROM Commands WHERE key_name='e_CharLodMin'
UNION ALL
SELECT id, 'en', 'Vegetation culling activation' FROM Commands WHERE key_name='e_CullVegActivation'
UNION ALL
SELECT id, 'en', 'Allow game decals' FROM Commands WHERE key_name='e_DecalsAllowGameDecals'
UNION ALL
SELECT id, 'en', 'Decal lifetime scale' FROM Commands WHERE key_name='e_DecalsLifeTimeScale'
UNION ALL
SELECT id, 'en', 'Object dissolve' FROM Commands WHERE key_name='e_Dissolve'
UNION ALL
SELECT id, 'en', 'Dynamic lights' FROM Commands WHERE key_name='e_DynamicLights'
UNION ALL
SELECT id, 'en', 'Effects quality' FROM Commands WHERE key_name='e_effect_quality'
UNION ALL
SELECT id, 'en', 'Entity view distance' FROM Commands WHERE key_name='e_ent_view_dist_ratio'
UNION ALL
SELECT id, 'en', 'Fog' FROM Commands WHERE key_name='e_fog'
UNION ALL
SELECT id, 'en', 'Global Illumination' FROM Commands WHERE key_name='e_GI'
UNION ALL
SELECT id, 'en', 'GSM shadow cache' FROM Commands WHERE key_name='e_GsmCache';
INSERT OR IGNORE INTO CommandTranslations (command_id, lang, description)
SELECT id, 'en', 'GSM LOD count' FROM Commands WHERE key_name='e_GsmLodsNum'
UNION ALL
SELECT id, 'en', 'HW occlusion culling (objects)' FROM Commands WHERE key_name='e_HwOcclusionCullingObjects'
UNION ALL
SELECT id, 'en', 'HW occlusion culling (particles)' FROM Commands WHERE key_name='e_HwOcclusionCullingparticles'
UNION ALL
SELECT id, 'en', 'HW occlusion culling (vegetation)' FROM Commands WHERE key_name='e_HwOcclusionCullingVegetation'
UNION ALL
SELECT id, 'en', 'HW occlusion culling (water)' FROM Commands WHERE key_name='e_HwOcclusionCullingWater'
UNION ALL
SELECT id, 'en', 'HW water occlusion culling (legacy)' FROM Commands WHERE key_name='e_hw_occlusion_culling_water'
UNION ALL
SELECT id, 'en', 'Enable movie jukebox' FROM Commands WHERE key_name='e_jukebox_movie_enable'
UNION ALL
SELECT id, 'en', 'Level' FROM Commands WHERE key_name='e_level'
UNION ALL
SELECT id, 'en', 'LOD component max size' FROM Commands WHERE key_name='e_LodCompMaxSize'
UNION ALL
SELECT id, 'en', 'Minimum LOD' FROM Commands WHERE key_name='e_LodMin'
UNION ALL
SELECT id, 'en', 'Min triangles for LOD' FROM Commands WHERE key_name='e_LodMinTtris'
UNION ALL
SELECT id, 'en', 'Force LOD use' FROM Commands WHERE key_name='e_LodsForceUse'
UNION ALL
SELECT id, 'en', 'Max view distance lerp' FROM Commands WHERE key_name='e_MaxViewDistSpecLerp'
UNION ALL
SELECT id, 'en', 'No terrain shadow draw' FROM Commands WHERE key_name='e_nodraw_terrain_shadow'
UNION ALL
SELECT id, 'en', 'Occlusion culling view distance' FROM Commands WHERE key_name='e_OcclusionCullingViewDistRatio'
UNION ALL
SELECT id, 'en', 'Optimized render objects' FROM Commands WHERE key_name='e_optimized_render_object'
UNION ALL
SELECT id, 'en', 'Object quality' FROM Commands WHERE key_name='e_ObjQuality'
UNION ALL
SELECT id, 'en', 'Particle diffuse cubemap' FROM Commands WHERE key_name='e_ParticlesDiffCM'
UNION ALL
SELECT id, 'en', 'Force soft particles' FROM Commands WHERE key_name='e_ParticlesForceSoftParticles'
UNION ALL
SELECT id, 'en', 'Particle Global Illumination' FROM Commands WHERE key_name='e_ParticlesGI'
UNION ALL
SELECT id, 'en', 'Max particle screen size' FROM Commands WHERE key_name='e_ParticlesMaxDrawScreen'
UNION ALL
SELECT id, 'en', 'Max particle screen fill' FROM Commands WHERE key_name='e_ParticlesMaxScreenFill'
UNION ALL
SELECT id, 'en', 'Min particle pixel size' FROM Commands WHERE key_name='e_ParticlesMinDrawPixels'
UNION ALL
SELECT id, 'en', 'Particle-object collisions' FROM Commands WHERE key_name='e_ParticlesObjectCollisions'
UNION ALL
SELECT id, 'en', 'Particle preload' FROM Commands WHERE key_name='e_ParticlesPreload'
UNION ALL
SELECT id, 'en', 'Particle quality' FROM Commands WHERE key_name='e_ParticlesQuality'
UNION ALL
SELECT id, 'en', 'Particle shadows' FROM Commands WHERE key_name='e_ParticlesShadows'
UNION ALL
SELECT id, 'en', 'Particle thread' FROM Commands WHERE key_name='e_ParticlesThread'
UNION ALL
SELECT id, 'en', 'Precache level' FROM Commands WHERE key_name='e_precache_level'
UNION ALL
SELECT id, 'en', 'Precache level' FROM Commands WHERE key_name='e_PrecacheLevel'
UNION ALL
SELECT id, 'en', 'Preload materials' FROM Commands WHERE key_name='e_PreloadMaterials'
UNION ALL
SELECT id, 'en', 'Prepare deformable objects on load' FROM Commands WHERE key_name='e_PrepareDeformableObjectsAtLoadTime'
UNION ALL
SELECT id, 'en', 'Procedural vegetation' FROM Commands WHERE key_name='e_proc_vegetation'
UNION ALL
SELECT id, 'en', 'Recursion' FROM Commands WHERE key_name='e_Recursion'
UNION ALL
SELECT id, 'en', 'Recursive occlusion culling' FROM Commands WHERE key_name='e_recursion_occlusion_culling'
UNION ALL
SELECT id, 'en', 'Render' FROM Commands WHERE key_name='e_Render'
UNION ALL
SELECT id, 'en', 'Shadows' FROM Commands WHERE key_name='e_shadows'
UNION ALL
SELECT id, 'en', 'Skip terrain culling' FROM Commands WHERE key_name='e_skip_terrain_culling'
UNION ALL
SELECT id, 'en', 'Sky box' FROM Commands WHERE key_name='e_SkyBox'
UNION ALL
SELECT id, 'en', 'Sky quality' FROM Commands WHERE key_name='e_SkyQuality'
UNION ALL
SELECT id, 'en', 'Sky type' FROM Commands WHERE key_name='e_SkyType'
UNION ALL
SELECT id, 'en', 'Static object render task buffer' FROM Commands WHERE key_name='e_StatObjBufferRenderTasks'
UNION ALL
SELECT id, 'en', 'Static object preload' FROM Commands WHERE key_name='e_StatObjPreload'
UNION ALL
SELECT id, 'en', 'CGF streaming' FROM Commands WHERE key_name='e_streamCgf'
UNION ALL
SELECT id, 'en', 'Sun' FROM Commands WHERE key_name='e_sun'
UNION ALL
SELECT id, 'en', 'Terrain ambient occlusion' FROM Commands WHERE key_name='e_TerrainAo'
UNION ALL
SELECT id, 'en', 'Terrain LOD' FROM Commands WHERE key_name='e_TerrainLodRatio'
UNION ALL
SELECT id, 'en', 'Max terrain occlusion culling distance' FROM Commands WHERE key_name='e_TerrainOcclusionCullingMaxDist'
UNION ALL
SELECT id, 'en', 'Terrain texture LOD' FROM Commands WHERE key_name='e_TerrainTextureLodRatio'
UNION ALL
SELECT id, 'en', 'Terrain texture LOD bias' FROM Commands WHERE key_name='e_TerrainTextureLodRatioBias';
INSERT OR IGNORE INTO CommandTranslations (command_id, lang, description)
SELECT id, 'en', 'Use backup shader' FROM Commands WHERE key_name='e_use_backup_shader'
UNION ALL
SELECT id, 'en', 'Terrain shadow from light source' FROM Commands WHERE key_name='e_use_terrain_shadow_light'
UNION ALL
SELECT id, 'en', 'Vegetation bending' FROM Commands WHERE key_name='e_VegetationBending'
UNION ALL
SELECT id, 'en', 'Minimum vegetation size' FROM Commands WHERE key_name='e_VegetationMinSize'
UNION ALL
SELECT id, 'en', 'Vegetation static instancing' FROM Commands WHERE key_name='e_vegetation_static_instancing'
UNION ALL
SELECT id, 'en', 'Vegetation sprites' FROM Commands WHERE key_name='e_VegetationSprites'
UNION ALL
SELECT id, 'en', 'Vegetation sprite batching' FROM Commands WHERE key_name='e_VegetationSpritesBatching'
UNION ALL
SELECT id, 'en', 'Min custom sprite distance' FROM Commands WHERE key_name='e_VegetationSpritesDistanceCustomRatioMin'
UNION ALL
SELECT id, 'en', 'Min sprite distance' FROM Commands WHERE key_name='e_VegetationSpritesDistanceatioMin'
UNION ALL
SELECT id, 'en', 'Vegetation color from terrain' FROM Commands WHERE key_name='e_VegetationUseTerrainColor'
UNION ALL
SELECT id, 'en', 'View distance' FROM Commands WHERE key_name='e_ViewDistRatio'
UNION ALL
SELECT id, 'en', 'Custom view distance' FROM Commands WHERE key_name='e_ViewDistRatioCustom'
UNION ALL
SELECT id, 'en', 'Detail view distance' FROM Commands WHERE key_name='e_ViewDistRatioDetail'
UNION ALL
SELECT id, 'en', 'Light view distance' FROM Commands WHERE key_name='e_ViewDistRatioLights'
UNION ALL
SELECT id, 'en', 'Vegetation view distance' FROM Commands WHERE key_name='e_ViewDistRatioVegetation'
UNION ALL
SELECT id, 'en', 'View distance' FROM Commands WHERE key_name='e_view_dist_ratio'
UNION ALL
SELECT id, 'en', 'Detail view distance' FROM Commands WHERE key_name='e_view_dist_ratio_detail'
UNION ALL
SELECT id, 'en', 'Vegetation view distance' FROM Commands WHERE key_name='e_view_dist_ratio_vegetation'
UNION ALL
SELECT id, 'en', 'Vegetation view distance' FROM Commands WHERE key_name='e_view_dist_vegetation'
UNION ALL
SELECT id, 'en', 'Soft particles on water' FROM Commands WHERE key_name='e_water_ocean_soft_particles'
UNION ALL
SELECT id, 'en', 'Wind' FROM Commands WHERE key_name='e_wind'
UNION ALL
SELECT id, 'en', 'Ocean' FROM Commands WHERE key_name='e_waterocean'
UNION ALL
SELECT id, 'en', 'Animation error clamp' FROM Commands WHERE key_name='ac_animErrorClamp'
UNION ALL
SELECT id, 'en', 'Animation time clamp' FROM Commands WHERE key_name='ac_clampTimeAnimation'
UNION ALL
SELECT id, 'en', 'Entity time clamp' FROM Commands WHERE key_name='ac_clampTimeEntity'
UNION ALL
SELECT id, 'en', 'Disable fancy transitions' FROM Commands WHERE key_name='ac_disableFancyTransitions'
UNION ALL
SELECT id, 'en', 'Minimum character LOD' FROM Commands WHERE key_name='ca_CharLodMin'
UNION ALL
SELECT id, 'en', 'Memory defragmentation' FROM Commands WHERE key_name='ca_MemoryDefragEnabled'
UNION ALL
SELECT id, 'en', 'Precache animation sets' FROM Commands WHERE key_name='ca_PrecacheAnimationSets'
UNION ALL
SELECT id, 'en', 'Shared vertices' FROM Commands WHERE key_name='ca_ShareVertex'
UNION ALL
SELECT id, 'en', 'Animation cache' FROM Commands WHERE key_name='ca_UseAnimationsCache'
UNION ALL
SELECT id, 'en', 'Facial animation' FROM Commands WHERE key_name='ca_UseFacialAnimation'
UNION ALL
SELECT id, 'en', 'Character physics' FROM Commands WHERE key_name='ca_UsePhysics'
UNION ALL
SELECT id, 'en', 'Disable animation thread' FROM Commands WHERE key_name='ca_disable_thread'
UNION ALL
SELECT id, 'en', 'Force LOD' FROM Commands WHERE key_name='ca_lod_force'
UNION ALL
SELECT id, 'en', 'LOD ratio' FROM Commands WHERE key_name='ca_lod_ratio'
UNION ALL
SELECT id, 'en', 'Animation thread' FROM Commands WHERE key_name='ca_thread'
UNION ALL
SELECT id, 'en', 'Ambient fire (world fire)' FROM Commands WHERE key_name='ai_AmbientFireEnable'
UNION ALL
SELECT id, 'en', 'Ambient fire quota' FROM Commands WHERE key_name='ai_AmbientFireQuota'
UNION ALL
SELECT id, 'en', 'Ambient fire update interval' FROM Commands WHERE key_name='ai_AmbientFireUpdateInterval'
UNION ALL
SELECT id, 'en', 'Ambient fire debug' FROM Commands WHERE key_name='ai_DebugDrawAmbientFire'
UNION ALL
SELECT id, 'en', 'DirectInput keys' FROM Commands WHERE key_name='i_dinputkeys'
UNION ALL
SELECT id, 'en', 'Flashlight fog volume' FROM Commands WHERE key_name='i_flashlight_has_fog_volume'
UNION ALL
SELECT id, 'en', 'Mouse acceleration' FROM Commands WHERE key_name='i_mouse_accel'
UNION ALL
SELECT id, 'en', 'Mouse inertia' FROM Commands WHERE key_name='i_mouse_inertia'
UNION ALL
SELECT id, 'en', 'Mouse smoothing' FROM Commands WHERE key_name='i_mouse_smooth'
UNION ALL
SELECT id, 'en', 'Input precache' FROM Commands WHERE key_name='i_precache'
UNION ALL
SELECT id, 'en', 'Threaded input' FROM Commands WHERE key_name='iThreaded'
UNION ALL
SELECT id, 'en', 'Particle effects' FROM Commands WHERE key_name='i_particleeffects'
UNION ALL
SELECT id, 'en', 'Reject effects' FROM Commands WHERE key_name='i_rejecteffects';
INSERT OR IGNORE INTO CommandTranslations (command_id, lang, description)
SELECT id, 'en', 'Ice effects' FROM Commands WHERE key_name='i_iceeffects'
UNION ALL
SELECT id, 'en', 'Light range' FROM Commands WHERE key_name='p_lightrange'
UNION ALL
SELECT id, 'en', 'General shader' FROM Commands WHERE key_name='q_ShaderGeneral'
UNION ALL
SELECT id, 'en', 'Post-process shader' FROM Commands WHERE key_name='q_ShaderPostProcess'
UNION ALL
SELECT id, 'en', 'Terrain shader' FROM Commands WHERE key_name='q_ShaderTerrain'
UNION ALL
SELECT id, 'en', 'Vegetation shader' FROM Commands WHERE key_name='q_ShaderVegetation'
UNION ALL
SELECT id, 'en', 'Restricted console' FROM Commands WHERE key_name='con_restricted'
UNION ALL
SELECT id, 'en', 'Aion heap size' FROM Commands WHERE key_name='g_aionHeapSize'
UNION ALL
SELECT id, 'en', 'FX level' FROM Commands WHERE key_name='g_fxLevel'
UNION ALL
SELECT id, 'en', 'GPU particle physics' FROM Commands WHERE key_name='g_gpu_particle_physics'
UNION ALL
SELECT id, 'en', 'Slot load state' FROM Commands WHERE key_name='g_loadSlotState'
UNION ALL
SELECT id, 'en', 'Mute pet sounds' FROM Commands WHERE key_name='g_muteMyPet'
UNION ALL
SELECT id, 'en', 'OBS volume' FROM Commands WHERE key_name='g_OBS_volume'
UNION ALL
SELECT id, 'en', 'Open special server list' FROM Commands WHERE key_name='g_openSpecialServerList'
UNION ALL
SELECT id, 'en', 'Player profile' FROM Commands WHERE key_name='g_playerprofile'
UNION ALL
SELECT id, 'en', 'Radial blur' FROM Commands WHERE key_name='g_radialBlur'
UNION ALL
SELECT id, 'en', 'Reconnect support' FROM Commands WHERE key_name='g_reconnectable'
UNION ALL
SELECT id, 'en', 'Screenshot path' FROM Commands WHERE key_name='g_screenshot_preset_path'
UNION ALL
SELECT id, 'en', 'UI action messages' FROM Commands WHERE key_name='g_showUIActionMsg'
UNION ALL
SELECT id, 'en', 'Teleport UI delay' FROM Commands WHERE key_name='g_teleportUIDelay'
UNION ALL
SELECT id, 'en', 'UI interpolation ID' FROM Commands WHERE key_name='g_ui_interpolation_id'
UNION ALL
SELECT id, 'en', 'UI interpolation type' FROM Commands WHERE key_name='g_ui_interpolation_type'
UNION ALL
SELECT id, 'en', 'UI shadow' FROM Commands WHERE key_name='g_ui_shadow'
UNION ALL
SELECT id, 'en', 'Siege warfare options' FROM Commands WHERE key_name='g_ui_siegewarfare_option'
UNION ALL
SELECT id, 'en', 'UI tile type' FROM Commands WHERE key_name='g_ui_tile_type'
UNION ALL
SELECT id, 'en', 'Transition animations' FROM Commands WHERE key_name='g_useTransitionAnimation'
UNION ALL
SELECT id, 'en', 'Glow effect' FROM Commands WHERE key_name='g_video_GLOW'
UNION ALL
SELECT id, 'en', 'GPU particle physics' FROM Commands WHERE key_name='gpu_particle_physics'
UNION ALL
SELECT id, 'en', 'HUD debug' FROM Commands WHERE key_name='hud_debug'
UNION ALL
SELECT id, 'en', 'HUD paused on start' FROM Commands WHERE key_name='hud_startpaused'
UNION ALL
SELECT id, 'en', 'Priority threshold' FROM Commands WHERE key_name='PriorityThreshold'
UNION ALL
SELECT id, 'en', 'MRT profile: background' FROM Commands WHERE key_name='g_cfg_video_MRT_BACKGROUND'
UNION ALL
SELECT id, 'en', 'MRT profile: bump mapping' FROM Commands WHERE key_name='g_cfg_video_MRT_BUMP'
UNION ALL
SELECT id, 'en', 'MRT profile: camera' FROM Commands WHERE key_name='g_cfg_video_MRT_CAMERA'
UNION ALL
SELECT id, 'en', 'MRT profile: depth of field' FROM Commands WHERE key_name='g_cfg_video_MRT_DOF'
UNION ALL
SELECT id, 'en', 'MRT profile: effects' FROM Commands WHERE key_name='g_cfg_video_MRT_EFFECT'
UNION ALL
SELECT id, 'en', 'MRT profile: entity distance' FROM Commands WHERE key_name='g_cfg_video_MRT_ENTITY_DIST'
UNION ALL
SELECT id, 'en', 'MRT profile: environment textures' FROM Commands WHERE key_name='g_cfg_video_MRT_ENV_TEX'
UNION ALL
SELECT id, 'en', 'MRT profile: anti-aliasing' FROM Commands WHERE key_name='g_cfg_video_MRT_FSAA'
UNION ALL
SELECT id, 'en', 'MRT profile: general' FROM Commands WHERE key_name='g_cfg_video_MRT_GENERAL'
UNION ALL
SELECT id, 'en', 'MRT profile: glare' FROM Commands WHERE key_name='g_cfg_video_MRT_GLARE'
UNION ALL
SELECT id, 'en', 'MRT profile: glow' FROM Commands WHERE key_name='g_cfg_video_MRT_GLOW'
UNION ALL
SELECT id, 'en', 'MRT profile: lowest' FROM Commands WHERE key_name='g_cfg_video_MRT_LOWEST'
UNION ALL
SELECT id, 'en', 'MRT profile: model cache' FROM Commands WHERE key_name='g_cfg_video_MRT_MODEL_CACHE'
UNION ALL
SELECT id, 'en', 'MRT profile: shaders' FROM Commands WHERE key_name='g_cfg_video_MRT_SHADER'
UNION ALL
SELECT id, 'en', 'MRT profile: shadows' FROM Commands WHERE key_name='g_cfg_video_MRT_SHADOW'
UNION ALL
SELECT id, 'en', 'MRT profile: skill effects' FROM Commands WHERE key_name='g_cfg_video_MRT_SKILLFX'
UNION ALL
SELECT id, 'en', 'MRT profile: sun shafts' FROM Commands WHERE key_name='g_cfg_video_MRT_SUNSHAFT'
UNION ALL
SELECT id, 'en', 'MRT profile: terrain distance' FROM Commands WHERE key_name='g_cfg_video_MRT_TERRAIN_DIST'
UNION ALL
SELECT id, 'en', 'MRT profile: textures' FROM Commands WHERE key_name='g_cfg_video_MRT_TEXTURE';
INSERT OR IGNORE INTO CommandTranslations (command_id, lang, description)
SELECT id, 'en', 'MRT profile: water' FROM Commands WHERE key_name='g_cfg_video_MRT_WATER'
UNION ALL
SELECT id, 'en', 'MRT profile: weather layers' FROM Commands WHERE key_name='g_cfg_video_MRT_WEATHERLAYER'
UNION ALL
SELECT id, 'en', 'Video effects level' FROM Commands WHERE key_name='g_cfg_video_EFFECT'
UNION ALL
SELECT id, 'en', 'Battery saver mode (mutes on low battery)' FROM Commands WHERE key_name='s_BatterySave_Enable'
UNION ALL
SELECT id, 'en', 'Sound sample rate (Hz)' FROM Commands WHERE key_name='s_FormatSampleRate'
UNION ALL
SELECT id, 'en', 'HRTF (surround sound in headphones)' FROM Commands WHERE key_name='s_HRTFEnable'
UNION ALL
SELECT id, 'en', 'Ignore game state for music' FROM Commands WHERE key_name='s_MusicIgnoreGameStatus'
UNION ALL
SELECT id, 'en', 'Mute music' FROM Commands WHERE key_name='s_MusicMute'
UNION ALL
SELECT id, 'en', 'Play music once' FROM Commands WHERE key_name='s_MusicPlayOnce'
UNION ALL
SELECT id, 'en', 'Music volume' FROM Commands WHERE key_name='s_MusicVolume'
UNION ALL
SELECT id, 'en', 'NPC sound ping' FROM Commands WHERE key_name='s_NCPing_Enable'
UNION ALL
SELECT id, 'en', 'Sound priority threshold' FROM Commands WHERE key_name='s_PriorityThreshold'
UNION ALL
SELECT id, 'en', 'Sound shading level (legacy)' FROM Commands WHERE key_name='s_spec_Shading'
UNION ALL
SELECT id, 'en', 'Mute music (duplicate)' FROM Commands WHERE key_name='ss_MusicMute';