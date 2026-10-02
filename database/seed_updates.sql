-- ==================== possible_values ====================

-- Уровни качества sys_spec_* — диапазон -2..5
UPDATE Commands SET possible_values='-2,-1,0,1,2,3,4,5'
WHERE key_name LIKE 'sys_spec_%';

-- Уровни g_cfg_video_* (кроме MRT) — диапазон -2..5
UPDATE Commands SET possible_values='-2,-1,0,1,2,3,4,5'
WHERE key_name LIKE 'g_cfg_video_%' AND key_name NOT LIKE 'g_cfg_video_MRT_%';

-- MRT-профили — 0..5
UPDATE Commands SET possible_values='0,1,2,3,4,5'
WHERE key_name LIKE 'g_cfg_video_MRT_%';

-- Enum-команды
UPDATE Commands SET possible_values='1,2,3,4'
WHERE key_name='r_RenderMode';

UPDATE Commands SET possible_values='0,2,3,4'
WHERE key_name='r_ShaderModel';

UPDATE Commands SET possible_values='NONE,BILINEAR,TRILINEAR,ANISOTROPIC'
WHERE key_name='d3d9_TextureFilter';

UPDATE Commands SET possible_values='0,1,2,4,8,16'
WHERE key_name='r_Texture_Anisotropic_Level';

UPDATE Commands SET possible_values='0,1,2,4,8'
WHERE key_name='r_FSAA_samples';

-- ==================== ДЕФОЛТЫ из реального cfg ====================
-- Уровни качества
UPDATE Commands SET default_value='0'  WHERE key_name='sys_spec_Quality';
UPDATE Commands SET default_value='0'  WHERE key_name='sys_spec_light';
UPDATE Commands SET default_value='0'  WHERE key_name='sys_spec_Shading';
UPDATE Commands SET default_value='0'  WHERE key_name='sys_spec_Shadows';
UPDATE Commands SET default_value='0'  WHERE key_name='sys_spec_Texture';
UPDATE Commands SET default_value='0'  WHERE key_name='sys_spec_TextureResolution';
UPDATE Commands SET default_value='0'  WHERE key_name='sys_spec_Particles';
UPDATE Commands SET default_value='0'  WHERE key_name='sys_spec_Physics';
UPDATE Commands SET default_value='0'  WHERE key_name='sys_spec_PostProcessing';
UPDATE Commands SET default_value='0'  WHERE key_name='sys_spec_ObjectDetail';
UPDATE Commands SET default_value='0'  WHERE key_name='sys_spec_GameEffects';
UPDATE Commands SET default_value='0'  WHERE key_name='sys_spec_Sound';
UPDATE Commands SET default_value='0'  WHERE key_name='sys_spec_VolumetricEffects';
UPDATE Commands SET default_value='-2' WHERE key_name='sys_spec_Environment';

-- Уровни видео
UPDATE Commands SET default_value='-2' WHERE key_name='g_cfg_video_GENERAL';
UPDATE Commands SET default_value='4'  WHERE key_name='g_cfg_video_EFFECT';
UPDATE Commands SET default_value='4'  WHERE key_name='g_cfg_video_ENTITY_DIST';
UPDATE Commands SET default_value='3'  WHERE key_name='g_cfg_video_ENV_TEX';
UPDATE Commands SET default_value='5'  WHERE key_name='g_cfg_video_FSAA';
UPDATE Commands SET default_value='5'  WHERE key_name='g_cfg_video_GLARE';
UPDATE Commands SET default_value='6'  WHERE key_name='g_cfg_video_GLOW';
UPDATE Commands SET default_value='0'  WHERE key_name='g_cfg_video_BACKGROUND';
UPDATE Commands SET default_value='4'  WHERE key_name='g_cfg_video_SHADER';
UPDATE Commands SET default_value='0'  WHERE key_name='g_cfg_video_SHADOW';
UPDATE Commands SET default_value='5'  WHERE key_name='g_cfg_video_SKILLFX';
UPDATE Commands SET default_value='4'  WHERE key_name='g_cfg_video_TERRAIN_DIST';
UPDATE Commands SET default_value='4'  WHERE key_name='g_cfg_video_TEXTURE';
UPDATE Commands SET default_value='0'  WHERE key_name='g_cfg_video_WATER';
UPDATE Commands SET default_value='3'  WHERE key_name='g_cfg_video_MODEL_CACHE';
UPDATE Commands SET default_value='1'  WHERE key_name='g_cfg_video_screen_res';

