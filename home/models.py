from django.db import models
# from django.contrib.gis.db import models

# Create your models here.
class RuralInfraAwcAcEnglishconverted(models.Model):
    geom = models.TextField(blank=True, null=True)
    awc_code = models.CharField(max_length=254, blank=True, null=True)
    district = models.CharField(max_length=254, blank=True, null=True)
    block_n = models.CharField(db_column='block_n', max_length=254, blank=True, null=True)
    project = models.CharField(max_length=254, blank=True, null=True)
    beat = models.CharField(max_length=254, blank=True, null=True)
    latitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    longitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    altitude = models.CharField(max_length=254, blank=True, null=True)
    accuracy = models.CharField(max_length=254, blank=True, null=True)
    objectid = models.BigIntegerField(blank=True, null=True)
    st_code = models.BigIntegerField(blank=True, null=True)
    st_name = models.CharField(max_length=254, blank=True, null=True)
    dist_code = models.BigIntegerField(blank=True, null=True)
    dist_name = models.CharField(max_length=254, blank=True, null=True)
    ac_no = models.BigIntegerField(blank=True, null=True)
    ac_name = models.CharField(max_length=254, blank=True, null=True)
    start = models.DateField(blank=True, null=True)
    end = models.DateField(blank=True, null=True)
    division = models.CharField(max_length=254, blank=True, null=True)
    district_1 = models.CharField(max_length=254, blank=True, null=True)
    project_2 = models.CharField(max_length=254, blank=True, null=True)
    beat_3 = models.CharField(max_length=254, blank=True, null=True)
    anganwadi_field = models.CharField(db_column='anganwadi_4', max_length=254, blank=True, null=True)  # Field renamed because it ended with '_'.
    agan_type = models.CharField(max_length=254, blank=True, null=True)
    agancbuil_field = models.CharField(db_column='agancbuil_const', max_length=254, blank=True, null=True)  # Field renamed because it ended with '_'.
    aganc_forrent = models.CharField(max_length=254, blank=True, null=True)
    yes_moveagan_govpre = models.CharField(max_length=254, blank=True, null=True)
    no_owner_agancbuil = models.CharField(max_length=254, blank=True, null=True)
    child_sitagan = models.CharField(max_length=254, blank=True, null=True)
    child_weigh_material = models.CharField(max_length=254, blank=True, null=True)
    child_weigh_mat_working = models.CharField(max_length=254, blank=True, null=True)
    adult_wtequip = models.CharField(max_length=254, blank=True, null=True)
    adult_wteq_working = models.CharField(max_length=254, blank=True, null=True)
    infant_meter = models.CharField(max_length=254, blank=True, null=True)
    infant_meter_working = models.CharField(max_length=254, blank=True, null=True)
    stadiometer = models.CharField(max_length=254, blank=True, null=True)
    stadm_working = models.CharField(max_length=254, blank=True, null=True)
    maint_repair_need = models.CharField(max_length=254, blank=True, null=True)
    agan_drinkwat_avail = models.CharField(max_length=254, blank=True, null=True)
    agan_tap = models.CharField(max_length=254, blank=True, null=True)
    plumb_workcond = models.CharField(max_length=254, blank=True, null=True)
    toil_fac = models.CharField(max_length=254, blank=True, null=True)
    toil_working = models.CharField(max_length=254, blank=True, null=True)
    electricity_connection = models.CharField(max_length=254, blank=True, null=True)
    solar_powersupply = models.CharField(max_length=254, blank=True, null=True)
    agan_tv = models.CharField(max_length=254, blank=True, null=True)
    tv_working = models.CharField(max_length=254, blank=True, null=True)
    agan_fenc = models.CharField(max_length=254, blank=True, null=True)
    agan_back_field = models.CharField(db_column='agan_back_gard', max_length=254, blank=True, null=True)  # Field renamed because it ended with '_'.
    space_own_field = models.CharField(db_column='space_own_garden', max_length=254, blank=True, null=True)  # Field renamed because it ended with '_'.
    vac_agan = models.CharField(max_length=254, blank=True, null=True)
    post_vac = models.CharField(max_length=254, blank=True, null=True)
    post_vac_aw_worker = models.BigIntegerField(blank=True, null=True)
    post_vac_help = models.BigIntegerField(blank=True, null=True)
    pro_fill_agan_post = models.CharField(max_length=254, blank=True, null=True)
    child0_6monage = models.BigIntegerField(blank=True, null=True)
    child6mon_field = models.BigIntegerField(db_column='child6mon_3yr', blank=True, null=True)  # Field renamed because it ended with '_'.
    child3_6y = models.BigIntegerField(db_column='child3 _6yrs', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    tot_no_child = models.BigIntegerField(blank=True, null=True)
    preg_moth_field = models.BigIntegerField(db_column='preg_moth_agan', blank=True, null=True)  # Field renamed because it ended with '_'.
    brestfeed_field = models.BigIntegerField(db_column='brestfeed_moth_agan', blank=True, null=True)  # Field renamed because it ended with '_'.
    preg_lact_field = models.BigIntegerField(db_column='preg_lact_moth', blank=True, null=True)  # Field renamed because it ended with '_'.
    aadh_notlinknuttrack = models.BigIntegerField(blank=True, null=True)
    preg_lact_mothaadh_notlinked_nuttrack = models.BigIntegerField(blank=True, null=True)
    child_weigh_meas_agan_mar22 = models.BigIntegerField(blank=True, null=True)
    child_heigh_meas_agan_mar22 = models.BigIntegerField(blank=True, null=True)
    no_suv_child_agan_jan_mar22 = models.BigIntegerField(blank=True, null=True)
    no_suv_child_recthr_jan_mar22 = models.BigIntegerField(blank=True, null=True)
    child_sam_field = models.BigIntegerField(db_column='child_sam_agan_jan_mar22', blank=True, null=True)  # Field renamed because it ended with '_'.
    child_rec_field = models.CharField(db_column='child_rec_vcdc_fac', max_length=254, blank=True, null=True)  # Field renamed because it ended with '_'.
    sam_child_field = models.BigIntegerField(db_column='sam_child_agan_vcdc_jan_mar22', blank=True, null=True)  # Field renamed because it ended with '_'.
    sam_agan_nrc_jan_mar22 = models.CharField(max_length=254, blank=True, null=True)
    no_adol_girl_dropsch_agan = models.BigIntegerField(blank=True, null=True)
    child_agan_sch_engl_priv_nurs = models.CharField(max_length=254, blank=True, null=True)
    ifyes_childenrol_agan_sch_priv_nurs_engl = models.BigIntegerField(blank=True, null=True)
    agan_rec_migr_bene = models.CharField(max_length=254, blank=True, null=True)
    bene_agan_field = models.BigIntegerField(db_column='bene_agan_migr_indist', blank=True, null=True)  # Field renamed because it ended with '_'.
    agan_bene_field = models.BigIntegerField(db_column='agan_bene_migr_outdist', blank=True, null=True)  # Field renamed because it ended with '_'.
    benetot_migr_out = models.CharField(max_length=254, blank=True, null=True)
    migrbenetot_agancentarea = models.BigIntegerField(blank=True, null=True)
    agan_serv_field = models.CharField(db_column='agan_serv_migr_outaganarea', max_length=254, blank=True, null=True)  # Field renamed because it ended with '_'.
    ifyes_aganspen10pergdp_endmar22 = models.CharField(max_length=254, blank=True, null=True)
    ifyes_gp_spent_10pergdp_endmarch22 = models.CharField(max_length=254, blank=True, null=True)
    aay = models.CharField(max_length=254, blank=True, null=True)
    totno_child_serv_aay_6mon_6yrs = models.CharField(max_length=254, blank=True, null=True)
    preg_lact_mother_serv_aay_ecd = models.CharField(max_length=254, blank=True, null=True)
    parvisit_inibalasch = models.CharField(max_length=254, blank=True, null=True)
    parent_visit_past_year = models.CharField(max_length=254, blank=True, null=True)
    balasch = models.BigIntegerField(blank=True, null=True)
    agan_und_balasch = models.CharField(max_length=254, blank=True, null=True)
    work_comund_balasch_mar22 = models.CharField(max_length=254, blank=True, null=True)
    ifcom_ongo_task_comp_undbalasch = models.CharField(max_length=254, blank=True, null=True)
    ifcom_ongo_task_comp_undbalasch_1 = models.BigIntegerField(blank=True, null=True)
    ifcom_ongo_task_comp_undbalasch_sandpit = models.CharField(max_length=254, blank=True, null=True)
    ifcom_ongo_task_comp_undbalasch_lawn = models.BigIntegerField(blank=True, null=True)
    ifcom_ongo_task_comp_undbalasch_display = models.BigIntegerField(blank=True, null=True)
    ifcom_ongo_task_comp_undbalasch_writboar = models.BigIntegerField(blank=True, null=True)
    sign_sup_chserv = models.CharField(max_length=254, blank=True, null=True)
    sign_sup_headmisurl = models.CharField(max_length=254, blank=True, null=True)
    field_id = models.BigIntegerField(db_column='_id', blank=True, null=True)  # Field renamed because it started with '_'.
    field_uuid = models.CharField(db_column='_uuid', max_length=254, blank=True, null=True)  # Field renamed because it started with '_'.
    field_submissio = models.CharField(db_column='_submission_time', max_length=254, blank=True, null=True)  # Field renamed because it started with '_'.
    field_validatio = models.CharField(db_column='_validation_status', max_length=254, blank=True, null=True)  # Field renamed because it started with '_'.
    field_notes = models.CharField(db_column='_notes', max_length=254, blank=True, null=True)  # Field renamed because it started with '_'.
    field_status = models.CharField(db_column='_status', max_length=254, blank=True, null=True)  # Field renamed because it started with '_'.
    field_submitted = models.CharField(db_column='_submitted_by', max_length=254, blank=True, null=True)  # Field renamed because it started with '_'.
    field_tags = models.CharField(db_column='_tags', max_length=254, blank=True, null=True)  # Field renamed because it started with '_'.
    field_index = models.BigIntegerField(db_column='_index', blank=True, null=True)  # Field renamed because it started with '_'.
    field_108 = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rural_infra_awc_ac_englishConverted_merge_1'
