-- ==================== Команды из стандартного system.cfg ====================
-- Помечаем как 'simple' — попадут в режим «Стандартные»

UPDATE Commands SET mode='simple' WHERE key_name IN (
    'g_ThirdPersonRange', 'g_blend_time', 'g_blendout_time',
    'g_cam_key_rot', 'g_cam_rot_ratio', 'g_cfg_version',
    'g_cfg_video_MODEL_CACHE', 'g_cfg_video_SHADER', 'g_cfg_video_SHADOW',
    'g_cfg_video_SKILLFX', 'g_cfg_video_TERRAIN_DIST',
    'g_cfg_video_TEXTURE', 'g_cfg_video_WATER',
    'g_cfg_video_screen_res', 'g_chainSkillChangeCooltimeDelay',
    'g_chainSkillIndicateDelay', 'g_chatlog', 'g_client_var',
    'g_enableSkillVoice', 'g_maxfps', 'g_save_preset', 'g_showFps',
    'g_show_breath', 'g_uiContour', 'g_uiFX', 'g_ui_font',
    'g_ui_stillview', 'g_verbose_animation',
    -- r_
    'r_DetailDistance', 'r_FSAA_samples', 'r_Height', 'r_RenderMode',
    'r_RestoreLeft', 'r_RestoreTop', 'r_ShaderModel',
    'r_ShadersPrecache', 'r_ShadowBlur', 'r_TexBumpResolution',
    'r_TexLMResolution', 'r_TexResolution', 'r_TexSkyResolution',
    'r_Texture_Anisotropic_Level', 'r_TexturesStreamPoolSize',
    'r_VSync', 'r_Vegetation_PerpixelLight', 'r_WaterReflections',
    'r_WaterReflections_MaxViewDist', 'r_WaterUpdateDistance',
    'r_Width', 'r_WindowHeight', 'r_WindowWidth', 'r_checkSunVis',
    -- e_
    'e_beach', 'e_decals', 'e_light_maps', 'e_light_maps_quality',
    'e_maxdistance_ratio_entities', 'e_maxdistance_terrain',
    'e_obj_view_dist_ratio', 'e_objects_fade_on_distance',
    'e_particles_fullfx', 'e_particles_max_count',
    'e_shadow_maps', 'e_shadow_spots', 'e_vegetation_min_size',
    'e_vegetation_update_shadow_every_frame', 'e_water_render_distance',
    'e_weather_fx_enable',
    -- ca_
    'ca_AnimWarningLevel', 'ca_AnimationDeferredLoad',
    'ca_AnimationUnloadCheckPerFrame', 'ca_AnimationUnloadDelay',
    'ca_AnimationUnloadMaxPerFrame', 'ca_ClothMode', 'ca_DrawBones',
    'ca_EnableCCG', 'ca_EnableCharacterShadowVolume',
    'ca_EnableCubicBlending', 'ca_EnableDecals', 'ca_EnableLightUpdate',
    'ca_EnableTangentSkinning', 'ca_HairAnim', 'ca_KeepModels',
    'ca_LodBias', 'ca_NoDrawShadowVolumes', 'ca_NoMorph',
    'ca_NormalizeBases', 'ca_SSEEnable', 'ca_SafeReskin',
    'ca_ambient_light_range',
    -- s_
    's_MasterVolume', 's_SFXVolume_COMMENT_GOSSIP',
    's_SFXVolume_COMMENT_NPC', 's_SFXVolume_COMMENT_QUEST',
    's_SFXVolume_COMMENT_SYSTEM', 's_SFXVolume_ENV',
    's_SFXVolume_FX', 's_SFXVolume_UI', 's_SFXVolume_WEATHER',
    's_SampleRate',
    -- sys_
    'sys_AdaptiveCharLOD', 'sys_SSInfo', 'sys_StreamCompressionMask',
    'sys_skiponlowspec'
);