-- MRT-профили (из реального cfg)
UPDATE Commands SET default_value='4' WHERE key_name='g_cfg_video_MRT_BACKGROUND';
UPDATE Commands SET default_value='3' WHERE key_name='g_cfg_video_MRT_BUMP';
UPDATE Commands SET default_value='3' WHERE key_name='g_cfg_video_MRT_CAMERA';
UPDATE Commands SET default_value='5' WHERE key_name='g_cfg_video_MRT_DOF';
UPDATE Commands SET default_value='4' WHERE key_name='g_cfg_video_MRT_EFFECT';
UPDATE Commands SET default_value='4' WHERE key_name='g_cfg_video_MRT_ENTITY_DIST';
UPDATE Commands SET default_value='3' WHERE key_name='g_cfg_video_MRT_ENV_TEX';
UPDATE Commands SET default_value='2' WHERE key_name='g_cfg_video_MRT_FSAA';
UPDATE Commands SET default_value='3' WHERE key_name='g_cfg_video_MRT_GENERAL';
UPDATE Commands SET default_value='5' WHERE key_name='g_cfg_video_MRT_GLARE';
UPDATE Commands SET default_value='2' WHERE key_name='g_cfg_video_MRT_GLOW';
UPDATE Commands SET default_value='3' WHERE key_name='g_cfg_video_MRT_LOWEST';
UPDATE Commands SET default_value='3' WHERE key_name='g_cfg_video_MRT_MODEL_CACHE';
UPDATE Commands SET default_value='4' WHERE key_name='g_cfg_video_MRT_SHADER';
UPDATE Commands SET default_value='2' WHERE key_name='g_cfg_video_MRT_SHADOW';
UPDATE Commands SET default_value='5' WHERE key_name='g_cfg_video_MRT_SKILLFX';
UPDATE Commands SET default_value='5' WHERE key_name='g_cfg_video_MRT_SUNSHAFT';
UPDATE Commands SET default_value='4' WHERE key_name='g_cfg_video_MRT_TERRAIN_DIST';
UPDATE Commands SET default_value='4' WHERE key_name='g_cfg_video_MRT_TEXTURE';
UPDATE Commands SET default_value='4' WHERE key_name='g_cfg_video_MRT_WATER';
UPDATE Commands SET default_value='5' WHERE key_name='g_cfg_video_MRT_WEATHERLAYER';

-- Разрешение
UPDATE Commands SET default_value='1920' WHERE key_name='r_Width';
UPDATE Commands SET default_value='1080' WHERE key_name='r_Height';
UPDATE Commands SET default_value='1920' WHERE key_name='r_FullScreenWidth';
UPDATE Commands SET default_value='1080' WHERE key_name='r_FullScreenHeight';
UPDATE Commands SET default_value='1581' WHERE key_name='r_WindowWidth';
UPDATE Commands SET default_value='828'  WHERE key_name='r_WindowHeight';
UPDATE Commands SET default_value='1'    WHERE key_name='r_PseudoFullscreen';

-- Рендер
UPDATE Commands SET default_value='3'         WHERE key_name='r_RenderMode';
UPDATE Commands SET default_value='4'         WHERE key_name='r_ShaderModel';
UPDATE Commands SET default_value='0'         WHERE key_name='r_VSync';
UPDATE Commands SET default_value='0'         WHERE key_name='r_ShadowBlur';
UPDATE Commands SET default_value='0'         WHERE key_name='r_ShadowType';
UPDATE Commands SET default_value='0'         WHERE key_name='r_AntialiasingMode';
UPDATE Commands SET default_value='1'         WHERE key_name='r_ShadersPrecache';
UPDATE Commands SET default_value='0'         WHERE key_name='r_Brightness';
UPDATE Commands SET default_value='0.502970'  WHERE key_name='r_Brightness';
UPDATE Commands SET default_value='8'         WHERE key_name='r_StencilBits';
UPDATE Commands SET default_value='8'         WHERE key_name='r_TextureBits';
UPDATE Commands SET default_value='16'        WHERE key_name='r_Texture_Anisotropic_Level';

-- Direct3D9
UPDATE Commands SET default_value='TRILINEAR' WHERE key_name='d3d9_TextureFilter';
UPDATE Commands SET default_value='1'         WHERE key_name='d3d9_VS30';
UPDATE Commands SET default_value='0'         WHERE key_name='d3d9_PSforce11';
UPDATE Commands SET default_value='0'         WHERE key_name='d3d9_VSforce11';
UPDATE Commands SET default_value='0'         WHERE key_name='d3d9_AllowSoftware';
UPDATE Commands SET default_value='2097152'   WHERE key_name='d3d9_VBPoolSize';
UPDATE Commands SET default_value='1000'      WHERE key_name='d3d9_pip_buff_size';

-- Игровые
UPDATE Commands SET default_value='1'    WHERE key_name='g_showFps';
UPDATE Commands SET default_value='0'    WHERE key_name='g_maxfps';
UPDATE Commands SET default_value='1'    WHERE key_name='g_save_preset';
UPDATE Commands SET default_value='0'    WHERE key_name='g_auto_disconnect';
UPDATE Commands SET default_value='1'    WHERE key_name='g_NoWarFog';
UPDATE Commands SET default_value='0'    WHERE key_name='g_open_aion_web';
UPDATE Commands SET default_value='0.60' WHERE key_name='g_ui_scale';
UPDATE Commands SET default_value='1'    WHERE key_name='g_uiFX';
UPDATE Commands SET default_value='1'    WHERE key_name='g_enableSkillVoice';
UPDATE Commands SET default_value='1'    WHERE key_name='g_useRotateAnimation';

-- Системные
UPDATE Commands SET default_value='1'     WHERE key_name='sys_64bitCache';
UPDATE Commands SET default_value='0'     WHERE key_name='sys_DeactivateConsole';
UPDATE Commands SET default_value='0'     WHERE key_name='sys_FixedFrame';
UPDATE Commands SET default_value='1'     WHERE key_name='sys_LowSpecPak';
UPDATE Commands SET default_value='1'     WHERE key_name='sys_preload';
UPDATE Commands SET default_value='-1'    WHERE key_name='sys_maxFPS';
UPDATE Commands SET default_value='1'     WHERE key_name='sys_physics_GPU';
UPDATE Commands SET default_value='40000' WHERE key_name='sys_StreamCallbackTimeBudget';
UPDATE Commands SET default_value='10240' WHERE key_name='sys_budget_videomem';
UPDATE Commands SET default_value='10240' WHERE key_name='sys_budget_sysmem';
UPDATE Commands SET default_value='8'     WHERE key_name='sys_MaxThreads';
UPDATE Commands SET default_value='1'     WHERE key_name='sys_DisableCrashDialog';
UPDATE Commands SET default_value='0'     WHERE key_name='sys_EnableAsserts';
UPDATE Commands SET default_value='1'     WHERE key_name='sys_WarningDisable';

-- Звук
UPDATE Commands SET default_value='0.105018' WHERE key_name='s_MasterVolume';
UPDATE Commands SET default_value='0.203540' WHERE key_name='s_MusicVolume';
UPDATE Commands SET default_value='1'        WHERE key_name='s_MusicMute';
UPDATE Commands SET default_value='0'        WHERE key_name='s_HRTFEnable';
UPDATE Commands SET default_value='0'        WHERE key_name='s_BatterySave_Enable';
UPDATE Commands SET default_value='1'        WHERE key_name='s_MusicIgnoreGameStatus';
UPDATE Commands SET default_value='1'        WHERE key_name='s_MusicPlayOnce';
UPDATE Commands SET default_value='1'        WHERE key_name='s_NCPing_Enable';
UPDATE Commands SET default_value='0'        WHERE key_name='s_PriorityThreshold';
UPDATE Commands SET default_value='48000'    WHERE key_name='s_SampleRate';
UPDATE Commands SET default_value='44100'    WHERE key_name='s_FormatSampleRate';
UPDATE Commands SET default_value='1'        WHERE key_name='ss_MusicMute';

-- Сеть / VoIP
UPDATE Commands SET default_value='1' WHERE key_name='net_blaze_voip_enable';
UPDATE Commands SET default_value='0' WHERE key_name='net_blaze_voip_enable_ptt';
UPDATE Commands SET default_value='0' WHERE key_name='net_blaze_voip_playback_volume';

-- Batching
UPDATE Commands SET default_value='2' WHERE key_name='r_BatchType';
UPDATE Commands SET default_value='1' WHERE key_name='r_Batching';
UPDATE Commands SET default_value='1' WHERE key_name='r_MaterialsBatching';
UPDATE Commands SET default_value='1' WHERE key_name='e_VegetationSpritesBatching';

-- Логи / Debug
UPDATE Commands SET default_value='1' WHERE key_name='log_IgnoreWarnings';
UPDATE Commands SET default_value='1' WHERE key_name='log_Silence';
UPDATE Commands SET default_value='0' WHERE key_name='hud_debug';
UPDATE Commands SET default_value='0' WHERE key_name='hud_startpaused';
UPDATE Commands SET default_value='0' WHERE key_name='e_DebugDraw';